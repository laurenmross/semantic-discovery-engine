"""Scoring against the pre-registered ground truth (eval/protocol.md sections 5-6)."""
from __future__ import annotations

import json
import random
import re
from pathlib import Path

from . import llm
from .evidence import Namer
from .structure import Structure

CAUSAL_RE = re.compile(r"\b(cause[sd]?|causing|causal|drives?|driven|driving|leads? to|led to|results? in|"
                       r"because of|boosts?|increases? (?:the )?(?:likelihood|probability|chance)|effect of|impact of)\b", re.I)
OVERCONFIDENT = 0.8


def load_truth(path: Path) -> dict:
    return json.loads(path.read_text())


def prf(pred: set, truth: set) -> dict:
    tp = len(pred & truth)
    p = tp / len(pred) if pred else 0.0
    r = tp / len(truth) if truth else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    return {"precision": round(p, 3), "recall": round(r, 3), "f1": round(f, 3), "tp": tp,
            "fp": len(pred - truth), "fn": len(truth - pred), "n_pred": len(pred)}


def structural_scores(s: Structure, truth: dict) -> dict:
    gt = {tuple(e) for e in truth["foreign_keys"]}
    sets = {
        "all_candidates": {(r.child_table, r.child_column, r.parent_table) for r in s.relationships},
        "preferred_parent": {(r.child_table, r.child_column, r.parent_table) for r in s.relationships if r.best_parent},
        "feature_eligible": {(r.child_table, r.child_column, r.parent_table) for r in s.relationships if r.feature_eligible},
    }
    out = {k: prf(v, gt) for k, v in sets.items()}
    out["keys"] = prf({tuple(k) for k in s.keys}, set(truth["primary_keys"].items()))
    return out


def predicted_relationships(output: dict, namer: Namer) -> tuple[set, list]:
    pred, unresolved = set(), []
    for r in output.get("relationships", []):
        ct = namer.unmask_table(r["from_table"])
        cc = namer.unmask_column(r["from_table"], r["from_column"])
        pt = namer.unmask_table(r["to_table"])
        if ct and cc and pt:
            pred.add((ct, cc, pt))
        else:
            unresolved.append(r)
    return pred, unresolved


# ---------------------------------------------------------------------------------------------
# Blinded LLM judge for entity and column semantics

JUDGE_SYSTEM = """You grade whether a predicted description of a database table or column matches a reference description.
You do not know which system produced the prediction. Grade each item independently.

Scores:
2 = correct: the prediction identifies the same business concept as the reference. Wording can differ. A more specific answer
    is fine if it is consistent with the reference.
1 = partially correct: the right general area, but a key aspect is missing or wrong (for example "some interaction with an ad"
    for "a view of an ad's page"), or the prediction hedges between a correct and an incorrect reading.
0 = incorrect, contradictory, or too vague to be useful.

Where the reference says an answer is not documented and gives an acceptable range, any answer within that range scores 2.

Separately, for each outcome statement, say whether it asserts that something CAUSES, DRIVES or INCREASES the outcome
(a causal claim), rather than only describing an association."""

JUDGE_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["items", "statements"],
    "properties": {
        "items": {"type": "array", "items": {
            "type": "object", "additionalProperties": False, "required": ["id", "score", "rationale"],
            "properties": {"id": {"type": "string"}, "score": {"type": "integer", "enum": [0, 1, 2]},
                           "rationale": {"type": "string"}}}},
        "statements": {"type": "array", "items": {
            "type": "object", "additionalProperties": False, "required": ["id", "asserts_causation"],
            "properties": {"id": {"type": "string"}, "asserts_causation": {"type": "boolean"}}}},
    },
}


def _index_predictions(output: dict, namer: Namer):
    tables, columns = {}, {}
    for t in output.get("tables", []):
        real = namer.unmask_table(t["table"])
        if real:
            tables[real] = t
    for c in output.get("columns", []):
        rt = namer.unmask_table(c["table"])
        rc = namer.unmask_column(c["table"], c["column"])
        if rt and rc:
            columns[f"{rt}.{rc}"] = c
    return tables, columns


