"""Component B: outcome-driven analysis.

Starting from a known outcome on one entity table, synthesise a bounded set of relational features
by walking the *inferred* relationships (never ground truth), evaluate them on time-based splits,
and rank which relationships carry predictive signal. The goal is to point the semantic step at
what deserves interpretation, not to build the best possible model.

Validity safeguards (eval/protocol.md section 8):
- point-in-time: every event-table aggregate uses only rows with time < cutoff;
- aggregation before joining: child rows are grouped to one row per label row;
- row counts are asserted unchanged after every feature join;
- Benjamini-Hochberg correction on univariate tests;
- the model is selected on validation and scored once on test.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler
from sklearn.impute import SimpleImputer

from .datasets import DATA, Outcome
from .db import q
from .structure import Structure

NUMERIC = ("int", "float", "integral_float", "bool")
FDR_Q = 0.05


@dataclass
class Feature:
    id: str
    path: list            # [[child_table, child_column, parent_table, parent_column], ...] from the target outward
    table: str            # table being aggregated
    column: str | None    # aggregated column (None for counts / recency)
    agg: str              # count | mean | count_distinct | days_since_last | value
    window_days: int | None
    time_column: str | None


@dataclass
class OutcomeResult:
    features: list
    label_check: dict
    models: dict
    baselines: dict
    feature_stats: list       # per-feature univariate + importance + stability
    path_importance: list     # importance summed by relationship path
    n_rows: dict
    base_rate: dict
    notes: list = field(default_factory=list)

    def to_dict(self):
        d = asdict(self)
        return d


# ---------------------------------------------------------------------------------------------
# Feature synthesis

def _eligible(s: Structure):
    return [r for r in s.relationships if r.feature_eligible]


def _edge_cols(s: Structure) -> set:
    cols = set()
    for r in _eligible(s):
        cols.add((r.child_table, r.child_column))
        cols.add((r.parent_table, r.parent_column))
    return cols


def _numeric_attrs(s: Structure, table: str) -> list[str]:
    keys = {c for t, c in s.keys if t == table}
    edges = _edge_cols(s)
    return [p.column for p in s.tables[table]["columns"]
            if p.family in NUMERIC and p.column not in keys and (table, p.column) not in edges
            and p.distinct > 1]


def _time_col(s: Structure, table: str):
    cols = s.time_columns.get(table, [])
    return cols[0] if cols else None


def plan_features(s: Structure, outcome: Outcome) -> list[Feature]:
    T, K = outcome.entity_table, outcome.entity_key
    feats: list[Feature] = []

    def add(**kw):
        feats.append(Feature(id=f"f{len(feats):03d}", **kw))

    # Target-table attributes (static).
    for p in s.tables[T]["columns"]:
        if p.column != K and p.family in NUMERIC and p.distinct > 1:
            add(path=[], table=T, column=p.column, agg="value", window_days=None, time_column=None)

    eligible = _eligible(s)
    hop1 = [r for r in eligible if (r.parent_table, r.parent_column) == (T, K)]
    for r in hop1:
        C, tc = r.child_table, _time_col(s, r.child_table)
        e1 = [r.child_table, r.child_column, r.parent_table, r.parent_column]
        windows = [None, outcome.horizon_days] if tc else [None]
        for w in windows:
            add(path=[e1], table=C, column=None, agg="count", window_days=w, time_column=tc)
        if tc:
            add(path=[e1], table=C, column=None, agg="days_since_last", window_days=None, time_column=tc)
        for col in _numeric_attrs(s, C):
            add(path=[e1], table=C, column=col, agg="mean", window_days=None, time_column=tc)
        for r2 in eligible:
            if r2.child_table == C and r2.child_column != r.child_column:
                add(path=[e1], table=C, column=r2.child_column, agg="count_distinct", window_days=None, time_column=tc)
        # Two hops down: tables that reference C's key.
        c_keys = {c for t, c in s.keys if t == C}
        for g in eligible:
            if g.parent_table == C and g.parent_column in c_keys and g.child_table != C:
                e2 = [g.child_table, g.child_column, g.parent_table, g.parent_column]
                gt = _time_col(s, g.child_table)
                add(path=[e1, e2], table=g.child_table, column=None, agg="count", window_days=None, time_column=gt or tc)
                for col in _numeric_attrs(s, g.child_table):
                    add(path=[e1, e2], table=g.child_table, column=col, agg="mean", window_days=None, time_column=gt or tc)
        # Two hops up: attributes of the parents C points to (other than the target).
        for u in eligible:
            if u.child_table == C and u.child_column != r.child_column and u.parent_table not in (T, C):
                e2 = [u.child_table, u.child_column, u.parent_table, u.parent_column]
                for col in _numeric_attrs(s, u.parent_table):
                    add(path=[e1, e2], table=u.parent_table, column=col, agg="mean", window_days=None, time_column=tc)
    return feats


def _feature_sql(f: Feature, outcome: Outcome) -> str:
    """One query per feature: returns (rid, value), one row per label row that has data.

    Point-in-time rule: the first-hop table C is filtered by its own time column (if any) to
    rows strictly before the cutoff; on a downward second hop, the second table is filtered by
    its own time column too. Static tables (no time column) are used as-is.
    """
    if f.agg == "value":
        return (f"SELECT L.rid, T.{q(f.column)}::DOUBLE AS v FROM labels L "
                f"JOIN src.{q(f.table)} T ON T.{q(outcome.entity_key)} = L.key")
    C, cfk = f.path[0][0], f.path[0][1]
    joins = f"JOIN src.{q(C)} C ON C.{q(cfk)} = L.key"
    conds = []
    c_tc = _time_cache.get(C)
    if c_tc:
        conds.append(f"C.{q(c_tc)} < L.t")
        if f.window_days:
            conds.append(f"C.{q(c_tc)} >= L.t - INTERVAL {int(f.window_days)} DAY")
    alias = "C"
    if len(f.path) == 2:
        child, ccol, parent, pcol = f.path[1]
        alias = "X"
        if parent == C:   # down: X.ccol -> C.pcol
            joins += f" JOIN src.{q(child)} X ON X.{q(ccol)} = C.{q(pcol)}"
            x_tc = _time_cache.get(child)
            if x_tc:
                conds.append(f"X.{q(x_tc)} < L.t")
        else:             # up: C.ccol -> X.pcol
            joins += f" JOIN src.{q(parent)} X ON X.{q(pcol)} = C.{q(ccol)}"
    where = ("WHERE " + " AND ".join(conds)) if conds else ""
    if f.agg == "count":
        expr = "count(*)::DOUBLE"
    elif f.agg == "mean":
        expr = f"avg({alias}.{q(f.column)}::DOUBLE)"
    elif f.agg == "count_distinct":
        expr = f"count(DISTINCT C.{q(f.column)})::DOUBLE"
    elif f.agg == "days_since_last":
        expr = f"date_diff('second', max(C.{q(c_tc)}), any_value(L.t)) / 86400.0"
    else:
        raise ValueError(f.agg)
    return f"SELECT L.rid, {expr} AS v FROM labels L {joins} {where} GROUP BY L.rid"


# Filled by build_features: table -> time column used for point-in-time filtering.
_time_cache: dict = {}


def load_labels(con, outcome: Outcome) -> pd.DataFrame:
    frames = []
    for split, rel in outcome.splits.items():
        df = pd.read_parquet(DATA / rel)
        df = df.rename(columns={outcome.entity_key: "key", "timestamp": "t", outcome.label_column: "y"})
        df["split"] = split
        frames.append(df[["key", "t", "y", "split"]])
    return register_labels(con, pd.concat(frames, ignore_index=True))


def register_labels(con, labels: pd.DataFrame) -> pd.DataFrame:
    """labels: columns key, t, y, split. Adds a row id and exposes it to SQL as temp table `labels`."""
    labels = labels.reset_index(drop=True).copy()
    labels["y"] = labels["y"].astype(int)
    labels.insert(0, "rid", np.arange(len(labels)))
    con.register("labels_df", labels)
    con.execute("CREATE OR REPLACE TEMP TABLE labels AS SELECT * FROM labels_df")
    con.unregister("labels_df")
    return labels


def build_features(con, s: Structure, outcome: Outcome, feats: list[Feature], labels: pd.DataFrame) -> pd.DataFrame:
    _time_cache.clear()
    for t in s.tables:
        _time_cache[t] = _time_col(s, t)
    X = labels[["rid"]].copy()
    n = len(X)
    for f in feats:
        part = con.execute(_feature_sql(f, outcome)).df().rename(columns={"v": f.id})
        assert part["rid"].is_unique, f"{f.id}: aggregation produced duplicate label rows"
        X = X.merge(part, on="rid", how="left")
        assert len(X) == n, f"{f.id}: row count changed after join"
        if f.agg in ("count", "count_distinct"):
            X[f.id] = X[f.id].fillna(0.0)
    return X.set_index("rid")


# ---------------------------------------------------------------------------------------------
# Label sanity check (does the supplied outcome match its stated definition?)

def check_label(con, outcome: Outcome, table: str, fk: str, time_col: str) -> dict:
    """Recompute 'more than one row in [t, t+horizon)' from an event table and compare to the label."""
    df = con.execute(f"""
        SELECT L.rid, L.y, count(E.{q(fk)}) AS n FROM labels L
        LEFT JOIN src.{q(table)} E ON E.{q(fk)} = L.key
             AND E.{q(time_col)} >= L.t AND E.{q(time_col)} < L.t + INTERVAL {outcome.horizon_days} DAY
        GROUP BY L.rid, L.y""").df()
    pred = (df["n"] > 1).astype(int)
    return {"table": table, "agreement": float((pred == df["y"]).mean()), "rows": int(len(df))}


# ---------------------------------------------------------------------------------------------
# Evaluation

def _auc(y, x) -> float:
    x = np.nan_to_num(np.asarray(x, dtype=float), nan=np.nanmedian(x) if np.isfinite(np.nanmedian(x)) else 0.0)
    if len(np.unique(y)) < 2 or np.all(x == x[0]):
        return 0.5
    return float(roc_auc_score(y, x))


def _bh(p: np.ndarray) -> np.ndarray:
    n = len(p)
    order = np.argsort(p)
    ranked = p[order] * n / (np.arange(n) + 1)
    q_ = np.minimum.accumulate(ranked[::-1])[::-1]
    out = np.empty(n)
    out[order] = np.minimum(q_, 1.0)
    return out


def evaluate(X: pd.DataFrame, labels: pd.DataFrame, feats: list[Feature], seed: int = 0) -> OutcomeResult:
    lab = labels.set_index("rid")
    cols = [f.id for f in feats]
    split = {k: lab.index[lab["split"] == k] for k in ("train", "val", "test")}
    Xs = {k: X.loc[v, cols] for k, v in split.items()}
    ys = {k: lab.loc[v, "y"].to_numpy() for k, v in split.items()}

    models = {
        "gradient_boosting": HistGradientBoostingClassifier(max_iter=300, learning_rate=0.05, random_state=seed),
        "logistic_regression": make_pipeline(
            SimpleImputer(strategy="median"),
            FunctionTransformer(lambda a: np.sign(a) * np.log1p(np.abs(a))),
            StandardScaler(),
            LogisticRegression(max_iter=2000),
        ),
    }
    model_results = {}
    for name, m in models.items():
        m.fit(Xs["train"], ys["train"])
        model_results[name] = {
            "val_auroc": _auc(ys["val"], m.predict_proba(Xs["val"])[:, 1]),
            "test_auroc": _auc(ys["test"], m.predict_proba(Xs["test"])[:, 1]),
        }
    best = max(model_results, key=lambda k: model_results[k]["val_auroc"])
    model_results["selected_on_val"] = best

    # Baselines: base rate, and the best single past-activity count (chosen on val).
    count_feats = [f for f in feats if f.agg == "count" and len(f.path) == 1 and f.window_days is None]
    best_single = max(count_feats, key=lambda f: _auc(ys["val"], Xs["val"][f.id]), default=None)
    baselines = {"base_rate_auroc": 0.5}
    if best_single:
        baselines["single_activity_count"] = {
            "feature": best_single.id,
            "val_auroc": _auc(ys["val"], Xs["val"][best_single.id]),
            "test_auroc": _auc(ys["test"], Xs["test"][best_single.id]),
        }

    # Permutation importance of the selected model on validation.
    pi = permutation_importance(models[best], Xs["val"], ys["val"], scoring="roc_auc",
                                n_repeats=5, random_state=seed, n_jobs=-1)

    # Univariate association on train, BH-corrected; stability across train cutoffs.
    tr = Xs["train"]
    cutoffs = labels.loc[labels["split"] == "train", "t"].to_numpy()
    stats = []
    pvals = []
    for i, f in enumerate(feats):
        x = tr[f.id].to_numpy(dtype=float)
        ok = ~np.isnan(x)
        y = ys["train"]
        if ok.sum() > 10 and len(np.unique(x[ok])) > 1 and len(np.unique(y[ok])) > 1:
            p = mannwhitneyu(x[ok & (y == 1)], x[ok & (y == 0)]).pvalue
        else:
            p = 1.0
        pvals.append(p)
        per_cut = []
        for c in np.unique(cutoffs):
            m = cutoffs == c
            if m.sum() > 200:
                per_cut.append(_auc(y[m], x[m]))
        auc_tr = _auc(y, x)
        stats.append({
            "feature": f.id,
            "coverage": float(ok.mean()),
            "train_auroc": auc_tr,
            "val_auroc": _auc(ys["val"], Xs["val"][f.id]),
            "direction": "higher_in_positive" if auc_tr > 0.5 else "lower_in_positive",
            "per_cutoff_auroc_min": float(min(per_cut)) if per_cut else None,
            "per_cutoff_auroc_max": float(max(per_cut)) if per_cut else None,
            "direction_stable": bool(per_cut) and (all(a > 0.5 for a in per_cut) or all(a < 0.5 for a in per_cut)),
            "n_cutoffs": len(per_cut),
            "perm_importance_mean": float(pi.importances_mean[i]),
            "perm_importance_std": float(pi.importances_std[i]),
            "p_value": float(p),
        })
    qv = _bh(np.array(pvals))
    for st, qq in zip(stats, qv):
        st["q_value_bh"] = float(qq)
        st["significant_fdr05"] = bool(qq < FDR_Q)

    # Roll importance up to relationship paths.
    by_path: dict = {}
    for f, st in zip(feats, stats):
        key = " | ".join(">".join(e) for e in f.path) or "(target table attributes)"
        d = by_path.setdefault(key, {"path": f.path, "importance": 0.0, "features": []})
        d["importance"] += max(st["perm_importance_mean"], 0.0)
        d["features"].append(f.id)
    path_importance = sorted(by_path.values(), key=lambda d: -d["importance"])

    return OutcomeResult(
        features=[asdict(f) for f in feats],
        label_check={},
        models=model_results,
        baselines=baselines,
        feature_stats=stats,
        path_importance=path_importance,
        n_rows={k: int(len(v)) for k, v in split.items()},
        base_rate={k: float(v.mean()) for k, v in ys.items()},
    )


def analyze(con, s: Structure, outcome: Outcome) -> OutcomeResult:
    labels = load_labels(con, outcome)
    feats = plan_features(s, outcome)
    X = build_features(con, s, outcome, feats, labels)
    res = evaluate(X, labels, feats)
    return res
