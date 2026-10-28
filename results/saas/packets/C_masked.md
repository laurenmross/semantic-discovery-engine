## Business outcome of interest (supplied by the business)
- Conversion: whether the entity identified by T05.c02 reaches the business's conversion milestone in the 16 days after the cutoff timestamp (entities that already reached it are excluded).
- Outcome entity: T05.c02

## Schema (tables, columns, types, row counts, example values)
### Table T01  [S:t:T01]  rows=13577665
- c01: BIGINT; examples ['9', '10', '14']  [S:c:T01.c01]
    profile: nulls=0.0% distinct=15 unique=no min=1 max=15 mean=6.354 top=1:1664620, 5:1456916, 4:1405663, 8:1248449, 2:1247915, 9:1040136
- c02: BIGINT; examples ['911330994', '959645336', '919409939']  [S:c:T01.c02]
    profile: nulls=0.0% distinct=83543 unique=no min=100009566 max=999991544 mean=5.511e+08
- c03: DOUBLE; examples ['2742.0', '5660.0', '4225.0']  [S:c:T01.c03]
    profile: nulls=0.0% distinct=33076 unique=no min=100.0 max=115377.0 mean=3801 (float type holding only whole numbers)
- c04: TIMESTAMP_NS; examples ['2025-07-01 03:49:42', '2025-07-02 05:12:41', '2025-07-02 08:07:25']  [S:c:T01.c04]
    profile: nulls=0.0% distinct=10835043 unique=no min=2025-07-01 02:02:34 max=2026-06-29 23:45:30

### Table T02  [S:t:T02]  rows=4229
- c01: BIGINT; examples ['2', '4', '5']  [S:c:T02.c01]
    profile: nulls=0.0% distinct=6 unique=no min=1 max=6 mean=2.375 top=2:1794, 1:1049, 3:692, 5:303, 4:266, 6:125
- c02: BIGINT; examples ['1', '2', '3']  [S:c:T02.c02]
    profile: nulls=0.0% distinct=3 unique=no min=1 max=3 mean=1.257 top=1:3322, 2:729, 3:178
- c03: TIMESTAMP_NS; examples ['2025-07-07 07:50:35.314570834', '2025-07-13 12:14:29.685042654', '2025-07-04 11:06:39.74655652']  [S:c:T02.c03]
    profile: nulls=0.0% distinct=4229 unique=yes min=2025-07-04 11:06:39.74655652 max=2026-06-20 08:30:50.474160233
- c04: BIGINT; examples ['9278205', '4945591', '1378006']  [S:c:T02.c04]
    profile: nulls=0.0% distinct=4229 unique=yes min=501327 max=9997690 mean=5.232e+06
- c05: BIGINT; examples ['22594933', '94503550', '61507448']  [S:c:T02.c05]
    profile: nulls=0.0% distinct=4229 unique=yes min=10009439 max=99980611 mean=5.435e+07
- c06: TIMESTAMP_NS; examples ['2025-10-04 20:52:54.139537056', '2025-08-25 01:52:13.945263503', '2025-12-23 19:14:28.324253171']  [S:c:T02.c06]
    profile: nulls=82.8% distinct=729 unique=yes min=2025-08-25 01:52:13.945263503 max=2026-06-29 19:14:48.426980566

### Table T03  [S:t:T03]  rows=76345
- c01: TIMESTAMP_NS; examples ['2025-07-05 03:23:25', '2025-07-18 03:32:31', '2025-07-17 18:09:44']  [S:c:T03.c01]
    profile: nulls=0.0% distinct=76238 unique=no min=2025-07-01 14:22:06 max=2026-06-29 22:53:55
- c02: BIGINT; examples ['4', '2', '1']  [S:c:T03.c02]
    profile: nulls=0.0% distinct=4 unique=no min=1 max=4 mean=1.993 top=1:39944, 3:15188, 4:12127, 2:9086
- c03: BIGINT; examples ['911330994', '959645336', '372150613']  [S:c:T03.c03]
    profile: nulls=19.8% distinct=21324 unique=no min=100009566 max=999888827 mean=5.472e+08
- c04: BIGINT; examples ['1', '4', '2']  [S:c:T03.c04]
    profile: nulls=40.2% distinct=5 unique=no min=1 max=5 mean=3.002 top=None:30727, 4:9209, 1:9125, 3:9110, 5:9099, 2:9075
- c05: BIGINT; examples ['75091266', '22594933', '24071260']  [S:c:T03.c05]
    profile: nulls=0.0% distinct=18854 unique=no min=10006538 max=99983177 mean=5.502e+07
- c06: BIGINT; examples ['5763920', '9542057', '4456299']  [S:c:T03.c06]
    profile: nulls=0.0% distinct=76345 unique=yes min=1000028 max=9999912 mean=5.509e+06
- c07: TIMESTAMP_NS; examples ['2025-07-04 15:11:35', '2025-07-13 21:22:52', '2025-07-15 17:18:16']  [S:c:T03.c07]
    profile: nulls=0.0% distinct=76246 unique=no min=2025-07-01 10:18:36 max=2026-06-29 07:49:29

