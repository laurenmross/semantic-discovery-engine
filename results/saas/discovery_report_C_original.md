# Discovery report: saas, configuration C, original names, run 1

This is the output of the system as a reader would receive it. **Computed facts** come from deterministic analysis. **Interpretations** are the LLM's hypotheses, each with its confidence and the evidence IDs it cites (see `packets/C_original.md`).

## 1. Inferred entities (interpretation)

| Table | Concept | Kind | Confidence | Needs human check | Evidence |
|---|---|---|---|---|---|
| ACCT_MSTR | Customer account (trial sign-up / workspace); the outcome entity for trial-to-paid conversion | entity | 0.85 | no | S:t:ACCT_MSTR, S:k:ACCT_MSTR.acct_key, S:c:ACCT_MSTR.crt_ts, S:r:9 |
| EVT_STRM_01 | Product usage event log at user level (one row per in-app action, with a duration) | event | 0.75 | yes | S:t:EVT_STRM_01, S:a:37, S:r:8, S:c:EVT_STRM_01.evt_cd |
| EVT_STRM_02 | Automated lifecycle/onboarding email sends per account with open and click flags | event | 0.70 | yes | S:t:EVT_STRM_02, S:c:EVT_STRM_02.tmpl_cd, S:c:EVT_STRM_02.snd_ts, S:c:EVT_STRM_02.opn_flg |
| GEO_REF | Geography lookup (country/locale) with region grouping and time-zone offset | dimension | 0.70 | yes | S:t:GEO_REF, S:k:GEO_REF.geo_id, S:c:GEO_REF.tz_off, S:r:2 |
| INV_LN | Invoice line items billed against paid subscriptions | event | 0.75 | yes | S:t:INV_LN, S:k:INV_LN.inv_ln_key, S:r:15, S:c:INV_LN.amt |
| PLN_REF | Subscription plan catalogue (price, seat capacity, tier) | dimension | 0.80 | no | S:t:PLN_REF, S:k:PLN_REF.pln_id, S:c:PLN_REF.list_px, S:c:PLN_REF.seat_cap |
| SUB_HDR | Paid subscription header; at most one per account (likely the source of the conversion label) | entity | 0.80 | yes | S:t:SUB_HDR, S:k:SUB_HDR.sub_key, S:k:SUB_HDR.acct_key, S:r:19 |
| TKT_LOG | Customer support ticket log with severity and satisfaction rating | event | 0.75 | yes | S:t:TKT_LOG, S:k:TKT_LOG.tkt_no, S:c:TKT_LOG.sev, S:c:TKT_LOG.csat |
| USR_XREF | Users (seats) belonging to accounts, with role and inviter; links user-level activity to accounts | entity | 0.80 | no | S:t:USR_XREF, S:k:USR_XREF.usr_key, S:r:30, S:r:31 |

## 2. Relationships accepted by the interpreter

| Child column | Parent key | Confidence | Computed overlap evidence |
|---|---|---|---|
| EVT_STRM_01.usr_key | USR_XREF.usr_key | 0.92 | inclusion 1.0, coverage 0.9876, rank 1 |
| EVT_STRM_02.acct_key | ACCT_MSTR.acct_key | 0.93 | inclusion 1.0, coverage 1.0, rank 1 |
| INV_LN.sub_key | SUB_HDR.sub_key | 0.93 | inclusion 1.0, coverage 1.0, rank 1 |
| SUB_HDR.acct_key | ACCT_MSTR.acct_key | 0.85 | inclusion 1.0, coverage 0.2114, rank 1 |
| SUB_HDR.pln_id | PLN_REF.pln_id | 0.75 | inclusion 1.0, coverage 1.0, rank 1 |
| TKT_LOG.acct_key | ACCT_MSTR.acct_key | 0.92 | inclusion 1.0, coverage 0.9427, rank 1 |
| TKT_LOG.usr_key | USR_XREF.usr_key | 0.88 | inclusion 1.0, coverage 0.2521, rank 1 |
| USR_XREF.acct_key | ACCT_MSTR.acct_key | 0.93 | inclusion 1.0, coverage 1.0, rank 1 |
| USR_XREF.inv_by | USR_XREF.usr_key | 0.85 | inclusion 1.0, coverage 0.4006, rank 1 |
| ACCT_MSTR.geo_ref | GEO_REF.geo_id | 0.65 | inclusion 1.0, coverage 1.0, rank 1 |

