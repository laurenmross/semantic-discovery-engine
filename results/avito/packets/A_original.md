## Business outcome of interest (supplied by the business)
- User engagement: whether the user visits more than one ad in the 4 days after the cutoff timestamp.
- Outcome entity: UserInfo.UserID

## Schema (tables, columns, types, row counts, example values)
### Table AdsInfo  [S:t:AdsInfo]  rows=5960558
- AdID: BIGINT; examples ['0', '1', '2']  [S:c:AdsInfo.AdID]
- LocationID: BIGINT; examples ['497', '335', '341']  [S:c:AdsInfo.LocationID]
- CategoryID: BIGINT; examples ['22', '43', '47']  [S:c:AdsInfo.CategoryID]
- Price: DOUBLE; examples ['400.0', '6864.0', '7800000.0']  [S:c:AdsInfo.Price]
- Title: VARCHAR; examples ['[redacted ad title]', '[redacted ad title]', '[redacted ad title]']  [S:c:AdsInfo.Title]
- IsContext: DOUBLE; examples ['0.0', '1.0']  [S:c:AdsInfo.IsContext]

### Table Category  [S:t:Category]  rows=68
- CategoryID: BIGINT; examples ['0', '1', '2']  [S:c:Category.CategoryID]
- Level: BIGINT; examples ['1', '2', '3']  [S:c:Category.Level]
- ParentCategoryID: BIGINT; examples ['10', '9', '12']  [S:c:Category.ParentCategoryID]
- SubcategoryID: BIGINT; examples ['45', '5', '25']  [S:c:Category.SubcategoryID]

### Table Location  [S:t:Location]  rows=3512
- LocationID: BIGINT; examples ['0', '1', '2']  [S:c:Location.LocationID]
- Level: DOUBLE; examples ['2.0', '3.0', '1.0']  [S:c:Location.Level]
- RegionID: DOUBLE; examples ['70.0', '56.0', '64.0']  [S:c:Location.RegionID]
- CityID: DOUBLE; examples ['3024.0', '2791.0', '1139.0']  [S:c:Location.CityID]

### Table PhoneRequestsStream  [S:t:PhoneRequestsStream]  rows=302974
- UserID: BIGINT; examples ['38950', '18761', '88796']  [S:c:PhoneRequestsStream.UserID]
- IPID: DOUBLE; examples ['1629303.0', '109220.0', '1462925.0']  [S:c:PhoneRequestsStream.IPID]
- AdID: BIGINT; examples ['1938326', '3917327', '3806832']  [S:c:PhoneRequestsStream.AdID]
- PhoneRequestDate: TIMESTAMP_NS; examples ['2015-04-25 11:50:35', '2015-04-25 11:51:14', '2015-04-25 12:07:43']  [S:c:PhoneRequestsStream.PhoneRequestDate]

### Table SearchInfo  [S:t:SearchInfo]  rows=2579289
- UserID: BIGINT; examples ['2139', '1477', '68959']  [S:c:SearchInfo.UserID]
- SearchID: BIGINT; examples ['0', '1', '2']  [S:c:SearchInfo.SearchID]
- SearchDate: TIMESTAMP_NS; examples ['2015-04-25 00:00:01', '2015-04-25 00:00:02', '2015-04-25 00:00:03']  [S:c:SearchInfo.SearchDate]
- IPID: DOUBLE; examples ['837134.0', '2187370.0', '2089629.0']  [S:c:SearchInfo.IPID]
- IsUserLoggedOn: DOUBLE; examples ['1.0', '0.0']  [S:c:SearchInfo.IsUserLoggedOn]
- SearchQuery: VARCHAR; examples ['[redacted search query]', '[redacted search query]', '[redacted search query]']  [S:c:SearchInfo.SearchQuery]
- LocationID: BIGINT; examples ['497', '334', '375']  [S:c:SearchInfo.LocationID]
- CategoryID: BIGINT; examples ['34', '22', '60']  [S:c:SearchInfo.CategoryID]

### Table SearchStream  [S:t:SearchStream]  rows=9254702
- SearchID: BIGINT; examples ['541363', '162315', '1804098']  [S:c:SearchStream.SearchID]
- AdID: BIGINT; examples ['806173', '4316980', '2059012']  [S:c:SearchStream.AdID]
- Position: DOUBLE; examples ['8.0', '2.0', '7.0']  [S:c:SearchStream.Position]
- ObjectType: DOUBLE; examples ['1.0', '3.0', '2.0']  [S:c:SearchStream.ObjectType]
- HistCTR: DOUBLE; examples ['0.005902', '0.049664', '0.002413']  [S:c:SearchStream.HistCTR]
- IsClick: DOUBLE; examples ['0.0', '1.0']  [S:c:SearchStream.IsClick]
- SearchDate: TIMESTAMP_NS; examples ['2015-04-30 20:57:06', '2015-04-26 23:19:37', '2015-05-12 18:11:59']  [S:c:SearchStream.SearchDate]

### Table UserInfo  [S:t:UserInfo]  rows=98250
- UserID: BIGINT; examples ['0', '1', '2']  [S:c:UserInfo.UserID]
- UserAgentID: DOUBLE; examples ['54898.0', '15248.0', '12555.0']  [S:c:UserInfo.UserAgentID]
- UserAgentOSID: DOUBLE; examples ['20.0', '35.0', '30.0']  [S:c:UserInfo.UserAgentOSID]
- UserDeviceID: DOUBLE; examples ['2014.0', '4093.0', '2019.0']  [S:c:UserInfo.UserDeviceID]
- UserAgentFamilyID: DOUBLE; examples ['85.0', '25.0', '9.0']  [S:c:UserInfo.UserAgentFamilyID]

### Table VisitStream  [S:t:VisitStream]  rows=6454562
- UserID: BIGINT; examples ['76240', '88796', '77228']  [S:c:VisitStream.UserID]
- IPID: DOUBLE; examples ['711105.0', '1462925.0', '964705.0']  [S:c:VisitStream.IPID]
- AdID: BIGINT; examples ['2270750', '4865813', '4635684']  [S:c:VisitStream.AdID]
- ViewDate: TIMESTAMP_NS; examples ['2015-05-17 15:19:02', '2015-05-17 15:42:14', '2015-05-17 15:45:06']  [S:c:VisitStream.ViewDate]
