# NBS data platform API

The National Bureau of Statistics moved its database to a new platform in 2026
(`https://data.stats.gov.cn/dg/website/page.html`). The old `easyquery.htm`
interface now returns 403. NBS doesn't document the new platform's API; what
follows was read from the platform's own JavaScript and checked against live
responses in September 2026.

Base URL: `https://data.stats.gov.cn/dg/website/publicrelease/web/external`

Every response is JSON shaped like `{"success": true, "state": 20000, "message": "成功", "data": ...}`.
Unknown IDs don't fail: they come back as `success: true` with empty `data`.

## Endpoints

| Call | Parameters | Returns |
|---|---|---|
| `GET new/queryIndexTreeAsync` | `code` (1 monthly, 2 quarterly, 3 annual); `pid` (parent node id, omit for the root) | Child nodes: `_id`, `name`, `isLeaf`, `sdate`/`edate` years for split catalogs |
| `GET new/queryIndicatorsByCid` | `cid` (a leaf catalog id) | `data.list`: indicators with `_id`, `i_showname`, `du_name` (unit), `num_accuracy_value` (decimals) |
| `GET new/queryDtByCid` | `cid`, `rootId` | Latest period, e.g. `{"dt_all": "202608MM", "dt_name": "2026年8月"}` |
| `GET query` | `search` (keyword), `code` (1/2/3 or empty), `pagenum`, `pageSize` | `data.data`: matches with `indic_id`, `cid`, `show_name`, `type_value`, `dt`, `value`, `da` (region; `000000000000` is national) |
| `POST stream/esData` | JSON body, below | Rows by period, each with `values` |

The root of each tree holds a single node (`月度数据`, `季度数据`, `年度数据`) whose
children are the top-level categories.

## Fetching data

```json
{
  "cid": "<catalog id>",
  "indicatorIds": ["<indicator id>"],
  "daCatalogId": "",
  "das": [{"text": "全国", "value": "000000000000"}],
  "showType": 1,
  "dt": "202401MM-202608MM",
  "dts": ["202401MM-202608MM"]
}
```

- Period codes: `202608MM` (month), `202602SS` (2026 Q2), `2025YY` (year).
  A malformed `dt` gives HTTP 500.
- `das` must name the region. Without it the response is empty. The value
  `000000000000` means national.
- The response has one row per period in the range, newest first. An
  unpublished period has `"value": ""` or no `values` at all.
- Each value carries `_id` and `i_showname`. The script checks both against
  the curated entry, because the server returns an indicator's data even when
  `cid` is wrong.

## Adding or repairing a curated series

1. Find the indicator with `search`, or with `browse` from the top categories.
   Note the catalog id, indicator id and the exact `i_showname`.
2. Add an entry to `SERIES` in `scripts/nbs_macro.py`: `label` is the
   `i_showname` with runs of whitespace collapsed to one space; set
   `"index": True` if NBS publishes it as an index with last year = 100.
3. For a series split across catalogs by base period (CPI), list every catalog
   newest first with the first year it covers; the oldest gets `None`. When NBS
   rebases CPI again (next in 2031), add the new catalog at the top.
4. Run `python3 scripts/nbs_macro.py get <name> --start <early period>` and
   check the joins at each catalog boundary.
