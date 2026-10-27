## Business outcome of interest (supplied by the business)
- Engagement: whether the entity identified by T01.c04 has more than one qualifying interaction in the 4 days after the cutoff timestamp.
- Outcome entity: T01.c04

## Schema (tables, columns, types, row counts, example values)
### Table T01  [S:t:T01]  rows=98250
- c01: DOUBLE; examples ['54898.0', '15248.0', '12555.0']  [S:c:T01.c01]
    profile: nulls=0.0% distinct=7046 unique=no min=3.0 max=64016.0 mean=3.307e+04 (float type holding only whole numbers)
- c02: DOUBLE; examples ['2014.0', '4093.0', '2019.0']  [S:c:T01.c02]
    profile: nulls=0.0% distinct=892 unique=no min=5.0 max=4205.0 mean=2035 (float type holding only whole numbers)
- c03: DOUBLE; examples ['85.0', '25.0', '9.0']  [S:c:T01.c03]
    profile: nulls=0.0% distinct=45 unique=no min=1.0 max=89.0 mean=42.59 (float type holding only whole numbers)
- c04: BIGINT; examples ['0', '1', '2']  [S:c:T01.c04]
    profile: nulls=0.0% distinct=98250 unique=yes min=0 max=98249 mean=4.912e+04
- c05: DOUBLE; examples ['20.0', '35.0', '30.0']  [S:c:T01.c05]
    profile: nulls=0.0% distinct=32 unique=no min=1.0 max=51.0 mean=22.95 (float type holding only whole numbers)

### Table T02  [S:t:T02]  rows=6454562
- c01: BIGINT; examples ['2270750', '4865813', '4635684']  [S:c:T02.c01]
    profile: nulls=0.2% distinct=3811150 unique=no min=0 max=5960390 mean=2.965e+06
- c02: DOUBLE; examples ['711105.0', '1462925.0', '964705.0']  [S:c:T02.c02]
    profile: nulls=0.0% distinct=92845 unique=no min=73.0 max=2266670.0 mean=1.136e+06 (float type holding only whole numbers)
- c03: TIMESTAMP_NS; examples ['2015-05-17 15:19:02', '2015-05-17 15:42:14', '2015-05-17 15:45:06']  [S:c:T02.c03]
    profile: nulls=0.0% distinct=1805877 unique=no min=2015-04-25 00:00:00 max=2015-05-20 17:59:19
- c04: BIGINT; examples ['76240', '88796', '77228']  [S:c:T02.c04]
    profile: nulls=0.4% distinct=76574 unique=no min=0 max=98217 mean=4.91e+04

### Table T03  [S:t:T03]  rows=3512
- c01: DOUBLE; examples ['2.0', '3.0', '1.0']  [S:c:T03.c01]
    profile: nulls=0.0% distinct=3 unique=no min=1.0 max=3.0 mean=2.976 top=3.0:3429, 2.0:82, 1.0:1 (float type holding only whole numbers)
- c02: DOUBLE; examples ['70.0', '56.0', '64.0']  [S:c:T03.c02]
    profile: nulls=0.0% distinct=84 unique=no min=1.0 max=84.0 mean=41.22 (float type holding only whole numbers)
- c03: BIGINT; examples ['0', '1', '2']  [S:c:T03.c03]
    profile: nulls=0.0% distinct=3512 unique=yes min=0 max=3511 mean=1756
- c04: DOUBLE; examples ['3024.0', '2791.0', '1139.0']  [S:c:T03.c04]
    profile: nulls=0.0% distinct=3290 unique=no min=1.0 max=3722.0 mean=1857 (float type holding only whole numbers)

### Table T04  [S:t:T04]  rows=2579289
- c01: BIGINT; examples ['34', '22', '60']  [S:c:T04.c01]
    profile: nulls=0.0% distinct=39 unique=no min=0 max=67 mean=29.34
- c02: TIMESTAMP_NS; examples ['2015-04-25 00:00:01', '2015-04-25 00:00:02', '2015-04-25 00:00:03']  [S:c:T04.c02]
    profile: nulls=0.0% distinct=1351586 unique=no min=2015-04-25 00:00:01 max=2015-05-20 17:59:56
- c03: VARCHAR; examples ['<text, ~10 chars, Latin/other script>']  [S:c:T04.c03]
    profile: nulls=84.1% distinct=17371 unique=no avg_len=9.4
- c04: BIGINT; examples ['497', '334', '375']  [S:c:T04.c04]
    profile: nulls=0.0% distinct=2038 unique=no min=0 max=3443 mean=306.5
- c05: BIGINT; examples ['2139', '1477', '68959']  [S:c:T04.c05]
    profile: nulls=1.3% distinct=98137 unique=no min=0 max=98240 mean=4.851e+04
- c06: DOUBLE; examples ['837134.0', '2187370.0', '2089629.0']  [S:c:T04.c06]
    profile: nulls=0.0% distinct=113464 unique=no min=28.0 max=2266691.0 mean=1.139e+06 (float type holding only whole numbers)
- c07: DOUBLE; examples ['1.0', '0.0']  [S:c:T04.c07]
    profile: nulls=0.0% distinct=2 unique=no min=0.0 max=1.0 mean=0.3207 top=0.0:1752194, 1.0:827095 (float type holding only whole numbers)
- c08: BIGINT; examples ['0', '1', '2']  [S:c:T04.c08]
    profile: nulls=0.0% distinct=2579289 unique=yes min=0 max=2579288 mean=1.29e+06

### Table T05  [S:t:T05]  rows=5960558
- c01: BIGINT; examples ['497', '335', '341']  [S:c:T05.c01]
    profile: nulls=0.4% distinct=3363 unique=no min=1 max=3443 mean=346.7
- c02: BIGINT; examples ['22', '43', '47']  [S:c:T05.c02]
    profile: nulls=0.0% distinct=52 unique=no min=2 max=67 mean=38.37
- c03: BIGINT; examples ['0', '1', '2']  [S:c:T05.c03]
    profile: nulls=0.0% distinct=5960558 unique=yes min=0 max=5960557 mean=2.98e+06
- c04: DOUBLE; examples ['400.0', '6864.0', '7800000.0']  [S:c:T05.c04]
    profile: nulls=0.0% distinct=65562 unique=no min=0.0 max=999999999999.0 mean=5.451e+06
- c05: DOUBLE; examples ['0.0', '1.0']  [S:c:T05.c05]
    profile: nulls=0.0% distinct=2 unique=no min=0.0 max=1.0 mean=0.004151 top=0.0:5935816, 1.0:24742 (float type holding only whole numbers)
- c06: VARCHAR; examples ['<text, ~19 chars, Cyrillic script>']  [S:c:T05.c06]
    profile: nulls=0.0% distinct=3246389 unique=no avg_len=24.8

### Table T06  [S:t:T06]  rows=302974
- c01: DOUBLE; examples ['1629303.0', '109220.0', '1462925.0']  [S:c:T06.c01]
    profile: nulls=0.0% distinct=36355 unique=no min=63.0 max=2266665.0 mean=1.129e+06 (float type holding only whole numbers)
- c02: TIMESTAMP_NS; examples ['2015-04-25 11:50:35', '2015-04-25 11:51:14', '2015-04-25 12:07:43']  [S:c:T06.c02]
    profile: nulls=0.0% distinct=275103 unique=no min=2015-04-25 00:00:08 max=2015-05-20 17:55:09
- c03: BIGINT; examples ['1938326', '3917327', '3806832']  [S:c:T06.c03]
    profile: nulls=0.2% distinct=256195 unique=no min=9 max=5929465 mean=2.963e+06
- c04: BIGINT; examples ['38950', '18761', '88796']  [S:c:T06.c04]
    profile: nulls=0.4% distinct=37507 unique=no min=2 max=98139 mean=4.941e+04

### Table T07  [S:t:T07]  rows=68
- c01: BIGINT; examples ['45', '5', '25']  [S:c:T07.c01]
    profile: nulls=0.0% distinct=57 unique=no min=1 max=57 mean=31.59
- c02: BIGINT; examples ['0', '1', '2']  [S:c:T07.c02]
    profile: nulls=0.0% distinct=68 unique=yes min=0 max=67 mean=33.5
- c03: BIGINT; examples ['1', '2', '3']  [S:c:T07.c03]
    profile: nulls=0.0% distinct=3 unique=no min=1 max=3 mean=2.809 top=3:56, 2:11, 1:1
