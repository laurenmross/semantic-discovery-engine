## Business outcome of interest (supplied by the business)
- User engagement: whether the user visits more than one ad in the 4 days after the cutoff timestamp.
- Outcome entity: UserInfo.UserID

## Schema (tables, columns, types, row counts, example values)
### Table AdsInfo  [S:t:AdsInfo]  rows=5960558
- AdID: BIGINT; examples ['0', '1', '2']  [S:c:AdsInfo.AdID]
    profile: nulls=0.0% distinct=5960558 unique=yes min=0 max=5960557 mean=2.98e+06
- LocationID: BIGINT; examples ['497', '335', '341']  [S:c:AdsInfo.LocationID]
    profile: nulls=0.4% distinct=3363 unique=no min=1 max=3443 mean=346.7
- CategoryID: BIGINT; examples ['22', '43', '47']  [S:c:AdsInfo.CategoryID]
    profile: nulls=0.0% distinct=52 unique=no min=2 max=67 mean=38.37
- Price: DOUBLE; examples ['400.0', '6864.0', '7800000.0']  [S:c:AdsInfo.Price]
    profile: nulls=0.0% distinct=65562 unique=no min=0.0 max=999999999999.0 mean=5.451e+06
- Title: VARCHAR; examples ['[redacted ad title]', '[redacted ad title]', '[redacted ad title]']  [S:c:AdsInfo.Title]
    profile: nulls=0.0% distinct=3246389 unique=no avg_len=24.8
- IsContext: DOUBLE; examples ['0.0', '1.0']  [S:c:AdsInfo.IsContext]
    profile: nulls=0.0% distinct=2 unique=no min=0.0 max=1.0 mean=0.004151 top=0.0:5935816, 1.0:24742 (float type holding only whole numbers)

### Table Category  [S:t:Category]  rows=68
- CategoryID: BIGINT; examples ['0', '1', '2']  [S:c:Category.CategoryID]
    profile: nulls=0.0% distinct=68 unique=yes min=0 max=67 mean=33.5
- Level: BIGINT; examples ['1', '2', '3']  [S:c:Category.Level]
    profile: nulls=0.0% distinct=3 unique=no min=1 max=3 mean=2.809 top=3:56, 2:11, 1:1
- ParentCategoryID: BIGINT; examples ['10', '9', '12']  [S:c:Category.ParentCategoryID]
    profile: nulls=0.0% distinct=12 unique=no min=1 max=12 mean=6.632 top=12:11, 2:9, 4:8, 6:7, 8:7, 9:7
- SubcategoryID: BIGINT; examples ['45', '5', '25']  [S:c:Category.SubcategoryID]
    profile: nulls=0.0% distinct=57 unique=no min=1 max=57 mean=31.59

### Table Location  [S:t:Location]  rows=3512
- LocationID: BIGINT; examples ['0', '1', '2']  [S:c:Location.LocationID]
    profile: nulls=0.0% distinct=3512 unique=yes min=0 max=3511 mean=1756
- Level: DOUBLE; examples ['2.0', '3.0', '1.0']  [S:c:Location.Level]
    profile: nulls=0.0% distinct=3 unique=no min=1.0 max=3.0 mean=2.976 top=3.0:3429, 2.0:82, 1.0:1 (float type holding only whole numbers)
- RegionID: DOUBLE; examples ['70.0', '56.0', '64.0']  [S:c:Location.RegionID]
    profile: nulls=0.0% distinct=84 unique=no min=1.0 max=84.0 mean=41.22 (float type holding only whole numbers)
- CityID: DOUBLE; examples ['3024.0', '2791.0', '1139.0']  [S:c:Location.CityID]
    profile: nulls=0.0% distinct=3290 unique=no min=1.0 max=3722.0 mean=1857 (float type holding only whole numbers)

### Table PhoneRequestsStream  [S:t:PhoneRequestsStream]  rows=302974
- UserID: BIGINT; examples ['38950', '18761', '88796']  [S:c:PhoneRequestsStream.UserID]
    profile: nulls=0.4% distinct=37507 unique=no min=2 max=98139 mean=4.941e+04
- IPID: DOUBLE; examples ['1629303.0', '109220.0', '1462925.0']  [S:c:PhoneRequestsStream.IPID]
    profile: nulls=0.0% distinct=36355 unique=no min=63.0 max=2266665.0 mean=1.129e+06 (float type holding only whole numbers)
- AdID: BIGINT; examples ['1938326', '3917327', '3806832']  [S:c:PhoneRequestsStream.AdID]
    profile: nulls=0.2% distinct=256195 unique=no min=9 max=5929465 mean=2.963e+06
- PhoneRequestDate: TIMESTAMP_NS; examples ['2015-04-25 11:50:35', '2015-04-25 11:51:14', '2015-04-25 12:07:43']  [S:c:PhoneRequestsStream.PhoneRequestDate]
    profile: nulls=0.0% distinct=275103 unique=no min=2015-04-25 00:00:08 max=2015-05-20 17:55:09

### Table SearchInfo  [S:t:SearchInfo]  rows=2579289
- UserID: BIGINT; examples ['2139', '1477', '68959']  [S:c:SearchInfo.UserID]
    profile: nulls=1.3% distinct=98137 unique=no min=0 max=98240 mean=4.851e+04
- SearchID: BIGINT; examples ['0', '1', '2']  [S:c:SearchInfo.SearchID]
    profile: nulls=0.0% distinct=2579289 unique=yes min=0 max=2579288 mean=1.29e+06
- SearchDate: TIMESTAMP_NS; examples ['2015-04-25 00:00:01', '2015-04-25 00:00:02', '2015-04-25 00:00:03']  [S:c:SearchInfo.SearchDate]
    profile: nulls=0.0% distinct=1351586 unique=no min=2015-04-25 00:00:01 max=2015-05-20 17:59:56
- IPID: DOUBLE; examples ['837134.0', '2187370.0', '2089629.0']  [S:c:SearchInfo.IPID]
    profile: nulls=0.0% distinct=113464 unique=no min=28.0 max=2266691.0 mean=1.139e+06 (float type holding only whole numbers)
- IsUserLoggedOn: DOUBLE; examples ['1.0', '0.0']  [S:c:SearchInfo.IsUserLoggedOn]
    profile: nulls=0.0% distinct=2 unique=no min=0.0 max=1.0 mean=0.3207 top=0.0:1752194, 1.0:827095 (float type holding only whole numbers)
