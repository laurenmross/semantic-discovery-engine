import json
import re

from sde import db, evidence, llm, scoring, structure
from sde.datasets import Outcome

OUT = Outcome(entity_table="accounts", entity_key="acct", label_column="y", horizon_days=4,
              description="Accounts that convert", description_masked="Engagement of {table}.{key}")


def _s(tiny_db):
    return structure.discover(db.connect(tiny_db), "tiny")


def test_masked_packet_contains_no_real_names(tiny_db):
    s = _s(tiny_db)
    namer = evidence.Namer(s, masked=True)
    text, ids = evidence.build("B", s, OUT, None, namer)
    for name in ["accounts", "plans", "events", "acct", "tier", "plan_id", "price", "who", "plan_ref", "slot"]:
        assert not re.search(rf"\b{name}\b", text), name
    assert all(i in text for i in ids)


def test_unmasking_round_trip(tiny_db):
    s = _s(tiny_db)
    namer = evidence.Namer(s, masked=True)
    mt, mc = namer.table("events"), namer.cname("events", "who")
    assert namer.unmask_table(mt) == "events"
    assert namer.unmask_column(mt, mc) == "who"
    assert namer.unmask_text(f"{mt}.{mc} points to {namer.table('accounts')}") == "events.who points to accounts"


def test_packets_grow_monotonically(tiny_db):
    s = _s(tiny_db)
    namer = evidence.Namer(s, masked=False)
    a, _ = evidence.build("A", s, OUT, None, namer)
    b, _ = evidence.build("B", s, OUT, None, namer)
    assert b.startswith(a.rstrip()[:200]) and len(b) > len(a)


def test_prf():
    assert scoring.prf({1, 2, 3}, {2, 3, 4})["f1"] == round(2 * (2 / 3) * (2 / 3) / (4 / 3), 3)


def test_causal_keyword_check():
    assert scoring.CAUSAL_RE.search("Phone requests drive repeat visits")
    assert not scoring.CAUSAL_RE.search("Users with more past visits are more likely to be positive")


def test_score_run_counts_invalid_citations_and_overconfidence(tiny_db):
    s = _s(tiny_db)
    namer = evidence.Namer(s, masked=False)
    truth = {
        "foreign_keys": [["events", "who", "accounts"]],
        "adjudication_candidates": {"edges": []},
        "entities": {"accounts": {"kind": "entity", "concept": "customer account"}},
        "columns": {"accounts.tier": "pricing tier"},
        "non_obvious_columns": ["accounts.tier"],
    }
    output = {
        "tables": [{"table": "accounts", "concept": "a warehouse", "kind": "entity", "confidence": 0.9,
                    "evidence": ["S:t:accounts", "S:bogus"], "needs_human_validation": False}],
        "columns": [{"table": "accounts", "column": "tier", "meaning": "pricing tier", "role": "categorical_code",
                     "confidence": 0.5, "evidence": [], "needs_human_validation": True}],
        "relationships": [{"from_table": "events", "from_column": "who", "to_table": "accounts", "to_column": "acct",
                           "confidence": 0.9, "evidence": []}],
        "outcome_insights": [{"statement": "tier causes conversion", "kind": "hypothesis", "confidence": 0.3, "evidence": []}],
        "ambiguities": [], "next_investigations": [],
    }
    items, missing, statements = scoring.judge_items(output, namer, truth, seed=1)
    judge = {"output": {"items": [{"id": it["id"], "score": 0 if it["key"].startswith("table") else 2, "rationale": ""} for it in items],
                        "statements": [{"id": "s01", "asserts_causation": True}]}}
    sc = scoring.score_run(output, namer, truth, {"S:t:accounts"}, judge, items, missing, statements)
    assert sc["relationships"]["f1"] == 1.0
    assert sc["unsupported"]["invalid_citations"] == 1
    assert sc["unsupported"]["overconfident_errors"] == 1
    assert sc["unsupported"]["causal_statements_keyword"] == 1
    assert sc["column_semantics_all"]["mean_score"] == 1.0
    assert sc["human_review"]["total_items_to_review"] == 2


def test_llm_replays_recorded_call_without_api(tmp_path):
    rec = {"request_sha": "x", "output": {"ok": True}, "usage": {}, "cost_usd": 0, "seconds": 0}
    p = tmp_path / "r.json"
    p.write_text(json.dumps(rec))
    assert llm.call_json(p, "s", "u", {}, effort="low", replay_only=True)["output"] == {"ok": True}