### Table T04  [S:t:T04]  rows=61707
- c01: BIGINT; examples ['9278205', '4945591', '1378006']  [S:c:T04.c01]
    profile: nulls=0.0% distinct=4229 unique=no min=501327 max=9997690 mean=5.237e+06
- c02: BIGINT; examples ['1', '3', '4']  [S:c:T04.c02]
    profile: nulls=0.0% distinct=4 unique=no min=1 max=4 mean=2.024 top=1:25360, 3:25360, 2:10255, 4:732
- c03: DOUBLE; examples ['7900.0', '632.0', '-7588.0']  [S:c:T04.c03]
    profile: nulls=0.0% distinct=773 unique=no min=-99126.0 max=99900.0 mean=8384 (float type holding only whole numbers)
- c04: TIMESTAMP_NS; examples ['2025-07-07 07:50:35.314570834', '2025-08-06 07:50:35.314570834', '2025-09-05 07:50:35.314570834']  [S:c:T04.c04]
    profile: nulls=0.0% distinct=25360 unique=no min=2025-07-04 11:06:39.74655652 max=2026-06-29 23:49:31.168424111
- c05: BIGINT; examples ['63411137', '96127998', '37839780']  [S:c:T04.c05]
    profile: nulls=0.0% distinct=61707 unique=yes min=10000361 max=99998847 mean=5.501e+07

### Table T05  [S:t:T05]  rows=20000
- c01: TIMESTAMP_NS; examples ['2025-07-01 00:17:08.458175719', '2025-07-01 00:32:00.030784175', '2025-07-01 01:15:00.620040557']  [S:c:T05.c01]
    profile: nulls=0.0% distinct=20000 unique=yes min=2025-07-01 00:17:08.458175719 max=2026-05-30 22:34:31.079415791
- c02: BIGINT; examples ['75091266', '22594933', '24071260']  [S:c:T05.c02]
    profile: nulls=0.0% distinct=20000 unique=yes min=10006538 max=99983177 mean=5.482e+07
- c03: BIGINT; examples ['2', '1', '3']  [S:c:T05.c03]
    profile: nulls=0.0% distinct=4 unique=no min=1 max=4 mean=1.651 top=1:11025, 2:5935, 3:2044, 4:996
- c04: BIGINT; examples ['1', '5', '3']  [S:c:T05.c04]
    profile: nulls=0.0% distinct=6 unique=no min=1 max=6 mean=3.043 top=2:5937, 3:4103, 1:3023, 4:2995, 5:1981, 6:1961
- c05: BIGINT; examples ['2', '1', '5']  [S:c:T05.c05]
    profile: nulls=0.0% distinct=7 unique=no min=1 max=7 mean=2.47 top=1:7312, 2:5701, 4:2629, 3:1981, 6:1002, 5:708
- c06: BIGINT; examples ['1', '22', '16']  [S:c:T05.c06]
    profile: nulls=0.0% distinct=40 unique=no min=1 max=40 mean=20.48

### Table T06  [S:t:T06]  rows=84594
- c01: TIMESTAMP_NS; examples ['2025-07-01 00:17:08', '2025-07-01 00:32:00', '2025-08-14 16:12:29']  [S:c:T06.c01]
    profile: nulls=0.0% distinct=84485 unique=no min=2025-07-01 00:17:08 max=2026-07-01 09:39:30
- c02: BIGINT; examples ['1', '2', '3']  [S:c:T06.c02]
    profile: nulls=0.0% distinct=3 unique=no min=1 max=3 mean=1.991 top=2:45355, 1:20000, 3:19239
- c03: BIGINT; examples ['959645336', '828584695', '369477489']  [S:c:T06.c03]
    profile: nulls=23.6% distinct=33885 unique=no min=100009566 max=999991544 mean=5.515e+08
- c04: BIGINT; examples ['75091266', '22594933', '24071260']  [S:c:T06.c04]
    profile: nulls=0.0% distinct=20000 unique=no min=10006538 max=99983177 mean=5.436e+07
- c05: BIGINT; examples ['911330994', '959645336', '919409939']  [S:c:T06.c05]
    profile: nulls=0.0% distinct=84594 unique=yes min=100009566 max=999991544 mean=5.505e+08

### Table T07  [S:t:T07]  rows=40
- c01: BIGINT; examples ['4', '5', '2']  [S:c:T07.c01]
    profile: nulls=0.0% distinct=5 unique=no min=1 max=5 mean=2.925 top=4:11, 1:9, 2:8, 5:6, 3:6
- c02: BIGINT; examples ['2', '8', '-6']  [S:c:T07.c02]
    profile: nulls=0.0% distinct=13 unique=no min=-9 max=10 mean=-1.175 top=0:7, 2:4, -9:4, 1:4, -5:4, 10:3
- c03: BIGINT; examples ['1', '2', '3']  [S:c:T07.c03]
    profile: nulls=0.0% distinct=40 unique=yes min=1 max=40 mean=20.5

