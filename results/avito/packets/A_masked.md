## Business outcome of interest (supplied by the business)
- Engagement: whether the entity identified by T01.c04 has more than one qualifying interaction in the 4 days after the cutoff timestamp.
- Outcome entity: T01.c04

## Schema (tables, columns, types, row counts, example values)
### Table T01  [S:t:T01]  rows=98250
- c01: DOUBLE; examples ['54898.0', '15248.0', '12555.0']  [S:c:T01.c01]
- c02: DOUBLE; examples ['2014.0', '4093.0', '2019.0']  [S:c:T01.c02]
- c03: DOUBLE; examples ['85.0', '25.0', '9.0']  [S:c:T01.c03]
- c04: BIGINT; examples ['0', '1', '2']  [S:c:T01.c04]
- c05: DOUBLE; examples ['20.0', '35.0', '30.0']  [S:c:T01.c05]

### Table T02  [S:t:T02]  rows=6454562
- c01: BIGINT; examples ['2270750', '4865813', '4635684']  [S:c:T02.c01]
- c02: DOUBLE; examples ['711105.0', '1462925.0', '964705.0']  [S:c:T02.c02]
- c03: TIMESTAMP_NS; examples ['2015-05-17 15:19:02', '2015-05-17 15:42:14', '2015-05-17 15:45:06']  [S:c:T02.c03]
- c04: BIGINT; examples ['76240', '88796', '77228']  [S:c:T02.c04]

### Table T03  [S:t:T03]  rows=3512
- c01: DOUBLE; examples ['2.0', '3.0', '1.0']  [S:c:T03.c01]
- c02: DOUBLE; examples ['70.0', '56.0', '64.0']  [S:c:T03.c02]
- c03: BIGINT; examples ['0', '1', '2']  [S:c:T03.c03]
- c04: DOUBLE; examples ['3024.0', '2791.0', '1139.0']  [S:c:T03.c04]

### Table T04  [S:t:T04]  rows=2579289
- c01: BIGINT; examples ['34', '22', '60']  [S:c:T04.c01]
- c02: TIMESTAMP_NS; examples ['2015-04-25 00:00:01', '2015-04-25 00:00:02', '2015-04-25 00:00:03']  [S:c:T04.c02]
- c03: VARCHAR; examples ['<text, ~10 chars, Latin/other script>']  [S:c:T04.c03]
- c04: BIGINT; examples ['497', '334', '375']  [S:c:T04.c04]
- c05: BIGINT; examples ['2139', '1477', '68959']  [S:c:T04.c05]
- c06: DOUBLE; examples ['837134.0', '2187370.0', '2089629.0']  [S:c:T04.c06]
- c07: DOUBLE; examples ['1.0', '0.0']  [S:c:T04.c07]
- c08: BIGINT; examples ['0', '1', '2']  [S:c:T04.c08]

### Table T05  [S:t:T05]  rows=5960558
- c01: BIGINT; examples ['497', '335', '341']  [S:c:T05.c01]
- c02: BIGINT; examples ['22', '43', '47']  [S:c:T05.c02]
- c03: BIGINT; examples ['0', '1', '2']  [S:c:T05.c03]
- c04: DOUBLE; examples ['400.0', '6864.0', '7800000.0']  [S:c:T05.c04]
- c05: DOUBLE; examples ['0.0', '1.0']  [S:c:T05.c05]
- c06: VARCHAR; examples ['<text, ~19 chars, Cyrillic script>']  [S:c:T05.c06]

### Table T06  [S:t:T06]  rows=302974
- c01: DOUBLE; examples ['1629303.0', '109220.0', '1462925.0']  [S:c:T06.c01]
- c02: TIMESTAMP_NS; examples ['2015-04-25 11:50:35', '2015-04-25 11:51:14', '2015-04-25 12:07:43']  [S:c:T06.c02]
- c03: BIGINT; examples ['1938326', '3917327', '3806832']  [S:c:T06.c03]
- c04: BIGINT; examples ['38950', '18761', '88796']  [S:c:T06.c04]

### Table T07  [S:t:T07]  rows=68
- c01: BIGINT; examples ['45', '5', '25']  [S:c:T07.c01]
- c02: BIGINT; examples ['0', '1', '2']  [S:c:T07.c02]
- c03: BIGINT; examples ['1', '2', '3']  [S:c:T07.c03]
- c04: BIGINT; examples ['10', '9', '12']  [S:c:T07.c04]

### Table T08  [S:t:T08]  rows=9254702
- c01: BIGINT; examples ['806173', '4316980', '2059012']  [S:c:T08.c01]
- c02: DOUBLE; examples ['0.0', '1.0']  [S:c:T08.c02]
- c03: DOUBLE; examples ['1.0', '3.0', '2.0']  [S:c:T08.c03]
- c04: DOUBLE; examples ['8.0', '2.0', '7.0']  [S:c:T08.c04]
- c05: TIMESTAMP_NS; examples ['2015-04-30 20:57:06', '2015-04-26 23:19:37', '2015-05-12 18:11:59']  [S:c:T08.c05]
- c06: BIGINT; examples ['541363', '162315', '1804098']  [S:c:T08.c06]
- c07: DOUBLE; examples ['0.005902', '0.049664', '0.002413']  [S:c:T08.c07]
