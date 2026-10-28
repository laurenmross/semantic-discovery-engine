# Discovery report: rel-avito, configuration C, masked names, run 1

This is the output of the system as a reader would receive it. **Computed facts** come from deterministic analysis. **Interpretations** are the LLM's hypotheses, each with its confidence and the evidence IDs it cites (see `packets/C_masked.md`). Text in italics shows the real names, for evaluation only; the system never saw them.

## 1. Inferred entities (interpretation)

| Table | Concept | Kind | Confidence | Needs human check | Evidence |
|---|---|---|---|---|---|
| T01 _(actually: UserInfo)_ | User (outcome entity) with device/user-agent attributes | entity | 0.75 | yes | S:t:T01, S:k:T01.c04, S:r:21, S:r:48 |
| T02 _(actually: VisitStream)_ | Ad view/visit event log (user viewed an ad from an IP at a time) | event | 0.65 | yes | S:t:T02, S:a:129, S:r:18, S:r:21 |
| T03 _(actually: Location)_ | Location hierarchy (location with level, region, city) | dimension | 0.60 | yes | S:t:T03, S:k:T03.c03, S:c:T03.c01, S:r:44 |
| T04 _(actually: SearchInfo)_ | Search event (a search performed by a user, with category, location, query text, IP, logged-in flag) | event | 0.70 | yes | S:t:T04, S:k:T04.c08, S:c:T04.c02, S:c:T04.c03 |
| T05 _(actually: AdsInfo)_ | Ad / listing catalogue (ad with location, category, price, context flag, title) | entity | 0.70 | yes | S:t:T05, S:k:T05.c03, S:c:T05.c06, S:c:T05.c04 |
| T06 _(actually: PhoneRequestsStream)_ | Contact/phone-request event log (user requested contact for an ad) | event | 0.55 | yes | S:t:T06, S:a:127, S:r:75, S:r:76 |
| T07 _(actually: Category)_ | Category hierarchy dimension | dimension | 0.60 | yes | S:t:T07, S:k:T07.c02, S:c:T07.c03, S:r:39 |
| T08 _(actually: SearchStream)_ | Search result impressions (ads shown within a search, with position, type, historical CTR and click flag) | event | 0.65 | yes | S:t:T08, S:a:128, S:r:98, S:r:114 |

## 2. Relationships accepted by the interpreter

| Child column | Parent key | Confidence | Computed overlap evidence |
|---|---|---|---|
| T02.c04 | T01.c04 | 0.85 | inclusion 1.0, coverage 0.7794, rank 1 |
| T02.c01 | T05.c03 | 0.80 | inclusion 1.0, coverage 0.6394, rank 1 |
| T04.c05 | T01.c04 | 0.85 | inclusion 1.0, coverage 0.9988, rank 1 |
| T04.c04 | T03.c03 | 0.70 | inclusion 1.0, coverage 0.5803, rank 1 |
| T04.c01 | T07.c02 | 0.55 | inclusion 1.0, coverage 0.5735, rank 1 |
| T05.c01 | T03.c03 | 0.75 | inclusion 1.0, coverage 0.9576, rank 1 |
| T05.c02 | T07.c02 | 0.70 | inclusion 1.0, coverage 0.7647, rank 1 |
| T06.c03 | T05.c03 | 0.75 | inclusion 1.0, coverage 0.043, rank 1 |
| T06.c04 | T01.c04 | 0.80 | inclusion 1.0, coverage 0.3818, rank 1 |
| T08.c01 | T05.c03 | 0.80 | inclusion 1.0, coverage 0.438, rank 1 |
| T08.c06 | T04.c08 | 0.85 | inclusion 1.0, coverage 0.9873, rank 1 |

## 3. Predictive associations (computed facts, held-out data)

Selected model test AUROC: 0.668 (single best activity count: 0.655). These are associations measured on time-ordered data. They are not causal and do not establish meaning.

| Feature | Validation AUROC | Direction | Stable across cutoffs | q (BH) | Permutation importance |
|---|---|---|---|---|---|
| count_distinct(T02.c01) via T02.c04 -> T01.c04 | 0.688 | higher in positive | yes | 0 | 0.2798 |
| count(T02 rows) via T02.c04 -> T01.c04 | 0.683 | higher in positive | yes | 0 | 0.0321 |
| count_distinct(T06.c03) via T06.c04 -> T01.c04 | 0.604 | higher in positive | yes | 1e-147 | 0.0181 |
| count_distinct(T02.c02) via T02.c04 -> T01.c04 | 0.553 | higher in positive | yes | 3.2e-163 | 0.0144 |
| count(T06 rows) via T06.c04 -> T01.c04 | 0.603 | higher in positive | yes | 9.5e-147 | 0.0107 |
| count(T04 rows) via T04.c05 -> T01.c04 | 0.621 | higher in positive | yes | 1.1e-207 | 0.0034 |
| days_since_last(T04 rows) via T04.c05 -> T01.c04 | 0.450 | lower in positive | yes | 2.4e-37 | 0.0021 |
| mean(T05.c04) via T02.c04 -> T01.c04 then T02.c01 -> T05.c03 | 0.558 | higher in positive | yes | 4.7e-76 | 0.0015 |
| value(T01.c01) via (target table itself) | 0.512 | higher in positive | yes | 0.12 | 0.0014 |
| days_since_last(T02 rows) via T02.c04 -> T01.c04 | 0.425 | lower in positive | yes | 1.9e-76 | 0.0014 |

