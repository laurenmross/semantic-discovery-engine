"""Component A: structural discovery.

Everything here is name-agnostic: keys and relationships are inferred from values, never from
column names, so the same evidence is produced whether or not names are later masked.
Thresholds are fixed in eval/protocol.md section 9.
"""
from __future__ import annotations

import itertools
from dataclasses import asdict, dataclass, field

import networkx as nx

from . import db
from .db import q

INT_TYPES = ("TINYINT", "SMALLINT", "INTEGER", "BIGINT", "HUGEINT", "UTINYINT", "USMALLINT", "UINTEGER", "UBIGINT")
FLOAT_TYPES = ("FLOAT", "DOUBLE", "REAL")
TIME_PREFIXES = ("TIMESTAMP", "DATE")

# Protocol section 9.
INCLUSION_MIN = 0.95
CHILD_DISTINCT_MIN = 2
WEAK_DISTINCT_MAX = 100
WEAK_START_MAX = 1
MAX_PATH_HOPS = 3
# Amendment 1: feature eligibility (component B only).
ELIGIBLE_CHILD_DISTINCT = 20
ELIGIBLE_PARENT_FRACTION = 0.5


@dataclass
class ColumnProfile:
    table: str
    column: str
    dtype: str
    family: str                # int | float | integral_float | string | time | bool | other
    rows: int
    nulls: int
    distinct: int
    unique: bool
    min: str | None = None
    max: str | None = None
    mean: float | None = None
    avg_len: float | None = None
    top_values: list = field(default_factory=list)   # [(value, count)] for low-cardinality columns
    samples: list = field(default_factory=list)      # 3 example non-null values

    @property
    def null_frac(self) -> float:
        return self.nulls / self.rows if self.rows else 0.0

    @property
    def is_candidate_key(self) -> bool:
        return self.unique and self.nulls == 0 and self.family in ("int", "integral_float", "string") and self.rows > 1


@dataclass
class Relationship:
    child_table: str
    child_column: str
    parent_table: str
    parent_column: str
    inclusion: float           # share of distinct child values found in the parent key
    child_distinct: int
    parent_rows: int
    parent_coverage: float     # share of parent keys referenced at least once
    rows_per_parent_avg: float
    rows_per_parent_max: int
    weak: bool                 # protocol 9: overlapping small-integer ranges
    feature_eligible: bool     # amendment 1
    range_density: float = 0.0 # share of the child's value range occupied by parent keys (1.0 = inclusion is uninformative)
    child_is_key: bool = False # the child column is itself unique in its table
    parent_rank: int = 1       # rank among this child column's candidate parents, by parent_coverage
    best_parent: bool = True   # amendment 1: the preferred parent for this child column


@dataclass
class Structure:
    dataset: str
    tables: dict               # table -> {"rows": int, "columns": [ColumnProfile]}
    keys: list                 # [(table, column)]
    relationships: list        # [Relationship]
    time_columns: dict         # table -> [column]
    join_paths: list           # [[table, ...]]
    ambiguities: list          # [dict]

    def to_dict(self) -> dict:
        return {
            "dataset": self.dataset,
            "tables": {t: {"rows": v["rows"], "columns": [asdict(c) for c in v["columns"]]} for t, v in self.tables.items()},
            "keys": self.keys,
            "relationships": [asdict(r) for r in self.relationships],
            "time_columns": self.time_columns,
            "join_paths": self.join_paths,
            "ambiguities": self.ambiguities,
        }

    def profile(self, table: str, column: str) -> ColumnProfile:
        return next(c for c in self.tables[table]["columns"] if c.column == column)


def _family(dtype: str) -> str:
    d = dtype.upper()
    if d.startswith(INT_TYPES):
        return "int"
    if d.startswith(FLOAT_TYPES) or d.startswith("DECIMAL"):
        return "float"
    if d.startswith(TIME_PREFIXES):
        return "time"
    if d == "BOOLEAN":
        return "bool"
    if d == "VARCHAR":
        return "string"
    return "other"


