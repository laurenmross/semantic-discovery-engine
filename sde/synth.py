"""Synthetic B2B SaaS warehouse with planted semantics and known ground truth.

Why synthetic: the first experiment showed the model recognises the public RelBench Avito data even with
names masked, so the schema-only baseline hit the ceiling. This generator produces a fictional company's
data, created fresh from a seed, which no model can have seen.

Design goals (each maps to something the evaluation can measure):
- Entity keys are sparse random integers, so value overlap is real evidence; lookup tables use dense
  small integers, so some joins stay genuinely ambiguous.
- Table and column names imitate a legacy warehouse (cryptic abbreviations): informative but not obvious.
- A latent account "fit" drives trial-to-paid conversion and, independently, early behaviour:
  planted positive signals (usage codes 7 and 4, invited users), planted negative signals
  (usage code 11, severity-1 tickets), and a planted null (scheduled lifecycle emails).
- Leakage trap: usage rises sharply after conversion and subscription rows exist only for converters,
  so any point-in-time bug shows up as implausibly high predictive performance.

Everything is deterministic given the seed.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20261027
N_ACCT = 20_000
START = pd.Timestamp("2025-07-01")
LAST_TRIAL = pd.Timestamp("2026-05-31")
DATA_END = pd.Timestamp("2026-06-30")
OBS_DAYS = 5          # labels are evaluated at trial day 5
WINDOW_DAYS = 21      # conversion counts if it happens within 21 days of trial start
N_CODES = 15

PLANS = pd.DataFrame({
    "pln_id": [1, 2, 3, 4, 5, 6],
    "list_px": [29.0, 79.0, 149.0, 399.0, 999.0, 15.0],
    "seat_cap": [3, 10, 25, 100, 500, 50],
    "tier_rank": [1, 2, 3, 4, 5, 1],
})
SEG_PLANS = {1: [1, 2], 2: [2, 3], 3: [4, 5], 4: [6]}
EMAIL_DAYS = [0, 1, 3, 5, 8, 12, 16, 20]


def _sparse_ids(rng, n, lo, hi):
    return rng.choice(np.arange(lo, hi), size=n, replace=False)


def generate(out_dir: Path, seed: int = SEED, n_acct: int = N_ACCT) -> dict:
    rng = np.random.default_rng(seed)
    out_dir = Path(out_dir)
    (out_dir / "db").mkdir(parents=True, exist_ok=True)
    (out_dir / "tasks" / "trial-conversion").mkdir(parents=True, exist_ok=True)

    # --- reference tables ---
    geo = pd.DataFrame({"geo_id": np.arange(1, 41)})
    geo["rgn_cd"] = rng.integers(1, 6, len(geo))
    tz_by_region = {1: -8, 2: -5, 3: 0, 4: 1, 5: 9}
    geo["tz_off"] = [tz_by_region[r] + int(rng.integers(-1, 2)) for r in geo["rgn_cd"]]

    # --- accounts ---
    acct_key = _sparse_ids(rng, n_acct, 10_000_000, 99_999_999)
    span = (LAST_TRIAL - START).total_seconds()
    crt = START + pd.to_timedelta(np.sort(rng.uniform(0, span, n_acct)), unit="s")
    seg = rng.choice([1, 2, 3, 4], n_acct, p=[0.55, 0.30, 0.10, 0.05])
    src = rng.choice([1, 2, 3, 4, 5, 6], n_acct, p=[0.15, 0.30, 0.20, 0.15, 0.10, 0.10])
    emp = np.clip(seg * 2 - 1 + rng.integers(-1, 2, n_acct), 1, 7)
    z = rng.normal(0, 1, n_acct)                              # latent fit (never stored)
    seg_eff = np.array([0, 0.0, 0.3, 0.5, -0.6])[seg]
    src_eff = np.array([0, 0.3, 0.0, -0.3, 0.0, -0.5, 0.1])[src]
    p_conv = 1 / (1 + np.exp(-(-1.7 + 1.1 * z + seg_eff + src_eff)))
    converts = rng.random(n_acct) < p_conv
    conv_day = rng.integers(2, WINDOW_DAYS, n_acct)            # day of conversion if converting
    conv_time = crt + pd.to_timedelta(conv_day, unit="D") + pd.to_timedelta(rng.uniform(0, 86_400, n_acct), unit="s")

    accounts = pd.DataFrame({
        "seg_cd": seg, "crt_ts": crt, "acct_key": acct_key, "src_cd": src,
        "geo_ref": rng.integers(1, 41, n_acct), "emp_band": emp,
    })

    # --- users and usage events (simulated per account, day by day; times in epoch seconds) ---
    DAY = 86_400.0
    crt_s = (crt - pd.Timestamp(0)).total_seconds().to_numpy()
    end_s = (DATA_END - pd.Timestamp(0)).total_seconds()
    base_w = np.array([8, 6, 5, 0, 7, 4, 0, 6, 5, 4, 0, 3, 3, 2, 2], dtype=float)  # codes 1..15
    users, events, tickets, emails = [], [], [], []
    user_id_pool = iter(_sparse_ids(rng, n_acct * 12, 100_000_000, 999_999_999).tolist())
    for i in range(n_acct):
        zi, t0 = z[i], crt_s[i]
        is_conv, cday = bool(converts[i]), int(conv_day[i])
        horizon = int(min(60, (end_s - t0) // DAY))
        w = base_w.copy()
        w[6] = 0.5 * np.exp(1.0 * zi)     # code 7: invite teammate (planted +)
        w[3] = 1.5 * np.exp(0.9 * zi)     # code 4: connect integration (planted +)
        w[10] = 2.0 * np.exp(-0.9 * zi)   # code 11: error encountered (planted -)
        w = w / w.sum()
        admin = next(user_id_pool)
        acct_users = [(admin, t0)]
        users.append((admin, acct_key[i], 1, None, t0))
        for d in range(horizon):
            day_start = t0 + d * DAY
            if is_conv and d >= cday:
                phase = 1.5
            elif d < 7:
                phase = 1.0          # trial users are most active in week one
            elif d < WINDOW_DAYS:
                phase = 0.5
            else:
                phase = 0.08 * np.exp(-(d - WINDOW_DAYS) / 7)
            lam = 3.0 * np.exp(0.3 * zi) * phase
            active = [(u, c) for u, c in acct_users if c <= day_start + DAY]
            counts = rng.poisson(lam, len(active))
            for (uid, ucrt), n in zip(active, counts):
                if n == 0:
                    continue
                codes = rng.choice(N_CODES, n, p=w) + 1
                secs = day_start + np.sort(rng.uniform(0, DAY, n))
                durs = np.round(rng.lognormal(7.5 + 0.08 * codes, 0.6))
                for c, ts, dur in zip(codes.tolist(), secs.tolist(), durs.tolist()):
                    if ts < ucrt:
                        ts = ucrt + float(rng.uniform(1, 600))
                    events.append((uid, c, ts, dur))
                    if c == 7 and len(acct_users) < 25 and rng.random() < 0.6:
                        new = next(user_id_pool)
                        nts = ts + float(rng.uniform(300, 172_800))
                        acct_users.append((new, nts))
                        users.append((new, acct_key[i], int(rng.choice([2, 3], p=[0.7, 0.3])), uid, nts))
            # support tickets
            if d < 30:
                for sev, rate in ((1, 0.04 * np.exp(-1.0 * zi)), (2, 0.015), (3, 0.025), (4, 0.02)):
                    for _ in range(rng.poisson(rate)):
                        ots = day_start + float(rng.uniform(0, DAY))
                        opener = acct_users[int(rng.integers(len(acct_users)))][0] if rng.random() < 0.8 else None
                        cls = ots + float(rng.gamma(2.0, 6.0 * sev)) * 3600
                        csat = int(rng.integers(1, 6)) if rng.random() < 0.6 else None
                        tickets.append((acct_key[i], opener, ots, sev, csat, cls if cls < end_s else None))
        # lifecycle emails: fixed schedule until conversion (planted null on volume)
        p_open = 1 / (1 + np.exp(-(-0.8 + 0.4 * zi)))
        for k, d in enumerate(EMAIL_DAYS):
            ets = t0 + d * DAY + 9 * 3600
            if (is_conv and d >= cday) or ets >= end_s:
                break
            op = rng.random() < p_open
            emails.append((acct_key[i], k + 1, ets, int(op), int(op and rng.random() < 0.3)))

    to_ts = lambda col: pd.to_datetime(col, unit="s").dt.floor("s")
    users_df = pd.DataFrame(users, columns=["usr_key", "acct_key", "role_cd", "inv_by", "crt_ts"])
    users_df["inv_by"] = users_df["inv_by"].astype("Int64")
    users_df["crt_ts"] = to_ts(users_df["crt_ts"])
    events_df = pd.DataFrame(events, columns=["usr_key", "evt_cd", "evt_ts", "dur_ms"])
    events_df["evt_ts"] = to_ts(events_df["evt_ts"])
    tickets_df = pd.DataFrame(tickets, columns=["acct_key", "usr_key", "opn_ts", "sev", "csat", "cls_ts"])
    tickets_df["usr_key"] = tickets_df["usr_key"].astype("Int64")
    tickets_df["csat"] = tickets_df["csat"].astype("Int64")
    tickets_df["opn_ts"] = to_ts(tickets_df["opn_ts"])
    tickets_df["cls_ts"] = to_ts(tickets_df["cls_ts"].astype(float))
    tickets_df.insert(0, "tkt_no", _sparse_ids(rng, len(tickets_df), 1_000_000, 9_999_999))
    emails_df = pd.DataFrame(emails, columns=["acct_key", "tmpl_cd", "snd_ts", "opn_flg", "clk_flg"])
    emails_df["snd_ts"] = to_ts(emails_df["snd_ts"])

    # --- subscriptions and invoice lines (converters only) ---
    conv_idx = np.where(converts)[0]
    subs = pd.DataFrame({
        "sub_key": _sparse_ids(rng, len(conv_idx), 500_000, 9_999_999),
        "acct_key": acct_key[conv_idx],
        "st_ts": conv_time[conv_idx],
        "pln_id": [int(rng.choice(SEG_PLANS[s])) for s in seg[conv_idx]],
    })
    churn = rng.random(len(subs)) < 0.25
    end = subs["st_ts"] + pd.to_timedelta(rng.integers(30, 240, len(subs)), unit="D")
    subs["end_ts"] = end.where(churn & (end < DATA_END))
    subs["stat_cd"] = np.where(subs["end_ts"].notna(), 2, np.where(rng.random(len(subs)) < 0.05, 3, 1))
    subs = subs[["sub_key", "acct_key", "pln_id", "st_ts", "end_ts", "stat_cd"]]
    seats = users_df.groupby("acct_key").size()
    lines = []
    for _, s in subs.iterrows():
        plan = PLANS.set_index("pln_id").loc[s["pln_id"]]
        stop = s["end_ts"] if pd.notna(s["end_ts"]) else DATA_END
        bill = s["st_ts"]
        while bill < stop:
            base = plan["list_px"] * 100
            extra = max(0, int(seats.get(s["acct_key"], 1)) - int(plan["seat_cap"]))
            lines.append((s["sub_key"], 1, base, bill))
            sub_total = base
            if extra:
                lines.append((s["sub_key"], 2, extra * 500.0, bill))
                sub_total += extra * 500.0
            lines.append((s["sub_key"], 3, round(sub_total * 0.08), bill))
            if rng.random() < 0.03:
                lines.append((s["sub_key"], 4, -round(base * rng.uniform(0.1, 1.0)), bill))
            bill = bill + pd.Timedelta(days=30)
    inv = pd.DataFrame(lines, columns=["sub_key", "ln_typ", "amt", "bill_ts"])
    inv.insert(0, "inv_ln_key", _sparse_ids(rng, len(inv), 10_000_000, 99_999_999))

    tables = {
        "ACCT_MSTR": accounts,
        "GEO_REF": geo,
        "USR_XREF": users_df,
        "PLN_REF": PLANS,
        "SUB_HDR": subs,
        "INV_LN": inv,
        "EVT_STRM_01": events_df,
        "EVT_STRM_02": emails_df,
        "TKT_LOG": tickets_df,
    }
    for name, df in tables.items():
        df.to_parquet(out_dir / "db" / f"{name}.parquet", index=False)

    # --- labels: evaluated at trial day 5, for accounts not yet converted ---
    t_cut = crt + pd.Timedelta(days=OBS_DAYS)
    eligible = ~(converts & (conv_time < t_cut))
    lab = pd.DataFrame({"acct_key": acct_key, "timestamp": t_cut,
                        "converted": converts & (conv_time >= t_cut) & (conv_time < crt + pd.Timedelta(days=WINDOW_DAYS))})[eligible]
    splits = {"train": lab["timestamp"] < pd.Timestamp("2026-02-01"),
              "val": (lab["timestamp"] >= pd.Timestamp("2026-02-01")) & (lab["timestamp"] < pd.Timestamp("2026-04-01")),
              "test": lab["timestamp"] >= pd.Timestamp("2026-04-01")}
    for k, m in splits.items():
        lab[m].to_parquet(out_dir / "tasks" / "trial-conversion" / f"{k}.parquet", index=False)

    return {name: len(df) for name, df in tables.items()} | {"labels": int(len(lab)), "conversion_rate": float(lab["converted"].mean())}