- SearchQuery: VARCHAR; examples ['[redacted search query]', '[redacted search query]', '[redacted search query]']  [S:c:SearchInfo.SearchQuery]
    profile: nulls=84.1% distinct=17371 unique=no avg_len=9.4
- LocationID: BIGINT; examples ['497', '334', '375']  [S:c:SearchInfo.LocationID]
    profile: nulls=0.0% distinct=2038 unique=no min=0 max=3443 mean=306.5
- CategoryID: BIGINT; examples ['34', '22', '60']  [S:c:SearchInfo.CategoryID]
    profile: nulls=0.0% distinct=39 unique=no min=0 max=67 mean=29.34

### Table SearchStream  [S:t:SearchStream]  rows=9254702
- SearchID: BIGINT; examples ['541363', '162315', '1804098']  [S:c:SearchStream.SearchID]
    profile: nulls=0.0% distinct=2546557 unique=no min=0 max=2579288 mean=1.295e+06
- AdID: BIGINT; examples ['806173', '4316980', '2059012']  [S:c:SearchStream.AdID]
    profile: nulls=0.0% distinct=2610692 unique=no min=1 max=5929464 mean=2.978e+06
- Position: DOUBLE; examples ['8.0', '2.0', '7.0']  [S:c:SearchStream.Position]
    profile: nulls=0.0% distinct=5 unique=no min=1.0 max=8.0 mean=4.362 top=1.0:2546548, 7.0:2281343, 2.0:1826066, 6.0:1301252, 8.0:1299493 (float type holding only whole numbers)
- ObjectType: DOUBLE; examples ['1.0', '3.0', '2.0']  [S:c:SearchStream.ObjectType]
    profile: nulls=0.0% distinct=3 unique=no min=1.0 max=3.0 mean=2.074 top=3.0:4493367, 1.0:3811571, 2.0:949764 (float type holding only whole numbers)
- HistCTR: DOUBLE; examples ['0.005902', '0.049664', '0.002413']  [S:c:SearchStream.HistCTR]
    profile: nulls=51.4% distinct=46688 unique=no min=1e-05 max=1.0 mean=0.01055
- IsClick: DOUBLE; examples ['0.0', '1.0']  [S:c:SearchStream.IsClick]
    profile: nulls=53.4% distinct=2 unique=no min=0.0 max=1.0 mean=0.006034 top=None:4939582, 0.0:4289081, 1.0:26039 (float type holding only whole numbers)
- SearchDate: TIMESTAMP_NS; examples ['2015-04-30 20:57:06', '2015-04-26 23:19:37', '2015-05-12 18:11:59']  [S:c:SearchStream.SearchDate]
    profile: nulls=0.0% distinct=1343285 unique=no min=2015-04-25 00:00:01 max=2015-05-20 17:59:56

### Table UserInfo  [S:t:UserInfo]  rows=98250
- UserID: BIGINT; examples ['0', '1', '2']  [S:c:UserInfo.UserID]
    profile: nulls=0.0% distinct=98250 unique=yes min=0 max=98249 mean=4.912e+04
- UserAgentID: DOUBLE; examples ['54898.0', '15248.0', '12555.0']  [S:c:UserInfo.UserAgentID]
    profile: nulls=0.0% distinct=7046 unique=no min=3.0 max=64016.0 mean=3.307e+04 (float type holding only whole numbers)
- UserAgentOSID: DOUBLE; examples ['20.0', '35.0', '30.0']  [S:c:UserInfo.UserAgentOSID]
    profile: nulls=0.0% distinct=32 unique=no min=1.0 max=51.0 mean=22.95 (float type holding only whole numbers)
- UserDeviceID: DOUBLE; examples ['2014.0', '4093.0', '2019.0']  [S:c:UserInfo.UserDeviceID]
    profile: nulls=0.0% distinct=892 unique=no min=5.0 max=4205.0 mean=2035 (float type holding only whole numbers)
- UserAgentFamilyID: DOUBLE; examples ['85.0', '25.0', '9.0']  [S:c:UserInfo.UserAgentFamilyID]
    profile: nulls=0.0% distinct=45 unique=no min=1.0 max=89.0 mean=42.59 (float type holding only whole numbers)

### Table VisitStream  [S:t:VisitStream]  rows=6454562
- UserID: BIGINT; examples ['76240', '88796', '77228']  [S:c:VisitStream.UserID]
    profile: nulls=0.4% distinct=76574 unique=no min=0 max=98217 mean=4.91e+04
- IPID: DOUBLE; examples ['711105.0', '1462925.0', '964705.0']  [S:c:VisitStream.IPID]
    profile: nulls=0.0% distinct=92845 unique=no min=73.0 max=2266670.0 mean=1.136e+06 (float type holding only whole numbers)
- AdID: BIGINT; examples ['2270750', '4865813', '4635684']  [S:c:VisitStream.AdID]
    profile: nulls=0.2% distinct=3811150 unique=no min=0 max=5960390 mean=2.965e+06
- ViewDate: TIMESTAMP_NS; examples ['2015-05-17 15:19:02', '2015-05-17 15:42:14', '2015-05-17 15:45:06']  [S:c:VisitStream.ViewDate]
    profile: nulls=0.0% distinct=1805877 unique=no min=2015-04-25 00:00:00 max=2015-05-20 17:59:19

## Structural analysis (deterministic; computed from values only, never from names)
Candidate keys (100% unique, no nulls):
- AdsInfo.AdID  [S:k:AdsInfo.AdID]
- Category.CategoryID  [S:k:Category.CategoryID]
- Location.LocationID  [S:k:Location.LocationID]
- SearchInfo.SearchID  [S:k:SearchInfo.SearchID]
- UserInfo.UserID  [S:k:UserInfo.UserID]
Time columns: PhoneRequestsStream.PhoneRequestDate, SearchInfo.SearchDate, SearchStream.SearchDate, VisitStream.ViewDate