- c04: BIGINT; examples ['10', '9', '12']  [S:c:T07.c04]
    profile: nulls=0.0% distinct=12 unique=no min=1 max=12 mean=6.632 top=12:11, 2:9, 4:8, 6:7, 8:7, 9:7

### Table T08  [S:t:T08]  rows=9254702
- c01: BIGINT; examples ['806173', '4316980', '2059012']  [S:c:T08.c01]
    profile: nulls=0.0% distinct=2610692 unique=no min=1 max=5929464 mean=2.978e+06
- c02: DOUBLE; examples ['0.0', '1.0']  [S:c:T08.c02]
    profile: nulls=53.4% distinct=2 unique=no min=0.0 max=1.0 mean=0.006034 top=None:4939582, 0.0:4289081, 1.0:26039 (float type holding only whole numbers)
- c03: DOUBLE; examples ['1.0', '3.0', '2.0']  [S:c:T08.c03]
    profile: nulls=0.0% distinct=3 unique=no min=1.0 max=3.0 mean=2.074 top=3.0:4493367, 1.0:3811571, 2.0:949764 (float type holding only whole numbers)
- c04: DOUBLE; examples ['8.0', '2.0', '7.0']  [S:c:T08.c04]
    profile: nulls=0.0% distinct=5 unique=no min=1.0 max=8.0 mean=4.362 top=1.0:2546548, 7.0:2281343, 2.0:1826066, 6.0:1301252, 8.0:1299493 (float type holding only whole numbers)
- c05: TIMESTAMP_NS; examples ['2015-04-30 20:57:06', '2015-04-26 23:19:37', '2015-05-12 18:11:59']  [S:c:T08.c05]
    profile: nulls=0.0% distinct=1343285 unique=no min=2015-04-25 00:00:01 max=2015-05-20 17:59:56
- c06: BIGINT; examples ['541363', '162315', '1804098']  [S:c:T08.c06]
    profile: nulls=0.0% distinct=2546557 unique=no min=0 max=2579288 mean=1.295e+06
- c07: DOUBLE; examples ['0.005902', '0.049664', '0.002413']  [S:c:T08.c07]
    profile: nulls=51.4% distinct=46688 unique=no min=1e-05 max=1.0 mean=0.01055

## Structural analysis (deterministic; computed from values only, never from names)
Candidate keys (100% unique, no nulls):
- T05.c03  [S:k:T05.c03]
- T07.c02  [S:k:T07.c02]
- T03.c03  [S:k:T03.c03]
- T04.c08  [S:k:T04.c08]
- T01.c04  [S:k:T01.c04]
Time columns: T06.c02, T04.c02, T08.c05, T02.c03