def profile_column(con, table: str, column: str, dtype: str) -> ColumnProfile:
    t, c = f"src.{q(table)}", q(column)
    fam = _family(dtype)
    rows, nulls, distinct, mn, mx = con.execute(
        f"SELECT count(*), count(*) - count({c}), count(DISTINCT {c}), min({c})::VARCHAR, max({c})::VARCHAR FROM {t}"
    ).fetchall()[0]
    p = ColumnProfile(table, column, dtype, fam, rows, nulls, distinct,
                      unique=(distinct == rows - nulls and rows > 0), min=mn, max=mx)
    if fam == "float":
        non_integral = con.execute(
            f"SELECT count(*) FROM {t} WHERE {c} IS NOT NULL AND {c} <> floor({c})"
        ).fetchall()[0][0]
        if non_integral == 0 and distinct > 0:
            p.family = "integral_float"
    if p.family in ("int", "float", "integral_float", "bool"):
        p.mean = con.execute(f"SELECT avg({c}::DOUBLE) FROM {t}").fetchall()[0][0]
    if fam == "string":
        p.avg_len = con.execute(f"SELECT avg(length({c})) FROM {t}").fetchall()[0][0]
    if distinct <= 20:
        p.top_values = [
            (str(v), n) for v, n in con.execute(
                f"SELECT {c}::VARCHAR, count(*) n FROM {t} GROUP BY 1 ORDER BY n DESC, 1 LIMIT 20"
            ).fetchall()
        ]
    p.samples = [
        str(r[0]) for r in con.execute(
            f"SELECT DISTINCT {c}::VARCHAR FROM (SELECT {c} FROM {t} WHERE {c} IS NOT NULL LIMIT 1000) LIMIT 3"
        ).fetchall()
    ]
    return p


def _key_like(p: ColumnProfile) -> bool:
    return p.family in ("int", "integral_float", "string") and p.distinct >= CHILD_DISTINCT_MIN


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _is_weak(child: ColumnProfile, parent: ColumnProfile) -> bool:
    small = child.distinct <= WEAK_DISTINCT_MAX and parent.distinct <= WEAK_DISTINCT_MAX
    starts = [_num(child.min), _num(parent.min)]
    near_zero = all(s is not None and s <= WEAK_START_MAX for s in starts)
    return small and near_zero


def infer_relationships(con, profiles: dict, keys: list) -> list[Relationship]:
    rels = []
    # Materialise each candidate child column's distinct values once.
    child_cols = [p for cols in profiles.values() for p in cols if _key_like(p)]
    for i, p in enumerate(child_cols):
        con.execute(
            f"CREATE OR REPLACE TEMP TABLE d{i} AS SELECT DISTINCT {q(p.column)} AS v "
            f"FROM src.{q(p.table)} WHERE {q(p.column)} IS NOT NULL"
        )
    for (pt, pc) in keys:
        parent = next(c for c in profiles[pt] if c.column == pc)
        for i, child in enumerate(child_cols):
            if (child.table, child.column) == (pt, pc):
                continue
            # Compatible type families: strings with strings, integer-like with integer-like.
            if (child.family == "string") != (parent.family == "string"):
                continue
            hit = con.execute(
                f"SELECT count(*) FROM d{i} WHERE v IN (SELECT {q(pc)} FROM src.{q(pt)})"
            ).fetchall()[0][0]
            inclusion = hit / child.distinct
            if inclusion < INCLUSION_MIN or parent.rows <= 1:
                continue
            avg_rpp, max_rpp = con.execute(
                f"SELECT avg(n), max(n) FROM (SELECT count(*) n FROM src.{q(child.table)} "
                f"WHERE {q(child.column)} IS NOT NULL GROUP BY {q(child.column)})"
            ).fetchall()[0]
            lo, hi = _num(child.min), _num(child.max)
            density = 1.0
            if child.family != "string" and lo is not None and hi is not None:
                in_range = con.execute(
                    f"SELECT count(DISTINCT {q(pc)}) FROM src.{q(pt)} WHERE {q(pc)} BETWEEN ? AND ?", [lo, hi]
                ).fetchall()[0][0]
                density = in_range / (hi - lo + 1)
            rels.append(Relationship(
                child.table, child.column, pt, pc,
                inclusion=round(inclusion, 4),
                child_distinct=child.distinct,
                parent_rows=parent.rows,
                parent_coverage=round(hit / parent.distinct, 4),
                rows_per_parent_avg=round(float(avg_rpp or 0), 2),
                rows_per_parent_max=int(max_rpp or 0),
                weak=_is_weak(child, parent),
                feature_eligible=child.distinct >= min(ELIGIBLE_CHILD_DISTINCT, ELIGIBLE_PARENT_FRACTION * parent.rows),
                range_density=round(min(density, 1.0), 4),
                child_is_key=child.is_candidate_key,
            ))
    _rank_parents(rels)
    return rels


