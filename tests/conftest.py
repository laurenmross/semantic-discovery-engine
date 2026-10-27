"""A tiny synthetic 'unfamiliar' database with known structure, used by every test."""
from types import SimpleNamespace

import duckdb
import pytest


@pytest.fixture()
def tiny_db(tmp_path):
    path = tmp_path / "source.duckdb"
    con = duckdb.connect(str(path))
    # Sparse non-sequential ids so value overlap is informative; plus a small-integer measure.
    con.execute("CREATE TABLE accounts AS SELECT i * 7 + 1000 AS acct, (i % 3) AS tier FROM range(200) t(i)")
    con.execute("CREATE TABLE plans AS SELECT i + 500 AS plan_id, (i * 10.0 + 0.99) AS price FROM range(30) t(i)")
    con.execute("""CREATE TABLE events AS
        SELECT (i % 200) * 7 + 1000 AS who, (i % 30) + 500 AS plan_ref, (i % 5) + 1 AS slot,
               TIMESTAMP '2024-01-01' + INTERVAL (i % 40) DAY AS happened_at
        FROM range(4000) t(i)""")
    con.close()
    return SimpleNamespace(name="tiny", db_path=path)