Candidate relationships (child column values contained in a candidate key).
Fields: inclusion = share of distinct child values found in parent key; coverage = share of parent keys referenced; range_density = share of the child's value range filled by parent keys (near 1.0 means inclusion is weak evidence, because any small integers would match); rows/parent = avg and max child rows per referenced parent; rank = rank of this parent among this child column's candidates by coverage; preferred = top-ranked and plausible; weak = both sides are small integer ranges starting near 0/1.
- [S:r:1] T01.c01 -> T01.c04: inclusion=1.0 coverage=0.0717 range_density=1.0 rows/parent=13.94/7167 child_distinct=7046 rank=1 preferred=yes weak=no
- [S:r:2] T01.c01 -> T04.c08: inclusion=1.0 coverage=0.0027 range_density=1.0 rows/parent=13.94/7167 child_distinct=7046 rank=2 preferred=no weak=no
- [S:r:3] T01.c01 -> T05.c03: inclusion=1.0 coverage=0.0012 range_density=1.0 rows/parent=13.94/7167 child_distinct=7046 rank=3 preferred=no weak=no
- [S:r:4] T01.c02 -> T01.c04: inclusion=1.0 coverage=0.0091 range_density=1.0 rows/parent=110.14/85657 child_distinct=892 rank=1 preferred=yes weak=no
- [S:r:5] T01.c02 -> T04.c08: inclusion=1.0 coverage=0.0003 range_density=1.0 rows/parent=110.14/85657 child_distinct=892 rank=2 preferred=no weak=no
- [S:r:6] T01.c02 -> T05.c03: inclusion=1.0 coverage=0.0001 range_density=1.0 rows/parent=110.14/85657 child_distinct=892 rank=3 preferred=no weak=no
- [S:r:7] T01.c03 -> T03.c03: inclusion=1.0 coverage=0.0128 range_density=1.0 rows/parent=2183.31/39148 child_distinct=45 rank=1 preferred=yes weak=no
- [S:r:8] T01.c03 -> T01.c04: inclusion=1.0 coverage=0.0005 range_density=1.0 rows/parent=2183.31/39148 child_distinct=45 rank=2 preferred=no weak=no
- [S:r:9] T01.c03 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2183.31/39148 child_distinct=45 rank=3 preferred=no weak=no
- [S:r:10] T01.c03 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2183.31/39148 child_distinct=45 rank=4 preferred=no weak=no
- [S:r:11] T01.c04 -> T04.c08: inclusion=1.0 coverage=0.0381 range_density=1.0 rows/parent=1.0/1 child_distinct=98250 rank=1 preferred=no weak=no child_is_unique
- [S:r:12] T01.c04 -> T05.c03: inclusion=1.0 coverage=0.0165 range_density=1.0 rows/parent=1.0/1 child_distinct=98250 rank=2 preferred=no weak=no child_is_unique
- [S:r:13] T01.c05 -> T07.c02: inclusion=1.0 coverage=0.4706 range_density=1.0 rows/parent=3070.28/55038 child_distinct=32 rank=1 preferred=yes weak=yes
- [S:r:14] T01.c05 -> T03.c03: inclusion=1.0 coverage=0.0091 range_density=1.0 rows/parent=3070.28/55038 child_distinct=32 rank=2 preferred=no weak=no
- [S:r:15] T01.c05 -> T01.c04: inclusion=1.0 coverage=0.0003 range_density=1.0 rows/parent=3070.28/55038 child_distinct=32 rank=3 preferred=no weak=no
- [S:r:16] T01.c05 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=3070.28/55038 child_distinct=32 rank=4 preferred=no weak=no
- [S:r:17] T01.c05 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=3070.28/55038 child_distinct=32 rank=5 preferred=no weak=no
- [S:r:18] T02.c01 -> T05.c03: inclusion=1.0 coverage=0.6394 range_density=1.0 rows/parent=1.69/368 child_distinct=3811150 rank=1 preferred=yes weak=no
- [S:r:19] T02.c02 -> T04.c08: inclusion=1.0 coverage=0.036 range_density=1.0 rows/parent=69.52/7747 child_distinct=92845 rank=1 preferred=yes weak=no
- [S:r:20] T02.c02 -> T05.c03: inclusion=1.0 coverage=0.0156 range_density=1.0 rows/parent=69.52/7747 child_distinct=92845 rank=2 preferred=no weak=no
- [S:r:21] T02.c04 -> T01.c04: inclusion=1.0 coverage=0.7794 range_density=1.0 rows/parent=83.92/7747 child_distinct=76574 rank=1 preferred=yes weak=no
- [S:r:22] T02.c04 -> T04.c08: inclusion=1.0 coverage=0.0297 range_density=1.0 rows/parent=83.92/7747 child_distinct=76574 rank=2 preferred=no weak=no
- [S:r:23] T02.c04 -> T05.c03: inclusion=1.0 coverage=0.0128 range_density=1.0 rows/parent=83.92/7747 child_distinct=76574 rank=3 preferred=no weak=no
- [S:r:24] T03.c01 -> T07.c02: inclusion=1.0 coverage=0.0441 range_density=1.0 rows/parent=1170.67/3429 child_distinct=3 rank=1 preferred=yes weak=yes
- [S:r:25] T03.c01 -> T03.c03: inclusion=1.0 coverage=0.0009 range_density=1.0 rows/parent=1170.67/3429 child_distinct=3 rank=2 preferred=no weak=no
- [S:r:26] T03.c01 -> T01.c04: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1170.67/3429 child_distinct=3 rank=3 preferred=no weak=no
- [S:r:27] T03.c01 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1170.67/3429 child_distinct=3 rank=4 preferred=no weak=no
- [S:r:28] T03.c01 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1170.67/3429 child_distinct=3 rank=5 preferred=no weak=no
- [S:r:29] T03.c02 -> T03.c03: inclusion=1.0 coverage=0.0239 range_density=1.0 rows/parent=41.8/221 child_distinct=84 rank=1 preferred=yes weak=no
- [S:r:30] T03.c02 -> T01.c04: inclusion=1.0 coverage=0.0009 range_density=1.0 rows/parent=41.8/221 child_distinct=84 rank=2 preferred=no weak=no
- [S:r:31] T03.c02 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=41.8/221 child_distinct=84 rank=3 preferred=no weak=no
- [S:r:32] T03.c02 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=41.8/221 child_distinct=84 rank=4 preferred=no weak=no
- [S:r:33] T03.c03 -> T01.c04: inclusion=1.0 coverage=0.0357 range_density=1.0 rows/parent=1.0/1 child_distinct=3512 rank=1 preferred=no weak=no child_is_unique
- [S:r:34] T03.c03 -> T04.c08: inclusion=1.0 coverage=0.0014 range_density=1.0 rows/parent=1.0/1 child_distinct=3512 rank=2 preferred=no weak=no child_is_unique
- [S:r:35] T03.c03 -> T05.c03: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=1.0/1 child_distinct=3512 rank=3 preferred=no weak=no child_is_unique
- [S:r:36] T03.c04 -> T01.c04: inclusion=1.0 coverage=0.0335 range_density=1.0 rows/parent=1.07/10 child_distinct=3290 rank=1 preferred=yes weak=no
- [S:r:37] T03.c04 -> T04.c08: inclusion=1.0 coverage=0.0013 range_density=1.0 rows/parent=1.07/10 child_distinct=3290 rank=2 preferred=no weak=no
- [S:r:38] T03.c04 -> T05.c03: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=1.07/10 child_distinct=3290 rank=3 preferred=no weak=no
- [S:r:39] T04.c01 -> T07.c02: inclusion=1.0 coverage=0.5735 range_density=1.0 rows/parent=66135.62/282406 child_distinct=39 rank=1 preferred=yes weak=yes
- [S:r:40] T04.c01 -> T03.c03: inclusion=1.0 coverage=0.0111 range_density=1.0 rows/parent=66135.62/282406 child_distinct=39 rank=2 preferred=no weak=no
- [S:r:41] T04.c01 -> T01.c04: inclusion=1.0 coverage=0.0004 range_density=1.0 rows/parent=66135.62/282406 child_distinct=39 rank=3 preferred=no weak=no
- [S:r:42] T04.c01 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=66135.62/282406 child_distinct=39 rank=4 preferred=no weak=no
- [S:r:43] T04.c01 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=66135.62/282406 child_distinct=39 rank=5 preferred=no weak=no
- [S:r:44] T04.c04 -> T03.c03: inclusion=1.0 coverage=0.5803 range_density=1.0 rows/parent=1265.6/346481 child_distinct=2038 rank=1 preferred=yes weak=no
- [S:r:45] T04.c04 -> T01.c04: inclusion=1.0 coverage=0.0207 range_density=1.0 rows/parent=1265.6/346481 child_distinct=2038 rank=2 preferred=no weak=no
- [S:r:46] T04.c04 -> T04.c08: inclusion=1.0 coverage=0.0008 range_density=1.0 rows/parent=1265.6/346481 child_distinct=2038 rank=3 preferred=no weak=no
- [S:r:47] T04.c04 -> T05.c03: inclusion=1.0 coverage=0.0003 range_density=1.0 rows/parent=1265.6/346481 child_distinct=2038 rank=4 preferred=no weak=no
- [S:r:48] T04.c05 -> T01.c04: inclusion=1.0 coverage=0.9988 range_density=1.0 rows/parent=25.95/5592 child_distinct=98137 rank=1 preferred=yes weak=no
- [S:r:49] T04.c05 -> T04.c08: inclusion=1.0 coverage=0.038 range_density=1.0 rows/parent=25.95/5592 child_distinct=98137 rank=2 preferred=no weak=no
- [S:r:50] T04.c05 -> T05.c03: inclusion=1.0 coverage=0.0165 range_density=1.0 rows/parent=25.95/5592 child_distinct=98137 rank=3 preferred=no weak=no
- [S:r:51] T04.c06 -> T04.c08: inclusion=1.0 coverage=0.044 range_density=1.0 rows/parent=22.73/5592 child_distinct=113464 rank=1 preferred=yes weak=no
- [S:r:52] T04.c06 -> T05.c03: inclusion=1.0 coverage=0.019 range_density=1.0 rows/parent=22.73/5592 child_distinct=113464 rank=2 preferred=no weak=no
- [S:r:53] T04.c07 -> T07.c02: inclusion=1.0 coverage=0.0294 range_density=1.0 rows/parent=1289644.5/1752194 child_distinct=2 rank=1 preferred=yes weak=yes
- [S:r:54] T04.c07 -> T03.c03: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=1289644.5/1752194 child_distinct=2 rank=2 preferred=no weak=no
- [S:r:55] T04.c07 -> T01.c04: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1289644.5/1752194 child_distinct=2 rank=3 preferred=no weak=no
- [S:r:56] T04.c07 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1289644.5/1752194 child_distinct=2 rank=4 preferred=no weak=no
- [S:r:57] T04.c07 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1289644.5/1752194 child_distinct=2 rank=5 preferred=no weak=no
- [S:r:58] T04.c08 -> T05.c03: inclusion=1.0 coverage=0.4327 range_density=1.0 rows/parent=1.0/1 child_distinct=2579289 rank=1 preferred=no weak=no child_is_unique
- [S:r:59] T05.c01 -> T03.c03: inclusion=1.0 coverage=0.9576 range_density=1.0 rows/parent=1765.03/929887 child_distinct=3363 rank=1 preferred=yes weak=no
- [S:r:60] T05.c01 -> T01.c04: inclusion=1.0 coverage=0.0342 range_density=1.0 rows/parent=1765.03/929887 child_distinct=3363 rank=2 preferred=no weak=no
- [S:r:61] T05.c01 -> T04.c08: inclusion=1.0 coverage=0.0013 range_density=1.0 rows/parent=1765.03/929887 child_distinct=3363 rank=3 preferred=no weak=no
- [S:r:62] T05.c01 -> T05.c03: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=1765.03/929887 child_distinct=3363 rank=4 preferred=no weak=no
- [S:r:63] T05.c02 -> T07.c02: inclusion=1.0 coverage=0.7647 range_density=1.0 rows/parent=114625.5/741045 child_distinct=52 rank=1 preferred=yes weak=no
- [S:r:64] T05.c02 -> T03.c03: inclusion=1.0 coverage=0.0148 range_density=1.0 rows/parent=114625.5/741045 child_distinct=52 rank=2 preferred=no weak=no
- [S:r:65] T05.c02 -> T01.c04: inclusion=1.0 coverage=0.0005 range_density=1.0 rows/parent=114625.5/741045 child_distinct=52 rank=3 preferred=no weak=no
- [S:r:66] T05.c02 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=114625.5/741045 child_distinct=52 rank=4 preferred=no weak=no
- [S:r:67] T05.c02 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=114625.5/741045 child_distinct=52 rank=5 preferred=no weak=no
- [S:r:68] T05.c05 -> T07.c02: inclusion=1.0 coverage=0.0294 range_density=1.0 rows/parent=2980279.0/5935816 child_distinct=2 rank=1 preferred=yes weak=yes
- [S:r:69] T05.c05 -> T03.c03: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=2980279.0/5935816 child_distinct=2 rank=2 preferred=no weak=no
- [S:r:70] T05.c05 -> T01.c04: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2980279.0/5935816 child_distinct=2 rank=3 preferred=no weak=no
- [S:r:71] T05.c05 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2980279.0/5935816 child_distinct=2 rank=4 preferred=no weak=no
- [S:r:72] T05.c05 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2980279.0/5935816 child_distinct=2 rank=5 preferred=no weak=no
- [S:r:73] T06.c01 -> T04.c08: inclusion=1.0 coverage=0.0141 range_density=1.0 rows/parent=8.33/1123 child_distinct=36355 rank=1 preferred=yes weak=no
- [S:r:74] T06.c01 -> T05.c03: inclusion=1.0 coverage=0.0061 range_density=1.0 rows/parent=8.33/1123 child_distinct=36355 rank=2 preferred=no weak=no
- [S:r:75] T06.c03 -> T05.c03: inclusion=1.0 coverage=0.043 range_density=1.0 rows/parent=1.18/83 child_distinct=256195 rank=1 preferred=yes weak=no
- [S:r:76] T06.c04 -> T01.c04: inclusion=1.0 coverage=0.3818 range_density=1.0 rows/parent=8.04/1123 child_distinct=37507 rank=1 preferred=yes weak=no
- [S:r:77] T06.c04 -> T04.c08: inclusion=1.0 coverage=0.0145 range_density=1.0 rows/parent=8.04/1123 child_distinct=37507 rank=2 preferred=no weak=no
- [S:r:78] T06.c04 -> T05.c03: inclusion=1.0 coverage=0.0063 range_density=1.0 rows/parent=8.04/1123 child_distinct=37507 rank=3 preferred=no weak=no
- [S:r:79] T07.c01 -> T07.c02: inclusion=1.0 coverage=0.8382 range_density=1.0 rows/parent=1.19/12 child_distinct=57 rank=1 preferred=yes weak=yes
- [S:r:80] T07.c01 -> T03.c03: inclusion=1.0 coverage=0.0162 range_density=1.0 rows/parent=1.19/12 child_distinct=57 rank=2 preferred=no weak=no
- [S:r:81] T07.c01 -> T01.c04: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=1.19/12 child_distinct=57 rank=3 preferred=no weak=no
- [S:r:82] T07.c01 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1.19/12 child_distinct=57 rank=4 preferred=no weak=no
- [S:r:83] T07.c01 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1.19/12 child_distinct=57 rank=5 preferred=no weak=no
- [S:r:84] T07.c02 -> T03.c03: inclusion=1.0 coverage=0.0194 range_density=1.0 rows/parent=1.0/1 child_distinct=68 rank=1 preferred=no weak=no child_is_unique
- [S:r:85] T07.c02 -> T01.c04: inclusion=1.0 coverage=0.0007 range_density=1.0 rows/parent=1.0/1 child_distinct=68 rank=2 preferred=no weak=no child_is_unique
- [S:r:86] T07.c02 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1.0/1 child_distinct=68 rank=3 preferred=no weak=no child_is_unique
- [S:r:87] T07.c02 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1.0/1 child_distinct=68 rank=4 preferred=no weak=no child_is_unique
- [S:r:88] T07.c03 -> T07.c02: inclusion=1.0 coverage=0.0441 range_density=1.0 rows/parent=22.67/56 child_distinct=3 rank=1 preferred=yes weak=yes
- [S:r:89] T07.c03 -> T03.c03: inclusion=1.0 coverage=0.0009 range_density=1.0 rows/parent=22.67/56 child_distinct=3 rank=2 preferred=no weak=no
- [S:r:90] T07.c03 -> T01.c04: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=22.67/56 child_distinct=3 rank=3 preferred=no weak=no
- [S:r:91] T07.c03 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=22.67/56 child_distinct=3 rank=4 preferred=no weak=no
- [S:r:92] T07.c03 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=22.67/56 child_distinct=3 rank=5 preferred=no weak=no
- [S:r:93] T07.c04 -> T07.c02: inclusion=1.0 coverage=0.1765 range_density=1.0 rows/parent=5.67/11 child_distinct=12 rank=1 preferred=yes weak=yes
- [S:r:94] T07.c04 -> T03.c03: inclusion=1.0 coverage=0.0034 range_density=1.0 rows/parent=5.67/11 child_distinct=12 rank=2 preferred=no weak=no
- [S:r:95] T07.c04 -> T01.c04: inclusion=1.0 coverage=0.0001 range_density=1.0 rows/parent=5.67/11 child_distinct=12 rank=3 preferred=no weak=no
- [S:r:96] T07.c04 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=5.67/11 child_distinct=12 rank=4 preferred=no weak=no
- [S:r:97] T07.c04 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=5.67/11 child_distinct=12 rank=5 preferred=no weak=no
- [S:r:98] T08.c01 -> T05.c03: inclusion=1.0 coverage=0.438 range_density=1.0 rows/parent=3.54/28986 child_distinct=2610692 rank=1 preferred=yes weak=no
- [S:r:99] T08.c02 -> T07.c02: inclusion=1.0 coverage=0.0294 range_density=1.0 rows/parent=2157560.0/4289081 child_distinct=2 rank=1 preferred=yes weak=yes
- [S:r:100] T08.c02 -> T03.c03: inclusion=1.0 coverage=0.0006 range_density=1.0 rows/parent=2157560.0/4289081 child_distinct=2 rank=2 preferred=no weak=no
- [S:r:101] T08.c02 -> T01.c04: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2157560.0/4289081 child_distinct=2 rank=3 preferred=no weak=no
- [S:r:102] T08.c02 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2157560.0/4289081 child_distinct=2 rank=4 preferred=no weak=no
- [S:r:103] T08.c02 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=2157560.0/4289081 child_distinct=2 rank=5 preferred=no weak=no
- [S:r:104] T08.c03 -> T07.c02: inclusion=1.0 coverage=0.0441 range_density=1.0 rows/parent=3084900.67/4493367 child_distinct=3 rank=1 preferred=yes weak=yes
- [S:r:105] T08.c03 -> T03.c03: inclusion=1.0 coverage=0.0009 range_density=1.0 rows/parent=3084900.67/4493367 child_distinct=3 rank=2 preferred=no weak=no
- [S:r:106] T08.c03 -> T01.c04: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=3084900.67/4493367 child_distinct=3 rank=3 preferred=no weak=no
- [S:r:107] T08.c03 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=3084900.67/4493367 child_distinct=3 rank=4 preferred=no weak=no
- [S:r:108] T08.c03 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=3084900.67/4493367 child_distinct=3 rank=5 preferred=no weak=no
- [S:r:109] T08.c04 -> T07.c02: inclusion=1.0 coverage=0.0735 range_density=1.0 rows/parent=1850940.4/2546548 child_distinct=5 rank=1 preferred=yes weak=yes
- [S:r:110] T08.c04 -> T03.c03: inclusion=1.0 coverage=0.0014 range_density=1.0 rows/parent=1850940.4/2546548 child_distinct=5 rank=2 preferred=no weak=no
- [S:r:111] T08.c04 -> T01.c04: inclusion=1.0 coverage=0.0001 range_density=1.0 rows/parent=1850940.4/2546548 child_distinct=5 rank=3 preferred=no weak=no
- [S:r:112] T08.c04 -> T04.c08: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1850940.4/2546548 child_distinct=5 rank=4 preferred=no weak=no
- [S:r:113] T08.c04 -> T05.c03: inclusion=1.0 coverage=0.0 range_density=1.0 rows/parent=1850940.4/2546548 child_distinct=5 rank=5 preferred=no weak=no
- [S:r:114] T08.c06 -> T04.c08: inclusion=1.0 coverage=0.9873 range_density=1.0 rows/parent=3.63/6 child_distinct=2546557 rank=1 preferred=yes weak=no
- [S:r:115] T08.c06 -> T05.c03: inclusion=1.0 coverage=0.4272 range_density=1.0 rows/parent=3.63/6 child_distinct=2546557 rank=2 preferred=no weak=no