## 4. Interpretations of the outcome evidence (hypotheses)

- **observed association** (confidence 0.75): Users with more distinct ads viewed and more view events (T02) before the cutoff are more often engaged; this is the strongest associated signal. _[P:f:f066, P:f:f063, P:path:1]_
- **observed association** (confidence 0.65): Higher counts of contact-request events (T06) and of searches (T04) and search impressions (T08) are also associated with engagement, but more weakly. _[P:f:f018, P:f:f015, P:f:f024, P:f:f032]_
- **observed association** (confidence 0.60): More recent activity (fewer days since last view/search) is associated with engagement. _[P:f:f065, P:f:f026, P:f:f017]_
- **observed association** (confidence 0.65): Static user attributes in T01 (device/agent codes) show essentially no association with engagement. _[P:f:f000, P:f:f001, P:f:f002, P:f:f003]_
- **observed association** (confidence 0.70): Predictability is modest: the model only slightly beats a single past-activity count, and base rate is high (~0.9), dropping in the test period. _[P:m:1, P:m:2]_
- **hypothesis** (confidence 0.40): The 'qualifying interaction' likely corresponds to ad views (T02) or searches, which would explain why past view volume is the dominant predictor (behavioural persistence). _[P:path:1, P:f:f064]_

## 5. Column meanings (interpretation)

| Column | Meaning | Role | Confidence |
|---|---|---|---|
| T01.c01 _(actually: UserInfo.UserAgentID)_ | User-agent identifier (browser string id); not a link to users | categorical_code | 0.40 |
| T01.c02 _(actually: UserInfo.UserDeviceID)_ | Device or user-agent sub-attribute identifier | categorical_code | 0.35 |
| T01.c03 _(actually: UserInfo.UserAgentFamilyID)_ | User-agent family or OS code (45 values) | categorical_code | 0.35 |
| T01.c04 _(actually: UserInfo.UserID)_ | User identifier | primary_key | 0.90 |
| T01.c05 _(actually: UserInfo.UserAgentOSID)_ | User-agent OS or family code (32 values) | categorical_code | 0.35 |
| T02.c01 _(actually: VisitStream.AdID)_ | Ad viewed | foreign_key | 0.80 |
| T02.c02 _(actually: VisitStream.IPID)_ | IP address identifier (shared id space with T04.c06/T06.c01; no IP table) | identifier_not_foreign_key | 0.50 |
| T02.c03 _(actually: VisitStream.ViewDate)_ | View timestamp | timestamp | 0.85 |
| T02.c04 _(actually: VisitStream.UserID)_ | User who viewed the ad | foreign_key | 0.85 |
| T03.c01 _(actually: Location.Level)_ | Location level in hierarchy (1-3; mostly 3) | categorical_code | 0.55 |
| T03.c02 _(actually: Location.RegionID)_ | Region identifier | categorical_code | 0.50 |
| T03.c03 _(actually: Location.LocationID)_ | Location identifier | primary_key | 0.85 |
| T03.c04 _(actually: Location.CityID)_ | City identifier | categorical_code | 0.45 |
| T04.c01 _(actually: SearchInfo.CategoryID)_ | Search category | foreign_key | 0.60 |
| T04.c02 _(actually: SearchInfo.SearchDate)_ | Search timestamp | timestamp | 0.85 |
| T04.c03 _(actually: SearchInfo.SearchQuery)_ | Free-text search query (often empty) | text | 0.65 |
| T04.c04 _(actually: SearchInfo.LocationID)_ | Search location | foreign_key | 0.70 |
| T04.c05 _(actually: SearchInfo.UserID)_ | User who searched | foreign_key | 0.85 |
| T04.c06 _(actually: SearchInfo.IPID)_ | IP address identifier | identifier_not_foreign_key | 0.50 |
| T04.c07 _(actually: SearchInfo.IsUserLoggedOn)_ | User logged-in flag at search time (32% yes) | flag | 0.50 |
| T04.c08 _(actually: SearchInfo.SearchID)_ | Search identifier | primary_key | 0.90 |
| T05.c01 _(actually: AdsInfo.LocationID)_ | Ad location | foreign_key | 0.75 |
| T05.c02 _(actually: AdsInfo.CategoryID)_ | Ad category | foreign_key | 0.70 |
| T05.c03 _(actually: AdsInfo.AdID)_ | Ad identifier | primary_key | 0.90 |
| T05.c04 _(actually: AdsInfo.Price)_ | Ad price (with sentinel extreme values) | measure | 0.60 |
| T05.c05 _(actually: AdsInfo.IsContext)_ | Contextual/paid ad flag (0.4% positive) | flag | 0.45 |
| T05.c06 _(actually: AdsInfo.Title)_ | Ad title (Cyrillic text) | text | 0.70 |
| T06.c01 _(actually: PhoneRequestsStream.IPID)_ | IP address identifier | identifier_not_foreign_key | 0.50 |
| T06.c02 _(actually: PhoneRequestsStream.PhoneRequestDate)_ | Contact request timestamp | timestamp | 0.80 |
| T06.c03 _(actually: PhoneRequestsStream.AdID)_ | Ad for which contact was requested | foreign_key | 0.75 |
| T06.c04 _(actually: PhoneRequestsStream.UserID)_ | User requesting contact | foreign_key | 0.80 |
| T07.c01 _(actually: Category.SubcategoryID)_ | Subcategory code (separate id space, 1-57) | categorical_code | 0.35 |
| T07.c02 _(actually: Category.CategoryID)_ | Category identifier | primary_key | 0.85 |
| T07.c03 _(actually: Category.Level)_ | Category level (1-3) | categorical_code | 0.55 |
| T07.c04 _(actually: Category.ParentCategoryID)_ | Parent category code (12 values) | categorical_code | 0.45 |
| T08.c01 _(actually: SearchStream.AdID)_ | Ad shown in search results | foreign_key | 0.80 |
| T08.c02 _(actually: SearchStream.IsClick)_ | Click flag (null for non-tracked ad types; ~0.6% clicks) | flag | 0.60 |
| T08.c03 _(actually: SearchStream.ObjectType)_ | Ad/object type (1-3) | categorical_code | 0.50 |
| T08.c04 _(actually: SearchStream.Position)_ | Display position of ad on results page | categorical_code | 0.50 |
| T08.c05 _(actually: SearchStream.SearchDate)_ | Impression/search timestamp | timestamp | 0.70 |
| T08.c06 _(actually: SearchStream.SearchID)_ | Search in which ad appeared | foreign_key | 0.85 |
| T08.c07 _(actually: SearchStream.HistCTR)_ | Historical click-through rate of ad (null where not applicable) | measure | 0.55 |