### Table T08  [S:t:T08]  rows=147025
- c01: BIGINT; examples ['1', '2', '3']  [S:c:T08.c01]
    profile: nulls=0.0% distinct=8 unique=no min=1 max=8 mean=4.319 top=1:20000, 2:20000, 3:19588, 4:19098, 5:18412, 6:17536
- c02: BIGINT; examples ['75091266', '22594933', '24071260']  [S:c:T08.c02]
    profile: nulls=0.0% distinct=20000 unique=no min=10006538 max=99983177 mean=5.487e+07
- c03: BIGINT; examples ['1', '0']  [S:c:T08.c03]
    profile: nulls=0.0% distinct=2 unique=no min=0 max=1 mean=0.3102 top=0:101425, 1:45600
- c04: TIMESTAMP_NS; examples ['2025-07-01 09:17:08', '2025-07-02 09:17:08', '2025-07-04 09:17:08']  [S:c:T08.c04]
    profile: nulls=0.0% distinct=146606 unique=no min=2025-07-01 09:17:08 max=2026-06-20 07:34:31
- c05: BIGINT; examples ['0', '1']  [S:c:T08.c05]
    profile: nulls=0.0% distinct=2 unique=no min=0 max=1 mean=0.09415 top=0:133182, 1:13843

### Table T09  [S:t:T09]  rows=6
- c01: DOUBLE; examples ['29.0', '79.0', '149.0']  [S:c:T09.c01]
    profile: nulls=0.0% distinct=6 unique=yes min=15.0 max=999.0 mean=278.3 top=399.0:1, 15.0:1, 149.0:1, 29.0:1, 79.0:1, 999.0:1 (float type holding only whole numbers)
- c02: BIGINT; examples ['1', '2', '3']  [S:c:T09.c02]
    profile: nulls=0.0% distinct=5 unique=no min=1 max=5 mean=2.667 top=1:2, 5:1, 2:1, 3:1, 4:1
- c03: BIGINT; examples ['3', '10', '25']  [S:c:T09.c03]
    profile: nulls=0.0% distinct=6 unique=yes min=3 max=500 mean=114.7 top=500:1, 100:1, 3:1, 50:1, 10:1, 25:1
- c04: BIGINT; examples ['1', '2', '3']  [S:c:T09.c04]
    profile: nulls=0.0% distinct=6 unique=yes min=1 max=6 mean=3.5 top=5:1, 2:1, 1:1, 6:1, 3:1, 4:1

## Structural analysis (deterministic; computed from values only, never from names)
Candidate keys (100% unique, no nulls):
- T05.c02  [S:k:T05.c02]
- T07.c03  [S:k:T07.c03]
- T04.c05  [S:k:T04.c05]
- T09.c04  [S:k:T09.c04]
- T09.c01  [S:k:T09.c01]
- T09.c03  [S:k:T09.c03]
- T02.c04  [S:k:T02.c04]
- T02.c05  [S:k:T02.c05]
- T03.c06  [S:k:T03.c06]
- T06.c05  [S:k:T06.c05]
Time columns: T05.c01, T01.c04, T08.c04, T04.c04, T02.c03, T02.c06, T03.c07, T03.c01, T06.c01