Candidate relationships (child column values contained in a candidate key).
Fields: inclusion = share of distinct child values found in parent key; coverage = share of parent keys referenced; range_density = share of the child's value range filled by parent keys (near 1.0 means inclusion is weak evidence, because any small integers would match); rows/parent = avg and max child rows per referenced parent; rank = rank of this parent among this child column's candidates by coverage; preferred = top-ranked and plausible; weak = both sides are small integer ranges starting near 0/1.
- [S:r:1] AdsInfo.CategoryID -> Category.CategoryID: inclusion=1.0 coverage=0.7647 range_density=1.0 rows/parent=114625.5/741045 child_distinct=52 rank=1 preferred=yes weak=no
- [S:r:2] AdsInfo.CategoryID -> Location.LocationID: inclusion=1.0 coverage=0.0148 range_density=1.0 rows/parent=114625.5/741045 child_distinct=52 rank=2 preferred=no weak=no
- [S:r:3] AdsInfo.CategoryID -> UserInfo.UserID: inclusion=1.0 coverage=0.0005 range_density=1.0 rows/parent=114625.5/741045 child_distinct=52 rank=3 preferred=no weak=no
- [S:r:4] AdsInfo.CategoryID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=114625.5/741045 child_distinct=52 rank=4 preferred=no weak=no
- [S:r:5] AdsInfo.CategoryID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=114625.5/741045 child_distinct=52 rank=5 preferred=no weak=no
- [S:r:6] AdsInfo.IsContext -> Category.CategoryID: inclusion=1.0 coverage=0.0294 range_density=1.0 rows/parent=2980279.0/5935816 child_distinct=2 rank=1 preferred=yes weak=yes
- [S:r:7] AdsInfo.IsContext -> Location.LocationID: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=2980279.0/5935816 child_distinct=2 rank=2 preferred=no weak=no
- [S:r:8] AdsInfo.IsContext -> UserInfo.UserID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2980279.0/5935816 child_distinct=2 rank=3 preferred=no weak=no
- [S:r:9] AdsInfo.IsContext -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2980279.0/5935816 child_distinct=2 rank=4 preferred=no weak=no
- [S:r:10] AdsInfo.IsContext -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2980279.0/5935816 child_distinct=2 rank=5 preferred=no weak=no
- [S:r:11] AdsInfo.LocationID -> Location.LocationID: inclusion=1.0 coverage=0.9576 range_density=1.0 rows/parent=1765.03/929887 child_distinct=3363 rank=1 preferred=yes weak=no
- [S:r:12] AdsInfo.LocationID -> UserInfo.UserID: inclusion=1.0 coverage=0.0342 range_density=1.0 rows/parent=1765.03/929887 child_distinct=3363 rank=2 preferred=no weak=no
- [S:r:13] AdsInfo.LocationID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0013 range_density=1.0 rows/parent=1765.03/929887 child_distinct=3363 rank=3 preferred=no weak=no
- [S:r:14] AdsInfo.LocationID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=1765.03/929887 child_distinct=3363 rank=4 preferred=no weak=no
- [S:r:15] Category.CategoryID -> Location.LocationID: inclusion=1.0 coverage=0.0194 range_density=1.0 rows/parent=1.0/1 child_distinct=68 rank=1 preferred=no weak=no child_is_unique
- [S:r:16] Category.CategoryID -> UserInfo.UserID: inclusion=1.0 coverage=0.0007 range_density=1.0 rows/parent=1.0/1 child_distinct=68 rank=2 preferred=no weak=no child_is_unique
- [S:r:17] Category.CategoryID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1.0/1 child_distinct=68 rank=3 preferred=no weak=no child_is_unique
- [S:r:18] Category.CategoryID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1.0/1 child_distinct=68 rank=4 preferred=no weak=no child_is_unique
- [S:r:19] Category.Level -> Category.CategoryID: inclusion=1.0 coverage=0.0441 range_density=1.0 rows/parent=22.67/56 child_distinct=3 rank=1 preferred=yes weak=yes
- [S:r:20] Category.Level -> Location.LocationID: inclusion=1.0 coverage=0.0009 range_density=1.0 rows/parent=22.67/56 child_distinct=3 rank=2 preferred=no weak=no
- [S:r:21] Category.Level -> UserInfo.UserID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=22.67/56 child_distinct=3 rank=3 preferred=no weak=no
- [S:r:22] Category.Level -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=22.67/56 child_distinct=3 rank=4 preferred=no weak=no
- [S:r:23] Category.Level -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=22.67/56 child_distinct=3 rank=5 preferred=no weak=no
- [S:r:24] Category.ParentCategoryID -> Category.CategoryID: inclusion=1.0 coverage=0.1765 range_density=1.0 rows/parent=5.67/11 child_distinct=12 rank=1 preferred=yes weak=yes
- [S:r:25] Category.ParentCategoryID -> Location.LocationID: inclusion=1.0 coverage=0.0034 range_density=1.0 rows/parent=5.67/11 child_distinct=12 rank=2 preferred=no weak=no
- [S:r:26] Category.ParentCategoryID -> UserInfo.UserID: inclusion=1.0 coverage=0.0001 range_density=1.0 rows/parent=5.67/11 child_distinct=12 rank=3 preferred=no weak=no
- [S:r:27] Category.ParentCategoryID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=5.67/11 child_distinct=12 rank=4 preferred=no weak=no
- [S:r:28] Category.ParentCategoryID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=5.67/11 child_distinct=12 rank=5 preferred=no weak=no
- [S:r:29] Category.SubcategoryID -> Category.CategoryID: inclusion=1.0 coverage=0.8382 range_density=1.0 rows/parent=1.19/12 child_distinct=57 rank=1 preferred=yes weak=yes
- [S:r:30] Category.SubcategoryID -> Location.LocationID: inclusion=1.0 coverage=0.0162 range_density=1.0 rows/parent=1.19/12 child_distinct=57 rank=2 preferred=no weak=no
- [S:r:31] Category.SubcategoryID -> UserInfo.UserID: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=1.19/12 child_distinct=57 rank=3 preferred=no weak=no
- [S:r:32] Category.SubcategoryID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1.19/12 child_distinct=57 rank=4 preferred=no weak=no
- [S:r:33] Category.SubcategoryID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1.19/12 child_distinct=57 rank=5 preferred=no weak=no
- [S:r:34] Location.CityID -> UserInfo.UserID: inclusion=1.0 coverage=0.0335 range_density=1.0 rows/parent=1.07/10 child_distinct=3290 rank=1 preferred=yes weak=no
- [S:r:35] Location.CityID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0013 range_density=1.0 rows/parent=1.07/10 child_distinct=3290 rank=2 preferred=no weak=no
- [S:r:36] Location.CityID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=1.07/10 child_distinct=3290 rank=3 preferred=no weak=no
- [S:r:37] Location.Level -> Category.CategoryID: inclusion=1.0 coverage=0.0441 range_density=1.0 rows/parent=1170.67/3429 child_distinct=3 rank=1 preferred=yes weak=yes
- [S:r:38] Location.Level -> Location.LocationID: inclusion=1.0 coverage=0.0009 range_density=1.0 rows/parent=1170.67/3429 child_distinct=3 rank=2 preferred=no weak=no
- [S:r:39] Location.Level -> UserInfo.UserID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1170.67/3429 child_distinct=3 rank=3 preferred=no weak=no
- [S:r:40] Location.Level -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1170.67/3429 child_distinct=3 rank=4 preferred=no weak=no
- [S:r:41] Location.Level -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1170.67/3429 child_distinct=3 rank=5 preferred=no weak=no
- [S:r:42] Location.LocationID -> UserInfo.UserID: inclusion=1.0 coverage=0.0357 range_density=1.0 rows/parent=1.0/1 child_distinct=3512 rank=1 preferred=no weak=no child_is_unique
- [S:r:43] Location.LocationID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0014 range_density=1.0 rows/parent=1.0/1 child_distinct=3512 rank=2 preferred=no weak=no child_is_unique
- [S:r:44] Location.LocationID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=1.0/1 child_distinct=3512 rank=3 preferred=no weak=no child_is_unique
- [S:r:45] Location.RegionID -> Location.LocationID: inclusion=1.0 coverage=0.0239 range_density=1.0 rows/parent=41.8/221 child_distinct=84 rank=1 preferred=yes weak=no
- [S:r:46] Location.RegionID -> UserInfo.UserID: inclusion=1.0 coverage=0.0009 range_density=1.0 rows/parent=41.8/221 child_distinct=84 rank=2 preferred=no weak=no
- [S:r:47] Location.RegionID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=41.8/221 child_distinct=84 rank=3 preferred=no weak=no
- [S:r:48] Location.RegionID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=41.8/221 child_distinct=84 rank=4 preferred=no weak=no
- [S:r:49] PhoneRequestsStream.AdID -> AdsInfo.AdID: inclusion=1.0 coverage=0.043 range_density=1.0 rows/parent=1.18/83 child_distinct=256195 rank=1 preferred=yes weak=no
- [S:r:50] PhoneRequestsStream.IPID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0141 range_density=1.0 rows/parent=8.33/1123 child_distinct=36355 rank=1 preferred=yes weak=no
- [S:r:51] PhoneRequestsStream.IPID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0061 range_density=1.0 rows/parent=8.33/1123 child_distinct=36355 rank=2 preferred=no weak=no
- [S:r:52] PhoneRequestsStream.UserID -> UserInfo.UserID: inclusion=1.0 coverage=0.3818 range_density=1.0 rows/parent=8.04/1123 child_distinct=37507 rank=1 preferred=yes weak=no
- [S:r:53] PhoneRequestsStream.UserID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0145 range_density=1.0 rows/parent=8.04/1123 child_distinct=37507 rank=2 preferred=no weak=no
- [S:r:54] PhoneRequestsStream.UserID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0063 range_density=1.0 rows/parent=8.04/1123 child_distinct=37507 rank=3 preferred=no weak=no
- [S:r:55] SearchInfo.CategoryID -> Category.CategoryID: inclusion=1.0 coverage=0.5735 range_density=1.0 rows/parent=66135.62/282406 child_distinct=39 rank=1 preferred=yes weak=yes
- [S:r:56] SearchInfo.CategoryID -> Location.LocationID: inclusion=1.0 coverage=0.0111 range_density=1.0 rows/parent=66135.62/282406 child_distinct=39 rank=2 preferred=no weak=no
- [S:r:57] SearchInfo.CategoryID -> UserInfo.UserID: inclusion=1.0 coverage=0.0004 range_density=1.0 rows/parent=66135.62/282406 child_distinct=39 rank=3 preferred=no weak=no
- [S:r:58] SearchInfo.CategoryID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=66135.62/282406 child_distinct=39 rank=4 preferred=no weak=no
- [S:r:59] SearchInfo.CategoryID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=66135.62/282406 child_distinct=39 rank=5 preferred=no weak=no
- [S:r:60] SearchInfo.IPID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.044 range_density=1.0 rows/parent=22.73/5592 child_distinct=113464 rank=1 preferred=yes weak=no
- [S:r:61] SearchInfo.IPID -> AdsInfo.AdID: inclusion=1.0 coverage=0.019 range_density=1.0 rows/parent=22.73/5592 child_distinct=113464 rank=2 preferred=no weak=no
- [S:r:62] SearchInfo.IsUserLoggedOn -> Category.CategoryID: inclusion=1.0 coverage=0.0294 range_density=1.0 rows/parent=1289644.5/1752194 child_distinct=2 rank=1 preferred=yes weak=yes
- [S:r:63] SearchInfo.IsUserLoggedOn -> Location.LocationID: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=1289644.5/1752194 child_distinct=2 rank=2 preferred=no weak=no
- [S:r:64] SearchInfo.IsUserLoggedOn -> UserInfo.UserID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1289644.5/1752194 child_distinct=2 rank=3 preferred=no weak=no
- [S:r:65] SearchInfo.IsUserLoggedOn -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1289644.5/1752194 child_distinct=2 rank=4 preferred=no weak=no
- [S:r:66] SearchInfo.IsUserLoggedOn -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1289644.5/1752194 child_distinct=2 rank=5 preferred=no weak=no
- [S:r:67] SearchInfo.LocationID -> Location.LocationID: inclusion=1.0 coverage=0.5803 range_density=1.0 rows/parent=1265.6/346481 child_distinct=2038 rank=1 preferred=yes weak=no
- [S:r:68] SearchInfo.LocationID -> UserInfo.UserID: inclusion=1.0 coverage=0.0207 range_density=1.0 rows/parent=1265.6/346481 child_distinct=2038 rank=2 preferred=no weak=no
- [S:r:69] SearchInfo.LocationID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0008 range_density=1.0 rows/parent=1265.6/346481 child_distinct=2038 rank=3 preferred=no weak=no
- [S:r:70] SearchInfo.LocationID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0003 range_density=1.0 rows/parent=1265.6/346481 child_distinct=2038 rank=4 preferred=no weak=no
- [S:r:71] SearchInfo.SearchID -> AdsInfo.AdID: inclusion=1.0 coverage=0.4327 range_density=1.0 rows/parent=1.0/1 child_distinct=2579289 rank=1 preferred=no weak=no child_is_unique
- [S:r:72] SearchInfo.UserID -> UserInfo.UserID: inclusion=1.0 coverage=0.9988 range_density=1.0 rows/parent=25.95/5592 child_distinct=98137 rank=1 preferred=yes weak=no
- [S:r:73] SearchInfo.UserID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.038 range_density=1.0 rows/parent=25.95/5592 child_distinct=98137 rank=2 preferred=no weak=no
- [S:r:74] SearchInfo.UserID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0165 range_density=1.0 rows/parent=25.95/5592 child_distinct=98137 rank=3 preferred=no weak=no
- [S:r:75] SearchStream.AdID -> AdsInfo.AdID: inclusion=1.0 coverage=0.438 range_density=1.0 rows/parent=3.54/28986 child_distinct=2610692 rank=1 preferred=yes weak=no
- [S:r:76] SearchStream.IsClick -> Category.CategoryID: inclusion=1.0 coverage=0.0294 range_density=1.0 rows/parent=2157560.0/4289081 child_distinct=2 rank=1 preferred=yes weak=yes
- [S:r:77] SearchStream.IsClick -> Location.LocationID: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=2157560.0/4289081 child_distinct=2 rank=2 preferred=no weak=no
- [S:r:78] SearchStream.IsClick -> UserInfo.UserID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2157560.0/4289081 child_distinct=2 rank=3 preferred=no weak=no
- [S:r:79] SearchStream.IsClick -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2157560.0/4289081 child_distinct=2 rank=4 preferred=no weak=no
- [S:r:80] SearchStream.IsClick -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2157560.0/4289081 child_distinct=2 rank=5 preferred=no weak=no
- [S:r:81] SearchStream.ObjectType -> Category.CategoryID: inclusion=1.0 coverage=0.0441 range_density=1.0 rows/parent=3084900.67/4493367 child_distinct=3 rank=1 preferred=yes weak=yes
- [S:r:82] SearchStream.ObjectType -> Location.LocationID: inclusion=1.0 coverage=0.0009 range_density=1.0 rows/parent=3084900.67/4493367 child_distinct=3 rank=2 preferred=no weak=no
- [S:r:83] SearchStream.ObjectType -> UserInfo.UserID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=3084900.67/4493367 child_distinct=3 rank=3 preferred=no weak=no
- [S:r:84] SearchStream.ObjectType -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=3084900.67/4493367 child_distinct=3 rank=4 preferred=no weak=no
- [S:r:85] SearchStream.ObjectType -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=3084900.67/4493367 child_distinct=3 rank=5 preferred=no weak=no
- [S:r:86] SearchStream.Position -> Category.CategoryID: inclusion=1.0 coverage=0.0735 range_density=1.0 rows/parent=1850940.4/2546548 child_distinct=5 rank=1 preferred=yes weak=yes
- [S:r:87] SearchStream.Position -> Location.LocationID: inclusion=1.0 coverage=0.0014 range_density=1.0 rows/parent=1850940.4/2546548 child_distinct=5 rank=2 preferred=no weak=no
- [S:r:88] SearchStream.Position -> UserInfo.UserID: inclusion=1.0 coverage=0.0001 range_density=1.0 rows/parent=1850940.4/2546548 child_distinct=5 rank=3 preferred=no weak=no
- [S:r:89] SearchStream.Position -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1850940.4/2546548 child_distinct=5 rank=4 preferred=no weak=no
- [S:r:90] SearchStream.Position -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1850940.4/2546548 child_distinct=5 rank=5 preferred=no weak=no
- [S:r:91] SearchStream.SearchID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.9873 range_density=1.0 rows/parent=3.63/6 child_distinct=2546557 rank=1 preferred=yes weak=no
- [S:r:92] SearchStream.SearchID -> AdsInfo.AdID: inclusion=1.0 coverage=0.4272 range_density=1.0 rows/parent=3.63/6 child_distinct=2546557 rank=2 preferred=no weak=no
- [S:r:93] UserInfo.UserAgentFamilyID -> Location.LocationID: inclusion=1.0 coverage=0.0128 range_density=1.0 rows/parent=2183.31/39148 child_distinct=45 rank=1 preferred=yes weak=no
- [S:r:94] UserInfo.UserAgentFamilyID -> UserInfo.UserID: inclusion=1.0 coverage=0.0005 range_density=1.0 rows/parent=2183.31/39148 child_distinct=45 rank=2 preferred=no weak=no
- [S:r:95] UserInfo.UserAgentFamilyID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2183.31/39148 child_distinct=45 rank=3 preferred=no weak=no
- [S:r:96] UserInfo.UserAgentFamilyID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2183.31/39148 child_distinct=45 rank=4 preferred=no weak=no
- [S:r:97] UserInfo.UserAgentID -> UserInfo.UserID: inclusion=1.0 coverage=0.0717 range_density=1.0 rows/parent=13.94/7167 child_distinct=7046 rank=1 preferred=yes weak=no
- [S:r:98] UserInfo.UserAgentID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0027 range_density=1.0 rows/parent=13.94/7167 child_distinct=7046 rank=2 preferred=no weak=no
- [S:r:99] UserInfo.UserAgentID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0012 range_density=1.0 rows/parent=13.94/7167 child_distinct=7046 rank=3 preferred=no weak=no
- [S:r:100] UserInfo.UserAgentOSID -> Category.CategoryID: inclusion=1.0 coverage=0.4706 range_density=1.0 rows/parent=3070.28/55038 child_distinct=32 rank=1 preferred=yes weak=yes
- [S:r:101] UserInfo.UserAgentOSID -> Location.LocationID: inclusion=1.0 coverage=0.0091 range_density=1.0 rows/parent=3070.28/55038 child_distinct=32 rank=2 preferred=no weak=no
- [S:r:102] UserInfo.UserAgentOSID -> UserInfo.UserID: inclusion=1.0 coverage=0.0003 range_density=1.0 rows/parent=3070.28/55038 child_distinct=32 rank=3 preferred=no weak=no
- [S:r:103] UserInfo.UserAgentOSID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=3070.28/55038 child_distinct=32 rank=4 preferred=no weak=no
- [S:r:104] UserInfo.UserAgentOSID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=3070.28/55038 child_distinct=32 rank=5 preferred=no weak=no
- [S:r:105] UserInfo.UserDeviceID -> UserInfo.UserID: inclusion=1.0 coverage=0.0091 range_density=1.0 rows/parent=110.14/85657 child_distinct=892 rank=1 preferred=yes weak=no
- [S:r:106] UserInfo.UserDeviceID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0003 range_density=1.0 rows/parent=110.14/85657 child_distinct=892 rank=2 preferred=no weak=no
- [S:r:107] UserInfo.UserDeviceID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0001 range_density=1.0 rows/parent=110.14/85657 child_distinct=892 rank=3 preferred=no weak=no
- [S:r:108] UserInfo.UserID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0381 range_density=1.0 rows/parent=1.0/1 child_distinct=98250 rank=1 preferred=no weak=no child_is_unique
- [S:r:109] UserInfo.UserID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0165 range_density=1.0 rows/parent=1.0/1 child_distinct=98250 rank=2 preferred=no weak=no child_is_unique
- [S:r:110] VisitStream.AdID -> AdsInfo.AdID: inclusion=1.0 coverage=0.6394 range_density=1.0 rows/parent=1.69/368 child_distinct=3811150 rank=1 preferred=yes weak=no
- [S:r:111] VisitStream.IPID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.036 range_density=1.0 rows/parent=69.52/7747 child_distinct=92845 rank=1 preferred=yes weak=no
- [S:r:112] VisitStream.IPID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0156 range_density=1.0 rows/parent=69.52/7747 child_distinct=92845 rank=2 preferred=no weak=no
- [S:r:113] VisitStream.UserID -> UserInfo.UserID: inclusion=1.0 coverage=0.7794 range_density=1.0 rows/parent=83.92/7747 child_distinct=76574 rank=1 preferred=yes weak=no
- [S:r:114] VisitStream.UserID -> SearchInfo.SearchID: inclusion=1.0 coverage=0.0297 range_density=1.0 rows/parent=83.92/7747 child_distinct=76574 rank=2 preferred=no weak=no
- [S:r:115] VisitStream.UserID -> AdsInfo.AdID: inclusion=1.0 coverage=0.0128 range_density=1.0 rows/parent=83.92/7747 child_distinct=76574 rank=3 preferred=no weak=no

