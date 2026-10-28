"""Evidence packets for configurations A, B and C, rendered with original or masked names.

Every fact the LLM sees carries an evidence ID (S:... structural, P:... predictive) so that each
interpretation can cite what supports it, and citations can be checked mechanically.
"""
from __future__ import annotations

import json
import random
import re

from .datasets import Outcome
from .structure import Structure

CONFIGS = ("A", "B", "C")
NAMINGS = ("original", "masked")
MASK_SEED = 7


class Namer:
    """Maps real table/column names to display names. Masked names are a fixed random permutation."""

    def __init__(self, s: Structure, masked: bool, seed: int = MASK_SEED):
        self.masked = masked
        self.t, self.c = {}, {}
        rng = random.Random(seed)
        tables = sorted(s.tables)
        order = tables[:]
        rng.shuffle(order)
        for i, t in enumerate(order, 1):
            self.t[t] = f"T{i:02d}" if masked else t
            cols = [p.column for p in s.tables[t]["columns"]]
            perm = cols[:]
            rng.shuffle(perm)
            for j, c in enumerate(perm, 1):
                self.c[(t, c)] = f"c{j:02d}" if masked else c
        self.inv_t = {v: k for k, v in self.t.items()}
        self.inv_c = {(self.t[t], v): c for (t, c), v in self.c.items()}

    def table(self, t: str) -> str:
        return self.t[t]

    def col(self, t: str, c: str) -> str:
        return f"{self.t[t]}.{self.c[(t, c)]}"

    def cname(self, t: str, c: str) -> str:
        return self.c[(t, c)]

    def column_order(self, s: Structure, t: str) -> list[str]:
        cols = [p.column for p in s.tables[t]["columns"]]
        return sorted(cols, key=lambda c: self.c[(t, c)]) if self.masked else cols

    def table_order(self, s: Structure) -> list[str]:
        return sorted(s.tables, key=lambda t: self.t[t])

    # Inverse mapping for scoring.
    def unmask_table(self, name: str) -> str | None:
        name = (name or "").strip()
        if name in self.inv_t:
            return self.inv_t[name]
        low = {k.lower(): v for k, v in self.inv_t.items()}
        return low.get(name.lower())

    def unmask_column(self, table_display: str, col: str) -> str | None:
        t = self.unmask_table(table_display)
        if t is None:
            return None
        col = (col or "").strip()
        if "." in col:
            col = col.split(".", 1)[1]
        key = (self.t[t], col)
        if key in self.inv_c:
            return self.inv_c[key]
        low = {(a, b.lower()): v for (a, b), v in self.inv_c.items() if a == self.t[t]}
        return low.get((self.t[t], col.lower()))

    def unmask_text(self, text: str) -> str:
        """Replace masked references (T03, T03.c02) in free text with real names."""
        if not self.masked or not text:
            return text

        def rep(m):
            t = self.inv_t.get(m.group(1))
            if t is None:
                return m.group(0)
            if m.group(2):
                c = self.inv_c.get((m.group(1), m.group(2)))
                return f"{t}.{c}" if c else t
            return t
        return re.sub(r"\b(T\d\d)(?:\.(c\d\d))?\b", rep, text)


def _text_descriptor(values: list[str]) -> str:
    if not values:
        return "<text>"
    script = "Cyrillic" if any(re.search("[Ѐ-ӿ]", v) for v in values) else "Latin/other"
    avg = sum(len(v) for v in values) / len(values)
    return f"<text, ~{avg:.0f} chars, {script} script>"


def _fmt_values(p, namer: Namer, values: list[str]) -> list[str]:
    if p.family == "string" and namer.masked:
        return [_text_descriptor(values)]
    return [v if len(v) <= 60 else v[:57] + "..." for v in values]


def _path_str(path: list, namer: Namer) -> str:
    if not path:
        return "(target table itself)"
    return " then ".join(f"{namer.col(c, cc)} -> {namer.col(p, pc)}" for c, cc, p, pc in path)