## 3. Predictive associations (computed facts, held-out data)

Selected model test AUROC: 0.746 (single best activity count: 0.570). These are associations measured on time-ordered data. They are not causal and do not establish meaning.

| Feature | Validation AUROC | Direction | Stable across cutoffs | q (BH) | Permutation importance |
|---|---|---|---|---|---|
| count(EVT_STRM_01 rows) via USR_XREF.acct_key -> ACCT_MSTR.acct_key then EVT_STRM_01.usr_key -> USR_XREF.usr_key | 0.702 | higher in positive | yes | 9.6e-206 | 0.2084 |
| count(TKT_LOG rows) via USR_XREF.acct_key -> ACCT_MSTR.acct_key then TKT_LOG.usr_key -> USR_XREF.usr_key | 0.464 | lower in positive | yes | 9.6e-28 | 0.0806 |
| count_distinct(TKT_LOG.usr_key) via TKT_LOG.acct_key -> ACCT_MSTR.acct_key | 0.471 | lower in positive | yes | 2.6e-21 | 0.0309 |
| count_where(TKT_LOG.sev) via USR_XREF.acct_key -> ACCT_MSTR.acct_key then TKT_LOG.usr_key -> USR_XREF.usr_key | 0.452 | lower in positive | yes | 1.9e-44 | 0.0162 |
| count_where(EVT_STRM_01.evt_cd) via USR_XREF.acct_key -> ACCT_MSTR.acct_key then EVT_STRM_01.usr_key -> USR_XREF.usr_key | 0.424 | lower in positive | yes | 1.5e-34 | 0.0124 |
| count_where(EVT_STRM_01.evt_cd) via USR_XREF.acct_key -> ACCT_MSTR.acct_key then EVT_STRM_01.usr_key -> USR_XREF.usr_key | 0.659 | higher in positive | yes | 1.1e-167 | 0.0114 |
| mean(TKT_LOG.csat) via USR_XREF.acct_key -> ACCT_MSTR.acct_key then TKT_LOG.usr_key -> USR_XREF.usr_key | 0.506 | higher in positive | no | 0.12 | 0.0088 |
| count_where(TKT_LOG.csat) via TKT_LOG.acct_key -> ACCT_MSTR.acct_key | 0.489 | lower in positive | yes | 5.7e-05 | 0.0084 |
| mean(TKT_LOG.sev) via USR_XREF.acct_key -> ACCT_MSTR.acct_key then TKT_LOG.usr_key -> USR_XREF.usr_key | 0.548 | higher in positive | yes | 7.7e-18 | 0.0080 |
| count_where(TKT_LOG.csat) via TKT_LOG.acct_key -> ACCT_MSTR.acct_key | 0.494 | lower in positive | yes | 1.4e-08 | 0.0065 |

## 4. Interpretations of the outcome evidence (hypotheses)

- **observed association** (confidence 0.85): Total product usage event count across an account's users before the cutoff is the strongest single association: higher in accounts that convert (AUROC ~0.70, stable). _[P:f:f042, P:path:1]_
- **observed association** (confidence 0.70): Most specific event types (e.g. evt_cd 4, 7, 1, 5, 8) are higher in converting accounts, while evt_cd 11 is lower in converting accounts; evt_cd 11 may represent an error/friction or exploratory action, but its meaning is unknown. _[P:f:f048, P:f:f051, P:f:f045, P:f:f049, P:f:f052]_
- **observed association** (confidence 0.75): More support tickets during the trial (especially sev=1 tickets) are associated with lower conversion, whether counted via users or account. _[P:f:f060, P:f:f018, P:f:f063, P:f:f023, P:f:f032]_
- **observed association** (confidence 0.60): Ticket satisfaction (csat) shows no stable association with conversion. _[P:f:f062, P:f:f022]_
- **observed association** (confidence 0.65): Larger trial teams (more users, more distinct inviters, more role 2/3 users) are weakly associated with higher conversion. _[P:f:f034, P:f:f041, P:f:f039, P:f:f040, P:f:f037]_
- **observed association** (confidence 0.65): Email send counts/templates carry no signal (AUROC 0.500), consistent with a fixed sign-up-relative drip schedule; email open rate is mildly higher in converting accounts. _[P:f:f004, P:f:f010, P:f:f008, P:f:f009]_
- **observed association** (confidence 0.60): Firmographic attributes on the account (seg_cd, src_cd, emp_band, geo_ref) show weak or unstable associations. _[P:f:f000, P:f:f001, P:f:f003, P:f:f002]_
- **observed association** (confidence 0.75): The combined model (AUROC ~0.74 test) clearly outperforms the best single count baseline (0.57), suggesting early engagement and support signals together are predictive of conversion. _[P:m:1, P:m:2]_
- **hypothesis** (confidence 0.40): Ticket volume may reflect onboarding friction among non-converting trials, while high usage may reflect realised product value; these are interpretations, not causal findings. _[P:f:f060, P:f:f042]_