Candidate relationships (child column values contained in a candidate key).
Fields: inclusion = share of distinct child values found in parent key; coverage = share of parent keys referenced; range_density = share of the child's value range filled by parent keys (near 1.0 means inclusion is weak evidence, because any small integers would match); rows/parent = avg and max child rows per referenced parent; rank = rank of this parent among this child column's candidates by coverage; preferred = top-ranked and plausible; weak = both sides are small integer ranges starting near 0/1.
- [S:r:1] T01.c01 -> T07.c03: inclusion=1.0 coverage=0.375 range_density=1.0 rows/parent=905177.67/1664620 child_distinct=15 rank=1 preferred=yes weak=yes
- [S:r:2] T01.c02 -> T06.c05: inclusion=1.0 coverage=0.9876 range_density=0.0001 rows/parent=162.52/942 child_distinct=83543 rank=1 preferred=yes weak=no
- [S:r:3] T02.c01 -> T09.c04: inclusion=1.0 coverage=1.0 range_density=1.0 rows/parent=704.83/1794 child_distinct=6 rank=1 preferred=yes weak=yes
- [S:r:4] T02.c01 -> T07.c03: inclusion=1.0 coverage=0.15 range_density=1.0 rows/parent=704.83/1794 child_distinct=6 rank=2 preferred=no weak=yes
- [S:r:5] T02.c02 -> T09.c04: inclusion=1.0 coverage=0.5 range_density=1.0 rows/parent=1409.67/3322 child_distinct=3 rank=1 preferred=yes weak=yes
- [S:r:6] T02.c02 -> T07.c03: inclusion=1.0 coverage=0.075 range_density=1.0 rows/parent=1409.67/3322 child_distinct=3 rank=2 preferred=no weak=yes
- [S:r:7] T02.c05 -> T05.c02: inclusion=1.0 coverage=0.2114 range_density=0.0002 rows/parent=1.0/1 child_distinct=4229 rank=1 preferred=no weak=no child_is_unique
- [S:r:8] T03.c02 -> T09.c04: inclusion=1.0 coverage=0.6667 range_density=1.0 rows/parent=19086.25/39944 child_distinct=4 rank=1 preferred=yes weak=yes
- [S:r:9] T03.c02 -> T07.c03: inclusion=1.0 coverage=0.1 range_density=1.0 rows/parent=19086.25/39944 child_distinct=4 rank=2 preferred=no weak=yes
- [S:r:10] T03.c03 -> T06.c05: inclusion=1.0 coverage=0.2521 range_density=0.0001 rows/parent=2.87/78 child_distinct=21324 rank=1 preferred=yes weak=no
- [S:r:11] T03.c04 -> T09.c04: inclusion=1.0 coverage=0.8333 range_density=1.0 rows/parent=9123.6/9209 child_distinct=5 rank=1 preferred=yes weak=yes
- [S:r:12] T03.c04 -> T07.c03: inclusion=1.0 coverage=0.125 range_density=1.0 rows/parent=9123.6/9209 child_distinct=5 rank=2 preferred=no weak=yes
- [S:r:13] T03.c05 -> T05.c02: inclusion=1.0 coverage=0.9427 range_density=0.0002 rows/parent=4.05/95 child_distinct=18854 rank=1 preferred=yes weak=no
- [S:r:14] T04.c01 -> T02.c04: inclusion=1.0 coverage=1.0 range_density=0.0004 rows/parent=14.59/39 child_distinct=4229 rank=1 preferred=yes weak=no
- [S:r:15] T04.c02 -> T09.c04: inclusion=1.0 coverage=0.6667 range_density=1.0 rows/parent=15426.75/25360 child_distinct=4 rank=1 preferred=yes weak=yes
- [S:r:16] T04.c02 -> T07.c03: inclusion=1.0 coverage=0.1 range_density=1.0 rows/parent=15426.75/25360 child_distinct=4 rank=2 preferred=no weak=yes
- [S:r:17] T05.c03 -> T09.c04: inclusion=1.0 coverage=0.6667 range_density=1.0 rows/parent=5000.0/11025 child_distinct=4 rank=1 preferred=yes weak=yes
- [S:r:18] T05.c03 -> T07.c03: inclusion=1.0 coverage=0.1 range_density=1.0 rows/parent=5000.0/11025 child_distinct=4 rank=2 preferred=no weak=yes
- [S:r:19] T05.c04 -> T09.c04: inclusion=1.0 coverage=1.0 range_density=1.0 rows/parent=3333.33/5937 child_distinct=6 rank=1 preferred=yes weak=yes
- [S:r:20] T05.c04 -> T07.c03: inclusion=1.0 coverage=0.15 range_density=1.0 rows/parent=3333.33/5937 child_distinct=6 rank=2 preferred=no weak=yes
- [S:r:21] T05.c05 -> T07.c03: inclusion=1.0 coverage=0.175 range_density=1.0 rows/parent=2857.14/7312 child_distinct=7 rank=1 preferred=yes weak=yes
- [S:r:22] T05.c06 -> T07.c03: inclusion=1.0 coverage=1.0 range_density=1.0 rows/parent=500.0/542 child_distinct=40 rank=1 preferred=yes weak=yes
- [S:r:23] T06.c02 -> T09.c04: inclusion=1.0 coverage=0.5 range_density=1.0 rows/parent=28198.0/45355 child_distinct=3 rank=1 preferred=yes weak=yes
- [S:r:24] T06.c02 -> T07.c03: inclusion=1.0 coverage=0.075 range_density=1.0 rows/parent=28198.0/45355 child_distinct=3 rank=2 preferred=no weak=yes
- [S:r:25] T06.c03 -> T06.c05: inclusion=1.0 coverage=0.4006 range_density=0.0001 rows/parent=1.91/11 child_distinct=33885 rank=1 preferred=yes weak=no
- [S:r:26] T06.c04 -> T05.c02: inclusion=1.0 coverage=1.0 range_density=0.0002 rows/parent=4.23/25 child_distinct=20000 rank=1 preferred=yes weak=no
- [S:r:27] T07.c01 -> T09.c04: inclusion=1.0 coverage=0.8333 range_density=1.0 rows/parent=8.0/11 child_distinct=5 rank=1 preferred=yes weak=yes
- [S:r:28] T07.c01 -> T07.c03: inclusion=1.0 coverage=0.125 range_density=1.0 rows/parent=8.0/11 child_distinct=5 rank=2 preferred=no weak=yes
- [S:r:29] T08.c01 -> T07.c03: inclusion=1.0 coverage=0.2 range_density=1.0 rows/parent=18378.12/20000 child_distinct=8 rank=1 preferred=yes weak=yes
- [S:r:30] T08.c02 -> T05.c02: inclusion=1.0 coverage=1.0 range_density=0.0002 rows/parent=7.35/8 child_distinct=20000 rank=1 preferred=yes weak=no
- [S:r:31] T09.c02 -> T09.c04: inclusion=1.0 coverage=0.8333 range_density=1.0 rows/parent=1.2/2 child_distinct=5 rank=1 preferred=yes weak=yes
- [S:r:32] T09.c02 -> T07.c03: inclusion=1.0 coverage=0.125 range_density=1.0 rows/parent=1.2/2 child_distinct=5 rank=2 preferred=no weak=yes
- [S:r:33] T09.c04 -> T07.c03: inclusion=1.0 coverage=0.15 range_density=1.0 rows/parent=1.0/1 child_distinct=6 rank=1 preferred=no weak=yes child_is_unique

