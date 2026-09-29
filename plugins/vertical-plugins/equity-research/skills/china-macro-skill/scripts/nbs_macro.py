#!/usr/bin/env python3
"""
Fetch Chinese national macro data from the National Bureau of Statistics (NBS).

Talks to the JSON API behind the NBS data platform (data.stats.gov.cn/dg/),
which replaced the old easyquery.htm interface in 2026. The API is
undocumented, so curated series are checked against the name NBS gives them
and fail loudly if the database is reorganised. Standard library only.

Usage:
  python scripts/nbs_macro.py list
  python scripts/nbs_macro.py latest [SERIES ...]
  python scripts/nbs_macro.py get SERIES [SERIES ...] [--start 2024-01] [--end 2026-08] [--format csv|json]
  python scripts/nbs_macro.py search KEYWORD [--freq M|Q|Y]
  python scripts/nbs_macro.py browse [--freq M|Q|Y] [--node ID]
  python scripts/nbs_macro.py fetch --catalog ID --indicator ID --freq M|Q|Y [--start ...] [--end ...]

Periods are written 2026-08 (monthly), 2026Q2 (quarterly) or 2025 (annual).
Exit status: 0 on success, 1 if any series failed (reason on stderr), 2 for bad arguments.
"""
import argparse
import csv
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone

BASE_URL = "https://data.stats.gov.cn/dg/website/publicrelease/web/external"
ATTRIBUTION = "来源：国家统计局 (Source: National Bureau of Statistics of China)"
CHINA_TZ = timezone(timedelta(hours=8))
NATIONAL = {"text": "全国", "value": "000000000000"}
TIMEOUT = 30  # seconds
ATTEMPTS = 3  # connections from outside China are sometimes reset mid-handshake
RETRY_PAUSE = 2  # seconds, doubled after each failure
REQUEST_GAP = 0.5  # seconds between requests, to go easy on the site

# Most monthly activity data for January and February comes out as one figure
# in mid-March, so December can be the latest month until then. GDP comes out
# about three weeks after each quarter ends.
MAX_AGE_DAYS = {"M": 95, "Q": 125}
SEARCH_CODES = {"M": 1, "Q": 2, "Y": 3}
_CODE = re.compile(r"^(\d{4})(\d{2})?(MM|SS|YY)$")