## 5. Column meanings (interpretation)

| Column | Meaning | Role | Confidence |
|---|---|---|---|
| ACCT_MSTR.acct_key | Account identifier | primary_key | 0.95 |
| ACCT_MSTR.seg_cd | Customer segment code (4 levels, e.g. SMB/mid-market/enterprise); not a plan reference | categorical_code | 0.50 |
| ACCT_MSTR.crt_ts | Account creation timestamp (trial start) | timestamp | 0.85 |
| ACCT_MSTR.src_cd | Acquisition source/channel code (6 levels) | categorical_code | 0.50 |
| ACCT_MSTR.geo_ref | Account geography, reference to GEO_REF | foreign_key | 0.70 |
| ACCT_MSTR.emp_band | Company employee-size band (7 ordered bands) | categorical_code | 0.55 |
| EVT_STRM_01.usr_key | User who performed the event | foreign_key | 0.90 |
| EVT_STRM_01.evt_cd | Event/action type code (15 types); not a geography reference | categorical_code | 0.70 |
| EVT_STRM_01.evt_ts | Event timestamp | timestamp | 0.90 |
| EVT_STRM_01.dur_ms | Event/session duration in milliseconds | measure | 0.75 |
| EVT_STRM_02.acct_key | Account the email was sent to | foreign_key | 0.90 |
| EVT_STRM_02.tmpl_cd | Email template / drip-step number (1-8; steps 1 and 2 sent to every account, later steps to fewer) | categorical_code | 0.65 |
| EVT_STRM_02.snd_ts | Email send timestamp; examples share the account-creation clock time, suggesting a schedule relative to sign-up | timestamp | 0.70 |
| EVT_STRM_02.opn_flg | Email opened flag | flag | 0.75 |
| EVT_STRM_02.clk_flg | Email link clicked flag | flag | 0.75 |
| GEO_REF.geo_id | Geography identifier | primary_key | 0.90 |
| GEO_REF.rgn_cd | Region grouping code (5 regions) | categorical_code | 0.60 |
| GEO_REF.tz_off | Time-zone offset from UTC in hours | measure | 0.70 |
| INV_LN.inv_ln_key | Invoice line identifier | primary_key | 0.90 |
| INV_LN.sub_key | Subscription billed | foreign_key | 0.90 |
| INV_LN.ln_typ | Invoice line type (types 1 and 3 each occur once per billing event, e.g. base charge and tax; 2 and 4 rarer, e.g. add-on/discount/refund) | categorical_code | 0.50 |
| INV_LN.amt | Line amount, likely in minor currency units (e.g. 7900 = 79.00 list price; negatives = credits/discounts) | measure | 0.60 |
| INV_LN.bill_ts | Billing timestamp (monthly cycle from subscription start) | timestamp | 0.80 |
| PLN_REF.pln_id | Plan identifier | primary_key | 0.90 |
| PLN_REF.list_px | Plan list price (per billing period) | measure | 0.80 |
| PLN_REF.seat_cap | Maximum seats/users allowed on plan | measure | 0.75 |
| PLN_REF.tier_rank | Plan tier ordering (two plans share rank 1); not a FK | categorical_code | 0.60 |
| SUB_HDR.sub_key | Subscription identifier | primary_key | 0.90 |
| SUB_HDR.acct_key | Account that holds the subscription (unique: one subscription per account) | foreign_key | 0.85 |
| SUB_HDR.pln_id | Plan subscribed to | foreign_key | 0.75 |
| SUB_HDR.st_ts | Paid subscription start (conversion) timestamp | timestamp | 0.80 |
| SUB_HDR.end_ts | Subscription end/cancellation timestamp; null while active | timestamp | 0.80 |
| SUB_HDR.stat_cd | Subscription status (1 active; 2 ended/cancelled — count 729 matches non-null end_ts; 3 other e.g. paused/past-due) | categorical_code | 0.65 |
| TKT_LOG.tkt_no | Support ticket number | primary_key | 0.90 |
| TKT_LOG.acct_key | Account that raised the ticket | foreign_key | 0.90 |
| TKT_LOG.usr_key | User who raised the ticket (null ~20%, e.g. tickets not tied to a logged-in user) | foreign_key | 0.80 |
| TKT_LOG.opn_ts | Ticket opened timestamp | timestamp | 0.85 |
| TKT_LOG.sev | Ticket severity/priority level (1-4; scale direction unknown, 1 most common) | categorical_code | 0.60 |
| TKT_LOG.csat | Customer satisfaction rating 1-5, null when not rated | measure | 0.70 |
| TKT_LOG.cls_ts | Ticket closed timestamp | timestamp | 0.85 |
| USR_XREF.usr_key | User identifier | primary_key | 0.90 |
| USR_XREF.acct_key | Account the user belongs to | foreign_key | 0.90 |
| USR_XREF.role_cd | User role (1 = account owner/creator, exactly one per account; 2 and 3 e.g. member/admin or viewer) | categorical_code | 0.70 |
| USR_XREF.inv_by | User who invited this user; null for owners (null share 23.6% ≈ 20000/84594) | foreign_key | 0.80 |
| USR_XREF.crt_ts | User creation/join timestamp (owner's equals account creation) | timestamp | 0.80 |

## 6. Unresolved ambiguities

- Meanings of evt_cd values (15 event types) are unknown, so behavioural insights cannot be named. _[S:c:EVT_STRM_01.evt_cd, P:f:f055]_
- Direction of TKT_LOG.sev scale is unknown (is 1 lowest or highest severity?); mean sev is higher in converters while sev=1 counts are lower. _[S:c:TKT_LOG.sev, P:f:f061, P:f:f063]_
- Codes seg_cd, src_cd, emp_band, role_cd 2/3, stat_cd 3, ln_typ and tier_rank have no lookup tables; overlaps with PLN_REF/GEO_REF are likely coincidental. _[S:a:27, S:a:28, S:a:15, S:a:36]_
- Whether SUB_HDR.st_ts is the exact conversion event used for the label, and whether accounts can have multiple subscriptions over time (data shows one per account). _[S:k:SUB_HDR.acct_key, S:c:SUB_HDR.st_ts]_
- TKT_LOG covers 94% of accounts with ~4 tickets each, unusually high for trials; tickets may include automated or onboarding contacts. _[S:r:24, S:c:TKT_LOG.usr_key]_
- Units of INV_LN.amt (minor units vs major) and meaning of negative lines. _[S:c:INV_LN.amt]_
- Window=all and window=16 features are identical because the history before cutoff is only ~5 days, so recency windows add nothing. _[P:f:f034, P:f:f035, P:f:f018, P:f:f019]_

## 7. Suggested next investigations

- Obtain event-type dictionary for evt_cd and profile per-type usage by converters vs non-converters (esp. evt_cd 11 and 4).
- Confirm the label is derived from SUB_HDR.st_ts and verify no leakage from post-cutoff rows.
- Build breadth/activation features: distinct active users, distinct event types, active days, time-to-first-key-action within the 5 trial days.
- Investigate ticket content/categories and sev scale to understand why ticket volume is lower among converters.
- Check email timing relative to cutoff and open/click behaviour per template; consider controlled experiments before attributing any effect.
- Join SUB_HDR to PLN_REF and INV_LN to analyse converted plan mix and revenue, and validate amt units and ln_typ meanings.
- Assess calibration and segment-level performance of the model (seg_cd, emp_band, src_cd).

## 8. Limitations

- Meanings are inferred from data patterns. Nothing here is an organisation-approved (governed) definition.
- Relationship candidates come from value overlap. On dense integer keys, overlap alone is weak evidence (see range_density).
- Predictive associations come from a single dataset and time period. They may not hold in other periods.
- Static tables (no time column) are used as-is and may contain information recorded after a cutoff.