Join paths (2-3 hops) over preferred, non-weak relationships:
- [S:p:1] T05 - T06 - T01
- [S:p:2] T01 - T06 - T05 - T08
- [S:p:3] T01 - T06 - T03
- [S:p:4] T08 - T05 - T03
- [S:p:5] T08 - T05 - T06

Structural ambiguities:
- [S:a:1] multiple_parents at T05.c03: T07.c03, T09.c04
- [S:a:2] multiple_parents at T05.c04: T07.c03, T09.c04
- [S:a:3] multiple_parents at T07.c01: T07.c03, T09.c04
- [S:a:4] multiple_parents at T04.c02: T07.c03, T09.c04
- [S:a:5] multiple_parents at T09.c02: T07.c03, T09.c04
- [S:a:6] multiple_parents at T02.c01: T07.c03, T09.c04
- [S:a:7] multiple_parents at T02.c02: T07.c03, T09.c04
- [S:a:8] multiple_parents at T03.c04: T07.c03, T09.c04
- [S:a:9] multiple_parents at T03.c02: T07.c03, T09.c04
- [S:a:10] multiple_parents at T06.c02: T07.c03, T09.c04
- [S:a:11] low_support at T02.c05: T05.c02: only 4229 distinct child values; may be coincidental
- [S:a:12] weak_overlap at T05.c03: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:13] weak_overlap at T05.c04: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:14] weak_overlap at T05.c06: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:15] weak_overlap at T05.c05: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:16] weak_overlap at T01.c01: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:17] weak_overlap at T08.c01: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:18] weak_overlap at T07.c01: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:19] weak_overlap at T04.c02: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:20] weak_overlap at T09.c04: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:21] weak_overlap at T09.c02: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:22] weak_overlap at T02.c01: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:23] weak_overlap at T02.c02: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:24] weak_overlap at T03.c02: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:25] weak_overlap at T03.c04: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:26] weak_overlap at T06.c02: T07.c03: small overlapping integer ranges; may be coincidental
- [S:a:27] weak_overlap at T05.c03: T09.c04: small overlapping integer ranges; may be coincidental
- [S:a:28] weak_overlap at T05.c04: T09.c04: small overlapping integer ranges; may be coincidental
- [S:a:29] weak_overlap at T07.c01: T09.c04: small overlapping integer ranges; may be coincidental
- [S:a:30] weak_overlap at T04.c02: T09.c04: small overlapping integer ranges; may be coincidental
- [S:a:31] weak_overlap at T09.c02: T09.c04: small overlapping integer ranges; may be coincidental
- [S:a:32] weak_overlap at T02.c01: T09.c04: small overlapping integer ranges; may be coincidental
- [S:a:33] weak_overlap at T02.c02: T09.c04: small overlapping integer ranges; may be coincidental
- [S:a:34] weak_overlap at T03.c02: T09.c04: small overlapping integer ranges; may be coincidental
- [S:a:35] weak_overlap at T03.c04: T09.c04: small overlapping integer ranges; may be coincidental
- [S:a:36] weak_overlap at T06.c02: T09.c04: small overlapping integer ranges; may be coincidental
- [S:a:37] no_candidate_key at T01: no single column is unique and non-null (event log, or composite key?)
- [S:a:38] unmatched_identifier at T01.c03: 33076 distinct integer values matching no key here; possibly a reference to a table not present, or a measure
- [S:a:39] no_candidate_key at T08: no single column is unique and non-null (event log, or composite key?)
- [S:a:40] multiple_time_columns at T02: T02.c03, T02.c06
- [S:a:41] multiple_time_columns at T03: T03.c07, T03.c01

## Outcome-driven analysis (predictive associations; NOT causal, NOT semantic proof)
Label rows: {'train': 12136, 'val': 3469, 'test': 3749} (time-based splits: train, then validation, then test). Positive rate: {'train': 0.185, 'val': 0.184, 'test': 0.186}.
Features were built only from candidate relationships marked preferred and non-weak, using only rows dated before each cutoff.
- [P:m:1] Model performance (AUROC; 0.5 = chance): gradient_boosting: val=0.715 test=0.740; logistic_regression: val=0.715 test=0.746; selected on validation: logistic_regression
- [P:m:2] Baseline: best single past-activity count (f034) test AUROC=0.570

