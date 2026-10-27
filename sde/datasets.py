"""Dataset registry: where each dataset comes from, and the outcome a user supplies for it.

The outcome spec is an *input* to the system (the business tells us what it cares about).
Nothing here describes the schema's relationships or semantics; those are what the system
must discover.
"""
from __future__ import annotations

import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from urllib.request import urlretrieve

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RELBENCH = "https://relbench.stanford.edu/download"


@dataclass(frozen=True)
class Outcome:
    entity_table: str          # table whose rows the outcome is defined on
    entity_key: str            # key column in that table (and in the label files)
    label_column: str          # label column in the label files
    horizon_days: int          # label window after each cutoff
    description: str           # business definition, with names unmasked
    description_masked: str    # same definition with {table}/{key} placeholders, for masked runs
    splits: dict = field(default_factory=dict)  # split name -> parquet path (relative to DATA)


@dataclass(frozen=True)
class Dataset:
    name: str
    urls: dict                 # local zip name -> URL
    outcome: Outcome | None = None

    @property
    def dir(self) -> Path:
        return DATA / self.name

    @property
    def db_path(self) -> Path:
        return self.dir / "source.duckdb"


DATASETS = {
    "avito": Dataset(
        name="avito",
        urls={
            "db.zip": f"{RELBENCH}/rel-avito/db.zip",
            "user-visits.zip": f"{RELBENCH}/rel-avito/tasks/user-visits.zip",
        },
        outcome=Outcome(
            entity_table="UserInfo",
            entity_key="UserID",
            label_column="num_click",
            horizon_days=4,
            description=(
                "User engagement: whether the user visits more than one ad in the 4 days "
                "after the cutoff timestamp."
            ),
            description_masked=(
                "Engagement: whether the entity identified by {table}.{key} has more than one "
                "qualifying interaction in the 4 days after the cutoff timestamp."
            ),
            splits={
                "train": "avito/tasks/user-visits/train.parquet",
                "val": "avito/tasks/user-visits/val.parquet",
                "test": "avito/tasks/user-visits/test.parquet",
            },
        ),
    ),
    # Development dataset: used only to sanity-check structural heuristics.
    "f1": Dataset(name="f1", urls={"db.zip": f"{RELBENCH}/rel-f1/db.zip"}),
}


def download(ds: Dataset) -> None:
    """Fetch and unzip the raw parquet files. Idempotent."""
    raw = ds.dir / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    for fname, url in ds.urls.items():
        dest = raw / fname
        if not dest.exists():
            print(f"downloading {url}")
            urlretrieve(url, dest)
        target = ds.dir / ("tasks" if fname != "db.zip" else "")
        with zipfile.ZipFile(dest) as z:
            z.extractall(target)
