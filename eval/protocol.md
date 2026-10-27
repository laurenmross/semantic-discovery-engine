# Evaluation protocol (pre-registered)

**Status:** frozen before any LLM run and before any structural or predictive output was scored.
This file was committed to git before the code that produces results. Later changes are listed in the
"Amendments" section at the bottom, each with its date and the reason for it. Results that rely on an amendment are flagged.

## 1. Question

Does adding (B) deterministic structural analysis, and then (C) outcome-driven predictive evidence, to an LLM's
context measurably improve how well it understands an unfamiliar relational database, compared with (A) an LLM
that sees only the schema?

## 2. Dataset

- **Evaluation dataset:** RelBench `rel-avito`: 8 tables, about 25M rows, from the Avito Context Ad Clicks data (an online classifieds marketplace).
  - The outcome is the RelBench `user-visits` task: does a user visit more than one ad in the 4 days after a cutoff?
  - Train, validation and test are RelBench's own time-based splits (validation from 2015-05-08, test from 2015-05-14).
- **Development dataset:** RelBench `rel-f1`. All structural heuristics and thresholds were developed and sanity-checked
  only on synthetic test fixtures and `rel-f1`, never tuned on `rel-avito`.
- **Read-only:** the source parquet files are never modified. Analysis connects to DuckDB with `read_only=True`.

## 3. Conditions

A 3 × 2 design: three configurations, each run with original names and with masked names.

| Config | What the LLM sees |
|---|---|
| **A**: schema only | Table and column names, types, row counts, 3 example values per column, the outcome statement |
| **B**: + structural | A, plus a column profile (null %, distinct count, uniqueness, min/max, top values), candidate keys, candidate relationships with inclusion and cardinality evidence, join paths, time columns and structural ambiguities |
| **C**: + outcome | B, plus outcome-driven evidence: relational features built **only from relationships inferred in B** (never from ground truth), their held-out predictive value, univariate associations corrected for multiple testing, and stability across time windows |

| Naming | Description |
|---|---|
| **original** | Real table and column names |
| **masked** | Tables renamed `T01..T08` and columns `c01..cNN` (a fixed random permutation, seed 7). Free-text values are replaced by a descriptor (length and script), not shown. Numbers, dates and categorical codes are shown as they are. |

**Why the masked condition exists:** Avito and RelBench are public, and the model has very likely seen them.
With original names, the model can "understand" the data from memory. The masked condition removes names, the main
memorization cue, and stands in for an undocumented warehouse. **The masked condition is the primary test; original names are secondary.**

The outcome statement is identical for every configuration. With masked names it gives the business definition with names masked:
*"engagement: whether the entity identified by `<masked key>` has more than one qualifying interaction in the 4 days after the cutoff."*

**Model and repeats:** every cell uses `claude-opus-5-5` (effort `high`) with the same JSON output schema, enforced by
structured outputs. Each cell runs 3 times, using the API's default sampling (it no longer accepts a `temperature` setting), so we can see
run-to-run variation. Total: 18 interpretation runs.

**No refusal fallbacks.** Server-side fallbacks could quietly switch some cells to a different model. Refusals are recorded and reported instead.

## 4. Ground truth

Recorded in `eval/ground_truth/avito.json` **before any run was scored.**

- **Relationships:** the foreign-key map in RelBench's published dataset definition (`provenance/avito.py`), which is independent of
  this project: 11 foreign-key edges and 5 primary keys.
- **Entities:** for each table, the business concept and its kind (entity, dimension or event), reconstructed from the
  Avito competition's data description and RelBench's dataset description.
- **Column semantics:** what each column means, from the same sources.
  - Where the documentation is silent (for example `Category.SubcategoryID` and `Location.Level`), the key records an "acceptable range" of answers rather than a single answer.
  - A human should verify the semantic key before results are treated as final. Until then, the semantic results are labeled **provisional**.

**Disclosure:** the developer (Claude Code, with the project owner) knew the RelBench schema before writing the heuristics.
Mitigations:
- the structural inference never uses names;
- its thresholds are fixed in this file;
- it is reported on its own, as a deterministic component, so any overfitting would be visible.

## 5. Metrics