Join paths (2-3 hops) over preferred, non-weak relationships:
- [S:p:1] T05 - T03 - T04
- [S:p:2] T05 - T03 - T01
- [S:p:3] T07 - T05 - T03
- [S:p:4] T07 - T05 - T06
- [S:p:5] T07 - T05 - T03 - T04
- [S:p:6] T07 - T05 - T08
- [S:p:7] T07 - T05 - T03 - T01
- [S:p:8] T07 - T05 - T02
- [S:p:9] T03 - T05 - T06
- [S:p:10] T03 - T05 - T08
- [S:p:11] T03 - T05 - T02
- [S:p:12] T06 - T05 - T08
- [S:p:13] T06 - T05 - T02
- [S:p:14] T08 - T04 - T01
- [S:p:15] T08 - T05 - T02

Structural ambiguities:
- [S:a:1] multiple_parents at T05.c02: T05.c03, T07.c02, T03.c03, T04.c08, T01.c04
- [S:a:2] multiple_parents at T05.c05: T05.c03, T07.c02, T03.c03, T04.c08, T01.c04
- [S:a:3] multiple_parents at T05.c01: T05.c03, T03.c03, T04.c08, T01.c04
- [S:a:4] multiple_parents at T07.c02: T05.c03, T03.c03, T04.c08, T01.c04
- [S:a:5] multiple_parents at T07.c03: T05.c03, T07.c02, T03.c03, T04.c08, T01.c04
- [S:a:6] multiple_parents at T07.c04: T05.c03, T07.c02, T03.c03, T04.c08, T01.c04
- [S:a:7] multiple_parents at T07.c01: T05.c03, T07.c02, T03.c03, T04.c08, T01.c04
- [S:a:8] multiple_parents at T03.c04: T05.c03, T04.c08, T01.c04
- [S:a:9] multiple_parents at T03.c01: T05.c03, T07.c02, T03.c03, T04.c08, T01.c04
- [S:a:10] multiple_parents at T03.c03: T05.c03, T04.c08, T01.c04
- [S:a:11] multiple_parents at T03.c02: T05.c03, T03.c03, T04.c08, T01.c04
- [S:a:12] multiple_parents at T06.c01: T05.c03, T04.c08
- [S:a:13] multiple_parents at T06.c04: T05.c03, T04.c08, T01.c04
- [S:a:14] multiple_parents at T04.c01: T05.c03, T07.c02, T03.c03, T04.c08, T01.c04
- [S:a:15] multiple_parents at T04.c06: T05.c03, T04.c08
- [S:a:16] multiple_parents at T04.c07: T05.c03, T07.c02, T03.c03, T04.c08, T01.c04
- [S:a:17] multiple_parents at T04.c04: T05.c03, T03.c03, T04.c08, T01.c04
- [S:a:18] multiple_parents at T04.c05: T05.c03, T04.c08, T01.c04
- [S:a:19] multiple_parents at T08.c02: T05.c03, T07.c02, T03.c03, T04.c08, T01.c04
- [S:a:20] multiple_parents at T08.c03: T05.c03, T07.c02, T03.c03, T04.c08, T01.c04
- [S:a:21] multiple_parents at T08.c04: T05.c03, T07.c02, T03.c03, T04.c08, T01.c04
- [S:a:22] multiple_parents at T08.c06: T05.c03, T04.c08
- [S:a:23] multiple_parents at T01.c03: T05.c03, T03.c03, T04.c08, T01.c04
- [S:a:24] multiple_parents at T01.c01: T05.c03, T04.c08, T01.c04
- [S:a:25] multiple_parents at T01.c05: T05.c03, T07.c02, T03.c03, T04.c08, T01.c04
- [S:a:26] multiple_parents at T01.c02: T05.c03, T04.c08, T01.c04
- [S:a:27] multiple_parents at T01.c04: T05.c03, T04.c08
- [S:a:28] multiple_parents at T02.c02: T05.c03, T04.c08
- [S:a:29] multiple_parents at T02.c04: T05.c03, T04.c08, T01.c04
- [S:a:30] low_support at T05.c01: T05.c03: only 3363 distinct child values; may be coincidental
- [S:a:31] low_support at T05.c02: T05.c03: only 52 distinct child values; may be coincidental
- [S:a:32] low_support at T05.c05: T05.c03: only 2 distinct child values; may be coincidental
- [S:a:33] low_support at T07.c02: T05.c03: only 68 distinct child values; may be coincidental
- [S:a:34] low_support at T07.c03: T05.c03: only 3 distinct child values; may be coincidental
- [S:a:35] low_support at T07.c04: T05.c03: only 12 distinct child values; may be coincidental
- [S:a:36] low_support at T07.c01: T05.c03: only 57 distinct child values; may be coincidental
- [S:a:37] low_support at T03.c03: T05.c03: only 3512 distinct child values; may be coincidental
- [S:a:38] low_support at T03.c01: T05.c03: only 3 distinct child values; may be coincidental
- [S:a:39] low_support at T03.c02: T05.c03: only 84 distinct child values; may be coincidental
- [S:a:40] low_support at T03.c04: T05.c03: only 3290 distinct child values; may be coincidental
- [S:a:41] low_support at T06.c04: T05.c03: only 37507 distinct child values; may be coincidental
- [S:a:42] low_support at T06.c01: T05.c03: only 36355 distinct child values; may be coincidental
- [S:a:43] low_support at T04.c05: T05.c03: only 98137 distinct child values; may be coincidental
- [S:a:44] low_support at T04.c08: T05.c03: only 2579289 distinct child values; may be coincidental
- [S:a:45] low_support at T04.c06: T05.c03: only 113464 distinct child values; may be coincidental
- [S:a:46] low_support at T04.c07: T05.c03: only 2 distinct child values; may be coincidental
- [S:a:47] low_support at T04.c04: T05.c03: only 2038 distinct child values; may be coincidental
- [S:a:48] low_support at T04.c01: T05.c03: only 39 distinct child values; may be coincidental
- [S:a:49] low_support at T08.c06: T05.c03: only 2546557 distinct child values; may be coincidental
- [S:a:50] low_support at T08.c04: T05.c03: only 5 distinct child values; may be coincidental
- [S:a:51] low_support at T08.c03: T05.c03: only 3 distinct child values; may be coincidental
- [S:a:52] low_support at T08.c02: T05.c03: only 2 distinct child values; may be coincidental
- [S:a:53] low_support at T01.c04: T05.c03: only 98250 distinct child values; may be coincidental
- [S:a:54] low_support at T01.c01: T05.c03: only 7046 distinct child values; may be coincidental
- [S:a:55] low_support at T01.c05: T05.c03: only 32 distinct child values; may be coincidental
- [S:a:56] low_support at T01.c02: T05.c03: only 892 distinct child values; may be coincidental
- [S:a:57] low_support at T01.c03: T05.c03: only 45 distinct child values; may be coincidental
- [S:a:58] low_support at T02.c04: T05.c03: only 76574 distinct child values; may be coincidental
- [S:a:59] low_support at T02.c02: T05.c03: only 92845 distinct child values; may be coincidental
- [S:a:60] weak_overlap at T05.c05: T07.c02: small overlapping integer ranges; may be coincidental
- [S:a:61] weak_overlap at T07.c03: T07.c02: small overlapping integer ranges; may be coincidental
- [S:a:62] weak_overlap at T07.c04: T07.c02: small overlapping integer ranges; may be coincidental
- [S:a:63] weak_overlap at T07.c01: T07.c02: small overlapping integer ranges; may be coincidental
- [S:a:64] weak_overlap at T03.c01: T07.c02: small overlapping integer ranges; may be coincidental
- [S:a:65] weak_overlap at T04.c07: T07.c02: small overlapping integer ranges; may be coincidental
- [S:a:66] weak_overlap at T04.c01: T07.c02: small overlapping integer ranges; may be coincidental
- [S:a:67] weak_overlap at T08.c04: T07.c02: small overlapping integer ranges; may be coincidental
- [S:a:68] weak_overlap at T08.c03: T07.c02: small overlapping integer ranges; may be coincidental
- [S:a:69] weak_overlap at T08.c02: T07.c02: small overlapping integer ranges; may be coincidental
- [S:a:70] weak_overlap at T01.c05: T07.c02: small overlapping integer ranges; may be coincidental
- [S:a:71] low_support at T05.c02: T03.c03: only 52 distinct child values; may be coincidental
- [S:a:72] low_support at T05.c05: T03.c03: only 2 distinct child values; may be coincidental
- [S:a:73] low_support at T07.c02: T03.c03: only 68 distinct child values; may be coincidental
- [S:a:74] low_support at T07.c03: T03.c03: only 3 distinct child values; may be coincidental
- [S:a:75] low_support at T07.c04: T03.c03: only 12 distinct child values; may be coincidental
- [S:a:76] low_support at T07.c01: T03.c03: only 57 distinct child values; may be coincidental
- [S:a:77] low_support at T03.c01: T03.c03: only 3 distinct child values; may be coincidental
- [S:a:78] low_support at T04.c07: T03.c03: only 2 distinct child values; may be coincidental
- [S:a:79] low_support at T04.c01: T03.c03: only 39 distinct child values; may be coincidental
- [S:a:80] low_support at T08.c04: T03.c03: only 5 distinct child values; may be coincidental
- [S:a:81] low_support at T08.c03: T03.c03: only 3 distinct child values; may be coincidental
- [S:a:82] low_support at T08.c02: T03.c03: only 2 distinct child values; may be coincidental
- [S:a:83] low_support at T01.c05: T03.c03: only 32 distinct child values; may be coincidental
- [S:a:84] low_support at T05.c01: T04.c08: only 3363 distinct child values; may be coincidental
- [S:a:85] low_support at T05.c02: T04.c08: only 52 distinct child values; may be coincidental
- [S:a:86] low_support at T05.c05: T04.c08: only 2 distinct child values; may be coincidental
- [S:a:87] low_support at T07.c02: T04.c08: only 68 distinct child values; may be coincidental
- [S:a:88] low_support at T07.c03: T04.c08: only 3 distinct child values; may be coincidental
- [S:a:89] low_support at T07.c04: T04.c08: only 12 distinct child values; may be coincidental
- [S:a:90] low_support at T07.c01: T04.c08: only 57 distinct child values; may be coincidental
- [S:a:91] low_support at T03.c03: T04.c08: only 3512 distinct child values; may be coincidental
- [S:a:92] low_support at T03.c01: T04.c08: only 3 distinct child values; may be coincidental
- [S:a:93] low_support at T03.c02: T04.c08: only 84 distinct child values; may be coincidental
- [S:a:94] low_support at T03.c04: T04.c08: only 3290 distinct child values; may be coincidental
- [S:a:95] low_support at T06.c04: T04.c08: only 37507 distinct child values; may be coincidental
- [S:a:96] low_support at T04.c05: T04.c08: only 98137 distinct child values; may be coincidental
- [S:a:97] low_support at T04.c07: T04.c08: only 2 distinct child values; may be coincidental
- [S:a:98] low_support at T04.c04: T04.c08: only 2038 distinct child values; may be coincidental
- [S:a:99] low_support at T04.c01: T04.c08: only 39 distinct child values; may be coincidental
- [S:a:100] low_support at T08.c04: T04.c08: only 5 distinct child values; may be coincidental
- [S:a:101] low_support at T08.c03: T04.c08: only 3 distinct child values; may be coincidental
- [S:a:102] low_support at T08.c02: T04.c08: only 2 distinct child values; may be coincidental
- [S:a:103] low_support at T01.c04: T04.c08: only 98250 distinct child values; may be coincidental
- [S:a:104] low_support at T01.c01: T04.c08: only 7046 distinct child values; may be coincidental
- [S:a:105] low_support at T01.c05: T04.c08: only 32 distinct child values; may be coincidental
- [S:a:106] low_support at T01.c02: T04.c08: only 892 distinct child values; may be coincidental
- [S:a:107] low_support at T01.c03: T04.c08: only 45 distinct child values; may be coincidental
- [S:a:108] low_support at T02.c04: T04.c08: only 76574 distinct child values; may be coincidental
- [S:a:109] low_support at T05.c01: T01.c04: only 3363 distinct child values; may be coincidental
- [S:a:110] low_support at T05.c02: T01.c04: only 52 distinct child values; may be coincidental
- [S:a:111] low_support at T05.c05: T01.c04: only 2 distinct child values; may be coincidental
- [S:a:112] low_support at T07.c02: T01.c04: only 68 distinct child values; may be coincidental
- [S:a:113] low_support at T07.c03: T01.c04: only 3 distinct child values; may be coincidental
- [S:a:114] low_support at T07.c04: T01.c04: only 12 distinct child values; may be coincidental
- [S:a:115] low_support at T07.c01: T01.c04: only 57 distinct child values; may be coincidental
- [S:a:116] low_support at T03.c03: T01.c04: only 3512 distinct child values; may be coincidental
- [S:a:117] low_support at T03.c01: T01.c04: only 3 distinct child values; may be coincidental
- [S:a:118] low_support at T03.c02: T01.c04: only 84 distinct child values; may be coincidental
- [S:a:119] low_support at T04.c07: T01.c04: only 2 distinct child values; may be coincidental
- [S:a:120] low_support at T04.c04: T01.c04: only 2038 distinct child values; may be coincidental
- [S:a:121] low_support at T04.c01: T01.c04: only 39 distinct child values; may be coincidental
- [S:a:122] low_support at T08.c04: T01.c04: only 5 distinct child values; may be coincidental
- [S:a:123] low_support at T08.c03: T01.c04: only 3 distinct child values; may be coincidental
- [S:a:124] low_support at T08.c02: T01.c04: only 2 distinct child values; may be coincidental
- [S:a:125] low_support at T01.c05: T01.c04: only 32 distinct child values; may be coincidental
- [S:a:126] low_support at T01.c03: T01.c04: only 45 distinct child values; may be coincidental
- [S:a:127] no_candidate_key at T06: no single column is unique and non-null (event log, or composite key?)
- [S:a:128] no_candidate_key at T08: no single column is unique and non-null (event log, or composite key?)
- [S:a:129] no_candidate_key at T02: no single column is unique and non-null (event log, or composite key?)