Relationship paths ranked by summed permutation importance (validation):
- [P:path:1] importance=0.2426 path: T06.c04 -> T05.c02 then T01.c02 -> T06.c05 features=['f042', 'f043', 'f044', 'f045', 'f046', 'f047', 'f048', 'f049', 'f050', 'f051', 'f052', 'f053', 'f054', 'f055', 'f056', 'f057', 'f058', 'f059']
- [P:path:2] importance=0.1416 path: T06.c04 -> T05.c02 then T03.c03 -> T06.c05 features=['f060', 'f061', 'f062', 'f063', 'f064', 'f065', 'f066', 'f067', 'f068', 'f069', 'f070', 'f071']
- [P:path:3] importance=0.0503 path: T03.c05 -> T05.c02 features=['f018', 'f019', 'f020', 'f021', 'f022', 'f023', 'f024', 'f025', 'f026', 'f027', 'f028', 'f029', 'f030', 'f031', 'f032']
- [P:path:4] importance=0.0116 path: T06.c04 -> T05.c02 features=['f034', 'f035', 'f036', 'f037', 'f038', 'f039', 'f040', 'f041']
- [P:path:5] importance=0.0061 path: (target table itself) features=['f000', 'f001', 'f002', 'f003']
- [P:path:6] importance=0.0018 path: T08.c02 -> T05.c02 features=['f004', 'f005', 'f006', 'f007', 'f008', 'f009', 'f010', 'f011', 'f012', 'f013', 'f014', 'f015', 'f016', 'f017']
- [P:path:7] importance=0.0009 path: T03.c05 -> T05.c02 then T03.c03 -> T06.c05 features=['f033']

