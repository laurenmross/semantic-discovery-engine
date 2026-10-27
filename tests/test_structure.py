import duckdb
import pytest

from sde import db, structure


def test_keys_and_relationships_are_inferred_from_values(tiny_db):
    con = db.connect(tiny_db)
    s = structure.discover(con, "tiny")
    assert set(s.keys) == {("accounts", "acct"), ("plans", "plan_id")}
    preferred = {(r.child_table, r.child_column, r.parent_table) for r in s.relationships if r.best_parent}
    assert ("events", "who", "accounts") in preferred
    assert ("events", "plan_ref", "plans") in preferred
    assert s.time_columns == {"events": ["happened_at"]}


def test_small_integer_measure_is_not_feature_eligible(tiny_db):
    con = db.connect(tiny_db)
    s = structure.discover(con, "tiny")
    # events.slot (values 1..5) matches no sparse key, so it must never become a feature edge.
    assert not any(r.child_column == "slot" and r.feature_eligible for r in s.relationships)


def test_source_is_read_only(tiny_db):
    con = db.connect(tiny_db)
    with pytest.raises(duckdb.Error):
        con.execute("DELETE FROM src.accounts")
    assert con.execute("SELECT count(*) FROM src.accounts").fetchall()[0][0] == 200


def test_rank_parents_prefers_highest_coverage():
    mk = lambda pt, cov: structure.Relationship("c", "x", pt, "k", 1.0, 50, 100, cov, 1, 1, False, True)
    rels = [mk("low", 0.1), mk("high", 0.9)]
    structure._rank_parents(rels)
    best = [r.parent_table for r in rels if r.best_parent]
    assert best == ["high"]