## Outcome-driven analysis (predictive associations; NOT causal, NOT semantic proof)
Label rows: {'train': 86619, 'val': 29979, 'test': 36129} (time-based splits: train, then validation, then test). Positive rate: {'train': 0.906, 'val': 0.903, 'test': 0.851}.
Features were built only from candidate relationships marked preferred and non-weak, using only rows dated before each cutoff.
- [P:m:1] Model performance (AUROC; 0.5 = chance): gradient_boosting: val=0.703 test=0.671; logistic_regression: val=0.704 test=0.668; selected on validation: logistic_regression
- [P:m:2] Baseline: best single past-activity count (f063) test AUROC=0.655

Relationship paths ranked by summed permutation importance (validation):
- [P:path:1] importance=0.3282 path: T02.c04 -> T01.c04 features=['f063', 'f064', 'f065', 'f066', 'f067']
- [P:path:2] importance=0.0299 path: T06.c04 -> T01.c04 features=['f015', 'f016', 'f017', 'f018', 'f019']
- [P:path:3] importance=0.0090 path: T04.c05 -> T01.c04 features=['f024', 'f025', 'f026', 'f027', 'f028', 'f029', 'f030']
- [P:path:4] importance=0.0031 path: T04.c05 -> T01.c04 then T08.c06 -> T04.c08 features=['f032', 'f033', 'f034', 'f035', 'f036']
- [P:path:5] importance=0.0015 path: T02.c04 -> T01.c04 then T02.c01 -> T05.c03 features=['f068', 'f069']
- [P:path:6] importance=0.0015 path: T01.c01 -> T01.c04 features=['f039', 'f040', 'f041', 'f042']
- [P:path:7] importance=0.0015 path: (target table itself) features=['f000', 'f001', 'f002', 'f003']
- [P:path:8] importance=0.0012 path: T01.c02 -> T01.c04 then T02.c04 -> T01.c04 features=['f061']
- [P:path:9] importance=0.0012 path: T02.c04 -> T01.c04 then T02.c02 -> T04.c08 features=['f070', 'f071']
- [P:path:10] importance=0.0011 path: T01.c02 -> T01.c04 features=['f051', 'f052', 'f053', 'f054']
- [P:path:11] importance=0.0011 path: T01.c02 -> T01.c04 then T04.c05 -> T01.c04 features=['f058', 'f059', 'f060']
- [P:path:12] importance=0.0005 path: T03.c04 -> T01.c04 features=['f004', 'f005', 'f006']
- [P:path:13] importance=0.0005 path: T04.c05 -> T01.c04 then T02.c02 -> T04.c08 features=['f037']
- [P:path:14] importance=0.0005 path: T06.c04 -> T01.c04 then T06.c01 -> T04.c08 features=['f022', 'f023']
- [P:path:15] importance=0.0004 path: T01.c01 -> T01.c04 then T02.c04 -> T01.c04 features=['f049']
- [P:path:16] importance=0.0004 path: T03.c04 -> T01.c04 then T05.c01 -> T03.c03 features=['f007', 'f008', 'f009']
- [P:path:17] importance=0.0003 path: T04.c05 -> T01.c04 then T06.c01 -> T04.c08 features=['f031']
- [P:path:18] importance=0.0003 path: T03.c04 -> T01.c04 then T04.c04 -> T03.c03 features=['f010', 'f011', 'f012']
- [P:path:19] importance=0.0002 path: T01.c01 -> T01.c04 then T04.c05 -> T01.c04 features=['f046', 'f047', 'f048']
- [P:path:20] importance=0.0002 path: T01.c01 -> T01.c04 then T06.c04 -> T01.c04 features=['f045']
- [P:path:21] importance=0.0002 path: T06.c04 -> T01.c04 then T06.c03 -> T05.c03 features=['f020', 'f021']
- [P:path:22] importance=0.0001 path: T01.c02 -> T01.c04 then T06.c04 -> T01.c04 features=['f057']
- [P:path:23] importance=0.0001 path: T03.c04 -> T01.c04 then T01.c03 -> T03.c03 features=['f013', 'f014']
- [P:path:24] importance=0.0000 path: T01.c02 -> T01.c04 then T03.c04 -> T01.c04 features=['f055', 'f056']
- [P:path:25] importance=0.0000 path: T01.c01 -> T01.c04 then T03.c04 -> T01.c04 features=['f043', 'f044']
- [P:path:26] importance=0.0000 path: T01.c02 -> T01.c04 then T01.c03 -> T03.c03 features=['f062']
- [P:path:27] importance=0.0000 path: T04.c05 -> T01.c04 then T04.c04 -> T03.c03 features=['f038']
- [P:path:28] importance=0.0000 path: T01.c01 -> T01.c04 then T01.c03 -> T03.c03 features=['f050']

