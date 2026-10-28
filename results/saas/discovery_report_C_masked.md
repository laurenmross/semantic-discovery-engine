# Discovery report: saas, configuration C, masked names, run 1

This is the output of the system as a reader would receive it. **Computed facts** come from deterministic analysis. **Interpretations** are the LLM's hypotheses, each with its confidence and the evidence IDs it cites (see `packets/C_masked.md`). Text in italics shows the real names, for evaluation only; the system never saw them.

## 1. Inferred entities (interpretation)

| Table | Concept | Kind | Confidence | Needs human check | Evidence |
|---|---|---|---|---|---|
| T05 _(actually: ACCT_MSTR)_ | Customer account (signup-level entity whose conversion is predicted), one row per account with signup time and categorical attributes | entity | 0.75 | yes | S:t:T05, S:k:T05.c02, S:c:T05.c01, S:r:26 |
| T06 _(actually: USR_XREF)_ | Users/members belonging to an account; exactly one role-1 user per account (likely the owner/creator); self-reference likely means invited-by | entity | 0.65 | yes | S:t:T06, S:k:T06.c05, S:r:26, S:r:25 |
| T01 _(actually: EVT_STRM_01)_ | High-volume product usage event log at user level (event type, numeric value, timestamp) | event | 0.70 | yes | S:t:T01, S:a:37, S:r:2, S:c:T01.c01 |
| T02 _(actually: SUB_HDR)_ | Paid subscriptions: at most one per account, with plan, billing option, start time and optional end/cancellation time; plausibly the conversion milestone | entity | 0.60 | yes | S:t:T02, S:k:T02.c04, S:k:T02.c05, S:r:7 |
| T04 _(actually: INV_LN)_ | Billing transactions/ledger lines per subscription (type, signed amount, roughly monthly timestamps) | event | 0.60 | yes | S:t:T04, S:r:14, S:c:T04.c02, S:c:T04.c03 |
| T03 _(actually: TKT_LOG)_ | Support tickets/cases raised by accounts (optionally tied to a user), with category, optional 1-5 rating, open and close timestamps | event | 0.50 | yes | S:t:T03, S:k:T03.c06, S:r:13, S:r:10 |
| T08 _(actually: EVT_STRM_02)_ | Scheduled lifecycle/onboarding message sequence per account (step 1-8) with two engagement flags (e.g. opened, clicked) | event | 0.50 | yes | S:t:T08, S:a:39, S:r:30, S:c:T08.c01 |
| T07 _(actually: GEO_REF)_ | Geographic dimension (40 rows, e.g. country) with a 5-value grouping (region) and a small signed integer (possibly UTC offset) | dimension | 0.45 | yes | S:t:T07, S:k:T07.c03, S:c:T07.c01, S:c:T07.c02 |
| T09 _(actually: PLN_REF)_ | Pricing plan dimension (6 plans with price, tier and capacity/seat limit) | dimension | 0.60 | yes | S:t:T09, S:c:T09.c01, S:c:T09.c03, S:k:T09.c04 |

## 2. Relationships accepted by the interpreter

| Child column | Parent key | Confidence | Computed overlap evidence |
|---|---|---|---|
| T06.c04 | T05.c02 | 0.90 | inclusion 1.0, coverage 1.0, rank 1 |
| T01.c02 | T06.c05 | 0.88 | inclusion 1.0, coverage 0.9876, rank 1 |
| T03.c05 | T05.c02 | 0.85 | inclusion 1.0, coverage 0.9427, rank 1 |
| T03.c03 | T06.c05 | 0.75 | inclusion 1.0, coverage 0.2521, rank 1 |
| T08.c02 | T05.c02 | 0.90 | inclusion 1.0, coverage 1.0, rank 1 |
| T04.c01 | T02.c04 | 0.90 | inclusion 1.0, coverage 1.0, rank 1 |
| T02.c05 | T05.c02 | 0.75 | inclusion 1.0, coverage 0.2114, rank 1 |
| T06.c03 | T06.c05 | 0.65 | inclusion 1.0, coverage 0.4006, rank 1 |
| T02.c01 | T09.c04 | 0.50 | inclusion 1.0, coverage 1.0, rank 1 |
| T05.c06 | T07.c03 | 0.50 | inclusion 1.0, coverage 1.0, rank 1 |
| T05.c04 | T09.c04 | 0.25 | inclusion 1.0, coverage 1.0, rank 1 |

## 3. Predictive associations (computed facts, held-out data)