# Each segment is (first year, catalog id, indicator id), newest first. NBS
# starts a new catalog when it rebases an index (CPI every five years; the
# next is due in 2031 and must be added here). The oldest segment has no first year.
SERIES = {
    "cpi_yoy": {
        "description": "CPI, % change on a year earlier",
        "label": "居民消费价格指数 (上年同月=100)", "unit": "%", "freq": "M", "index": True,
        "segments": [
            (2026, "5c7452825c7c4dcba391db5ca7f335c5", "53180dfb9c14411ba4b762307c85920c"),
            (2021, "809d2522b0fe4be89142650341b19083", "4ae9047687934a6390984c21d6ddab96"),
            (2016, "9d4eec43537742a7ab5d63db97fa2f51", "e5c318ffdbbc4d38898e52b52267eb25"),
            (None, "954cfd7597e34b919ec71caf6aeead51", "4c1065dd4e984b25a21190c843551697"),
        ],
    },
    "ppi_yoy": {
        "description": "Producer prices, % change on a year earlier",
        "label": "工业生产者出厂价格指数 (上年同月=100)", "unit": "%", "freq": "M", "index": True,
        "segments": [(None, "60e8b361f11c4a878c652a6487a25561", "150633e52b9a470a9a9fd1b296dd6c5b")],
    },
    "pmi_manufacturing": {
        "description": "Official manufacturing PMI (50 = no change)",
        "label": "制造业采购经理指数 (%)", "unit": "index", "freq": "M",
        "segments": [(None, "93ffbb1aa85740d3aa2618371508b606", "a09aa989bdcf4cffa2021795722eb916")],
    },
    "pmi_non_manufacturing": {
        "description": "Official non-manufacturing PMI (50 = no change)",
        "label": "非制造业商务活动指数 (%)", "unit": "index", "freq": "M",
        "segments": [(None, "7a64a6e25aec4a8e9dde044ecd9e2cce", "88a150208f6e4a1db8babe41ae700f66")],
    },
    "industrial_output_yoy": {
        "description": "Industrial value added, % change on a year earlier",
        "label": "规上工业增加值同比增长 (%)", "unit": "%", "freq": "M",
        "segments": [(None, "3f2e14f0542348ed9fe02476eca3450b", "ef1b1765960d45a29b4d7c4ca91be916")],
    },
    "retail_sales_yoy": {
        "description": "Retail sales, % change on a year earlier",
        "label": "社会消费品零售总额同比增长 (%)", "unit": "%", "freq": "M",
        "segments": [(None, "d0cb882c7f27443ab6b3ef9421901961", "aaac57d54d2e465d91bc9f3ea1a8618e")],
    },
    "fixed_asset_investment_ytd_yoy": {
        "description": "Fixed-asset investment, year to date, % change on a year earlier",
        "label": "固定资产投资额累计增长 (%)", "unit": "%", "freq": "M",
        "segments": [(None, "5129067b149d4ddfbec1ffc478d35bfb", "7e570cf8071c4734a7d78d9f0a70fbe1")],
    },
    "property_investment_ytd_yoy": {
        "description": "Property development investment, year to date, % change on a year earlier",
        "label": "房地产投资_累计增长 (%)", "unit": "%", "freq": "M",
        "segments": [(None, "9206137ccf03460daa74b7799e0f3c31", "205e08cba8c2409980db58c98da91b6f")],
    },
    "unemployment_rate": {
        "description": "Surveyed urban unemployment rate, %",
        "label": "全国城镇调查失业率 (%)", "unit": "%", "freq": "M",
        "segments": [(None, "ee3b7046b390415b9b7745e3d16f6052", "3888eac6062945a79c8a27e5f13d4953")],
    },
    "m2_yoy": {
        "description": "M2 money supply, % change on a year earlier (central bank data, often a month behind)",
        "label": "货币和准货币 (M2) 供应量_同比增长 (%)", "unit": "%", "freq": "M",
        "segments": [(None, "82130c6621a745cda3d64b090e733383", "e03f2232631f41cd9d754a7d7feb4a81")],
    },
    "gdp_yoy": {
        "description": "Real GDP, % change on a year earlier",
        "label": "国内生产总值指数 (上年同期=100) 当季值", "unit": "%", "freq": "Q", "index": True,
        "segments": [(None, "f9b694c9b79e4ce5958bc88c6410fa67", "170e7f00f8c24ede863c0526b42ae81f")],
    },
}


class Unavailable(Exception):
    """NBS returned nothing usable."""


class Stale(Exception):
    """NBS returned data, but its latest value was too old."""


# --- periods ---------------------------------------------------------------
# A period is an integer: year*12 + month-1 (M), year*4 + quarter-1 (Q), or year (Y).

def label(freq, p):
    if freq == "M":
        return f"{p // 12}-{p % 12 + 1:02d}"
    if freq == "Q":
        return f"{p // 4}Q{p % 4 + 1}"
    return str(p)


def to_code(freq, p):
    if freq == "M":
        return f"{p // 12}{p % 12 + 1:02d}MM"
    if freq == "Q":
        return f"{p // 4}{p % 4 + 1:02d}SS"
    return f"{p}YY"


def from_code(freq, code):
    match = _CODE.match(code)
    suffix = {"M": "MM", "Q": "SS", "Y": "YY"}[freq]
    if not match or match.group(3) != suffix:
        raise Unavailable(f"unexpected NBS period code {code!r} for a {freq} series")
    year, part = int(match.group(1)), int(match.group(2) or 1)
    return {"M": year * 12 + part - 1, "Q": year * 4 + part - 1, "Y": year}[freq]


def period_of(freq, day):
    return {"M": day.year * 12 + day.month - 1, "Q": day.year * 4 + (day.month - 1) // 3,
            "Y": day.year}[freq]


def period_end(freq, p):
    if freq == "M":
        year, month = divmod(p + 1, 12)
    elif freq == "Q":
        year, month = divmod((p + 1) * 3, 12)
    else:
        year, month = p + 1, 0
    return date(year, month + 1, 1) - timedelta(days=1)