Join paths (2-3 hops) over preferred, non-weak relationships:
- [S:p:1] AdsInfo - Location - SearchInfo
- [S:p:2] AdsInfo - Location - UserInfo
- [S:p:3] Category - AdsInfo - Location
- [S:p:4] Category - AdsInfo - PhoneRequestsStream
- [S:p:5] Category - AdsInfo - Location - SearchInfo
- [S:p:6] Category - AdsInfo - SearchStream
- [S:p:7] Category - AdsInfo - Location - UserInfo
- [S:p:8] Category - AdsInfo - VisitStream
- [S:p:9] Location - AdsInfo - PhoneRequestsStream
- [S:p:10] Location - AdsInfo - SearchStream
- [S:p:11] Location - AdsInfo - VisitStream
- [S:p:12] PhoneRequestsStream - AdsInfo - SearchStream
- [S:p:13] PhoneRequestsStream - AdsInfo - VisitStream
- [S:p:14] SearchStream - SearchInfo - UserInfo
- [S:p:15] SearchStream - AdsInfo - VisitStream

Structural ambiguities:
- [S:a:1] multiple_parents at AdsInfo.CategoryID: AdsInfo.AdID, Category.CategoryID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:2] multiple_parents at AdsInfo.IsContext: AdsInfo.AdID, Category.CategoryID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:3] multiple_parents at AdsInfo.LocationID: AdsInfo.AdID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:4] multiple_parents at Category.CategoryID: AdsInfo.AdID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:5] multiple_parents at Category.Level: AdsInfo.AdID, Category.CategoryID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:6] multiple_parents at Category.ParentCategoryID: AdsInfo.AdID, Category.CategoryID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:7] multiple_parents at Category.SubcategoryID: AdsInfo.AdID, Category.CategoryID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:8] multiple_parents at Location.CityID: AdsInfo.AdID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:9] multiple_parents at Location.Level: AdsInfo.AdID, Category.CategoryID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:10] multiple_parents at Location.LocationID: AdsInfo.AdID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:11] multiple_parents at Location.RegionID: AdsInfo.AdID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:12] multiple_parents at PhoneRequestsStream.IPID: AdsInfo.AdID, SearchInfo.SearchID
- [S:a:13] multiple_parents at PhoneRequestsStream.UserID: AdsInfo.AdID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:14] multiple_parents at SearchInfo.CategoryID: AdsInfo.AdID, Category.CategoryID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:15] multiple_parents at SearchInfo.IPID: AdsInfo.AdID, SearchInfo.SearchID
- [S:a:16] multiple_parents at SearchInfo.IsUserLoggedOn: AdsInfo.AdID, Category.CategoryID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:17] multiple_parents at SearchInfo.LocationID: AdsInfo.AdID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:18] multiple_parents at SearchInfo.UserID: AdsInfo.AdID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:19] multiple_parents at SearchStream.IsClick: AdsInfo.AdID, Category.CategoryID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:20] multiple_parents at SearchStream.ObjectType: AdsInfo.AdID, Category.CategoryID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:21] multiple_parents at SearchStream.Position: AdsInfo.AdID, Category.CategoryID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:22] multiple_parents at SearchStream.SearchID: AdsInfo.AdID, SearchInfo.SearchID
- [S:a:23] multiple_parents at UserInfo.UserAgentFamilyID: AdsInfo.AdID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:24] multiple_parents at UserInfo.UserAgentID: AdsInfo.AdID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:25] multiple_parents at UserInfo.UserAgentOSID: AdsInfo.AdID, Category.CategoryID, Location.LocationID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:26] multiple_parents at UserInfo.UserDeviceID: AdsInfo.AdID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:27] multiple_parents at UserInfo.UserID: AdsInfo.AdID, SearchInfo.SearchID
- [S:a:28] multiple_parents at VisitStream.IPID: AdsInfo.AdID, SearchInfo.SearchID
- [S:a:29] multiple_parents at VisitStream.UserID: AdsInfo.AdID, SearchInfo.SearchID, UserInfo.UserID
- [S:a:30] low_support at AdsInfo.LocationID: AdsInfo.AdID: only 3363 distinct child values; may be coincidental
- [S:a:31] low_support at AdsInfo.CategoryID: AdsInfo.AdID: only 52 distinct child values; may be coincidental
- [S:a:32] low_support at AdsInfo.IsContext: AdsInfo.AdID: only 2 distinct child values; may be coincidental
- [S:a:33] low_support at Category.CategoryID: AdsInfo.AdID: only 68 distinct child values; may be coincidental
- [S:a:34] low_support at Category.Level: AdsInfo.AdID: only 3 distinct child values; may be coincidental
- [S:a:35] low_support at Category.ParentCategoryID: AdsInfo.AdID: only 12 distinct child values; may be coincidental
- [S:a:36] low_support at Category.SubcategoryID: AdsInfo.AdID: only 57 distinct child values; may be coincidental
- [S:a:37] low_support at Location.LocationID: AdsInfo.AdID: only 3512 distinct child values; may be coincidental
- [S:a:38] low_support at Location.Level: AdsInfo.AdID: only 3 distinct child values; may be coincidental
- [S:a:39] low_support at Location.RegionID: AdsInfo.AdID: only 84 distinct child values; may be coincidental
- [S:a:40] low_support at Location.CityID: AdsInfo.AdID: only 3290 distinct child values; may be coincidental
- [S:a:41] low_support at PhoneRequestsStream.UserID: AdsInfo.AdID: only 37507 distinct child values; may be coincidental
- [S:a:42] low_support at PhoneRequestsStream.IPID: AdsInfo.AdID: only 36355 distinct child values; may be coincidental
- [S:a:43] low_support at SearchInfo.UserID: AdsInfo.AdID: only 98137 distinct child values; may be coincidental
- [S:a:44] low_support at SearchInfo.SearchID: AdsInfo.AdID: only 2579289 distinct child values; may be coincidental
- [S:a:45] low_support at SearchInfo.IPID: AdsInfo.AdID: only 113464 distinct child values; may be coincidental
- [S:a:46] low_support at SearchInfo.IsUserLoggedOn: AdsInfo.AdID: only 2 distinct child values; may be coincidental
- [S:a:47] low_support at SearchInfo.LocationID: AdsInfo.AdID: only 2038 distinct child values; may be coincidental
- [S:a:48] low_support at SearchInfo.CategoryID: AdsInfo.AdID: only 39 distinct child values; may be coincidental
- [S:a:49] low_support at SearchStream.SearchID: AdsInfo.AdID: only 2546557 distinct child values; may be coincidental
- [S:a:50] low_support at SearchStream.Position: AdsInfo.AdID: only 5 distinct child values; may be coincidental
- [S:a:51] low_support at SearchStream.ObjectType: AdsInfo.AdID: only 3 distinct child values; may be coincidental
- [S:a:52] low_support at SearchStream.IsClick: AdsInfo.AdID: only 2 distinct child values; may be coincidental
- [S:a:53] low_support at UserInfo.UserID: AdsInfo.AdID: only 98250 distinct child values; may be coincidental
- [S:a:54] low_support at UserInfo.UserAgentID: AdsInfo.AdID: only 7046 distinct child values; may be coincidental
- [S:a:55] low_support at UserInfo.UserAgentOSID: AdsInfo.AdID: only 32 distinct child values; may be coincidental
- [S:a:56] low_support at UserInfo.UserDeviceID: AdsInfo.AdID: only 892 distinct child values; may be coincidental
- [S:a:57] low_support at UserInfo.UserAgentFamilyID: AdsInfo.AdID: only 45 distinct child values; may be coincidental
- [S:a:58] low_support at VisitStream.UserID: AdsInfo.AdID: only 76574 distinct child values; may be coincidental
- [S:a:59] low_support at VisitStream.IPID: AdsInfo.AdID: only 92845 distinct child values; may be coincidental
- [S:a:60] weak_overlap at AdsInfo.IsContext: Category.CategoryID: small overlapping integer ranges; may be coincidental
- [S:a:61] weak_overlap at Category.Level: Category.CategoryID: small overlapping integer ranges; may be coincidental
- [S:a:62] weak_overlap at Category.ParentCategoryID: Category.CategoryID: small overlapping integer ranges; may be coincidental
- [S:a:63] weak_overlap at Category.SubcategoryID: Category.CategoryID: small overlapping integer ranges; may be coincidental
- [S:a:64] weak_overlap at Location.Level: Category.CategoryID: small overlapping integer ranges; may be coincidental
- [S:a:65] weak_overlap at SearchInfo.IsUserLoggedOn: Category.CategoryID: small overlapping integer ranges; may be coincidental
- [S:a:66] weak_overlap at SearchInfo.CategoryID: Category.CategoryID: small overlapping integer ranges; may be coincidental
- [S:a:67] weak_overlap at SearchStream.Position: Category.CategoryID: small overlapping integer ranges; may be coincidental
- [S:a:68] weak_overlap at SearchStream.ObjectType: Category.CategoryID: small overlapping integer ranges; may be coincidental
- [S:a:69] weak_overlap at SearchStream.IsClick: Category.CategoryID: small overlapping integer ranges; may be coincidental
- [S:a:70] weak_overlap at UserInfo.UserAgentOSID: Category.CategoryID: small overlapping integer ranges; may be coincidental
- [S:a:71] low_support at AdsInfo.CategoryID: Location.LocationID: only 52 distinct child values; may be coincidental
- [S:a:72] low_support at AdsInfo.IsContext: Location.LocationID: only 2 distinct child values; may be coincidental
- [S:a:73] low_support at Category.CategoryID: Location.LocationID: only 68 distinct child values; may be coincidental
- [S:a:74] low_support at Category.Level: Location.LocationID: only 3 distinct child values; may be coincidental
- [S:a:75] low_support at Category.ParentCategoryID: Location.LocationID: only 12 distinct child values; may be coincidental
- [S:a:76] low_support at Category.SubcategoryID: Location.LocationID: only 57 distinct child values; may be coincidental
- [S:a:77] low_support at Location.Level: Location.LocationID: only 3 distinct child values; may be coincidental
- [S:a:78] low_support at SearchInfo.IsUserLoggedOn: Location.LocationID: only 2 distinct child values; may be coincidental
- [S:a:79] low_support at SearchInfo.CategoryID: Location.LocationID: only 39 distinct child values; may be coincidental
- [S:a:80] low_support at SearchStream.Position: Location.LocationID: only 5 distinct child values; may be coincidental
- [S:a:81] low_support at SearchStream.ObjectType: Location.LocationID: only 3 distinct child values; may be coincidental
- [S:a:82] low_support at SearchStream.IsClick: Location.LocationID: only 2 distinct child values; may be coincidental
- [S:a:83] low_support at UserInfo.UserAgentOSID: Location.LocationID: only 32 distinct child values; may be coincidental
- [S:a:84] low_support at AdsInfo.LocationID: SearchInfo.SearchID: only 3363 distinct child values; may be coincidental
- [S:a:85] low_support at AdsInfo.CategoryID: SearchInfo.SearchID: only 52 distinct child values; may be coincidental
- [S:a:86] low_support at AdsInfo.IsContext: SearchInfo.SearchID: only 2 distinct child values; may be coincidental
- [S:a:87] low_support at Category.CategoryID: SearchInfo.SearchID: only 68 distinct child values; may be coincidental
- [S:a:88] low_support at Category.Level: SearchInfo.SearchID: only 3 distinct child values; may be coincidental
- [S:a:89] low_support at Category.ParentCategoryID: SearchInfo.SearchID: only 12 distinct child values; may be coincidental
- [S:a:90] low_support at Category.SubcategoryID: SearchInfo.SearchID: only 57 distinct child values; may be coincidental
- [S:a:91] low_support at Location.LocationID: SearchInfo.SearchID: only 3512 distinct child values; may be coincidental
- [S:a:92] low_support at Location.Level: SearchInfo.SearchID: only 3 distinct child values; may be coincidental
- [S:a:93] low_support at Location.RegionID: SearchInfo.SearchID: only 84 distinct child values; may be coincidental
- [S:a:94] low_support at Location.CityID: SearchInfo.SearchID: only 3290 distinct child values; may be coincidental
- [S:a:95] low_support at PhoneRequestsStream.UserID: SearchInfo.SearchID: only 37507 distinct child values; may be coincidental
- [S:a:96] low_support at SearchInfo.UserID: SearchInfo.SearchID: only 98137 distinct child values; may be coincidental
- [S:a:97] low_support at SearchInfo.IsUserLoggedOn: SearchInfo.SearchID: only 2 distinct child values; may be coincidental
- [S:a:98] low_support at SearchInfo.LocationID: SearchInfo.SearchID: only 2038 distinct child values; may be coincidental
- [S:a:99] low_support at SearchInfo.CategoryID: SearchInfo.SearchID: only 39 distinct child values; may be coincidental
- [S:a:100] low_support at SearchStream.Position: SearchInfo.SearchID: only 5 distinct child values; may be coincidental
- [S:a:101] low_support at SearchStream.ObjectType: SearchInfo.SearchID: only 3 distinct child values; may be coincidental
- [S:a:102] low_support at SearchStream.IsClick: SearchInfo.SearchID: only 2 distinct child values; may be coincidental
- [S:a:103] low_support at UserInfo.UserID: SearchInfo.SearchID: only 98250 distinct child values; may be coincidental
- [S:a:104] low_support at UserInfo.UserAgentID: SearchInfo.SearchID: only 7046 distinct child values; may be coincidental
- [S:a:105] low_support at UserInfo.UserAgentOSID: SearchInfo.SearchID: only 32 distinct child values; may be coincidental
- [S:a:106] low_support at UserInfo.UserDeviceID: SearchInfo.SearchID: only 892 distinct child values; may be coincidental
- [S:a:107] low_support at UserInfo.UserAgentFamilyID: SearchInfo.SearchID: only 45 distinct child values; may be coincidental
- [S:a:108] low_support at VisitStream.UserID: SearchInfo.SearchID: only 76574 distinct child values; may be coincidental
- [S:a:109] low_support at AdsInfo.LocationID: UserInfo.UserID: only 3363 distinct child values; may be coincidental
- [S:a:110] low_support at AdsInfo.CategoryID: UserInfo.UserID: only 52 distinct child values; may be coincidental
- [S:a:111] low_support at AdsInfo.IsContext: UserInfo.UserID: only 2 distinct child values; may be coincidental
- [S:a:112] low_support at Category.CategoryID: UserInfo.UserID: only 68 distinct child values; may be coincidental
- [S:a:113] low_support at Category.Level: UserInfo.UserID: only 3 distinct child values; may be coincidental
- [S:a:114] low_support at Category.ParentCategoryID: UserInfo.UserID: only 12 distinct child values; may be coincidental
- [S:a:115] low_support at Category.SubcategoryID: UserInfo.UserID: only 57 distinct child values; may be coincidental
- [S:a:116] low_support at Location.LocationID: UserInfo.UserID: only 3512 distinct child values; may be coincidental
- [S:a:117] low_support at Location.Level: UserInfo.UserID: only 3 distinct child values; may be coincidental
- [S:a:118] low_support at Location.RegionID: UserInfo.UserID: only 84 distinct child values; may be coincidental
- [S:a:119] low_support at SearchInfo.IsUserLoggedOn: UserInfo.UserID: only 2 distinct child values; may be coincidental
- [S:a:120] low_support at SearchInfo.LocationID: UserInfo.UserID: only 2038 distinct child values; may be coincidental
- [S:a:121] low_support at SearchInfo.CategoryID: UserInfo.UserID: only 39 distinct child values; may be coincidental
- [S:a:122] low_support at SearchStream.Position: UserInfo.UserID: only 5 distinct child values; may be coincidental
- [S:a:123] low_support at SearchStream.ObjectType: UserInfo.UserID: only 3 distinct child values; may be coincidental
- [S:a:124] low_support at SearchStream.IsClick: UserInfo.UserID: only 2 distinct child values; may be coincidental
- [S:a:125] low_support at UserInfo.UserAgentOSID: UserInfo.UserID: only 32 distinct child values; may be coincidental
- [S:a:126] low_support at UserInfo.UserAgentFamilyID: UserInfo.UserID: only 45 distinct child values; may be coincidental
- [S:a:127] no_candidate_key at PhoneRequestsStream: no single column is unique and non-null (event log, or composite key?)
- [S:a:128] no_candidate_key at SearchStream: no single column is unique and non-null (event log, or composite key?)
- [S:a:129] no_candidate_key at VisitStream: no single column is unique and non-null (event log, or composite key?)
