# Discovery report: rel-avito, configuration C, original names, run 1

This is the output of the system as a reader would receive it. **Computed facts** come from deterministic analysis. **Interpretations** are the LLM's hypotheses, each with its confidence and the evidence IDs it cites (see `packets/C_original.md`).

## 1. Inferred entities (interpretation)

| Table | Concept | Kind | Confidence | Needs human check | Evidence |
|---|---|---|---|---|---|
| AdsInfo | Advertisement (classified listing) catalogue: one row per ad with its location, category, price, title and a context-ad flag | entity | 0.85 | no | S:t:AdsInfo, S:k:AdsInfo.AdID, S:c:AdsInfo.Title, S:c:AdsInfo.Price |
| Category | Ad/search category hierarchy with 3 levels (1 root, 11 level-2, 56 level-3) | dimension | 0.80 | no | S:t:Category, S:k:Category.CategoryID, S:c:Category.Level, S:c:Category.ParentCategoryID |
| Location | Geographic location dimension (country/region/city levels) with region and city codes | dimension | 0.75 | no | S:t:Location, S:k:Location.LocationID, S:c:Location.Level, S:c:Location.RegionID |
| PhoneRequestsStream | Event log of users requesting a seller's phone number on an ad (contact events) | event | 0.75 | yes | S:t:PhoneRequestsStream, S:a:127, S:r:49, S:r:52 |
| SearchInfo | Search session/event: one row per search performed by a user, with query text, search location/category filters, login status and IP | event | 0.80 | no | S:t:SearchInfo, S:k:SearchInfo.SearchID, S:c:SearchInfo.SearchQuery, S:r:72 |
| SearchStream | Ad impressions shown on search result pages: one row per (search, ad) shown, with position, ad object type, historical CTR and click flag | bridge | 0.75 | no | S:t:SearchStream, S:a:128, S:r:91, S:r:75 |
| UserInfo | User entity (outcome entity) with browser/user-agent, OS, device and agent-family codes | entity | 0.85 | no | S:t:UserInfo, S:k:UserInfo.UserID, S:c:UserInfo.UserAgentID, S:c:UserInfo.UserDeviceID |
| VisitStream | Event log of users viewing/visiting ad pages; likely the source of the engagement outcome | event | 0.80 | yes | S:t:VisitStream, S:a:129, S:r:110, S:r:113 |

## 2. Relationships accepted by the interpreter

| Child column | Parent key | Confidence | Computed overlap evidence |
|---|---|---|---|
| AdsInfo.CategoryID | Category.CategoryID | 0.85 | inclusion 1.0, coverage 0.7647, rank 1 |
| AdsInfo.LocationID | Location.LocationID | 0.85 | inclusion 1.0, coverage 0.9576, rank 1 |
| Category.ParentCategoryID | Category.CategoryID | 0.55 | inclusion 1.0, coverage 0.1765, rank 1 |
| PhoneRequestsStream.AdID | AdsInfo.AdID | 0.85 | inclusion 1.0, coverage 0.043, rank 1 |
| PhoneRequestsStream.UserID | UserInfo.UserID | 0.85 | inclusion 1.0, coverage 0.3818, rank 1 |
| SearchInfo.UserID | UserInfo.UserID | 0.90 | inclusion 1.0, coverage 0.9988, rank 1 |
| SearchInfo.LocationID | Location.LocationID | 0.80 | inclusion 1.0, coverage 0.5803, rank 1 |
| SearchInfo.CategoryID | Category.CategoryID | 0.75 | inclusion 1.0, coverage 0.5735, rank 1 |
| SearchStream.SearchID | SearchInfo.SearchID | 0.90 | inclusion 1.0, coverage 0.9873, rank 1 |
| SearchStream.AdID | AdsInfo.AdID | 0.85 | inclusion 1.0, coverage 0.438, rank 1 |
| VisitStream.AdID | AdsInfo.AdID | 0.85 | inclusion 1.0, coverage 0.6394, rank 1 |
| VisitStream.UserID | UserInfo.UserID | 0.85 | inclusion 1.0, coverage 0.7794, rank 1 |

## 3. Predictive associations (computed facts, held-out data)

Selected model test AUROC: 0.668 (single best activity count: 0.655). These are associations measured on time-ordered data. They are not causal and do not establish meaning.