def parse_period(text, freq, end):
    """'2026-08', '2026Q2' or '2025', read as the first (or, for ``end``, last) matching period."""
    text = text.strip().upper()
    if m := re.fullmatch(r"(\d{4})-(\d{1,2})", text):
        months = [(int(m.group(1)), int(m.group(2)))] * 2
    elif m := re.fullmatch(r"(\d{4})-?Q([1-4])", text):
        year, q = int(m.group(1)), int(m.group(2))
        months = [(year, q * 3 - 2), (year, q * 3)]
    elif m := re.fullmatch(r"(\d{4})", text):
        months = [(int(m.group(1)), 1), (int(m.group(1)), 12)]
    else:
        raise ValueError(f"can't read period {text!r}; use 2026-08, 2026Q2 or 2025")
    year, month = months[1] if end else months[0]
    if not 1 <= month <= 12:
        raise ValueError(f"can't read period {text!r}; month out of range")
    return period_of(freq, date(year, month, 1))


def period_range(freq, start, end, default_years):
    current = period_of(freq, datetime.now(CHINA_TZ).date())
    last = min(parse_period(end, freq, True), current) if end else current
    back = default_years * {"M": 12, "Q": 4, "Y": 1}[freq]
    first = parse_period(start, freq, False) if start else last - back
    if first > last:
        raise ValueError(f"start {label(freq, first)} is after end {label(freq, last)}")
    return first, last


# --- NBS API ---------------------------------------------------------------

_last_request = 0.0


def request(path, params=None, body=None):
    """GET (or POST ``body`` as JSON) and return the decoded response, retrying connection resets."""
    global _last_request
    url = f"{BASE_URL}/{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    data = json.dumps(body).encode() if body is not None else None
    headers = {"Content-Type": "application/json"} if body is not None else {}
    for attempt in range(ATTEMPTS):
        time.sleep(max(0.0, _last_request + REQUEST_GAP - time.monotonic()))
        _last_request = time.monotonic()
        try:
            with urllib.request.urlopen(
                urllib.request.Request(url, data=data, headers=headers), timeout=TIMEOUT
            ) as response:
                payload = json.loads(response.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as exc:
            raise Unavailable(f"NBS answered HTTP {exc.code} for {path}") from exc
        except (urllib.error.URLError, ConnectionError, TimeoutError) as exc:
            if attempt == ATTEMPTS - 1:
                raise Unavailable(f"couldn't reach NBS ({path}): {exc}") from exc
            time.sleep(RETRY_PAUSE * 2**attempt)
        except ValueError as exc:  # a web page instead of JSON
            raise Unavailable(f"NBS sent something other than JSON for {path}") from exc
    if not isinstance(payload, dict) or not payload.get("success"):
        message = payload.get("message") if isinstance(payload, dict) else payload
        raise Unavailable(f"NBS refused {path}: {message}")
    return payload["data"]


def fetch_values(catalog, indicator, freq, first, last, expected=None, index=False):
    """Values by period for one indicator, and the name NBS gave it."""
    dates = f"{to_code(freq, first)}-{to_code(freq, last)}"
    rows = request("stream/esData", body={
        "cid": catalog, "indicatorIds": [indicator], "daCatalogId": "",
        "das": [NATIONAL], "showType": 1, "dt": dates, "dts": [dates],
    })
    values, shown = {}, None
    try:
        for row in rows:
            for item in row["values"]:
                shown = " ".join(item["i_showname"].split())
                if item["_id"] != indicator or (expected and shown != expected):
                    raise Unavailable(
                        f"NBS indicator {indicator} came back as {shown!r}, not "
                        f"{expected!r}; its database may have been reorganised"
                    )
                p = from_code(freq, row["code"])
                text = item["value"]
                if text != "" and first <= p <= last:
                    value = float(text)
                    if index:  # published with the same period last year = 100
                        value = round(value - 100, len(text.partition(".")[2]))
                    values[p] = value
    except (KeyError, TypeError, AttributeError, ValueError) as exc:
        raise Unavailable(f"unexpected NBS response shape: {type(exc).__name__}: {exc}") from exc
    return values, shown


def check_fresh(name, freq, values, last, max_age_days):
    if not values:
        raise Unavailable(f"NBS returned no values for {name}")
    latest = max(values)
    reference = min(period_end(freq, last), datetime.now(CHINA_TZ).date())
    if max_age_days is not None and (reference - period_end(freq, latest)).days > max_age_days:
        raise Stale(
            f"latest {name} value is for {label(freq, latest)}, more than "
            f"{max_age_days} days before {reference}"
        )


def curated(name, start=None, end=None, max_age_days=None, default_years=5):
    spec = SERIES[name]
    freq = spec["freq"]
    first, last = period_range(freq, start, end, default_years)
    values, until = {}, last
    for since, catalog, indicator in spec["segments"]:
        segment_start = first if since is None else period_of(freq, date(since, 1, 1))
        if until >= max(first, segment_start):
            got, _ = fetch_values(catalog, indicator, freq, max(first, segment_start), until,
                                  expected=spec["label"], index=spec.get("index", False))
            values.update(got)
        until = min(until, segment_start - 1)
    limit = MAX_AGE_DAYS[freq] if max_age_days is None else max_age_days
    check_fresh(name, freq, values, last, limit)
    return values


# --- commands --------------------------------------------------------------

def write_csv(header, rows):
    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)