Features (agg over the path; window in days before cutoff; univariate AUROC on train/val; direction; stability of direction across training cutoffs; BH-adjusted q-value; permutation importance):
- [P:f:f042] count(T01 rows) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.707 val=0.702 higher_in_positive stable=yes q=9.6e-206 perm_imp=0.2084 coverage=100%
- [P:f:f060] count(T03 rows) window=all via T06.c04 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.436 val=0.464 lower_in_positive stable=yes q=9.6e-28 perm_imp=0.0806 coverage=100%
- [P:f:f032] count_distinct(T03.c03) window=all via T03.c05 -> T05.c02: auroc train=0.446 val=0.471 lower_in_positive stable=yes q=2.6e-21 perm_imp=0.0309 coverage=100%
- [P:f:f063] count_where(T03 rows where T03.c02 = 1) window=all via T06.c04 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.433 val=0.452 lower_in_positive stable=yes q=1.9e-44 perm_imp=0.0162 coverage=100%
- [P:f:f055] count_where(T01 rows where T01.c01 = 11) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.426 val=0.424 lower_in_positive stable=yes q=1.5e-34 perm_imp=0.0124 coverage=100%
- [P:f:f048] count_where(T01 rows where T01.c01 = 4) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.662 val=0.659 higher_in_positive stable=yes q=1.1e-167 perm_imp=0.0114 coverage=100%
- [P:f:f062] mean(T03.c04) window=all via T06.c04 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.506 val=0.506 higher_in_positive stable=no q=0.12 perm_imp=0.0088 coverage=25%
- [P:f:f031] count_where(T03 rows where T03.c04 = 5) window=all via T03.c05 -> T05.c02: auroc train=0.487 val=0.489 lower_in_positive stable=yes q=5.7e-05 perm_imp=0.0084 coverage=100%
- [P:f:f061] mean(T03.c02) window=all via T06.c04 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.551 val=0.548 higher_in_positive stable=yes q=7.7e-18 perm_imp=0.0080 coverage=38%
- [P:f:f027] count_where(T03 rows where T03.c04 = 1) window=all via T03.c05 -> T05.c02: auroc train=0.482 val=0.494 lower_in_positive stable=yes q=1.4e-08 perm_imp=0.0065 coverage=100%
- [P:f:f036] days_since_last(T06 rows) window=all via T06.c04 -> T05.c02: auroc train=0.440 val=0.439 lower_in_positive stable=yes q=2.2e-64 perm_imp=0.0058 coverage=100%
- [P:f:f070] count_where(T03 rows where T03.c04 = 4) window=all via T06.c04 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.489 val=0.500 lower_in_positive stable=yes q=0.00012 perm_imp=0.0057 coverage=100%
- [P:f:f066] count_where(T03 rows where T03.c02 = 4) window=all via T06.c04 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.493 val=0.507 lower_in_positive stable=yes q=0.024 perm_imp=0.0054 coverage=100%
- [P:f:f065] count_where(T03 rows where T03.c02 = 3) window=all via T06.c04 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.501 val=0.498 higher_in_positive stable=no q=0.94 perm_imp=0.0050 coverage=100%
- [P:f:f071] count_where(T03 rows where T03.c04 = 5) window=all via T06.c04 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.491 val=0.492 lower_in_positive stable=no q=0.0017 perm_imp=0.0043 coverage=100%
- [P:f:f064] count_where(T03 rows where T03.c02 = 2) window=all via T06.c04 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.499 val=0.502 lower_in_positive stable=no q=0.86 perm_imp=0.0040 coverage=100%
- [P:f:f051] count_where(T01 rows where T01.c01 = 7) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.601 val=0.598 higher_in_positive stable=yes q=1e-105 perm_imp=0.0036 coverage=100%
- [P:f:f001] value(T05.c04) window=all via (target table itself): auroc train=0.474 val=0.467 lower_in_positive stable=no q=0.00012 perm_imp=0.0030 coverage=100%
- [P:f:f000] value(T05.c03) window=all via (target table itself): auroc train=0.529 val=0.544 higher_in_positive stable=yes q=2.1e-06 perm_imp=0.0029 coverage=100%
- [P:f:f069] count_where(T03 rows where T03.c04 = 3) window=all via T06.c04 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.488 val=0.493 lower_in_positive stable=yes q=1.5e-05 perm_imp=0.0028 coverage=100%
- [P:f:f045] count_where(T01 rows where T01.c01 = 1) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.607 val=0.601 higher_in_positive stable=yes q=4.4e-58 perm_imp=0.0025 coverage=100%
- [P:f:f037] mean(T06.c02) window=all via T06.c04 -> T05.c02: auroc train=0.560 val=0.562 higher_in_positive stable=yes q=4e-65 perm_imp=0.0022 coverage=100%
- [P:f:f024] count_where(T03 rows where T03.c02 = 2) window=all via T03.c05 -> T05.c02: auroc train=0.499 val=0.503 lower_in_positive stable=no q=0.86 perm_imp=0.0020 coverage=100%
- [P:f:f008] mean(T08.c03) window=all via T08.c02 -> T05.c02: auroc train=0.568 val=0.573 higher_in_positive stable=yes q=2.2e-26 perm_imp=0.0018 coverage=100%
- [P:f:f049] count_where(T01 rows where T01.c01 = 5) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.612 val=0.608 higher_in_positive stable=yes q=2.1e-63 perm_imp=0.0017 coverage=100%
- [P:f:f041] count_distinct(T06.c03) window=all via T06.c04 -> T05.c02: auroc train=0.560 val=0.561 higher_in_positive stable=yes q=1.5e-64 perm_imp=0.0012 coverage=100%
- [P:f:f028] count_where(T03 rows where T03.c04 = 2) window=all via T03.c05 -> T05.c02: auroc train=0.485 val=0.488 lower_in_positive stable=yes q=8.3e-07 perm_imp=0.0010 coverage=100%
- [P:f:f033] mean(T06.c02) window=all via T03.c05 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.508 val=0.515 higher_in_positive stable=yes q=6e-17 perm_imp=0.0009 coverage=38%
- [P:f:f030] count_where(T03 rows where T03.c04 = 4) window=all via T03.c05 -> T05.c02: auroc train=0.485 val=0.494 lower_in_positive stable=yes q=5.1e-06 perm_imp=0.0009 coverage=100%
- [P:f:f043] mean(T01.c01) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.448 val=0.448 lower_in_positive stable=yes q=1.9e-14 perm_imp=0.0009 coverage=100%
- [P:f:f039] count_where(T06 rows where T06.c02 = 2) window=all via T06.c04 -> T05.c02: auroc train=0.546 val=0.546 higher_in_positive stable=yes q=2.8e-48 perm_imp=0.0008 coverage=100%
- [P:f:f068] count_where(T03 rows where T03.c04 = 2) window=all via T06.c04 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.486 val=0.490 lower_in_positive stable=yes q=1.5e-06 perm_imp=0.0008 coverage=100%
- [P:f:f025] count_where(T03 rows where T03.c02 = 3) window=all via T03.c05 -> T05.c02: auroc train=0.500 val=0.495 higher_in_positive stable=no q=1 perm_imp=0.0007 coverage=100%
- [P:f:f034] count(T06 rows) window=all via T06.c04 -> T05.c02: auroc train=0.560 val=0.562 higher_in_positive stable=yes q=3.2e-65 perm_imp=0.0006 coverage=100%
- [P:f:f035] count(T06 rows) window=16 via T06.c04 -> T05.c02: auroc train=0.560 val=0.562 higher_in_positive stable=yes q=3.2e-65 perm_imp=0.0006 coverage=100%
- [P:f:f046] count_where(T01 rows where T01.c01 = 2) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.599 val=0.597 higher_in_positive stable=yes q=2.9e-51 perm_imp=0.0005 coverage=100%
- [P:f:f040] count_where(T06 rows where T06.c02 = 3) window=all via T06.c04 -> T05.c02: auroc train=0.528 val=0.536 higher_in_positive stable=yes q=7.5e-39 perm_imp=0.0005 coverage=100%
- [P:f:f054] count_where(T01 rows where T01.c01 = 10) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.584 val=0.590 higher_in_positive stable=yes q=1.1e-38 perm_imp=0.0003 coverage=100%
- [P:f:f056] count_where(T01 rows where T01.c01 = 12) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.574 val=0.564 higher_in_positive stable=yes q=1.4e-31 perm_imp=0.0003 coverage=100%
- [P:f:f058] count_where(T01 rows where T01.c01 = 14) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.544 val=0.557 higher_in_positive stable=yes q=1.2e-13 perm_imp=0.0003 coverage=100%
- [P:f:f047] count_where(T01 rows where T01.c01 = 3) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.595 val=0.605 higher_in_positive stable=yes q=9.9e-48 perm_imp=0.0002 coverage=100%
- [P:f:f003] value(T05.c05) window=all via (target table itself): auroc train=0.528 val=0.535 higher_in_positive stable=no q=3.7e-05 perm_imp=0.0001 coverage=100%
- [P:f:f057] count_where(T01 rows where T01.c01 = 13) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.568 val=0.576 higher_in_positive stable=yes q=9.1e-27 perm_imp=0.0001 coverage=100%
- [P:f:f021] mean(T03.c02) window=all via T03.c05 -> T05.c02: auroc train=0.553 val=0.549 higher_in_positive stable=yes q=4.7e-18 perm_imp=0.0000 coverage=44%
- [P:f:f002] value(T05.c06) window=all via (target table itself): auroc train=0.504 val=0.495 higher_in_positive stable=no q=0.68 perm_imp=0.0000 coverage=100%
- [P:f:f004] count(T08 rows) window=all via T08.c02 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f005] count(T08 rows) window=16 via T08.c02 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f006] days_since_last(T08 rows) window=all via T08.c02 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f007] mean(T08.c01) window=all via T08.c02 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f010] count_where(T08 rows where T08.c01 = 1) window=all via T08.c02 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f011] count_where(T08 rows where T08.c01 = 2) window=all via T08.c02 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f012] count_where(T08 rows where T08.c01 = 3) window=all via T08.c02 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f013] count_where(T08 rows where T08.c01 = 4) window=all via T08.c02 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f014] count_where(T08 rows where T08.c01 = 5) window=all via T08.c02 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f015] count_where(T08 rows where T08.c01 = 6) window=all via T08.c02 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f016] count_where(T08 rows where T08.c01 = 7) window=all via T08.c02 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f017] count_where(T08 rows where T08.c01 = 8) window=all via T08.c02 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f038] count_where(T06 rows where T06.c02 = 1) window=all via T06.c04 -> T05.c02: auroc train=0.500 val=0.500 lower_in_positive stable=no q=1 perm_imp=0.0000 coverage=100%
- [P:f:f053] count_where(T01 rows where T01.c01 = 9) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.599 val=0.589 higher_in_positive stable=yes q=3.6e-51 perm_imp=-0.0000 coverage=100%
- [P:f:f026] count_where(T03 rows where T03.c02 = 4) window=all via T03.c05 -> T05.c02: auroc train=0.489 val=0.503 lower_in_positive stable=no q=0.0028 perm_imp=-0.0000 coverage=100%
- [P:f:f023] count_where(T03 rows where T03.c02 = 1) window=all via T03.c05 -> T05.c02: auroc train=0.423 val=0.441 lower_in_positive stable=yes q=2.1e-51 perm_imp=-0.0000 coverage=100%
- [P:f:f050] count_where(T01 rows where T01.c01 = 6) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.586 val=0.581 higher_in_positive stable=yes q=6.2e-40 perm_imp=-0.0002 coverage=100%
- [P:f:f067] count_where(T03 rows where T03.c04 = 1) window=all via T06.c04 -> T05.c02 then T03.c03 -> T06.c05: auroc train=0.486 val=0.493 lower_in_positive stable=yes q=3.8e-07 perm_imp=-0.0004 coverage=100%
- [P:f:f059] count_where(T01 rows where T01.c01 = 15) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.560 val=0.562 higher_in_positive stable=yes q=8.8e-24 perm_imp=-0.0004 coverage=100%
- [P:f:f029] count_where(T03 rows where T03.c04 = 3) window=all via T03.c05 -> T05.c02: auroc train=0.484 val=0.493 lower_in_positive stable=yes q=3.4e-07 perm_imp=-0.0004 coverage=100%
- [P:f:f022] mean(T03.c04) window=all via T03.c05 -> T05.c02: auroc train=0.505 val=0.500 higher_in_positive stable=no q=0.2 perm_imp=-0.0006 coverage=30%
- [P:f:f044] mean(T01.c03) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.491 val=0.469 lower_in_positive stable=no q=0.23 perm_imp=-0.0007 coverage=100%
- [P:f:f018] count(T03 rows) window=all via T03.c05 -> T05.c02: auroc train=0.426 val=0.454 lower_in_positive stable=yes q=2.4e-34 perm_imp=-0.0009 coverage=100%
- [P:f:f019] count(T03 rows) window=16 via T03.c05 -> T05.c02: auroc train=0.426 val=0.454 lower_in_positive stable=yes q=2.4e-34 perm_imp=-0.0009 coverage=100%
- [P:f:f020] days_since_last(T03 rows) window=all via T03.c05 -> T05.c02: auroc train=0.515 val=0.495 higher_in_positive stable=no q=0.0006 perm_imp=-0.0009 coverage=44%
- [P:f:f009] mean(T08.c05) window=all via T08.c02 -> T05.c02: auroc train=0.521 val=0.539 higher_in_positive stable=yes q=6.8e-05 perm_imp=-0.0014 coverage=100%
- [P:f:f052] count_where(T01 rows where T01.c01 = 8) window=all via T06.c04 -> T05.c02 then T01.c02 -> T06.c05: auroc train=0.605 val=0.626 higher_in_positive stable=yes q=5.8e-57 perm_imp=-0.0014 coverage=100%