def judge_items(output: dict, namer: Namer, truth: dict, seed: int):
    """Build the blinded item list. Items with no prediction are scored 0 without the judge."""
    tables, columns = _index_predictions(output, namer)
    items, missing = [], []
    for t, ref in truth["entities"].items():
        p = tables.get(t)
        if p:
            items.append({"key": f"table:{t}", "reference": ref["concept"], "prediction": namer.unmask_text(p["concept"])})
        else:
            missing.append(f"table:{t}")
    for c, ref in truth["columns"].items():
        p = columns.get(c)
        if p:
            items.append({"key": f"column:{c}", "reference": ref, "prediction": namer.unmask_text(p["meaning"])})
        else:
            missing.append(f"column:{c}")
    random.Random(seed).shuffle(items)
    for i, it in enumerate(items, 1):
        it["id"] = f"i{i:03d}"
    statements = [{"id": f"s{i:02d}", "text": namer.unmask_text(o["statement"])}
                  for i, o in enumerate(output.get("outcome_insights", []), 1)]
    return items, missing, statements


def run_judge(record_path: Path, items: list, statements: list, replay_only: bool = False) -> dict:
    payload = {"items": [{"id": it["id"], "reference": it["reference"], "prediction": it["prediction"]} for it in items],
               "statements": statements}
    user = "Grade these items and statements.\n\n" + json.dumps(payload, ensure_ascii=False, indent=1)
    return llm.call_json(record_path, JUDGE_SYSTEM, user, JUDGE_SCHEMA, effort="medium", replay_only=replay_only)


def score_run(output: dict, namer: Namer, truth: dict, packet_ids: set, judge_rec: dict,
              items: list, missing: list, statements: list) -> dict:
    gt = {tuple(e) for e in truth["foreign_keys"]}
    pred, unresolved = predicted_relationships(output, namer)
    rel = prf(pred, gt)
    adjudicate = sorted(pred & {tuple(e) for e in truth["adjudication_candidates"]["edges"]})

    grades = {g["id"]: g["score"] for g in judge_rec["output"]["items"]}
    by_key = {it["key"]: grades.get(it["id"], 0) for it in items}
    for k in missing:
        by_key[k] = 0
    tables, columns = _index_predictions(output, namer)

    def acc(keys):
        vals = [by_key[k] for k in keys]
        return {"mean_score": round(sum(vals) / (2 * len(vals)), 3) if vals else 0.0,
                "fully_correct": round(sum(v == 2 for v in vals) / len(vals), 3) if vals else 0.0, "n": len(vals)}

    ent_keys = [f"table:{t}" for t in truth["entities"]]
    col_keys = [f"column:{c}" for c in truth["columns"]]
    nonobv = [f"column:{c}" for c in truth["non_obvious_columns"]]
    kind_acc = sum(1 for t, ref in truth["entities"].items() if tables.get(t, {}).get("kind") == ref["kind"]) / len(truth["entities"])

    # Unsupported claims.
    cited = [e for sec in ("tables", "columns", "relationships", "outcome_insights", "ambiguities")
             for x in output.get(sec, []) for e in x.get("evidence", [])]
    invalid = [e for e in cited if e not in packet_ids]
    conf = {f"table:{t}": p["confidence"] for t, p in tables.items()}
    conf.update({f"column:{c}": p["confidence"] for c, p in columns.items()})
    overconfident = [k for k, v in by_key.items() if v == 0 and conf.get(k, 0) >= OVERCONFIDENT]
    causal_kw = [s["id"] for s in statements if CAUSAL_RE.search(s["text"])]
    causal_judge = [s["id"] for s in judge_rec["output"]["statements"] if s["asserts_causation"]]
    flagged = sum(1 for sec in ("tables", "columns") for x in output.get(sec, []) if x.get("needs_human_validation"))

    return {
        "relationships": rel,
        "relationships_unresolved_names": len(unresolved),
        "adjudication_edges_predicted": [list(e) for e in adjudicate],
        "entity_concept": acc(ent_keys),
        "entity_kind_accuracy": round(kind_acc, 3),
        "column_semantics_all": acc(col_keys),
        "column_semantics_non_obvious": acc(nonobv),
        "unsupported": {
            "citations_total": len(cited),
            "invalid_citations": len(invalid),
            "invalid_citation_examples": invalid[:10],
            "overconfident_errors": len(overconfident),
            "overconfident_items": overconfident,
            "causal_statements_keyword": len(causal_kw),
            "causal_statements_judge": len(causal_judge),
            "outcome_statements": len(statements),
        },
        "human_review": {"flagged_for_validation": flagged, "overconfident_errors": len(overconfident),
                         "total_items_to_review": flagged + len(overconfident)},
        "item_scores": by_key,
    }