def run_each(names, work):
    """Run ``work(name)`` for each name, reporting failures on stderr; return how many failed."""
    failed = 0
    for name in names:
        try:
            work(name)
        except (Unavailable, Stale) as exc:
            kind = "STALE" if isinstance(exc, Stale) else "UNAVAILABLE"
            print(f"{kind} {name}: {exc}", file=sys.stderr)
            failed += 1
    return failed


def cmd_list(args):
    write_csv(["series", "frequency", "unit", "description"],
              [[n, s["freq"], s["unit"], s["description"]] for n, s in SERIES.items()])
    return 0


def cmd_latest(args):
    rows = []

    def work(name):
        spec = SERIES[name]
        values = curated(name, max_age_days=args.max_age_days, default_years=2)
        periods = sorted(values)
        prev = periods[-2] if len(periods) > 1 else None
        rows.append([name, label(spec["freq"], periods[-1]), values[periods[-1]], spec["unit"],
                     label(spec["freq"], prev) if prev is not None else "",
                     values[prev] if prev is not None else ""])

    failed = run_each(args.series or list(SERIES), work)
    write_csv(["series", "period", "value", "unit", "previous_period", "previous_value"], rows)
    return 1 if failed else 0


def cmd_get(args):
    results = []

    def work(name):
        values = curated(name, args.start, args.end, args.max_age_days)
        results.append((name, SERIES[name], values))

    failed = run_each(args.series, work)
    if args.format == "json":
        json.dump({"attribution": ATTRIBUTION, "series": [
            {"series": name, "label": spec["label"], "unit": spec["unit"], "frequency": spec["freq"],
             "values": [{"period": label(spec["freq"], p), "value": values[p]} for p in sorted(values)]}
            for name, spec, values in results
        ]}, sys.stdout, ensure_ascii=False, indent=1)
        print()
    else:
        write_csv(["series", "period", "value", "unit"], [
            [name, label(spec["freq"], p), values[p], spec["unit"]]
            for name, spec, values in results for p in sorted(values)
        ])
    return 1 if failed else 0


def cmd_search(args):
    params = {"search": args.keyword, "code": SEARCH_CODES.get(args.freq, ""),
              "pagenum": 1, "pageSize": args.limit * 5}
    try:
        data = request("query", params=params)
        hits = {}
        for item in data["data"]:
            if item.get("da") not in (None, NATIONAL["value"]):
                continue
            freq = {"1": "M", "2": "Q", "3": "Y"}.get(str(item["type_value"]), "?")
            dt = str(item.get("dt", ""))  # 202608, 202602 (a quarter) or 2025
            if freq in ("M", "Q") and re.fullmatch(r"\d{6}", dt):
                dt = f"{dt[:4]}-{dt[4:]}" if freq == "M" else f"{dt[:4]}Q{int(dt[4:])}"
            hits.setdefault(item["indic_id"], [
                item["indic_id"], item["cid"], freq, " ".join(item["show_name"].split()),
                dt, item.get("value", ""),
            ])
    except Unavailable as exc:
        print(f"UNAVAILABLE search {args.keyword!r}: {exc}", file=sys.stderr)
        return 1
    except (KeyError, TypeError, AttributeError) as exc:
        print(f"UNAVAILABLE search {args.keyword!r}: unexpected response shape: {exc}", file=sys.stderr)
        return 1
    write_csv(["indicator", "catalog", "frequency", "name", "latest_period", "latest_value"],
              list(hits.values())[: args.limit])
    return 0


