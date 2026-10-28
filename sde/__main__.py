"""Command line: python -m sde <stage> [--dataset avito] [--runs 3] [--replay-only]"""
from __future__ import annotations

import argparse

from .pipeline import Experiment


def main() -> None:
    ap = argparse.ArgumentParser(prog="python -m sde", description=__doc__)
    ap.add_argument("stage", choices=["prepare", "discover", "outcome", "packets", "interpret", "score", "report", "all"])
    ap.add_argument("--dataset", default="avito")
    ap.add_argument("--runs", type=int, default=3, help="interpretation runs per cell")
    ap.add_argument("--replay-only", action="store_true", help="never call the API; use recorded responses only")
    ap.add_argument("--rebuild", action="store_true", help="recompute outcome.json and packets even if saved copies exist")
    a = ap.parse_args()
    exp = Experiment(a.dataset, runs=a.runs, replay_only=a.replay_only)
    if a.stage == "prepare":
        exp.prepare()
    elif a.stage == "discover":
        exp.discover()
    elif a.stage == "outcome":
        exp.outcome(rebuild=True)
    elif a.stage == "packets":
        exp.outcome(rebuild=a.rebuild)
        for cfg, naming in exp.cells():
            exp.packet(cfg, naming, rebuild=True)
    elif a.stage == "interpret":
        exp.interpret()
    elif a.stage == "score":
        exp.score()
    elif a.stage == "report":
        exp.discover(); exp.report()
    else:
        exp.run_all()
    print(f"outputs in {exp.out}")


if __name__ == "__main__":
    main()
