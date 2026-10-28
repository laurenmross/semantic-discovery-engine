## Business outcome of interest (supplied by the business)
- Conversion: whether the entity identified by T05.c02 reaches the business's conversion milestone in the 16 days after the cutoff timestamp (entities that already reached it are excluded).
- Outcome entity: T05.c02

## Schema (tables, columns, types, row counts, example values)
### Table T01  [S:t:T01]  rows=13577665
- c01: BIGINT; examples ['9', '10', '14']  [S:c:T01.c01]
- c02: BIGINT; examples ['911330994', '959645336', '919409939']  [S:c:T01.c02]
- c03: DOUBLE; examples ['2742.0', '5660.0', '4225.0']  [S:c:T01.c03]
- c04: TIMESTAMP_NS; examples ['2025-07-01 03:49:42', '2025-07-02 05:12:41', '2025-07-02 08:07:25']  [S:c:T01.c04]

### Table T02  [S:t:T02]  rows=4229
- c01: BIGINT; examples ['2', '4', '5']  [S:c:T02.c01]
- c02: BIGINT; examples ['1', '2', '3']  [S:c:T02.c02]
- c03: TIMESTAMP_NS; examples ['2025-07-07 07:50:35.314570834', '2025-07-13 12:14:29.685042654', '2025-07-04 11:06:39.74655652']  [S:c:T02.c03]
- c04: BIGINT; examples ['9278205', '4945591', '1378006']  [S:c:T02.c04]
- c05: BIGINT; examples ['22594933', '94503550', '61507448']  [S:c:T02.c05]
- c06: TIMESTAMP_NS; examples ['2025-10-04 20:52:54.139537056', '2025-08-25 01:52:13.945263503', '2025-12-23 19:14:28.324253171']  [S:c:T02.c06]

### Table T03  [S:t:T03]  rows=76345
- c01: TIMESTAMP_NS; examples ['2025-07-05 03:23:25', '2025-07-18 03:32:31', '2025-07-17 18:09:44']  [S:c:T03.c01]
- c02: BIGINT; examples ['4', '2', '1']  [S:c:T03.c02]
- c03: BIGINT; examples ['911330994', '959645336', '372150613']  [S:c:T03.c03]
- c04: BIGINT; examples ['1', '4', '2']  [S:c:T03.c04]
- c05: BIGINT; examples ['75091266', '22594933', '24071260']  [S:c:T03.c05]
- c06: BIGINT; examples ['5763920', '9542057', '4456299']  [S:c:T03.c06]
- c07: TIMESTAMP_NS; examples ['2025-07-04 15:11:35', '2025-07-13 21:22:52', '2025-07-15 17:18:16']  [S:c:T03.c07]

### Table T04  [S:t:T04]  rows=61707
- c01: BIGINT; examples ['9278205', '4945591', '1378006']  [S:c:T04.c01]
- c02: BIGINT; examples ['1', '3', '4']  [S:c:T04.c02]
- c03: DOUBLE; examples ['7900.0', '632.0', '-7588.0']  [S:c:T04.c03]
- c04: TIMESTAMP_NS; examples ['2025-07-07 07:50:35.314570834', '2025-08-06 07:50:35.314570834', '2025-09-05 07:50:35.314570834']  [S:c:T04.c04]
- c05: BIGINT; examples ['63411137', '96127998', '37839780']  [S:c:T04.c05]

### Table T05  [S:t:T05]  rows=20000
- c01: TIMESTAMP_NS; examples ['2025-07-01 00:17:08.458175719', '2025-07-01 00:32:00.030784175', '2025-07-01 01:15:00.620040557']  [S:c:T05.c01]
- c02: BIGINT; examples ['75091266', '22594933', '24071260']  [S:c:T05.c02]
- c03: BIGINT; examples ['2', '1', '3']  [S:c:T05.c03]
- c04: BIGINT; examples ['1', '5', '3']  [S:c:T05.c04]
- c05: BIGINT; examples ['2', '1', '5']  [S:c:T05.c05]
- c06: BIGINT; examples ['1', '22', '16']  [S:c:T05.c06]

### Table T06  [S:t:T06]  rows=84594
- c01: TIMESTAMP_NS; examples ['2025-07-01 00:17:08', '2025-07-01 00:32:00', '2025-08-14 16:12:29']  [S:c:T06.c01]
- c02: BIGINT; examples ['1', '2', '3']  [S:c:T06.c02]
- c03: BIGINT; examples ['959645336', '828584695', '369477489']  [S:c:T06.c03]
- c04: BIGINT; examples ['75091266', '22594933', '24071260']  [S:c:T06.c04]
- c05: BIGINT; examples ['911330994', '959645336', '919409939']  [S:c:T06.c05]

### Table T07  [S:t:T07]  rows=40
- c01: BIGINT; examples ['4', '5', '2']  [S:c:T07.c01]
- c02: BIGINT; examples ['2', '8', '-6']  [S:c:T07.c02]
- c03: BIGINT; examples ['1', '2', '3']  [S:c:T07.c03]

### Table T08  [S:t:T08]  rows=147025
- c01: BIGINT; examples ['1', '2', '3']  [S:c:T08.c01]
- c02: BIGINT; examples ['75091266', '22594933', '24071260']  [S:c:T08.c02]
- c03: BIGINT; examples ['1', '0']  [S:c:T08.c03]
- c04: TIMESTAMP_NS; examples ['2025-07-01 09:17:08', '2025-07-02 09:17:08', '2025-07-04 09:17:08']  [S:c:T08.c04]
- c05: BIGINT; examples ['0', '1']  [S:c:T08.c05]

### Table T09  [S:t:T09]  rows=6
- c01: DOUBLE; examples ['29.0', '79.0', '149.0']  [S:c:T09.c01]
- c02: BIGINT; examples ['1', '2', '3']  [S:c:T09.c02]
- c03: BIGINT; examples ['3', '10', '25']  [S:c:T09.c03]
- c04: BIGINT; examples ['1', '2', '3']  [S:c:T09.c04]