Selected model test AUROC: 0.746 (single best activity count: 0.570). These are associations measured on time-ordered data. They are not causal and do not establish meaning.

| Feature | Validation AUROC | Direction | Stable across cutoffs | q (BH) | Permutation importance |
|---|---|---|---|---|---|
| count(T01 rows) via T06.c04 -> T05.c02 then T01.c02 -> T06.c05 | 0.702 | higher in positive | yes | 9.6e-206 | 0.2084 |
| count(T03 rows) via T06.c04 -> T05.c02 then T03.c03 -> T06.c05 | 0.464 | lower in positive | yes | 9.6e-28 | 0.0806 |
| count_distinct(T03.c03) via T03.c05 -> T05.c02 | 0.471 | lower in positive | yes | 2.6e-21 | 0.0309 |
| count_where(T03.c02) via T06.c04 -> T05.c02 then T03.c03 -> T06.c05 | 0.452 | lower in positive | yes | 1.9e-44 | 0.0162 |
| count_where(T01.c01) via T06.c04 -> T05.c02 then T01.c02 -> T06.c05 | 0.424 | lower in positive | yes | 1.5e-34 | 0.0124 |
| count_where(T01.c01) via T06.c04 -> T05.c02 then T01.c02 -> T06.c05 | 0.659 | higher in positive | yes | 1.1e-167 | 0.0114 |
| mean(T03.c04) via T06.c04 -> T05.c02 then T03.c03 -> T06.c05 | 0.506 | higher in positive | no | 0.12 | 0.0088 |
| count_where(T03.c04) via T03.c05 -> T05.c02 | 0.489 | lower in positive | yes | 5.7e-05 | 0.0084 |
| mean(T03.c02) via T06.c04 -> T05.c02 then T03.c03 -> T06.c05 | 0.548 | higher in positive | yes | 7.7e-18 | 0.0080 |
| count_where(T03.c04) via T03.c05 -> T05.c02 | 0.494 | lower in positive | yes | 1.4e-08 | 0.0065 |

## 4. Interpretations of the outcome evidence (hypotheses)

- **observed association** (confidence 0.80): Total usage events (T01) across an account's users is the strongest single association with conversion: higher counts in positives (AUROC ~0.70), and this path carries most model importance. _[P:f:f042, P:path:1]_
- **observed association** (confidence 0.70): Event types differ in direction: counts of T01.c01 = 4 (and 7, 5, 1, 8) are higher in positives, while T01.c01 = 11 counts are lower in positives. _[P:f:f048, P:f:f051, P:f:f049, P:f:f045, P:f:f052]_
- **observed association** (confidence 0.65): More support tickets (T03), especially category T03.c02 = 1, are associated with lower conversion likelihood, both via account and via users. _[P:f:f060, P:f:f018, P:f:f063, P:f:f023, P:f:f032]_
- **observed association** (confidence 0.60): Accounts with more users and more recently added users (T06) are modestly more likely to convert. _[P:f:f034, P:f:f041, P:f:f036, P:f:f039]_
- **observed association** (confidence 0.60): Message sequence counts (T08) carry no signal (AUROC exactly 0.5), consistent with a deterministic schedule; engagement rate (mean T08.c03) is mildly higher in positives. _[P:f:f004, P:f:f010, P:f:f008, P:f:f009]_
- **observed association** (confidence 0.60): Account attributes in T05 have weak, partly unstable associations with conversion. _[P:f:f000, P:f:f001, P:f:f003, P:f:f002]_
- **observed association** (confidence 0.80): Overall, a multi-table model reaches test AUROC ~0.74 versus 0.57 for the best single count, so combining usage, users and tickets is predictive. _[P:m:1, P:m:2]_
- **hypothesis** (confidence 0.50): The conversion milestone is plausibly the creation of a paid subscription (a T02 row for the account, start at T02.c03); ~21% of accounts have one, close to the ~18.5% positive rate. _[S:r:7, S:k:T02.c05, P:m:1]_

## 5. Column meanings (interpretation)

