"""Leakage and join-safety tests for the outcome component."""
import duckdb
import pandas as pd

from sde import db, outcome, structure
from sde.datasets import Outcome

OUT = Outcome(entity_table="accounts", entity_key="acct", label_column="y", horizon_days=4,
              description="d", description_masked="d")


def _labels():
    return pd.DataFrame({"key": [1000, 1007, 1000], "t": pd.to_datetime(["2024-01-20", "2024-01-20", "2024-01-30"]),
                         "y": [1, 0, 1], "split": ["train", "train", "val"]})


def _features(tiny_db):
    con = db.connect(tiny_db)
    s = structure.discover(con, "tiny")
    labels = outcome.register_labels(con, _labels())
    feats = outcome.plan_features(s, OUT)
    return con, s, feats, labels, outcome.build_features(con, s, OUT, feats, labels)


def _count_feature(feats, window):
    return next(f.id for f in feats if f.agg == "count" and f.table == "events" and f.window_days == window and len(f.path) == 1)


def test_features_use_only_rows_before_cutoff(tiny_db):
    con, s, feats, labels, X = _features(tiny_db)
    fid = _count_feature(feats, None)
    expected = con.execute("SELECT count(*) FROM src.events WHERE who = 1000 AND happened_at < TIMESTAMP '2024-01-20'").fetchall()[0][0]
    assert X.loc[0, fid] == expected


def test_future_rows_do_not_change_features(tiny_db, tmp_path):
    _, _, feats, _, before = _features(tiny_db)
    w = duckdb.connect(str(tiny_db.db_path))
    w.execute("INSERT INTO events VALUES (1000, 500, 1, TIMESTAMP '2024-03-01'), (1000, 500, 1, TIMESTAMP '2024-01-30')")
    w.close()
    _, _, _, _, after = _features(tiny_db)
    # Rows at or after the latest cutoff (including exactly at it) must not move any feature.
    pd.testing.assert_frame_equal(before, after)


def test_window_feature_is_bounded(tiny_db):
    con, s, feats, labels, X = _features(tiny_db)
    fid = _count_feature(feats, 4)
    expected = con.execute("""SELECT count(*) FROM src.events WHERE who = 1000
        AND happened_at < TIMESTAMP '2024-01-20' AND happened_at >= TIMESTAMP '2024-01-16'""").fetchall()[0][0]
    assert X.loc[0, fid] == expected


def test_one_row_per_label_row(tiny_db):
    _, _, _, labels, X = _features(tiny_db)
    assert len(X) == len(labels) and X.index.is_unique


def test_benjamini_hochberg_matches_reference():
    import numpy as np
    p = np.array([0.01, 0.04, 0.03, 0.5])
    # Reference values from statsmodels.stats.multitest.multipletests(method="fdr_bh").
    from statsmodels.stats.multitest import multipletests
    assert np.allclose(outcome._bh(p), multipletests(p, method="fdr_bh")[1])