def _rank_parents(rels: list[Relationship]) -> None:
    """Amendment 1: choose one preferred parent per child column.

    When keys are dense integer sequences, a child column passes the inclusion test against many
    keys. The true parent is usually the one whose key set the child covers most completely.
    A unique child column (key-to-key) is only preferred if the two keys cover each other
    (a 1:1 extension table).
    """
    by_child: dict = {}
    for r in rels:
        by_child.setdefault((r.child_table, r.child_column), []).append(r)
    for rs in by_child.values():
        rs.sort(key=lambda r: (-r.parent_coverage, abs(r.parent_rows - r.child_distinct)))
        for i, r in enumerate(rs, 1):
            r.parent_rank = i
            one_to_one = r.child_is_key and r.parent_coverage >= INCLUSION_MIN
            r.best_parent = i == 1 and (not r.child_is_key or one_to_one)
            r.feature_eligible = r.feature_eligible and r.best_parent and not r.weak


def join_paths(tables: list[str], rels: list[Relationship]) -> list[list[str]]:
    g = nx.Graph()
    g.add_nodes_from(tables)
    for r in rels:
        if r.feature_eligible and r.child_table != r.parent_table:
            g.add_edge(r.child_table, r.parent_table)
    paths = []
    for a, b in itertools.combinations(sorted(tables), 2):
        try:
            p = nx.shortest_path(g, a, b)
        except nx.NetworkXNoPath:
            continue
        if 2 <= len(p) - 1 <= MAX_PATH_HOPS:
            paths.append(p)
    return paths


def find_ambiguities(profiles: dict, keys: list, rels: list[Relationship]) -> list[dict]:
    out = []
    by_child: dict = {}
    for r in rels:
        by_child.setdefault((r.child_table, r.child_column), []).append(r)
    for (t, c), rs in sorted(by_child.items()):
        if len(rs) > 1:
            out.append({"type": "multiple_parents", "table": t, "column": c,
                        "detail": [f"{r.parent_table}.{r.parent_column}" for r in rs]})
    for r in rels:
        if r.weak:
            out.append({"type": "weak_overlap", "table": r.child_table, "column": r.child_column,
                        "detail": f"{r.parent_table}.{r.parent_column}: small overlapping integer ranges; may be coincidental"})
        elif not r.feature_eligible:
            out.append({"type": "low_support", "table": r.child_table, "column": r.child_column,
                        "detail": f"{r.parent_table}.{r.parent_column}: only {r.child_distinct} distinct child values; may be coincidental"})
    linked = set(by_child) | {tuple(k) for k in keys}
    for t, cols in profiles.items():
        if not any(k[0] == t for k in keys):
            out.append({"type": "no_candidate_key", "table": t, "column": None,
                        "detail": "no single column is unique and non-null (event log, or composite key?)"})
        for p in cols:
            # Identifier-looking columns with many values that match no key in this database.
            if (t, p.column) not in linked and p.family in ("int", "integral_float") and p.distinct > 1000 and not p.unique:
                out.append({"type": "unmatched_identifier", "table": t, "column": p.column,
                            "detail": f"{p.distinct} distinct integer values matching no key here; possibly a reference to a table not present, or a measure"})
        times = [p.column for p in cols if p.family == "time"]
        if len(times) > 1:
            out.append({"type": "multiple_time_columns", "table": t, "column": None, "detail": times})
    return out


def discover(con, dataset: str) -> Structure:
    profiles = {}
    for t in db.tables(con):
        profiles[t] = [profile_column(con, t, c, d) for c, d in db.columns(con, t)]
    keys = [(t, p.column) for t, cols in profiles.items() for p in cols if p.is_candidate_key]
    rels = infer_relationships(con, profiles, keys)
    time_cols = {t: [p.column for p in cols if p.family == "time"] for t, cols in profiles.items()}
    time_cols = {t: v for t, v in time_cols.items() if v}
    return Structure(
        dataset=dataset,
        tables={t: {"rows": cols[0].rows if cols else 0, "columns": cols} for t, cols in profiles.items()},
        keys=keys,
        relationships=rels,
        time_columns=time_cols,
        join_paths=join_paths(list(profiles), rels),
        ambiguities=find_ambiguities(profiles, keys, rels),
    )