| Column | Meaning | Role | Confidence |
|---|---|---|---|
| T01.c01 _(actually: EVT_STRM_01.evt_cd)_ | Event type code (15 values); no dimension table present | categorical_code | 0.60 |
| T01.c02 _(actually: EVT_STRM_01.usr_key)_ | User who performed the event (references T06.c05) | foreign_key | 0.85 |
| T01.c03 _(actually: EVT_STRM_01.dur_ms)_ | Numeric event value (whole numbers 100-115377; e.g. duration or size); matches no key | measure | 0.45 |
| T01.c04 _(actually: EVT_STRM_01.evt_ts)_ | Event timestamp | timestamp | 0.85 |
| T02.c01 _(actually: SUB_HDR.pln_id)_ | Plan of the subscription (likely references T09.c04; all 6 values used) | foreign_key | 0.50 |
| T02.c02 _(actually: SUB_HDR.stat_cd)_ | Billing option/cycle or similar 3-level category (e.g. monthly/annual) | categorical_code | 0.35 |
| T02.c03 _(actually: SUB_HDR.st_ts)_ | Subscription start timestamp (possibly the conversion time) | timestamp | 0.60 |
| T02.c04 _(actually: SUB_HDR.sub_key)_ | Subscription identifier | primary_key | 0.85 |
| T02.c05 _(actually: SUB_HDR.acct_key)_ | Account that holds the subscription (references T05.c02; unique so one subscription per account) | foreign_key | 0.75 |
| T02.c06 _(actually: SUB_HDR.end_ts)_ | Subscription end/cancellation timestamp; null (82.8%) when still active | timestamp | 0.60 |
| T03.c01 _(actually: TKT_LOG.cls_ts)_ | Ticket close/resolution timestamp (examples are later than c07) | timestamp | 0.45 |
| T03.c02 _(actually: TKT_LOG.sev)_ | Ticket category/type (4 values) | categorical_code | 0.50 |
| T03.c03 _(actually: TKT_LOG.usr_key)_ | User who raised the ticket (references T06.c05; null 19.8%) | foreign_key | 0.75 |
| T03.c04 _(actually: TKT_LOG.csat)_ | Optional 1-5 rating (e.g. satisfaction score), roughly uniform, null 40% | measure | 0.45 |
| T03.c05 _(actually: TKT_LOG.acct_key)_ | Account the ticket belongs to (references T05.c02) | foreign_key | 0.85 |
| T03.c06 _(actually: TKT_LOG.tkt_no)_ | Ticket identifier | primary_key | 0.85 |
| T03.c07 _(actually: TKT_LOG.opn_ts)_ | Ticket creation/open timestamp | timestamp | 0.50 |
| T04.c01 _(actually: INV_LN.sub_key)_ | Subscription the transaction belongs to (references T02.c04) | foreign_key | 0.90 |
| T04.c02 _(actually: INV_LN.ln_typ)_ | Transaction type (types 1 and 3 have identical counts, e.g. invoice/payment pairs; type 4 rare, e.g. refund) | categorical_code | 0.50 |
| T04.c03 _(actually: INV_LN.amt)_ | Signed transaction amount (negative values suggest credits/refunds) | measure | 0.60 |
| T04.c04 _(actually: INV_LN.bill_ts)_ | Transaction timestamp; examples step by 30 days from subscription start (billing periods) | timestamp | 0.70 |
| T04.c05 _(actually: INV_LN.inv_ln_key)_ | Transaction identifier | primary_key | 0.85 |
| T05.c01 _(actually: ACCT_MSTR.crt_ts)_ | Account signup/creation timestamp | timestamp | 0.75 |
| T05.c02 _(actually: ACCT_MSTR.acct_key)_ | Account identifier (outcome entity) | primary_key | 0.90 |
| T05.c03 _(actually: ACCT_MSTR.seg_cd)_ | 4-level account attribute (e.g. company size band) | categorical_code | 0.35 |
| T05.c04 _(actually: ACCT_MSTR.src_cd)_ | 6-level account attribute; possibly plan of interest at signup (same range as T09.c04) or industry | categorical_code | 0.30 |
| T05.c05 _(actually: ACCT_MSTR.emp_band)_ | 7-level account attribute (e.g. acquisition channel) | categorical_code | 0.30 |
| T05.c06 _(actually: ACCT_MSTR.geo_ref)_ | Geography of account (likely references T07.c03, 40 values all used) | foreign_key | 0.50 |
| T06.c01 _(actually: USR_XREF.crt_ts)_ | User creation/join timestamp (role-1 user's time matches account signup) | timestamp | 0.70 |
| T06.c02 _(actually: USR_XREF.role_cd)_ | User role (1 = exactly one per account, likely owner; 2/3 other roles) | categorical_code | 0.60 |
| T06.c03 _(actually: USR_XREF.inv_by)_ | Inviting/parent user (self-reference to T06.c05); null ~23.6% (~owners) | foreign_key | 0.65 |
| T06.c04 _(actually: USR_XREF.acct_key)_ | Account the user belongs to (references T05.c02) | foreign_key | 0.90 |
| T06.c05 _(actually: USR_XREF.usr_key)_ | User identifier | primary_key | 0.90 |
| T07.c01 _(actually: GEO_REF.rgn_cd)_ | Grouping of geographies (e.g. region, 5 values) | categorical_code | 0.35 |
| T07.c02 _(actually: GEO_REF.tz_off)_ | Signed small integer -9..10 (possibly UTC offset) | other | 0.30 |
| T07.c03 _(actually: GEO_REF.geo_id)_ | Geography identifier | primary_key | 0.75 |
| T08.c01 _(actually: EVT_STRM_02.tmpl_cd)_ | Sequence step number (1-8; steps 1-2 sent to every account, later steps decreasing) | categorical_code | 0.50 |
| T08.c02 _(actually: EVT_STRM_02.acct_key)_ | Account receiving the message (references T05.c02) | foreign_key | 0.90 |
| T08.c03 _(actually: EVT_STRM_02.opn_flg)_ | Engagement flag (31% = 1; e.g. opened) | flag | 0.45 |
| T08.c04 _(actually: EVT_STRM_02.snd_ts)_ | Send timestamp; appears scheduled at fixed offsets from signup | timestamp | 0.55 |
| T08.c05 _(actually: EVT_STRM_02.clk_flg)_ | Second, rarer engagement flag (9.4% = 1; e.g. clicked) | flag | 0.45 |
| T09.c01 _(actually: PLN_REF.list_px)_ | Plan price (15-999) | measure | 0.55 |
| T09.c02 _(actually: PLN_REF.tier_rank)_ | Plan tier/level (1-5, one value shared by two plans) | categorical_code | 0.40 |
| T09.c03 _(actually: PLN_REF.seat_cap)_ | Plan capacity limit (e.g. seats/users 3-500) | measure | 0.45 |
| T09.c04 _(actually: PLN_REF.pln_id)_ | Plan identifier | primary_key | 0.70 |

## 6. Unresolved ambiguities

- Exact definition of the conversion milestone is not given; whether it is the T02 subscription start or something else is unconfirmed. _[S:r:7, S:a:11, S:c:T02.c03]_
- Small-integer codes (T05.c03/c04/c05, T03.c02, T04.c02, T06.c02, T02.c02, T07.c01, T09.c02) match T09.c04/T07.c03 by range only; most are likely coincidental and their labels are unknown. _[S:a:1, S:a:2, S:a:4, S:a:7]_
- T01.c01 event types have no lookup table; the meaning of type 11 (negative association) vs type 4 (positive) is unknown. _[S:a:16, P:f:f055, P:f:f048]_
- Which T03 timestamp is open vs close is inferred from a few examples only. _[S:a:41, S:c:T03.c01, S:c:T03.c07]_
- T01.c03 meaning (duration, size, value) is unclear and shows no association. _[S:a:38, P:f:f044]_
- T02.c06 could be cancellation or end-of-trial; T04.c02 types and negative amounts need confirmation. _[S:c:T02.c06, S:c:T04.c02, S:c:T04.c03]_

## 7. Suggested next investigations

- Confirm with the business that conversion = first T02 row per account and check timing of T02.c03 vs label windows (leakage check).
- Obtain labels for T01.c01 event types and analyse type 11 and type 4 usage in early account life.
- Check consistency between T03.c05 and the account of T03.c03 via T06.c04.
- Verify T06.c02 = 1 is the owner and T06.c03 nulls coincide with role 1.
- Test T05.c04 against T02.c01 to see if it represents intended plan; validate T05.c06 -> T07.c03 and T07.c02 as UTC offset.
- Add time-windowed (e.g. first 7/14 days) usage and ticket features and ticket resolution time (T03.c01 - T03.c07).
- Inspect T04 type-1/type-3 pairing and negative amounts to confirm invoice/payment/refund semantics.

## 8. Limitations

- Meanings are inferred from data patterns. Nothing here is an organisation-approved (governed) definition.
- Relationship candidates come from value overlap. On dense integer keys, overlap alone is weak evidence (see range_density).
- Predictive associations come from a single dataset and time period. They may not hold in other periods.
- Static tables (no time column) are used as-is and may contain information recorded after a cutoff.
