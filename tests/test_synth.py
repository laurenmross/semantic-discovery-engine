"""The synthetic dataset: determinism, label definition, and per-value features without leakage."""
from types import SimpleNamespace

import pandas as pd

from sde import db, outcome, structure, synth
from sde.datasets import DATASETS


def _gen(tmp_path, seed=1):
    d = tmp_path / f"saas{seed}"
    stats = synth.generate(d, seed=seed, n_acct=300)
    return d, stats


def test_generation_is_deterministic(tmp_path):
    d1, s1 = _gen(tmp_path / "a")
    d2, s2 = _gen(tmp_path / "b")
    assert s1 == s2
    a = pd.read_parquet(d1 / "db" / "EVT_STRM_01.parquet")
    b = pd.read_parquet(d2 / "db" / "EVT_STRM_01.parquet")
    pd.testing.assert_frame_equal(a, b)


def test_labels_match_subscription_starts(tmp_path):
    d, _ = _gen(tmp_path)
    subs = pd.read_parquet(d / "db" / "SUB_HDR.parquet").set_index("acct_key")["st_ts"]
    lab = pd.concat(pd.read_parquet(p) for p in (d / "tasks" / "trial-conversion").glob("*.parquet"))
    st = lab["acct_key"].map(subs)
    expected = st.notna() & (st >= lab["timestamp"]) & (st < lab["timestamp"] + pd.Timedelta(days=16))
    assert (expected == lab["converted"]).all()
    assert not (st < lab["timestamp"]).any(), "accounts converted before the cutoff must be excluded"


def test_per_value_features_use_only_pre_cutoff_rows(tmp_path):
    d, _ = _gen(tmp_path)
    ds = SimpleNamespace(name="t", db_path=d / "source.duckdb", dir=d)
    db.ingest(ds)
    con = db.connect(ds)
    s = structure.discover(con, "t")
    spec = DATASETS["saas"].outcome
    lab = pd.concat(pd.read_parquet(p).assign(split=p.stem) for p in (d / "tasks" / "trial-conversion").glob("*.parquet"))
    lab = lab.rename(columns={"acct_key": "key", "timestamp": "t", "converted": "y"})[["key", "t", "y", "split"]]
    labels = outcome.register_labels(con, lab)
    feats = outcome.plan_features(s, spec)
    f7 = [f for f in feats if f.agg == "count_where" and f.table == "EVT_STRM_01" and f.column == "evt_cd" and f.value == 7.0]
    assert f7, "expected a per-value feature for usage event code 7"
    X = outcome.build_features(con, s, spec, f7, labels)
    direct = con.execute("""SELECT L.rid, count(e.evt_cd) n FROM labels L
        LEFT JOIN src.USR_XREF u ON u.acct_key = L.key
        LEFT JOIN src.EVT_STRM_01 e ON e.usr_key = u.usr_key AND e.evt_cd = 7 AND e.evt_ts < L.t AND u.crt_ts < L.t
        GROUP BY L.rid ORDER BY L.rid""").df().set_index("rid")["n"]
    assert (X[f7[0].id] == direct.astype(float)).all()
