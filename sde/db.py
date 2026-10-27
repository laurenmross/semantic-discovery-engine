"""DuckDB access. The source database is built once from parquet, then only ever attached read-only."""
from __future__ import annotations

import duckdb

from .datasets import Dataset


def ingest(ds: Dataset) -> None:
    """Build source.duckdb from the parquet files (plain tables: no keys or constraints).

    This plays the role of an undocumented warehouse: RelBench's key metadata in the parquet
    footers is NOT carried into DuckDB.
    """
    if ds.db_path.exists():
        return
    con = duckdb.connect(str(ds.db_path))
    for f in sorted((ds.dir / "db").glob("*.parquet")):
        con.execute(f'CREATE TABLE "{f.stem}" AS SELECT * FROM read_parquet(?)', [str(f)])
    con.close()


def connect(ds: Dataset) -> duckdb.DuckDBPyConnection:
    """In-memory working connection with the source attached READ_ONLY as schema `src`.

    Scratch objects (temp tables) live in memory; the source cannot be written.
    """
    con = duckdb.connect()
    con.execute(f"ATTACH '{ds.db_path}' AS src (READ_ONLY)")
    return con


def tables(con) -> list[str]:
    rows = con.execute(
        "SELECT table_name FROM duckdb_tables() WHERE database_name='src' ORDER BY 1"
    ).fetchall()
    return [r[0] for r in rows]


def columns(con, table: str) -> list[tuple[str, str]]:
    rows = con.execute(
        "SELECT column_name, data_type FROM duckdb_columns() "
        "WHERE database_name='src' AND table_name=? ORDER BY column_index",
        [table],
    ).fetchall()
    return [(r[0], r[1]) for r in rows]


def q(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'
