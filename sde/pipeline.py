"""End-to-end experiment: discover -> outcome -> evidence packets -> interpret (A/B/C x names) -> score -> report."""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

from . import db, evidence, outcome, report, scoring, structure
from .datasets import DATASETS, ROOT, download
from .llm import LLMError, call_json

RESULTS = ROOT / "results"


def _dump(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1, default=str, ensure_ascii=False))


class Experiment:
    def __init__(self, dataset: str = "avito", runs: int = 3, replay_only: bool = False):
        self.ds = DATASETS[dataset]
        self.runs = runs
        self.replay_only = replay_only
        self.out = RESULTS / dataset
        self.truth = scoring.load_truth(ROOT / "eval" / "ground_truth" / f"{dataset}.json")
        self.timings: dict = {}
        self._con = None
        self._s = None
        self._o = None

    # -- stages -----------------------------------------------------------------------------
    def prepare(self):
        download(self.ds)
        db.ingest(self.ds)

    @property
    def con(self):
        if self._con is None:
            self._con = db.connect(self.ds)
        return self._con

    def discover(self) -> structure.Structure:
        if self._s is None:
            t0 = time.time()
            self._s = structure.discover(self.con, self.ds.name)
            self.timings["structural_discovery_s"] = round(time.time() - t0, 1)
            _dump(self.out / "structure.json", self._s.to_dict())
            _dump(self.out / "structural_scores.json", scoring.structural_scores(self._s, self.truth))
        return self._s

    def outcome(self, rebuild: bool = False) -> dict:
        # The saved outcome analysis is the evidence of record: reuse it unless asked to rebuild.
        if self._o is None and not rebuild and (self.out / "outcome.json").exists():
            self._o = json.loads((self.out / "outcome.json").read_text())
        if self._o is None:
            s = self.discover()
            t0 = time.time()
            res = outcome.analyze(self.con, s, self.ds.outcome).to_dict()
            # Data-validity check only (not given to the LLM): does the label match its stated definition?
            lc = self.ds.outcome.label_check
            res["label_check"] = outcome.check_label(self.con, self.ds.outcome, **lc) if lc else {}
            self.timings["outcome_analysis_s"] = round(time.time() - t0, 1)
            self._o = res
            _dump(self.out / "outcome.json", res)
        return self._o

    def cells(self):
        for cfg in evidence.CONFIGS:
            for naming in evidence.NAMINGS:
                yield cfg, naming

    def packet(self, cfg: str, naming: str, rebuild: bool = False):
        """Evidence packet for one cell. A saved packet is reused, so recorded LLM runs always match what the model saw."""
        s = self.discover()
        namer = evidence.Namer(s, masked=(naming == "masked"))
        p = self.out / "packets" / f"{cfg}_{naming}.md"
        if p.exists() and not rebuild:
            text = p.read_text()
            return text, set(re.findall(r"\[([SP]:[^\]\s]+)\]", text)), namer
        o = self.outcome() if cfg == "C" else None
        text, ids = evidence.build(cfg, s, self.ds.outcome, o, namer)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return text, ids, namer

    def interpret(self):
        for cfg, naming in self.cells():
            text, _, _ = self.packet(cfg, naming)
            for r in range(1, self.runs + 1):
                path = self.out / "runs" / f"{cfg}_{naming}_r{r}.json"
                try:
                    rec = call_json(path, evidence.SYSTEM_PROMPT, evidence.user_message(text),
                                    evidence.OUTPUT_SCHEMA, effort="high", replay_only=self.replay_only)
                    print(f"interpret {cfg}/{naming}/r{r}: {rec['seconds']}s ${rec['cost_usd']}")
                except LLMError as e:
                    print(f"interpret {cfg}/{naming}/r{r}: FAILED {e}")

    def score(self) -> dict:
        all_scores = {}
        for cfg, naming in self.cells():
            text, ids, namer = self.packet(cfg, naming)
            for r in range(1, self.runs + 1):
                run_path = self.out / "runs" / f"{cfg}_{naming}_r{r}.json"
                if not run_path.exists():
                    continue
                rec = json.loads(run_path.read_text())
                items, missing, statements = scoring.judge_items(rec["output"], namer, self.truth, seed=r)
                jrec = scoring.run_judge(self.out / "judge" / f"{cfg}_{naming}_r{r}.json", items, statements,
                                         replay_only=self.replay_only, signals=scoring.judge_signals(self.truth))
                sc = scoring.score_run(rec["output"], namer, self.truth, ids, jrec, items, missing, statements)
                sc["cost_usd"] = rec["cost_usd"]
                sc["judge_cost_usd"] = jrec["cost_usd"]
                sc["seconds"] = rec["seconds"]
                sc["usage"] = rec["usage"]
                all_scores[f"{cfg}_{naming}_r{r}"] = sc
                # Judge audit sheet: every decision, with real names, for human review.
                _dump(self.out / "judge_audit" / f"{cfg}_{naming}_r{r}.json", [
                    {**it, "score": next((g["score"] for g in jrec["output"]["items"] if g["id"] == it["id"]), None),
                     "rationale": next((g["rationale"] for g in jrec["output"]["items"] if g["id"] == it["id"]), None)}
                    for it in items])
        _dump(self.out / "scores.json", all_scores)
        return all_scores

    def report(self):
        report.write_all(self)

    def run_all(self):
        if not self.replay_only:
            self.prepare()
        self.discover()
        self.outcome()
        for cfg, naming in self.cells():
            self.packet(cfg, naming)
        self.interpret()
        self.score()
        _dump(self.out / "timings.json", self.timings)
        self.report()
