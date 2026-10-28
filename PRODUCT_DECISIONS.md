# Product decisions

## Why this problem matters

Data-heavy organizations rarely lack data. What they lack is *understood* data.

The work of turning raw tables into something an analyst or an AI can reason about is manual, slow, and goes stale. It includes:
- deciding which tables are authoritative;
- working out how they join;
- defining what each event and metric means.

Most "AI analyst" products work well once that layer exists and poorly before it. If part of that layer can be inferred, with evidence
and honest uncertainty, the time from "we have data" to "we can ask it questions" shrinks. That is valuable for:
- data teams onboarding new sources;
- companies after an acquisition;
- consultancies;
- any AI analytics product's onboarding.

## Core hypothesis

An LLM reasoning over **deterministic structural evidence** and **outcome-driven predictive evidence** can infer more correct business
semantics, with fewer unsupported claims, than an LLM given only the schema.

The outcome matters because a large database is a search problem. A known outcome (conversion, churn, engagement) shows where to look.

## Target users and potential value

| User | Job | Value if this works |
|---|---|---|
| Analytics engineer onboarding a new source | Write the first semantic model | A reviewed draft with evidence, instead of a blank file |
| AI analytics or BI vendor | Onboard a customer's warehouse | Faster time to first useful answer; fewer manual setup sessions |
| Data leader after an acquisition or migration | Understand inherited data | A map of what matters for key outcomes, with flagged ambiguities |

**The output is always a draft for human review, not an authority.** Governed definitions (what the organization *agrees* a metric means)
cannot come from data alone. The system's job is to make that human review faster and better targeted.

## MVP scope (this slice)

**In scope**
- One public relational database with a business outcome and independent foreign-key ground truth (RelBench `rel-avito`).
- Deterministic structural discovery and outcome-driven analysis.
- One LLM interpretation call per configuration.
- A pre-registered A/B/C comparison, with and without masked names.
- A human-readable discovery report.

**Out of scope**
- Knowledge graph storage, agent loops, iterative re-exploration, a UI, connectors to real warehouses, semantic-layer export (dbt/Cube YAML), and multi-dataset benchmarks.

## Major decisions and tradeoffs

| Decision | Alternatives considered | Why |
|---|---|---|
| **RelBench `rel-avito`** as the evaluation dataset | Berka/PKDD'99 banking (download links dead); Olist e-commerce (needs a Kaggle login; no machine-readable FK ground truth); RelBench `rel-hm` (only 3 tables, so relationship discovery is trivial); `rel-f1` (not a business outcome) | 8 tables, 11 published foreign keys as independent ground truth, a defined engagement outcome with official time splits, and undocumented-looking columns (`ObjectType`, `HistCTR`, `IPID`). `rel-f1` serves as a development set. |
| **Masked-name condition as the primary test** | Trust original names | The model has likely seen Avito and RelBench. Without masking, a good score could just mean "the model remembers this dataset". |
| **Pre-registration** (protocol and answer key committed before any results) | Decide metrics afterwards | A portfolio experiment is only credible if the evaluation can't have been fitted to the results. |
| **Name-agnostic structural inference** | Use column-name similarity (it would score much better with real names) | Keeps the structural evidence identical across naming conditions, and makes the component's limits visible. Name similarity is something the *LLM* can contribute. |
| **Small custom feature synthesis** instead of Featuretools | Featuretools Deep Feature Synthesis | Featuretools expects relationships to be *declared* in an EntitySet. Here they are *inferred* and partly wrong. A 150-line depth-2 synthesizer keeps the provenance of every feature (which inferred edges it used), and the evidence packets need that. Worth revisiting. |
| **Conventional models** (gradient boosting, logistic regression) | Graph neural networks, relational foundation models | The brief asks for conventional first. The predictive component exists to rank evidence, not to win a leaderboard. |
| **One structured-output LLM call** per run | Agentic exploration with SQL tools | A single call isolates the effect of the *evidence*. An agent adds many variables (tool use, path dependence, cost) that would confound the A/B/C comparison. |
| **Blinded LLM judge plus human audit** | Human-only grading; keyword matching | 18 runs × 50 items is too many to hand-grade every time. Keyword matching can't grade meaning. The audit measures how far the judge can be trusted. |
| **Record and replay every LLM call** | Re-call the API on every run | Anyone can re-score without a key or cost, and the outputs behind each number can be inspected. |
| **No refusal fallback** to another model | Use the API's server-side fallback | A silent model switch would contaminate the comparison. |

## Why some approaches were excluded (for now)

- **Training a model.** Out of scope by design. The question is whether existing models plus deterministic analysis are enough.
- **Knowledge graph, recursive agent.** These would make the system more impressive and the experiment less interpretable.
  They earn their place only if the single-pass comparison shows the evidence helps.
- **A Streamlit UI.** Optional in the brief. The markdown discovery report shows the output format without adding infrastructure.

## Related work (to be verified properly)

This is a working map from public documentation as I understand it, not a completed review. I have not verified current capabilities,
and **I make no claim that this architecture is novel.**

| Technology | What it appears to do |
|---|---|
| **dbt Semantic Layer / MetricFlow, Cube, AtScale** | Semantic layers authored by people (entities, measures, dimensions in config). This project is about drafting that kind of layer. |
| **Snowflake Cortex Analyst** (semantic models and views), **ThoughtSpot**, **Wren AI** | Natural-language analytics grounded in a semantic model. Several may now help *generate* that model; that needs checking before claiming a gap. |
| **Featuretools** | Automated feature synthesis over declared relationships. |
| **RelBench and relational deep learning** (Stanford); **Kumo's relational foundation model** | Prediction directly over multi-table databases, given the key graph. They answer "predict X"; this project asks "what does this data mean". The two could combine. |
| **Triple Whale / Moby** | A domain-specific ontology plus models plus AI reasoning. A strong reference point for what a *predefined* ontology buys you. |

A competitive review is listed as a next step below.

## What the experiments changed

- **Data the model cannot have seen is a requirement.** Experiment 1 showed that a public benchmark lets the model answer from memory.
- **Names are the strongest single signal**, even cryptic ones. The product value of structural and outcome evidence is concentrated where names are absent,
  misleading or inconsistent: raw event streams, code columns, IDs with no documentation. Positioning should follow: an assistant for the *undocumented
  corners* of a warehouse, not a replacement for reading column names.
- **Outcome evidence is a prioritization tool.** It reliably says *where to look*. That is a product claim I can now support with measurements. "It tells you what the data means" is not.

## What I would investigate next

1. **Close the loop from discovery to meaning.** Experiment 2 showed outcome evidence finds *which* unknown codes matter, but cannot say what they mean.
   The natural next step is targeted follow-up: let the system query the data around a high-signal code, for example co-occurring events and the users who trigger it,
   or ask a human one precise question. Then measure whether interpretation of those specific items improves.
   Also: have a human audit the judge, and add a completeness check, since one C run silently dropped a table.
2. **A second, structurally different dataset**, to see whether any effect generalizes.
3. **Let the LLM ask for evidence**, with a bounded SQL tool. This tests whether *targeted* exploration beats a fixed evidence packet.
4. **Outcome as the search budget.** Measure how much of the database the system needs to examine to reach a given semantic accuracy, with and without an outcome.
5. **Export a draft semantic model** (dbt/MetricFlow YAML) and measure human edit distance to an accepted version. This is the closest proxy for real value.
6. **Competitive review:** test whether current tools (Cortex Analyst's semantic model generation, Wren AI, and others) already draft semantic models from raw schemas, and how well.