def cmd_browse(args):
    """Children of a node in NBS's category tree; for a leaf catalog, the indicators in it."""
    code = SEARCH_CODES[args.freq]
    try:
        node = args.node
        if node is None:  # the root holds one node ("月度数据" etc.) whose children are the categories
            node = request("new/queryIndexTreeAsync", params={"code": code})[0]["_id"]
        children = request("new/queryIndexTreeAsync", params={"code": code, "pid": node})
        if children:
            write_csv(["node", "leaf", "name"],
                      [[c["_id"], "yes" if c["isLeaf"] else "no", " ".join(c["name"].split())]
                       for c in children])
            return 0
        found = request("new/queryIndicatorsByCid", params={"cid": node})["list"]
        write_csv(["indicator", "catalog", "frequency", "name", "unit"],
                  [[i["_id"], node, args.freq, " ".join(i["i_showname"].split()), i.get("du_name", "")]
                   for i in found])
    except Unavailable as exc:
        print(f"UNAVAILABLE browse {args.node or 'root'}: {exc}", file=sys.stderr)
        return 1
    except (KeyError, TypeError, AttributeError, IndexError) as exc:
        print(f"UNAVAILABLE browse {args.node or 'root'}: unexpected response shape: {exc}", file=sys.stderr)
        return 1
    return 0


def cmd_fetch(args):
    freq = args.freq
    first, last = period_range(freq, args.start, args.end, 5 if freq != "Y" else 15)
    try:
        values, shown = fetch_values(args.catalog, args.indicator, freq, first, last)
        check_fresh(args.indicator, freq, values, last, args.max_age_days)
    except (Unavailable, Stale) as exc:
        kind = "STALE" if isinstance(exc, Stale) else "UNAVAILABLE"
        print(f"{kind} {args.indicator}: {exc}", file=sys.stderr)
        return 1
    if args.format == "json":
        json.dump({"attribution": ATTRIBUTION, "indicator": args.indicator, "label": shown,
                   "frequency": freq,
                   "values": [{"period": label(freq, p), "value": values[p]} for p in sorted(values)]},
                  sys.stdout, ensure_ascii=False, indent=1)
        print()
    else:
        print(f"# {shown}", file=sys.stderr)
        write_csv(["period", "value"], [[label(freq, p), values[p]] for p in sorted(values)])
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Chinese national macro data from NBS.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="curated series")

    p = sub.add_parser("latest", help="latest and previous value of curated series")
    p.add_argument("series", nargs="*", metavar="SERIES", help="default: all curated series")
    p.add_argument("--max-age-days", type=int)

    p = sub.add_parser("get", help="history of curated series")
    p.add_argument("series", nargs="+", metavar="SERIES")
    p.add_argument("--start", help="first period, default five years before --end")
    p.add_argument("--end", help="last period, default the current one")
    p.add_argument("--format", choices=["csv", "json"], default="csv")
    p.add_argument("--max-age-days", type=int)

    p = sub.add_parser("search", help="find any national NBS indicator by Chinese keyword")
    p.add_argument("keyword")
    p.add_argument("--freq", choices=["M", "Q", "Y"])
    p.add_argument("--limit", type=int, default=20)

    p = sub.add_parser("browse", help="walk NBS's category tree when search misses")
    p.add_argument("--freq", choices=["M", "Q", "Y"], default="M")
    p.add_argument("--node", help="node id from a previous browse; omit for the top categories")

    p = sub.add_parser("fetch", help="history of any indicator found with search, values as published")
    p.add_argument("--catalog", required=True)
    p.add_argument("--indicator", required=True)
    p.add_argument("--freq", choices=["M", "Q", "Y"], required=True)
    p.add_argument("--start")
    p.add_argument("--end")
    p.add_argument("--format", choices=["csv", "json"], default="csv")
    p.add_argument("--max-age-days", type=int, help="off unless given")

    args = parser.parse_args(argv)
    unknown = [s for s in getattr(args, "series", None) or [] if s not in SERIES]
    if unknown:
        parser.error(f"unknown series {', '.join(unknown)}; choose from {', '.join(SERIES)}")
    commands = {"list": cmd_list, "latest": cmd_latest, "get": cmd_get,
                "search": cmd_search, "browse": cmd_browse, "fetch": cmd_fetch}
    try:
        return commands[args.command](args)
    except ValueError as exc:  # bad --start / --end
        parser.error(str(exc))


if __name__ == "__main__":
    sys.exit(main())