def build(config: str, s: Structure, outcome: Outcome, outcome_result: dict | None, namer: Namer) -> tuple[str, set]:
    assert config in CONFIGS
    ids: set = set()
    out: list[str] = []

    def eid(x: str) -> str:
        ids.add(x)
        return x

    # --- Outcome statement (identical across configs) ---
    if namer.masked:
        desc = outcome.description_masked.format(table=namer.table(outcome.entity_table),
                                                 key=namer.cname(outcome.entity_table, outcome.entity_key))
    else:
        desc = outcome.description
    out.append("## Business outcome of interest (supplied by the business)")
    out.append(f"- {desc}")
    out.append(f"- Outcome entity: {namer.col(outcome.entity_table, outcome.entity_key)}")
    out.append("")

    # --- A: schema ---
    out.append("## Schema (tables, columns, types, row counts, example values)")
    for t in namer.table_order(s):
        out.append(f"### Table {namer.table(t)}  [{eid('S:t:' + namer.table(t))}]  rows={s.tables[t]['rows']}")
        for c in namer.column_order(s, t):
            p = s.profile(t, c)
            line = f"- {namer.cname(t, c)}: {p.dtype}; examples {_fmt_values(p, namer, p.samples)}  [{eid('S:c:' + namer.col(t, c))}]"
            if config in ("B", "C"):
                extra = f"nulls={p.null_frac:.1%} distinct={p.distinct} unique={'yes' if p.unique else 'no'}"
                if p.family != "string":
                    extra += f" min={p.min} max={p.max}"
                if p.mean is not None:
                    extra += f" mean={p.mean:.4g}"
                if p.avg_len is not None:
                    extra += f" avg_len={p.avg_len:.1f}"
                if p.top_values:
                    tv = p.top_values if not (p.family == "string" and namer.masked) else [("<text>", n) for _, n in p.top_values]
                    extra += " top=" + ", ".join(f"{v}:{n}" for v, n in tv[:6])
                if p.family == "integral_float":
                    extra += " (float type holding only whole numbers)"
                line += "\n    profile: " + extra
            out.append(line)
        out.append("")
    if config == "A":
        return "\n".join(out), ids

    # --- B: structure ---
    out.append("## Structural analysis (deterministic; computed from values only, never from names)")
    out.append("Candidate keys (100% unique, no nulls):")
    for t, c in s.keys:
        out.append(f"- {namer.col(t, c)}  [{eid('S:k:' + namer.col(t, c))}]")
    out.append("Time columns: " + ", ".join(namer.col(t, c) for t, cs in s.time_columns.items() for c in cs))
    out.append("")
    out.append("Candidate relationships (child column values contained in a candidate key).")
    out.append("Fields: inclusion = share of distinct child values found in parent key; coverage = share of parent keys referenced; "
               "range_density = share of the child's value range filled by parent keys (near 1.0 means inclusion is weak evidence, "
               "because any small integers would match); rows/parent = avg and max child rows per referenced parent; "
               "rank = rank of this parent among this child column's candidates by coverage; preferred = top-ranked and plausible; "
               "weak = both sides are small integer ranges starting near 0/1.")
    for i, r in enumerate(sorted(s.relationships, key=lambda r: (namer.col(r.child_table, r.child_column), r.parent_rank)), 1):
        out.append(
            f"- [{eid(f'S:r:{i}')}] {namer.col(r.child_table, r.child_column)} -> {namer.col(r.parent_table, r.parent_column)}: "
            f"inclusion={r.inclusion} coverage={r.parent_coverage} range_density={r.range_density} "
            f"rows/parent={r.rows_per_parent_avg}/{r.rows_per_parent_max} child_distinct={r.child_distinct} "
            f"rank={r.parent_rank} preferred={'yes' if r.best_parent else 'no'} weak={'yes' if r.weak else 'no'}"
            f"{' child_is_unique' if r.child_is_key else ''}")
    out.append("")
    out.append("Join paths (2-3 hops) over preferred, non-weak relationships:")
    for i, p in enumerate(s.join_paths, 1):
        out.append(f"- [{eid(f'S:p:{i}')}] " + " - ".join(namer.table(t) for t in p))
    out.append("")
    out.append("Structural ambiguities:")
    for i, a in enumerate(s.ambiguities, 1):
        where = namer.col(a["table"], a["column"]) if a.get("column") else namer.table(a["table"])
        detail = a["detail"]
        if a["type"] == "multiple_parents":
            detail = ", ".join(namer.col(*d.split(".", 1)) for d in detail)
        elif a["type"] == "multiple_time_columns":
            detail = ", ".join(namer.col(a["table"], d) for d in detail)
        else:
            detail = re.sub(r"(\w+)\.(\w+):", lambda m: namer.col(m.group(1), m.group(2)) + ":" if m.group(1) in s.tables else m.group(0), str(detail))
        out.append(f"- [{eid(f'S:a:{i}')}] {a['type']} at {where}: {detail}")
    out.append("")
    if config == "B":
        return "\n".join(out), ids

    # --- C: outcome-driven evidence ---
    r = outcome_result
    assert r is not None
    feats = {f["id"]: f for f in r["features"]}
    out.append("## Outcome-driven analysis (predictive associations; NOT causal, NOT semantic proof)")
    out.append(f"Label rows: {r['n_rows']} (time-based splits: train, then validation, then test). "
               f"Positive rate: { {k: round(v, 3) for k, v in r['base_rate'].items()} }.")
    out.append(f"Features were built only from candidate relationships marked preferred and non-weak, using only rows dated before each cutoff.")
    m = r["models"]
    out.append(f"- [{eid('P:m:1')}] Model performance (AUROC; 0.5 = chance): "
               + "; ".join(f"{k}: val={v['val_auroc']:.3f} test={v['test_auroc']:.3f}" for k, v in m.items() if isinstance(v, dict))
               + f"; selected on validation: {m['selected_on_val']}")
    b = r["baselines"].get("single_activity_count")
    if b:
        out.append(f"- [{eid('P:m:2')}] Baseline: best single past-activity count ({b['feature']}) test AUROC={b['test_auroc']:.3f}")
    out.append("")
    out.append("Relationship paths ranked by summed permutation importance (validation):")
    for i, p in enumerate(r["path_importance"], 1):
        out.append(f"- [{eid(f'P:path:{i}')}] importance={p['importance']:.4f} path: {_path_str(p['path'], namer)} features={p['features']}")
    out.append("")
    out.append("Features (agg over the path; window in days before cutoff; univariate AUROC on train/val; direction; "
               "stability of direction across training cutoffs; BH-adjusted q-value; permutation importance):")
    stats = sorted(r["feature_stats"], key=lambda d: -d["perm_importance_mean"])
    for st in stats:
        f = feats[st["feature"]]
        if f["agg"] == "count_where":
            col = f"{namer.table(f['table'])} rows where {namer.col(f['table'], f['column'])} = {f['value']:g}"
        else:
            col = namer.col(f["table"], f["column"]) if f["column"] else namer.table(f["table"]) + " rows"
        out.append(
            f"- [{eid('P:f:' + f['id'])}] {f['agg']}({col}) window={f['window_days'] or 'all'} via {_path_str(f['path'], namer)}: "
            f"auroc train={st['train_auroc']:.3f} val={st['val_auroc']:.3f} {st['direction']} "
            f"stable={('yes' if st['direction_stable'] else 'no') if st['n_cutoffs'] else 'n/a'} q={st['q_value_bh']:.2g} "
            f"perm_imp={st['perm_importance_mean']:.4f} coverage={st['coverage']:.0%}")
    return "\n".join(out), ids


