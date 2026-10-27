"""Thin Claude client with an on-disk record of every call.

Each call is saved (request hash, response JSON, token usage, wall time) under results/. Re-running
the pipeline replays saved calls instead of calling the API, so anyone can reproduce the scoring and
report without an API key, and the exact model outputs behind every number are inspectable.
"""
from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path

MODEL = "claude-opus-5-5"
PRICE_PER_MTOK = {"input": 4.00, "output": 20.00, "cache_read": 0.20, "cache_write": 5.00}


class LLMError(RuntimeError):
    pass


def _load_dotenv() -> None:
    env = Path(__file__).resolve().parent.parent / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def cost_usd(usage: dict) -> float:
    return (usage.get("input_tokens", 0) * PRICE_PER_MTOK["input"]
            + usage.get("output_tokens", 0) * PRICE_PER_MTOK["output"]
            + usage.get("cache_read_input_tokens", 0) * PRICE_PER_MTOK["cache_read"]
            + usage.get("cache_creation_input_tokens", 0) * PRICE_PER_MTOK["cache_write"]) / 1e6


def call_json(record_path: Path, system: str, user: str, schema: dict, effort: str, max_tokens: int = 32000,
              replay_only: bool = False) -> dict:
    """Return {"output": parsed JSON, "usage": {...}, "seconds": float, "model": str, "request_sha": str}.

    If record_path exists, it is replayed without calling the API.
    """
    sha = hashlib.sha256(json.dumps([MODEL, effort, system, user, schema], sort_keys=True).encode()).hexdigest()[:16]
    if record_path.exists():
        rec = json.loads(record_path.read_text())
        if rec.get("request_sha") != sha:
            print(f"warning: {record_path.name} was recorded from a different prompt ({rec.get('request_sha')} != {sha}); replaying anyway")
        return rec
    if replay_only:
        raise LLMError(f"no recorded response at {record_path} and replay_only is set")

    _load_dotenv()
    import anthropic  # imported lazily so replay works without the SDK configured

    client = anthropic.Anthropic()
    t0 = time.time()
    with client.messages.stream(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
        output_config={"effort": effort, "format": {"type": "json_schema", "schema": schema}},
    ) as stream:
        msg = stream.get_final_message()
    seconds = time.time() - t0
    if msg.stop_reason == "refusal":
        raise LLMError(f"refusal: {msg.stop_details}")
    if msg.stop_reason == "max_tokens":
        raise LLMError("hit max_tokens before finishing the JSON output")
    text = next(b.text for b in msg.content if b.type == "text")
    usage = {k: getattr(msg.usage, k, 0) or 0 for k in
             ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")}
    rec = {"model": msg.model, "effort": effort, "request_sha": sha, "seconds": round(seconds, 1),
           "usage": usage, "cost_usd": round(cost_usd(usage), 4), "stop_reason": msg.stop_reason,
           "output": json.loads(text)}
    record_path.parent.mkdir(parents=True, exist_ok=True)
    record_path.write_text(json.dumps(rec, indent=1, ensure_ascii=False))
    return rec
