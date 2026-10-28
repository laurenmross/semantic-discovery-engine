## Business outcome of interest (supplied by the business)
- Trial-to-paid conversion: whether the account starts a paid subscription in the 16 days after the cutoff (cutoff = day 5 of the free trial; accounts already converted by then are excluded).
- Outcome entity: ACCT_MSTR.acct_key

## Schema (tables, columns, types, row counts, example values)
### Table ACCT_MSTR  [S:t:ACCT_MSTR]  rows=20000
- seg_cd: BIGINT; examples ['2', '1', '3']  [S:c:ACCT_MSTR.seg_cd]
- crt_ts: TIMESTAMP_NS; examples ['2025-07-01 00:17:08.458175719', '2025-07-01 00:32:00.030784175', '2025-07-01 01:15:00.620040557']  [S:c:ACCT_MSTR.crt_ts]
- acct_key: BIGINT; examples ['75091266', '22594933', '24071260']  [S:c:ACCT_MSTR.acct_key]
- src_cd: BIGINT; examples ['1', '5', '3']  [S:c:ACCT_MSTR.src_cd]
- geo_ref: BIGINT; examples ['1', '22', '16']  [S:c:ACCT_MSTR.geo_ref]
- emp_band: BIGINT; examples ['2', '1', '5']  [S:c:ACCT_MSTR.emp_band]

### Table EVT_STRM_01  [S:t:EVT_STRM_01]  rows=13577665
- usr_key: BIGINT; examples ['911330994', '959645336', '919409939']  [S:c:EVT_STRM_01.usr_key]
- evt_cd: BIGINT; examples ['9', '10', '14']  [S:c:EVT_STRM_01.evt_cd]
- evt_ts: TIMESTAMP_NS; examples ['2025-07-01 03:49:42', '2025-07-02 05:12:41', '2025-07-02 08:07:25']  [S:c:EVT_STRM_01.evt_ts]
- dur_ms: DOUBLE; examples ['2742.0', '5660.0', '4225.0']  [S:c:EVT_STRM_01.dur_ms]

### Table EVT_STRM_02  [S:t:EVT_STRM_02]  rows=147025
- acct_key: BIGINT; examples ['75091266', '22594933', '24071260']  [S:c:EVT_STRM_02.acct_key]
- tmpl_cd: BIGINT; examples ['1', '2', '3']  [S:c:EVT_STRM_02.tmpl_cd]
- snd_ts: TIMESTAMP_NS; examples ['2025-07-01 09:17:08', '2025-07-02 09:17:08', '2025-07-04 09:17:08']  [S:c:EVT_STRM_02.snd_ts]
- opn_flg: BIGINT; examples ['1', '0']  [S:c:EVT_STRM_02.opn_flg]
- clk_flg: BIGINT; examples ['0', '1']  [S:c:EVT_STRM_02.clk_flg]

### Table GEO_REF  [S:t:GEO_REF]  rows=40
- geo_id: BIGINT; examples ['1', '2', '3']  [S:c:GEO_REF.geo_id]
- rgn_cd: BIGINT; examples ['4', '5', '2']  [S:c:GEO_REF.rgn_cd]
- tz_off: BIGINT; examples ['2', '8', '-6']  [S:c:GEO_REF.tz_off]

### Table INV_LN  [S:t:INV_LN]  rows=61707
- inv_ln_key: BIGINT; examples ['63411137', '96127998', '37839780']  [S:c:INV_LN.inv_ln_key]
- sub_key: BIGINT; examples ['9278205', '4945591', '1378006']  [S:c:INV_LN.sub_key]
- ln_typ: BIGINT; examples ['1', '3', '4']  [S:c:INV_LN.ln_typ]
- amt: DOUBLE; examples ['7900.0', '632.0', '-7588.0']  [S:c:INV_LN.amt]
- bill_ts: TIMESTAMP_NS; examples ['2025-07-07 07:50:35.314570834', '2025-08-06 07:50:35.314570834', '2025-09-05 07:50:35.314570834']  [S:c:INV_LN.bill_ts]

### Table PLN_REF  [S:t:PLN_REF]  rows=6
- pln_id: BIGINT; examples ['1', '2', '3']  [S:c:PLN_REF.pln_id]
- list_px: DOUBLE; examples ['29.0', '79.0', '149.0']  [S:c:PLN_REF.list_px]
- seat_cap: BIGINT; examples ['3', '10', '25']  [S:c:PLN_REF.seat_cap]
- tier_rank: BIGINT; examples ['1', '2', '3']  [S:c:PLN_REF.tier_rank]

### Table SUB_HDR  [S:t:SUB_HDR]  rows=4229
- sub_key: BIGINT; examples ['9278205', '4945591', '1378006']  [S:c:SUB_HDR.sub_key]
- acct_key: BIGINT; examples ['22594933', '94503550', '61507448']  [S:c:SUB_HDR.acct_key]
- pln_id: BIGINT; examples ['2', '4', '5']  [S:c:SUB_HDR.pln_id]
- st_ts: TIMESTAMP_NS; examples ['2025-07-07 07:50:35.314570834', '2025-07-13 12:14:29.685042654', '2025-07-04 11:06:39.74655652']  [S:c:SUB_HDR.st_ts]
- end_ts: TIMESTAMP_NS; examples ['2025-10-04 20:52:54.139537056', '2025-08-25 01:52:13.945263503', '2025-12-23 19:14:28.324253171']  [S:c:SUB_HDR.end_ts]
- stat_cd: BIGINT; examples ['1', '2', '3']  [S:c:SUB_HDR.stat_cd]

### Table TKT_LOG  [S:t:TKT_LOG]  rows=76345
- tkt_no: BIGINT; examples ['5763920', '9542057', '4456299']  [S:c:TKT_LOG.tkt_no]
- acct_key: BIGINT; examples ['75091266', '22594933', '24071260']  [S:c:TKT_LOG.acct_key]
- usr_key: BIGINT; examples ['911330994', '959645336', '372150613']  [S:c:TKT_LOG.usr_key]
- opn_ts: TIMESTAMP_NS; examples ['2025-07-04 15:11:35', '2025-07-13 21:22:52', '2025-07-15 17:18:16']  [S:c:TKT_LOG.opn_ts]
- sev: BIGINT; examples ['4', '2', '1']  [S:c:TKT_LOG.sev]
- csat: BIGINT; examples ['1', '4', '2']  [S:c:TKT_LOG.csat]
- cls_ts: TIMESTAMP_NS; examples ['2025-07-05 03:23:25', '2025-07-18 03:32:31', '2025-07-17 18:09:44']  [S:c:TKT_LOG.cls_ts]

### Table USR_XREF  [S:t:USR_XREF]  rows=84594
- usr_key: BIGINT; examples ['911330994', '959645336', '919409939']  [S:c:USR_XREF.usr_key]
- acct_key: BIGINT; examples ['75091266', '22594933', '24071260']  [S:c:USR_XREF.acct_key]
- role_cd: BIGINT; examples ['1', '2', '3']  [S:c:USR_XREF.role_cd]
- inv_by: BIGINT; examples ['959645336', '828584695', '369477489']  [S:c:USR_XREF.inv_by]
- crt_ts: TIMESTAMP_NS; examples ['2025-07-01 00:17:08', '2025-07-01 00:32:00', '2025-08-14 16:12:29']  [S:c:USR_XREF.crt_ts]