## 6. Unresolved ambiguities

- What counts as a 'qualifying interaction' for the outcome (views, searches, contact requests, clicks) is not defined. _[P:path:1]_
- Meanings of T01.c01, c02, c03, c05 (device/agent codes) are uncertain; their candidate links to T01.c04/T03.c03/T07.c02 look coincidental. _[S:r:1, S:r:4, S:r:7, S:r:13]_
- T02.c02, T04.c06, T06.c01 appear to be an IP-like id with no parent table; candidate links to T04.c08 are likely coincidental. _[S:r:19, S:r:51, S:r:73]_
- T07.c01 and T07.c04 hierarchy semantics (subcategory vs parent) and T03.c02/c04 (region vs city) unclear. _[S:r:79, S:r:93, S:r:29, S:r:36]_
- T08.c02 nulls (53%) roughly match T08.c07 nulls; whether clicks are only tracked for certain ad types is unconfirmed. _[S:c:T08.c02, S:c:T08.c07, S:c:T08.c03]_
- Positive rate drops from 0.906 to 0.851 in test, suggesting temporal shift or edge effects near the data end date. _[P:m:1]_

## 7. Suggested next investigations

- Confirm with business the definition of qualifying interaction and which table generates the label.
- Check T08.c05 equals T04.c02 via T08.c06 join to verify denormalized search time.
- Cross-tab T08.c02 nulls with T08.c03 and T05.c05 to confirm click tracking only for contextual ads.
- Verify IP-id overlap among T02.c02, T04.c06, T06.c01.
- Inspect T07 and T03 rows to validate hierarchy columns.
- Investigate the test-period base-rate drop and add windowed/recency features for robustness.

## 8. Limitations

- Meanings are inferred from data patterns. Nothing here is an organisation-approved (governed) definition.
- Relationship candidates come from value overlap. On dense integer keys, overlap alone is weak evidence (see range_density).
- Predictive associations come from one dataset over about 3 weeks, with 3 training cutoffs. They may not hold in other periods.
- Static tables (no time column) are used as-is and may contain information recorded after a cutoff.