SYSTEM_PROMPT = """You are a careful data analyst who has been handed an unfamiliar relational database with no documentation.
Your job is to infer what the data means in business terms, using only the evidence provided.

Rules:
- Distinguish observed facts (stated in the evidence) from your hypotheses (your interpretation). Interpretations are hypotheses.
- Cite evidence IDs (for example S:c:..., S:r:3, P:f:f012) for every claim. Cite only IDs that appear in the evidence.
- Calibrate confidence (0 to 1). Use low confidence where evidence is thin or names are uninformative. Do not guess with high confidence.
- Predictive association is not semantic meaning and not causation. Never claim that one behaviour causes, drives or increases another;
  describe associations as associations.
- Candidate relationships are computed from value overlap and can be coincidental. Accept a relationship only if the evidence supports it.
- Mark items that need confirmation from a person who knows the business (needs_human_validation).
- Refer to tables and columns exactly by the names used in the evidence.
- Cover every table and every column."""

USER_TEMPLATE = """Below is everything known about the database. Produce your interpretation in the required JSON format.

- tables: one entry per table: the business concept it represents, and its kind (entity, dimension, event, bridge, other).
- columns: one entry per column: its business meaning and role.
- relationships: the foreign-key relationships you believe are real (child column -> parent key).
- outcome_insights: what the evidence suggests about the business outcome (associations or hypotheses; never causal claims).
- ambiguities: unresolved questions. next_investigations: the most valuable follow-up analyses.

{packet}"""

OUTPUT_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["tables", "columns", "relationships", "outcome_insights", "ambiguities", "next_investigations"],
    "properties": {
        "tables": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["table", "concept", "kind", "confidence", "evidence", "needs_human_validation"],
            "properties": {
                "table": {"type": "string"},
                "concept": {"type": "string"},
                "kind": {"type": "string", "enum": ["entity", "dimension", "event", "bridge", "other"]},
                "confidence": {"type": "number"},
                "evidence": {"type": "array", "items": {"type": "string"}},
                "needs_human_validation": {"type": "boolean"}}}},
        "columns": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["table", "column", "meaning", "role", "confidence", "evidence", "needs_human_validation"],
            "properties": {
                "table": {"type": "string"},
                "column": {"type": "string"},
                "meaning": {"type": "string"},
                "role": {"type": "string", "enum": ["primary_key", "foreign_key", "timestamp", "measure", "flag",
                                                     "categorical_code", "identifier_not_foreign_key", "text", "other"]},
                "confidence": {"type": "number"},
                "evidence": {"type": "array", "items": {"type": "string"}},
                "needs_human_validation": {"type": "boolean"}}}},
        "relationships": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["from_table", "from_column", "to_table", "to_column", "confidence", "evidence"],
            "properties": {
                "from_table": {"type": "string"}, "from_column": {"type": "string"},
                "to_table": {"type": "string"}, "to_column": {"type": "string"},
                "confidence": {"type": "number"},
                "evidence": {"type": "array", "items": {"type": "string"}}}}},
        "outcome_insights": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["statement", "kind", "confidence", "evidence"],
            "properties": {
                "statement": {"type": "string"},
                "kind": {"type": "string", "enum": ["observed_association", "hypothesis"]},
                "confidence": {"type": "number"},
                "evidence": {"type": "array", "items": {"type": "string"}}}}},
        "ambiguities": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["description", "evidence"],
            "properties": {"description": {"type": "string"},
                           "evidence": {"type": "array", "items": {"type": "string"}}}}},
        "next_investigations": {"type": "array", "items": {"type": "string"}},
    },
}


def user_message(packet: str) -> str:
    return USER_TEMPLATE.format(packet=packet)


def schema_json() -> str:
    return json.dumps(OUTPUT_SCHEMA)