**Primary metrics (masked condition)**
1. **Relationship precision, recall and F1:** the LLM's final foreign-key list compared with the 11 ground-truth edges.
   - An edge matches when (child table, child column, parent table) is correct.
   - Edges the model proposes that are not in RelBench (for example a self-reference such as `Category.ParentCategoryID`) count as false positives in the primary metric.
   - A secondary, **adjudicated** metric lists those edges separately for human review.
2. **Entity identification accuracy:** for each table, is the concept correct (2 points), partially correct (1) or wrong (0)? Kind (entity/dimension/event) is scored exactly.
3. **Column semantic accuracy:** the same 0/1/2 rubric for every column, reported for all columns and for the "non-obvious" subset
   pre-listed in the ground-truth file.

**Secondary metrics**
4. **Unsupported claims**, counted three ways:
   - (a) citations to evidence IDs that do not exist in the evidence packet;
   - (b) *overconfident errors*: confidence ≥ 0.8 but scored 0;
   - (c) causal language in outcome insights (a keyword check, then a judge check).
5. **Human review effort:** items the system marks as needing human validation, plus overconfident errors (wrong answers a reviewer would have to catch).
6. **Predictive performance:** AUROC on the RelBench test split.
   - Models: gradient boosting and logistic regression on the features found in C.
   - Comparison baselines: the base rate, and a single "past activity count" feature.
   - Reported apart from semantic metrics. **Better prediction is not treated as evidence of better understanding.**
7. **Runtime and model cost:** wall-clock time and token usage, per stage and per configuration.

**Structural component on its own:** the precision, recall and F1 of the deterministic relationship candidates, with no LLM involved.

## 6. Scoring

- **Relationships:** scored automatically by exact match after converting masked names back to real ones.
- **Entity and column semantics:** an LLM judge (`claude-opus-5-5`, effort `medium`) scores each prediction against the ground-truth key using the rubric.
  - The judge is **blinded**: it sees only the ground-truth description and the predicted text. It does not see the configuration, the naming condition or the run.
  - Masked predictions are converted back to real names before judging.
  - Every judge decision is saved to `results/` for human audit.
  - A human audits a random sample of 30 judge decisions. The rate at which the human agrees with the judge is reported.

## 7. Hypotheses and decision rule

- **H1:** B beats A on relationship F1 (masked).
- **H2:** C beats B on entity and column semantic accuracy (masked).
- **H3:** C does not increase unsupported claims compared with B.

**Decision rule:** a difference counts as "an improvement" only if the gap between the two configurations' means is larger than the
run-to-run range (max minus min) of either configuration. Otherwise the result is "no detectable difference".
With 8 tables, 11 edges and about 45 columns, this is a **small-sample experiment**. Results describe this dataset and do not establish general claims.

## 8. Validity safeguards (predictive component)

| Risk | Safeguard |
|---|---|
| Target leakage | Features use only rows with time < cutoff for each label row. The label window `[t, t+4d)` is never visible. A unit test checks this. |
| Invalid joins | Features use only inferred edges with inclusion ≥ 0.95 and a parent key that is 100% unique and non-null. |
| Duplicate amplification | Child tables are always aggregated to the target entity before joining. Row counts are asserted unchanged after each feature join. |
| Wrong time order | Time-based splits (RelBench's); the model is chosen on validation and scored once on test. |
| Spurious correlation / multiple testing | Univariate tests are corrected with Benjamini–Hochberg (q = 0.05). Each feature's importance is reported with its stability across time windows. |
| Unjustified causal claims | The prompt forbids causal claims. Outcome evidence is labeled "association". Causal wording is counted as an unsupported claim. |
| Evaluation contamination | The masked condition, a blinded judge, and ground truth never placed in any interpretation prompt. |

## 9. Fixed thresholds (structural inference)

- **Candidate key:** 100% unique and 0% null, among integer or string columns.
- **Candidate foreign key** (child column → parent candidate key):
  - matching type family;
  - at least 95% of the child's distinct non-null values found in the parent key (*inclusion*);
  - at least 2 distinct child values;
  - the parent key has more than 1 row.
- **Weak-candidate flag:** both columns are low-cardinality integers (≤ 100 distinct values) with ranges starting near 0 or 1, which suggests overlapping small numbers rather than a real link.
  - These candidates are kept but flagged as an ambiguity, not dropped.
- **Join paths:** shortest paths over accepted candidates, at most 3 hops.

## Amendments

_None yet._