| Feature | Validation AUROC | Direction | Stable across cutoffs | q (BH) | Permutation importance |
|---|---|---|---|---|---|
| count_distinct(VisitStream.AdID) via VisitStream.UserID -> UserInfo.UserID | 0.688 | higher in positive | yes | 0 | 0.2798 |
| count(VisitStream rows) via VisitStream.UserID -> UserInfo.UserID | 0.683 | higher in positive | yes | 0 | 0.0321 |
| count_distinct(PhoneRequestsStream.AdID) via PhoneRequestsStream.UserID -> UserInfo.UserID | 0.604 | higher in positive | yes | 1e-147 | 0.0181 |
| count_distinct(VisitStream.IPID) via VisitStream.UserID -> UserInfo.UserID | 0.553 | higher in positive | yes | 3.2e-163 | 0.0144 |
| count(PhoneRequestsStream rows) via PhoneRequestsStream.UserID -> UserInfo.UserID | 0.603 | higher in positive | yes | 9.5e-147 | 0.0107 |
| count(SearchInfo rows) via SearchInfo.UserID -> UserInfo.UserID | 0.621 | higher in positive | yes | 1.1e-207 | 0.0034 |
| days_since_last(SearchInfo rows) via SearchInfo.UserID -> UserInfo.UserID | 0.450 | lower in positive | yes | 2.4e-37 | 0.0021 |
| mean(AdsInfo.Price) via VisitStream.UserID -> UserInfo.UserID then VisitStream.AdID -> AdsInfo.AdID | 0.558 | higher in positive | yes | 4.7e-76 | 0.0015 |
| value(UserInfo.UserAgentID) via (target table itself) | 0.512 | higher in positive | yes | 0.12 | 0.0014 |
| days_since_last(VisitStream rows) via VisitStream.UserID -> UserInfo.UserID | 0.425 | lower in positive | yes | 1.9e-76 | 0.0014 |

## 4. Interpretations of the outcome evidence (hypotheses)

- **observed association** (confidence 0.85): Number of distinct ads a user viewed before the cutoff is the strongest single association with future engagement (higher in positives, stable across cutoffs). _[P:f:f066, P:path:1]_
- **observed association** (confidence 0.80): Overall past visit volume (all-time and last 4 days) is higher among engaged users; the best single count alone reaches test AUROC 0.655. _[P:f:f063, P:f:f064, P:m:2]_
- **observed association** (confidence 0.75): Past phone-request and search activity counts are also higher in positives, but weaker than visit activity. _[P:f:f018, P:f:f015, P:f:f024, P:f:f032, P:path:2]_
- **observed association** (confidence 0.65): More recent last activity (fewer days since last visit/search/phone request) is associated with positive outcome. _[P:f:f065, P:f:f026, P:f:f017]_
- **hypothesis** (confidence 0.60): The full model adds only modest lift over a single activity count (test AUROC ~0.67 vs 0.655), suggesting engagement is largely captured by prior activity level (habitual users stay engaged). _[P:m:1, P:m:2]_
- **observed association** (confidence 0.75): Device/user-agent attributes and the coincidental-overlap paths (CityID->UserID, UserAgentID->UserID, etc.) show near-chance AUROC and ~zero importance, consistent with them not being real relationships. _[P:f:f000, P:f:f004, P:f:f039, P:f:f051, P:path:12]_
- **observed association** (confidence 0.45): Users who viewed higher-priced ads have slightly higher engagement rates (weak association). _[P:f:f068]_
- **hypothesis** (confidence 0.50): Positive rate drops in the test period (0.851 vs ~0.90), indicating temporal drift or end-of-data truncation that may affect performance (test AUROC lower than val). _[P:m:1]_

## 5. Column meanings (interpretation)