Features (agg over the path; window in days before cutoff; univariate AUROC on train/val; direction; stability of direction across training cutoffs; BH-adjusted q-value; permutation importance):
- [P:f:f066] count_distinct(T02.c01) window=all via T02.c04 -> T01.c04: auroc train=0.639 val=0.688 higher_in_positive stable=yes q=0 perm_imp=0.2798 coverage=100%
- [P:f:f063] count(T02 rows) window=all via T02.c04 -> T01.c04: auroc train=0.636 val=0.683 higher_in_positive stable=yes q=0 perm_imp=0.0322 coverage=100%
- [P:f:f018] count_distinct(T06.c03) window=all via T06.c04 -> T01.c04: auroc train=0.569 val=0.604 higher_in_positive stable=yes q=1e-147 perm_imp=0.0181 coverage=100%
- [P:f:f067] count_distinct(T02.c02) window=all via T02.c04 -> T01.c04: auroc train=0.578 val=0.553 higher_in_positive stable=yes q=3.2e-163 perm_imp=0.0144 coverage=100%
- [P:f:f015] count(T06 rows) window=all via T06.c04 -> T01.c04: auroc train=0.568 val=0.603 higher_in_positive stable=yes q=9.5e-147 perm_imp=0.0107 coverage=100%
- [P:f:f024] count(T04 rows) window=all via T04.c05 -> T01.c04: auroc train=0.594 val=0.621 higher_in_positive stable=yes q=1.1e-207 perm_imp=0.0034 coverage=100%
- [P:f:f026] days_since_last(T04 rows) window=all via T04.c05 -> T01.c04: auroc train=0.470 val=0.450 lower_in_positive stable=yes q=2.4e-37 perm_imp=0.0021 coverage=43%
- [P:f:f068] mean(T05.c04) window=all via T02.c04 -> T01.c04 then T02.c01 -> T05.c03: auroc train=0.555 val=0.558 higher_in_positive stable=yes q=4.7e-76 perm_imp=0.0015 coverage=60%
- [P:f:f000] value(T01.c01) window=all via (target table itself): auroc train=0.507 val=0.512 higher_in_positive stable=yes q=0.12 perm_imp=0.0015 coverage=100%
- [P:f:f065] days_since_last(T02 rows) window=all via T02.c04 -> T01.c04: auroc train=0.451 val=0.425 lower_in_positive stable=yes q=1.9e-76 perm_imp=0.0014 coverage=60%
- [P:f:f025] count(T04 rows) window=4 via T04.c05 -> T01.c04: auroc train=0.584 val=0.601 higher_in_positive stable=yes q=1e-186 perm_imp=0.0012 coverage=100%
- [P:f:f061] count(T02 rows) window=all via T01.c02 -> T01.c04 then T02.c04 -> T01.c04: auroc train=0.500 val=0.501 higher_in_positive stable=no q=0.69 perm_imp=0.0012 coverage=100%
- [P:f:f029] count_distinct(T04.c04) window=all via T04.c05 -> T01.c04: auroc train=0.584 val=0.597 higher_in_positive stable=yes q=6.7e-173 perm_imp=0.0012 coverage=100%
- [P:f:f070] mean(T04.c07) window=all via T02.c04 -> T01.c04 then T02.c02 -> T04.c08: auroc train=0.529 val=0.520 higher_in_positive stable=yes q=0.15 perm_imp=0.0012 coverage=60%
- [P:f:f034] mean(T08.c03) window=all via T04.c05 -> T01.c04 then T08.c06 -> T04.c08: auroc train=0.502 val=0.503 higher_in_positive stable=no q=0.88 perm_imp=0.0011 coverage=43%
- [P:f:f054] count_distinct(T01.c01) window=all via T01.c02 -> T01.c04: auroc train=0.500 val=0.500 higher_in_positive stable=no q=1 perm_imp=0.0010 coverage=100%
- [P:f:f030] count_distinct(T04.c06) window=all via T04.c05 -> T01.c04: auroc train=0.578 val=0.574 higher_in_positive stable=yes q=1.3e-158 perm_imp=0.0010 coverage=100%
- [P:f:f039] count(T01 rows) window=all via T01.c01 -> T01.c04: auroc train=0.500 val=0.503 lower_in_positive stable=no q=1 perm_imp=0.0008 coverage=100%
- [P:f:f032] count(T08 rows) window=all via T04.c05 -> T01.c04 then T08.c06 -> T04.c08: auroc train=0.593 val=0.620 higher_in_positive stable=yes q=7.7e-207 perm_imp=0.0008 coverage=100%
- [P:f:f033] mean(T08.c04) window=all via T04.c05 -> T01.c04 then T08.c06 -> T04.c08: auroc train=0.507 val=0.505 higher_in_positive stable=yes q=0.58 perm_imp=0.0007 coverage=43%
- [P:f:f059] mean(T04.c07) window=all via T01.c02 -> T01.c04 then T04.c05 -> T01.c04: auroc train=0.500 val=0.500 higher_in_positive stable=yes q=0.45 perm_imp=0.0007 coverage=0%
- [P:f:f035] mean(T08.c07) window=all via T04.c05 -> T01.c04 then T08.c06 -> T04.c08: auroc train=0.494 val=0.493 lower_in_positive stable=yes q=0.08 perm_imp=0.0006 coverage=43%
- [P:f:f017] days_since_last(T06 rows) window=all via T06.c04 -> T01.c04: auroc train=0.491 val=0.467 lower_in_positive stable=yes q=6.7e-09 perm_imp=0.0005 coverage=28%
- [P:f:f064] count(T02 rows) window=4 via T02.c04 -> T01.c04: auroc train=0.623 val=0.657 higher_in_positive stable=yes q=0 perm_imp=0.0005 coverage=100%
- [P:f:f037] count(T02 rows) window=all via T04.c05 -> T01.c04 then T02.c02 -> T04.c08: auroc train=0.537 val=0.574 higher_in_positive stable=yes q=5.6e-94 perm_imp=0.0005 coverage=100%
- [P:f:f016] count(T06 rows) window=4 via T06.c04 -> T01.c04: auroc train=0.555 val=0.578 higher_in_positive stable=yes q=3.3e-118 perm_imp=0.0005 coverage=100%
- [P:f:f004] count(T03 rows) window=all via T03.c04 -> T01.c04: auroc train=0.502 val=0.503 higher_in_positive stable=yes q=0.12 perm_imp=0.0005 coverage=100%
- [P:f:f049] count(T02 rows) window=all via T01.c01 -> T01.c04 then T02.c04 -> T01.c04: auroc train=0.501 val=0.504 higher_in_positive stable=no q=0.81 perm_imp=0.0004 coverage=100%
- [P:f:f022] mean(T04.c07) window=all via T06.c04 -> T01.c04 then T06.c01 -> T04.c08: auroc train=0.521 val=0.529 higher_in_positive stable=yes q=1 perm_imp=0.0004 coverage=28%
- [P:f:f007] count(T05 rows) window=all via T03.c04 -> T01.c04 then T05.c01 -> T03.c03: auroc train=0.502 val=0.502 higher_in_positive stable=yes q=0.065 perm_imp=0.0004 coverage=100%
- [P:f:f031] count(T06 rows) window=all via T04.c05 -> T01.c04 then T06.c01 -> T04.c08: auroc train=0.520 val=0.550 higher_in_positive stable=yes q=6.4e-53 perm_imp=0.0003 coverage=100%
- [P:f:f060] mean(T04.c01) window=all via T01.c02 -> T01.c04 then T04.c05 -> T01.c04: auroc train=0.500 val=0.500 lower_in_positive stable=no q=0.93 perm_imp=0.0003 coverage=0%
- [P:f:f041] count_distinct(T01.c03) window=all via T01.c01 -> T01.c04: auroc train=0.500 val=0.503 lower_in_positive stable=no q=1 perm_imp=0.0003 coverage=100%
- [P:f:f042] count_distinct(T01.c02) window=all via T01.c01 -> T01.c04: auroc train=0.500 val=0.503 lower_in_positive stable=no q=1 perm_imp=0.0003 coverage=100%
- [P:f:f010] count(T04 rows) window=all via T03.c04 -> T01.c04 then T04.c04 -> T03.c03: auroc train=0.499 val=0.501 lower_in_positive stable=no q=0.71 perm_imp=0.0002 coverage=100%
- [P:f:f045] count(T06 rows) window=all via T01.c01 -> T01.c04 then T06.c04 -> T01.c04: auroc train=0.500 val=0.502 lower_in_positive stable=no q=0.8 perm_imp=0.0002 coverage=100%
- [P:f:f020] mean(T05.c04) window=all via T06.c04 -> T01.c04 then T06.c03 -> T05.c03: auroc train=0.513 val=0.527 higher_in_positive stable=yes q=1.9e-10 perm_imp=0.0002 coverage=28%
- [P:f:f057] count(T06 rows) window=all via T01.c02 -> T01.c04 then T06.c04 -> T01.c04: auroc train=0.500 val=0.500 lower_in_positive stable=no q=0.8 perm_imp=0.0001 coverage=100%
- [P:f:f046] count(T04 rows) window=all via T01.c01 -> T01.c04 then T04.c05 -> T01.c04: auroc train=0.500 val=0.503 higher_in_positive stable=no q=1 perm_imp=0.0001 coverage=100%
- [P:f:f013] count(T01 rows) window=all via T03.c04 -> T01.c04 then T01.c03 -> T03.c03: auroc train=0.500 val=0.500 lower_in_positive stable=no q=0.58 perm_imp=0.0001 coverage=100%
- [P:f:f058] count(T04 rows) window=all via T01.c02 -> T01.c04 then T04.c05 -> T01.c04: auroc train=0.500 val=0.501 higher_in_positive stable=yes q=0.64 perm_imp=0.0001 coverage=100%
- [P:f:f051] count(T01 rows) window=all via T01.c02 -> T01.c04: auroc train=0.500 val=0.500 higher_in_positive stable=no q=1 perm_imp=0.0001 coverage=100%
- [P:f:f047] mean(T04.c07) window=all via T01.c01 -> T01.c04 then T04.c05 -> T01.c04: auroc train=0.500 val=0.502 higher_in_positive stable=no q=1 perm_imp=0.0001 coverage=2%
- [P:f:f040] mean(T01.c05) window=all via T01.c01 -> T01.c04: auroc train=0.501 val=0.498 higher_in_positive stable=yes q=0.88 perm_imp=0.0001 coverage=7%
- [P:f:f023] mean(T04.c01) window=all via T06.c04 -> T01.c04 then T06.c01 -> T04.c08: auroc train=0.494 val=0.498 lower_in_positive stable=yes q=1 perm_imp=0.0001 coverage=28%
- [P:f:f048] mean(T04.c01) window=all via T01.c01 -> T01.c04 then T04.c05 -> T01.c04: auroc train=0.500 val=0.499 higher_in_positive stable=no q=0.88 perm_imp=0.0001 coverage=2%
- [P:f:f012] mean(T04.c01) window=all via T03.c04 -> T01.c04 then T04.c04 -> T03.c03: auroc train=0.500 val=0.502 lower_in_positive stable=no q=0.94 perm_imp=0.0000 coverage=1%
- [P:f:f071] mean(T04.c01) window=all via T02.c04 -> T01.c04 then T02.c02 -> T04.c08: auroc train=0.493 val=0.497 lower_in_positive stable=yes q=0.94 perm_imp=0.0000 coverage=60%
- [P:f:f056] mean(T03.c01) window=all via T01.c02 -> T01.c04 then T03.c04 -> T01.c04: auroc train=0.500 val=0.500 lower_in_positive stable=yes q=0.72 perm_imp=0.0000 coverage=0%
- [P:f:f028] mean(T04.c01) window=all via T04.c05 -> T01.c04: auroc train=0.505 val=0.515 higher_in_positive stable=no q=0.019 perm_imp=0.0000 coverage=43%
- [P:f:f005] mean(T03.c01) window=all via T03.c04 -> T01.c04: auroc train=0.500 val=0.500 higher_in_positive stable=no q=0.035 perm_imp=0.0000 coverage=3%
- [P:f:f062] mean(T03.c01) window=all via T01.c02 -> T01.c04 then T01.c03 -> T03.c03: auroc train=0.500 val=0.500 higher_in_positive stable=no q=0.72 perm_imp=0.0000 coverage=1%
- [P:f:f044] mean(T03.c01) window=all via T01.c01 -> T01.c04 then T03.c04 -> T01.c04: auroc train=0.500 val=0.500 higher_in_positive stable=yes q=0.72 perm_imp=0.0000 coverage=1%
- [P:f:f053] count_distinct(T01.c03) window=all via T01.c02 -> T01.c04: auroc train=0.500 val=0.500 higher_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f038] mean(T03.c01) window=all via T04.c05 -> T01.c04 then T04.c04 -> T03.c03: auroc train=0.488 val=0.482 lower_in_positive stable=yes q=0.0011 perm_imp=0.0000 coverage=43%
- [P:f:f043] count(T03 rows) window=all via T01.c01 -> T01.c04 then T03.c04 -> T01.c04: auroc train=0.500 val=0.500 lower_in_positive stable=no q=0.87 perm_imp=0.0000 coverage=100%
- [P:f:f009] mean(T05.c05) window=all via T03.c04 -> T01.c04 then T05.c01 -> T03.c03: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=3%
- [P:f:f021] mean(T05.c05) window=all via T06.c04 -> T01.c04 then T06.c03 -> T05.c03: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=28%
- [P:f:f069] mean(T05.c05) window=all via T02.c04 -> T01.c04 then T02.c01 -> T05.c03: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=60%
- [P:f:f050] mean(T03.c01) window=all via T01.c01 -> T01.c04 then T01.c03 -> T03.c03: auroc train=0.500 val=0.500 higher_in_positive stable=no q=0.81 perm_imp=0.0000 coverage=7%
- [P:f:f055] count(T03 rows) window=all via T01.c02 -> T01.c04 then T03.c04 -> T01.c04: auroc train=0.500 val=0.500 higher_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f052] mean(T01.c05) window=all via T01.c02 -> T01.c04: auroc train=0.500 val=0.500 lower_in_positive stable=no q=0.92 perm_imp=0.0000 coverage=1%
- [P:f:f019] count_distinct(T06.c01) window=all via T06.c04 -> T01.c04: auroc train=0.564 val=0.585 higher_in_positive stable=yes q=1e-133 perm_imp=-0.0000 coverage=100%
- [P:f:f008] mean(T05.c04) window=all via T03.c04 -> T01.c04 then T05.c01 -> T03.c03: auroc train=0.499 val=0.499 lower_in_positive stable=yes q=0.64 perm_imp=-0.0000 coverage=3%
- [P:f:f006] count_distinct(T03.c02) window=all via T03.c04 -> T01.c04: auroc train=0.502 val=0.503 higher_in_positive stable=yes q=0.12 perm_imp=-0.0000 coverage=100%
- [P:f:f002] value(T01.c02) window=all via (target table itself): auroc train=0.495 val=0.496 lower_in_positive stable=yes q=0.018 perm_imp=-0.0000 coverage=100%
- [P:f:f014] mean(T01.c05) window=all via T03.c04 -> T01.c04 then T01.c03 -> T03.c03: auroc train=0.500 val=0.500 lower_in_positive stable=no q=0.9 perm_imp=-0.0000 coverage=0%
- [P:f:f003] value(T01.c03) window=all via (target table itself): auroc train=0.504 val=0.501 higher_in_positive stable=no q=0.48 perm_imp=-0.0000 coverage=100%
- [P:f:f011] mean(T04.c07) window=all via T03.c04 -> T01.c04 then T04.c04 -> T03.c03: auroc train=0.500 val=0.499 lower_in_positive stable=no q=1 perm_imp=-0.0000 coverage=1%
- [P:f:f001] value(T01.c05) window=all via (target table itself): auroc train=0.498 val=0.493 lower_in_positive stable=no q=0.81 perm_imp=-0.0001 coverage=100%
- [P:f:f036] mean(T08.c02) window=all via T04.c05 -> T01.c04 then T08.c06 -> T04.c08: auroc train=0.524 val=0.541 higher_in_positive stable=yes q=1.1e-15 perm_imp=-0.0001 coverage=43%
- [P:f:f027] mean(T04.c07) window=all via T04.c05 -> T01.c04: auroc train=0.532 val=0.528 higher_in_positive stable=yes q=0.0029 perm_imp=-0.0002 coverage=43%