| Column | Meaning | Role | Confidence |
|---|---|---|---|
| AdsInfo.AdID | Unique ad identifier | primary_key | 0.95 |
| AdsInfo.LocationID | Location where the ad is posted | foreign_key | 0.85 |
| AdsInfo.CategoryID | Category of the ad | foreign_key | 0.85 |
| AdsInfo.Price | Listed price of the item (currency unknown, likely RUB); max 999999999999 looks like a placeholder/outlier | measure | 0.80 |
| AdsInfo.Title | Ad title text (Russian) | text | 0.90 |
| AdsInfo.IsContext | Flag: ad is a paid contextual ad (~0.4% of ads) | flag | 0.65 |
| Category.CategoryID | Unique category identifier | primary_key | 0.95 |
| Category.Level | Depth in category hierarchy (1=root, 2, 3=leaf) | categorical_code | 0.80 |
| Category.ParentCategoryID | Parent category in the hierarchy; 12 distinct values matches 1 level-1 + 11 level-2 categories | foreign_key | 0.60 |
| Category.SubcategoryID | Alternative/subcategory code, possibly from a separate numbering scheme; not clearly a reference to CategoryID | identifier_not_foreign_key | 0.40 |
| Location.LocationID | Unique location identifier | primary_key | 0.95 |
| Location.Level | Geographic level (1=country, 2=region, 3=city) | categorical_code | 0.70 |
| Location.RegionID | Region code (84 regions); separate code space, not a LocationID | categorical_code | 0.65 |
| Location.CityID | City code; separate code space (overlap with UserID is coincidental) | categorical_code | 0.65 |
| PhoneRequestsStream.UserID | User who requested the phone number | foreign_key | 0.85 |
| PhoneRequestsStream.IPID | Anonymised IP address identifier; no parent table | identifier_not_foreign_key | 0.70 |
| PhoneRequestsStream.AdID | Ad whose phone number was requested | foreign_key | 0.85 |
| PhoneRequestsStream.PhoneRequestDate | Timestamp of phone request | timestamp | 0.90 |
| SearchInfo.UserID | User who performed the search | foreign_key | 0.90 |
| SearchInfo.SearchID | Unique search identifier | primary_key | 0.95 |
| SearchInfo.SearchDate | Timestamp of search | timestamp | 0.90 |
| SearchInfo.IPID | Anonymised IP identifier | identifier_not_foreign_key | 0.70 |
| SearchInfo.IsUserLoggedOn | Flag: user was logged in during search (~32%) | flag | 0.85 |
| SearchInfo.SearchQuery | Free-text query; 84% null (browsing without query) | text | 0.85 |
| SearchInfo.LocationID | Location filter/context of the search | foreign_key | 0.80 |
| SearchInfo.CategoryID | Category filter/context of the search | foreign_key | 0.75 |
| SearchStream.SearchID | Search on whose result page the ad was shown | foreign_key | 0.90 |
| SearchStream.AdID | Ad shown in search results | foreign_key | 0.85 |
| SearchStream.Position | Display slot of the ad on the result page (only 1,2,6,7,8 observed) | categorical_code | 0.75 |
| SearchStream.ObjectType | Type of ad shown (likely 1=regular, 2=highlighted, 3=contextual) | categorical_code | 0.60 |
| SearchStream.HistCTR | Historical click-through rate of the ad; null share (51.4%) equals share of ObjectType 1+2 rows, so populated only for ObjectType 3 | measure | 0.70 |
| SearchStream.IsClick | Flag: impression was clicked (~0.6% of non-null); null for non-contextual rows and possibly a held-out period | flag | 0.70 |
| SearchStream.SearchDate | Timestamp of the search (denormalised from SearchInfo) | timestamp | 0.80 |
| UserInfo.UserID | Unique user identifier (outcome entity) | primary_key | 0.95 |
| UserInfo.UserAgentID | Browser user-agent string code; overlap with UserID coincidental | categorical_code | 0.65 |
| UserInfo.UserAgentOSID | Operating system code | categorical_code | 0.65 |
| UserInfo.UserDeviceID | Device model code | categorical_code | 0.65 |
| UserInfo.UserAgentFamilyID | Browser family code | categorical_code | 0.65 |
| VisitStream.UserID | User who viewed the ad | foreign_key | 0.85 |
| VisitStream.IPID | Anonymised IP identifier | identifier_not_foreign_key | 0.70 |
| VisitStream.AdID | Ad that was viewed | foreign_key | 0.85 |
| VisitStream.ViewDate | Timestamp of ad view | timestamp | 0.90 |

## 6. Unresolved ambiguities

- Exact definition of the outcome ('visits more than one ad') - presumably counted from VisitStream; unclear whether distinct AdID or row count and whether ads viewed via SearchStream clicks count. _[S:t:VisitStream, P:f:f066]_
- Meaning of SearchStream.ObjectType codes and why IsClick has slightly more nulls than HistCTR (possible held-out test period). _[S:c:SearchStream.ObjectType, S:c:SearchStream.IsClick, S:c:SearchStream.HistCTR]_
- Category.SubcategoryID semantics: separate code scheme vs reference to CategoryID; flagged weak overlap. _[S:c:Category.SubcategoryID, S:r:29, S:a:63]_
- Location.RegionID and CityID likely use their own code spaces; their candidate links to LocationID/UserID are probably coincidental. _[S:r:34, S:r:45, S:a:8, S:a:11]_
- IPID has no parent table; links to SearchInfo.SearchID are value-range coincidences. _[S:r:50, S:r:60, S:r:111]_
- AdsInfo.Price contains extreme placeholder-like values (999999999999) and zeros. _[S:c:AdsInfo.Price]_
- Days-since-last features cover only 43-60% of users, so many labeled users had no prior activity in some streams; how they are labeled/included is unclear. _[P:f:f065, P:f:f026, P:f:f017]_

## 7. Suggested next investigations

- Confirm the outcome construction (distinct vs total VisitStream rows in 4-day window) and check for leakage near the cutoff.
- Rebuild features excluding coincidental relationships (CityID, UserAgentID, UserDeviceID, IPID links) and re-evaluate model.
- Add recency-weighted and trend features (e.g., visits in last 1/2/7 days, slope) and session-based features from SearchStream clicks.
- Examine engagement by category and location of viewed/searched ads via valid FK joins.
- Investigate the drop in positive rate in the test period (seasonality, data end truncation at 2015-05-20).
- Validate ObjectType/IsClick/HistCTR semantics with business owners and compute contextual-ad click rate per user as a feature.
- Cohort analysis of new users (no prior activity) vs returning users to understand base rates.

## 8. Limitations

- Meanings are inferred from data patterns. Nothing here is an organisation-approved (governed) definition.
- Relationship candidates come from value overlap. On dense integer keys, overlap alone is weak evidence (see range_density).
- Predictive associations come from one dataset over about 3 weeks, with 3 training cutoffs. They may not hold in other periods.
- Static tables (no time column) are used as-is and may contain information recorded after a cutoff.
