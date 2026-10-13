"""Build the 17-company initiation pack as HTML (then print_pdf.mjs renders the PDF).

Run:  python3 build.py            -> ../report.html
      node print_pdf.mjs          -> ../China_HK_17_Short_Initiations_2026-10-12.pdf

Content: co_*.py (ratings inputs, estimates, page-1 text, valuation), v2_*.py (background, the business,
competition, TAM and three-statement commentary), fin_data.py + fin_model.py (balance sheet, cash flow, ratios).
"""
import html
import math
import os

from co_resources import COMPANIES as RES
from co_battery import COMPANIES as BAT
from co_tech import COMPANIES as TECH
from fin_model import fin_analysis
import v2_resources
import v2_battery
import v2_semis
import v2_growth
from v2_forces import FORCES
from v2_extra import EXTRA

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_HTML = os.path.join(HERE, "..", "report.html")

AS_OF = "12 October 2026"
USD_CNY = 6.6943
USD_HKD = 7.8475
RMB_PER_HKD = 0.8531
YEARS = ["FY23A", "FY24A", "FY25A", "FY26E", "FY27E", "FY28E"]
BUY_MIN, SELL_MAX = 0.20, -0.10

# Reference palette (dataviz skill, light mode; the PDF is print-only)
C = dict(
    ink="#0b0b0b", ink2="#52514e", muted="#898781", grid="#e1e0d9", axis="#c3c2b7",
    surface="#fcfcfb", page="#ffffff", accent="#104281", actual="#2a78d6", est="#86b6ef",
    neg="#e34948", good="#006300", crit="#d03b3b", wash="#eef4fc",
)

SHORT = dict(zijin="Zijin Mining", sany="Sany Heavy Industry", sieyuan="Sieyuan Electric", catl="CATL",
             sungrow="Sungrow Power", huayou="Huayou Cobalt", tianqi="Tianqi Lithium", ganfeng="Ganfeng Lithium",
             gigadevice="GigaDevice", jushi="China Jushi", jlmag="JL Mag Rare-Earth", hans="Han's Laser",
             horizon="Horizon Robotics", leaderdrive="Leaderdrive", edge="Edge Medical", zai="Z.AI (Zhipu AI)",
             minimax="MiniMax")

ORDER = ["zijin", "sany", "catl", "hans", "jlmag", "sungrow", "sieyuan", "gigadevice", "edge", "leaderdrive",
         "huayou", "tianqi", "ganfeng", "jushi", "horizon", "zai", "minimax"]


# ----------------------------------------------------------------------------- formatting
def esc(s):
    return html.escape(str(s), quote=False)


def num(x, dp=None):
    if x is None:
        return "–"
    if dp is None:
        ax = abs(x)
        dp = 0 if ax >= 100 else (1 if ax >= 10 else 2)
    s = f"{abs(x):,.{dp}f}"
    return f"({s})" if x < 0 else s


def pct(x, dp=1, sign=False):
    if x is None:
        return "–"
    s = f"{abs(x) * 100:.{dp}f}%"
    if sign:
        return ("+" if x >= 0 else "−") + s
    return s if x >= 0 else "−" + s


def mult(x):
    if x is None or x <= 0 or x > 999:
        return "n.m."
    return f"{x:.0f}x" if x >= 100 else f"{x:.1f}x"


def pnum(p):
    """Share-price style number: 2dp (3dp for sub-HK$5 quotes), none from 1,000."""
    if p >= 1000:
        return f"{p:,.0f}"
    if p < 5 and round(p, 2) != round(p, 3):
        return f"{p:.3f}"
    return f"{p:,.2f}"


def price_fmt(p, ccy):
    s = pnum(p)
    return f"{ccy}{s}" if ccy == "HK$" else f"RMB{s}"


def round_tp(x):
    step = 0.05 if x < 10 else 0.5 if x < 50 else 1 if x < 200 else 5 if x < 500 else 10
    return round(math.floor(x / step + 0.5) * step, 2)


def tp_str(x):
    """Prose style: 2dp below 100, whole numbers above."""
    if x < 100:
        return f"{x:.2f}"
    return f"{x:,.0f}"


# ----------------------------------------------------------------------------- model
def value_from(method, co, est_rev, est_eps):
    """Per-share value in the rated-line currency."""
    fx, shares, nc = co["fx"], co["shares"], co["net_cash"]
    t = method["type"]
    if t == "pe":
        eps = method.get("eps", est_eps[method.get("yr", 1)])
        return method["mult"] * eps * fx
    if t == "evs":
        rev = method.get("rev", est_rev[method.get("yr", 1)])
        disc = (1 + method.get("rate", 0)) ** method.get("disc_years", 0)
        equity = rev * method["mult"] / disc + nc
        return equity / shares * fx
    if t == "fut_pe":
        equity = method["np"] * method["mult"] / (1 + method["rate"]) ** method["years"] + nc
        return equity / shares * fx
    raise ValueError(t)


def compute(co):
    h, e = co["hist"], co["est"]
    rev = h["rev"] + e["rev"]
    gm = h["gm"] + e["gm"]
    npf = h["np"] + e["np"]
    est_eps = [x / co["shares"] for x in e["np"]]
    eps = (h.get("eps") or [None] * 3) + est_eps
    if "dps" in e:
        est_dps = e["dps"]
    elif "payout" in e:
        est_dps = [max(0.0, x * e["payout"]) for x in est_eps]
    else:
        est_dps = [None] * 3
    dps = (h.get("dps") or [None] * 3) + est_dps

    price_fin = co["price"] / co["fx"]                       # price in financial currency
    pe = [price_fin / x if (x and x > 0) else None for x in eps]
    dy = [x / price_fin if x is not None else None for x in dps]
    ev = co["ev"]
    evs = [ev / x if x else None for x in rev]

    def yoy(a, b):
        if a is None or b is None or a <= 0:
            return None
        return b / a - 1

    rev_g = [None] + [yoy(rev[i - 1], rev[i]) for i in range(1, 6)]
    np_g = [None] + [yoy(npf[i - 1], npf[i]) for i in range(1, 6)]
    nm = [(n / r) if (n is not None and r) else None for n, r in zip(npf, rev)]

    tp = round_tp(value_from(co["tp_method"], co, e["rev"], est_eps))
    up = tp / co["price"] - 1
    rating = "Buy" if up >= BUY_MIN else ("Sell" if up <= SELL_MAX else "Hold")
    bear = round_tp(value_from(co["scen"]["bear"], co, e["rev"], est_eps))
    bull = round_tp(value_from(co["scen"]["bull"], co, e["rev"], est_eps))

    mcap_usd = co["mcap_local"] / (USD_CNY if co["mcap_ccy"] == "RMB" else USD_HKD)
    m = dict(rev=rev, gm=gm, np=npf, eps=eps, dps=dps, pe=pe, dy=dy, evs=evs, rev_g=rev_g, np_g=np_g,
             nm=nm, tp=tp, up=up, rating=rating, bear=bear, bull=bull, mcap_usd=mcap_usd,
             price_fin=price_fin)

    big = co["fin_unit"].endswith("bn")
    fmt_v = (lambda x: num(x)) if big else (lambda x: f"{x:,.0f}")
    ph = dict(
        price=tp_str(co["price"]) if co["price"] >= 10 else f"{co['price']:.3f}",
        tp=tp_str(tp), up=pct(up, 0, sign=True), upabs=pct(abs(up), 0), rating=rating,
        bear=tp_str(bear), bull=tp_str(bull),
        dy26=pct(dy[3], 1) if dy[3] is not None else "–",
    )
    for i, yr in enumerate(["26", "27", "28"]):
        j = 3 + i
        ph[f"rev{yr}"] = fmt_v(rev[j])
        ph[f"np{yr}"] = fmt_v(abs(npf[j])) if big else f"{abs(npf[j]):,.0f}"
        ph[f"eps{yr}"] = f"{eps[j]:.2f}" if eps[j] is not None else "–"
        ph[f"pe{yr}"] = f"{pe[j]:.1f}" if pe[j] else "n.m."
        if pe[j] and pe[j] >= 100:
            ph[f"pe{yr}"] = f"{pe[j]:.0f}"
        ph[f"evs{yr}"] = f"{evs[j]:.1f}" if evs[j] else "n.m."
    if eps[4]:
        ph["pe27x"] = f"{(price_fin - co['net_cash'] / co['shares']) / eps[4]:.1f}"
        if co.get("a_price"):
            ph["pe27a"] = f"{co['a_price'] / eps[4]:.0f}"
    m["ph"] = ph
    return m


def fill(text, ph):
    out = text
    for k, v in ph.items():
        out = out.replace("{" + k + "}", str(v))
    if "{" in out and "}" in out:
        raise ValueError(f"unfilled placeholder in: {out[:120]}")
    return out


def compute_fin(co, m):
    """Three-statement analysis (fin_model) plus the placeholders the v2 commentary uses.

    Amount placeholders are absolute values: the prose carries the sign ("net debt of", "−RMB")."""
    fa = fin_analysis(co, m)
    big = co["fin_unit"].endswith("bn")

    def amt(x):
        if x is None:
            return "n.a."
        ax = abs(x)
        if not big:
            return f"{ax:,.0f}"
        return f"{ax:,.0f}" if ax >= 100 else (f"{ax:.1f}" if ax >= 1 else f"{ax:.2f}")

    def pc(x, dp=1):
        return "n.m." if x is None else f"{abs(x):.{dp}f}%"

    def xx(x):
        return "n.m." if x is None else f"{abs(x):.1f}x" if abs(x) >= 10 else f"{abs(x):.2f}x"

    def capex_pc(x):
        return "n.m." if x is None else (f"{x:.0f}%" if x >= 10 else f"{x:.1f}%")

    nc = fa["netcash_h"][:3] + fa["netcash_e"]
    fcf = fa["fcf_h"][:3] + fa["fcf_e"]
    roe = fa["roe_h"] + fa["roe_e"]
    payout = [(d / e * 100) if (d is not None and e and e > 0) else None for d, e in zip(m["dps"], m["eps"])]
    fa["payout"] = payout
    ph = m["ph"]
    for i, yr in enumerate(["23", "24", "25", "26", "27", "28"]):
        ph[f"nc{yr}"] = amt(nc[i])
        ph[f"fcf{yr}"] = amt(fcf[i])
        ph[f"roe{yr}"] = pc(roe[i])
    ph["ncj26"] = amt(fa["netcash_h"][3])
    ph["fcfttm"] = amt(fa["fcf_h"][3])
    ph["roa25"] = pc(fa["roa_h"][2])
    ph["ocfnp25"] = xx(fa["ocf_np_h"][2])
    ph["ndeq25"] = pc(fa["nd_eq_h"][2], 0)
    ph["ndebitda25"] = xx(fa["nd_ebitda_h"][2])
    ph["recvd25"] = "n.m." if fa["recv_d"][2] is None else f"{fa['recv_d'][2]:.0f}"
    ph["invd25"] = "n.m." if fa["inv_d"][2] is None else f"{fa['inv_d'][2]:.0f}"
    ph["apd25"] = "n.m." if fa["ap_d"][2] is None else f"{fa['ap_d'][2]:.0f}"
    ph["cr25"] = xx(fa["cr_h"][2])
    ph["capexr25"] = capex_pc(fa["capex_r_h"][2])
    ph["payout25"] = pc(payout[2], 0)
    m["fa"] = fa
    return fa


# ----------------------------------------------------------------------------- SVG charts
def svg_mix(items, width=250):
    """Horizontal single-hue bars for a composition (%)."""
    row = 21
    label_w = 0
    h = row * len(items) + 4
    vmax = max(v for _, v in items)
    bar_x = 2
    bar_wmax = width - 44
    out = [f'<svg class="chart" viewBox="0 0 {width} {h}" width="{width}" height="{h}" role="img" '
           f'aria-label="Revenue mix">']
    for i, (lab, v) in enumerate(items):
        y = i * row
        out.append(f'<text x="{bar_x}" y="{y + 8}" class="t-lab">{esc(lab)}</text>')
        w = max(2.0, bar_wmax * v / vmax)
        by = y + 11
        r = min(3, w / 2)
        out.append(f'<path d="M{bar_x},{by} H{bar_x + w - r} Q{bar_x + w},{by} {bar_x + w},{by + r} '
                   f'V{by + 7 - r} Q{bar_x + w},{by + 7} {bar_x + w - r},{by + 7} H{bar_x} Z" fill="{C["actual"]}"/>')
        out.append(f'<text x="{bar_x + w + 4}" y="{by + 6.5}" class="t-val">{v:.1f}%</text>'
                   if v % 1 else f'<text x="{bar_x + w + 4}" y="{by + 6.5}" class="t-val">{v:.0f}%</text>')
    out.append("</svg>")
    return "".join(out)


def nice_ticks(lo, hi, n=4):
    span = hi - lo
    if span <= 0:
        span = abs(hi) or 1
    raw = span / n
    mag = 10 ** math.floor(math.log10(raw))
    step = min((s * mag for s in (1, 2, 2.5, 5, 10) if s * mag >= raw), default=10 * mag)
    start = math.floor(lo / step) * step
    ticks = []
    t = start
    while t <= hi + step * 0.5:
        ticks.append(round(t, 10))
        t += step
    return ticks


def tick_label(v):
    av = abs(v)
    if av >= 1000:
        s = f"{av / 1000:.0f}K" if av % 1000 == 0 else f"{av / 1000:.1f}K"
    elif av >= 10 or av == 0:
        s = f"{av:.0f}"
    elif av >= 1:
        s = f"{av:.1f}".rstrip("0").rstrip(".")
    else:
        s = f"{av:.2f}".rstrip("0").rstrip(".")
    return ("−" if v < 0 else "") + s


def svg_columns(values, title, unit, width=318, height=164):
    """Column chart FY23A..FY28E, actual vs estimate; supports negative values."""
    vals = [v for v in values]
    present = [v for v in vals if v is not None]
    vmin = min(0, min(present))
    vmax = max(0, max(present))
    ticks = nice_ticks(vmin, vmax, 4)
    lo, hi = min(ticks[0], vmin), max(ticks[-1], vmax)
    left, right, top, bottom = 34, 6, 24, 20
    pw, phh = width - left - right, height - top - bottom

    def y(v):
        return top + (hi - v) / (hi - lo) * phh

    out = [f'<svg class="chart" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" '
           f'aria-label="{esc(title)}">',
           f'<text x="0" y="11" class="t-title">{esc(title)}</text>',
           f'<text x="0" y="21" class="t-sub">{esc(unit)}</text>']
    # legend (two series: actual / estimate)
    lx = width - 118
    out.append(f'<rect x="{lx}" y="4" width="9" height="9" rx="2" fill="{C["actual"]}"/>'
               f'<text x="{lx + 13}" y="12" class="t-leg">Actual</text>'
               f'<rect x="{lx + 56}" y="4" width="9" height="9" rx="2" fill="{C["est"]}"/>'
               f'<text x="{lx + 69}" y="12" class="t-leg">Estimate</text>')
    for t in ticks:
        yy = y(t)
        if top - 1 <= yy <= top + phh + 1:
            stroke = C["axis"] if t == 0 else C["grid"]
            out.append(f'<line x1="{left}" x2="{width - right}" y1="{yy:.1f}" y2="{yy:.1f}" stroke="{stroke}" '
                       f'stroke-width="1"/>')
            out.append(f'<text x="{left - 5}" y="{yy + 3:.1f}" class="t-tick" text-anchor="end">{tick_label(t)}</text>')
    slot = pw / 6
    bw = min(24, slot * 0.56)
    for i, v in enumerate(vals):
        cx = left + slot * i + slot / 2
        out.append(f'<text x="{cx:.1f}" y="{height - 6}" class="t-tick" text-anchor="middle">{YEARS[i]}</text>')
        if v is None:
            out.append(f'<text x="{cx:.1f}" y="{y(0) - 3:.1f}" class="t-tick" text-anchor="middle">n.a.</text>')
            continue
        fill_c = C["actual"] if i < 3 else C["est"]
        x0 = cx - bw / 2
        y0, y1 = y(0), y(v)
        r = min(4, abs(y1 - y0) / 2, bw / 2)
        if v >= 0:
            d = (f"M{x0:.1f},{y0:.1f} V{y1 + r:.1f} Q{x0:.1f},{y1:.1f} {x0 + r:.1f},{y1:.1f} "
                 f"H{x0 + bw - r:.1f} Q{x0 + bw:.1f},{y1:.1f} {x0 + bw:.1f},{y1 + r:.1f} V{y0:.1f} Z")
        else:
            d = (f"M{x0:.1f},{y0:.1f} V{y1 - r:.1f} Q{x0:.1f},{y1:.1f} {x0 + r:.1f},{y1:.1f} "
                 f"H{x0 + bw - r:.1f} Q{x0 + bw:.1f},{y1:.1f} {x0 + bw:.1f},{y1 - r:.1f} V{y0:.1f} Z")
        out.append(f'<path d="{d}" fill="{fill_c}"/>')
        if i in (2, 5):  # label last actual and last estimate only
            lab = num(v, 1 if abs(v) < 100 else 0) if abs(v) >= 1 else num(v, 2)
            ly = (y1 - 4) if v >= 0 else (y1 + 10)
            out.append(f'<text x="{cx:.1f}" y="{ly:.1f}" class="t-val" text-anchor="middle">{lab}</text>')
    out.append("</svg>")
    return "".join(out)


def svg_scenarios(co, m, width=318, height=132):
    """Football field: 52-week range, bear-to-bull range with base TP, and the current price."""
    ccy = co["ccy"]
    p, lo52, hi52 = co["price"], co["lo52"], co["hi52"]
    bear, bull, tp = m["bear"], m["bull"], m["tp"]
    vmin = min(lo52, bear, p) * 0.9
    vmax = max(hi52, bull, p) * 1.04
    vmin = 0 if vmin < (vmax - vmin) * 0.25 else vmin
    left, right = 70, 16
    pw = width - left - right

    def x(v):
        return left + (v - vmin) / (vmax - vmin) * pw

    lab = pnum
    rows = [("52-week range", lo52, hi52, None, C["axis"], 44),
            ("Bear – bull", bear, bull, tp, C["est"], 90)]
    out = [f'<svg class="chart" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" '
           f'aria-label="Valuation range">',
           f'<text x="0" y="11" class="t-title">Valuation range vs current price ({esc(ccy)})</text>']
    xp = x(p)
    out.append(f'<line x1="{xp:.1f}" x2="{xp:.1f}" y1="26" y2="{height - 18}" stroke="{C["ink"]}" '
               f'stroke-width="1.5"/>')
    for name, a, b, mid, colr, yc in rows:
        out.append(f'<text x="0" y="{yc + 3}" class="t-lab">{esc(name)}</text>')
        xa, xb = x(a), x(b)
        out.append(f'<rect x="{xa:.1f}" y="{yc - 5}" width="{max(2, xb - xa):.1f}" height="10" rx="3" fill="{colr}"/>')
        out.append(f'<text x="{xa:.1f}" y="{yc + 16}" class="t-tick" text-anchor="middle">{lab(a)}</text>')
        out.append(f'<text x="{xb:.1f}" y="{yc + 16}" class="t-tick" text-anchor="middle">{lab(b)}</text>')
        if mid is not None:
            xm = x(mid)
            out.append(f'<circle cx="{xm:.1f}" cy="{yc}" r="5" fill="{C["accent"]}" stroke="{C["page"]}" '
                       f'stroke-width="2"/>')
            if abs(xm - xp) < 30:   # keep the TP label clear of the price line
                tx, anc = (xm + 7, "start") if xm >= xp else (xm - 7, "end")
            else:
                tx, anc = xm, "middle"
            out.append(f'<text x="{tx:.1f}" y="{yc - 10}" class="t-val" text-anchor="{anc}">TP {lab(mid)}</text>')
    out.append(f'<text x="{xp:.1f}" y="{height - 5}" class="t-val" text-anchor="middle">Price {lab(p)}</text>')
    out.append("</svg>")
    return "".join(out)


def svg_upside(rows, width=700):
    """Summary: implied return to TP, diverging bars around zero (blue up, red down)."""
    row = 15
    top = 6
    h = top + row * len(rows) + 22
    left = 150
    right = 50
    vals = [r[1] for r in rows]
    vmin, vmax = min(0, min(vals)), max(vals)
    ticks = nice_ticks(vmin, vmax, 5)
    lo, hi = min(ticks[0], vmin), max(ticks[-1], vmax)
    pw = width - left - right

    def x(v):
        return left + (v - lo) / (hi - lo) * pw

    out = [f'<svg class="chart" viewBox="0 0 {width} {h}" width="{width}" height="{h}" role="img" '
           f'aria-label="Implied return to target price">']
    for t in ticks:
        xx = x(t)
        out.append(f'<line x1="{xx:.1f}" x2="{xx:.1f}" y1="{top - 4}" y2="{h - 18}" '
                   f'stroke="{C["axis"] if t == 0 else C["grid"]}" stroke-width="1"/>')
        out.append(f'<text x="{xx:.1f}" y="{h - 5}" class="t-tick" text-anchor="middle">{t * 100:+.0f}%</text>')
    for i, (name, v, rating) in enumerate(rows):
        yc = top + i * row + row / 2
        out.append(f'<text x="{left - 8}" y="{yc + 3.5}" class="t-lab" text-anchor="end">{esc(name)}</text>')
        x0, x1 = x(0), x(v)
        colr = C["actual"] if v >= 0 else C["neg"]
        bh = 11
        a, b = (x0, x1) if v >= 0 else (x1, x0)
        w = max(1.5, b - a)
        r = min(4, w / 2)
        if v >= 0:
            d = (f"M{a:.1f},{yc - bh / 2:.1f} H{b - r:.1f} Q{b:.1f},{yc - bh / 2:.1f} {b:.1f},{yc - bh / 2 + r:.1f} "
                 f"V{yc + bh / 2 - r:.1f} Q{b:.1f},{yc + bh / 2:.1f} {b - r:.1f},{yc + bh / 2:.1f} H{a:.1f} Z")
            tx, anchor = b + 5, "start"
        else:
            d = (f"M{b:.1f},{yc - bh / 2:.1f} H{a + r:.1f} Q{a:.1f},{yc - bh / 2:.1f} {a:.1f},{yc - bh / 2 + r:.1f} "
                 f"V{yc + bh / 2 - r:.1f} Q{a:.1f},{yc + bh / 2:.1f} {a + r:.1f},{yc + bh / 2:.1f} H{b:.1f} Z")
            tx, anchor = a - 5, "end"
        out.append(f'<path d="{d}" fill="{colr}"/>')
        out.append(f'<text x="{tx:.1f}" y="{yc + 3.5}" class="t-val" text-anchor="{anchor}">{v * 100:+.0f}% · '
                   f'{rating}</text>')
    out.append("</svg>")
    return "".join(out)


# ----------------------------------------------------------------------------- HTML blocks
def rating_pill(r):
    return f'<span class="pill pill-{r.lower()}">{r}</span>'


def fin_rows(co, m):
    """Page-1 key financials: rows of (label, values FY23A..FY28E, row class)."""
    unit = co["fin_unit"]
    big = unit.endswith("bn")
    cur = unit.split()[0]
    vfmt = (lambda v: num(v)) if big else (lambda v: "–" if v is None else f"({abs(v):,.0f})" if v < 0 else f"{v:,.0f}")
    rows = [(f"Revenue ({unit})", [vfmt(v) for v in m["rev"]], "")]
    rows.append(("&nbsp;&nbsp;YoY growth", [pct(v, 0, sign=True) for v in m["rev_g"]], "sub"))
    rows.append(("Gross margin", [("–" if v is None else f"{v:.1f}%") for v in m["gm"]], ""))
    if co["profile"] == "profit":
        rows.append((f"Net profit, attributable ({unit})", [vfmt(v) for v in m["np"]], ""))
        rows.append(("&nbsp;&nbsp;YoY growth", [pct(v, 0, sign=True) if v is not None else "n.m." for v in m["np_g"]],
                     "sub"))
        rows.append((f"EPS ({cur})", [("–" if v is None else (f"({abs(v):.2f})" if v < 0 else f"{v:.2f}"))
                                     for v in m["eps"]], ""))
        pe_lab = "P/E (x)" if co["ccy"] == "RMB" else "P/E on H-share price (x)"
        rows.append((pe_lab, [mult(v) for v in m["pe"]], "hl"))
        rows.append((f"DPS ({cur})", [("–" if v is None else f"{v:.2f}") for v in m["dps"]], ""))
        rows.append(("Dividend yield", [("–" if v is None else f"{v * 100:.1f}%") for v in m["dy"]], ""))
    else:
        rows.append((f"{co['loss_label']} ({unit})", [vfmt(v) for v in m["np"]], ""))
        rows.append(("&nbsp;&nbsp;Margin", [("–" if v is None else f"{v * 100:.0f}%") for v in m["nm"]], "sub"))
        rows.append(("EV/sales at current price (x)", [mult(v) for v in m["evs"]], "hl"))
    return rows


def fin_table(co, m):
    rows = fin_rows(co, m)
    head = "".join(f'<th class="{"e" if i >= 3 else ""}">{y}</th>' for i, y in enumerate(YEARS))
    body = []
    for lab, vals, cls in rows:
        tds = "".join(f'<td class="{"e" if i >= 3 else ""}">{v}</td>' for i, v in enumerate(vals))
        body.append(f'<tr class="{cls}"><th>{lab}</th>{tds}</tr>')
    return (f'<table class="fin"><thead><tr><th>Year to December</th>{head}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table>')


def key_data_rows(co, m):
    ccy = co["ccy"]
    p = co["price"]
    cur = co["fin_unit"].split()[0]
    big = co["fin_unit"].endswith("bn")
    nc = co["net_cash"]
    nc_s = (f"{cur}{abs(nc):,.1f}bn" if big else f"{cur}{abs(nc) / 1000:,.1f}bn")
    nc_lab = "Net cash" if nc >= 0 else "Net debt"
    nc_s += {"horizon": " (adj.)", "zai": " (pro forma)"}.get(co["key"], "")
    ev_s = f"{cur}{co['ev']:,.1f}bn" if big else f"{cur}{co['ev'] / 1000:,.1f}bn"
    mc = co["mcap_local"]
    mc_ccy = co["mcap_ccy"]
    mc_s = f"{mc_ccy}{mc:,.1f}bn" if mc < 1000 else f"{mc_ccy}{mc / 1000:,.2f}tn"
    if co.get("mcap_note"):
        mc_s += f" ({co['mcap_note']})"
    perf = (f"{co['ytd']:+.1f}% YTD" if co.get("ytd") is not None
            else f"{co['since_ipo']:+.0f}% since IPO")
    cons = co["cons"]
    cons_ccy = cons.get("tp_ccy", ccy)
    cons_s = price_fmt(cons["tp"], cons_ccy if cons_ccy == "HK$" else "RMB")
    if cons.get("tp_line"):
        cons_s += f" ({cons['tp_line']})"
    if cons.get("n"):
        cons_s += f", {cons['n']} analysts"
    sh = co["shares"]
    sh_s = f"{sh:,.2f}bn" if big else f"{sh:,.1f}m"
    rows = [
        ("Price (12 Oct 2026)", price_fmt(p, ccy)),
        ("Target price (12m)", price_fmt(m["tp"], ccy)),
        ("Implied return", pct(m["up"], 1, sign=True)),
        ("Market cap", f"{mc_s} / US${m['mcap_usd']:,.1f}bn"),
        ("Enterprise value", ev_s),
        (nc_lab, nc_s),
        ("Shares outstanding", sh_s),
        ("52-week range", f"{pnum(co['lo52'])} – {pnum(co['hi52'])}"),
        ("Performance", perf),
    ]
    if co["profile"] == "profit" and m["dy"][3] is not None:
        rows.append(("Dividend yield (FY26E)", f"{m['dy'][3] * 100:.1f}%"))
    rows.append(("Consensus target", cons_s))
    rows.append(("Other listing", co["listing"]))
    return rows


def key_data(co, m):
    rows = key_data_rows(co, m)
    trs = "".join(f"<tr><th>{esc(a)}</th><td>{esc(b)}</td></tr>" for a, b in rows)
    return f'<table class="kd">{trs}</table>'


def peer_rows(co, m):
    """Peer comparison: (header, rows, caption); the last row is the company itself."""
    def f(v):
        if v is None:
            return "n.m."
        return f"{v:.1f}x" if v < 100 else f"{v:.0f}x"
    head = ["Company", "Ticker", "Fwd P/E", "EV/EBITDA", "EV/sales"]
    rows = [[n, t, f(a), f(b), f(c)] for n, t, a, b, c in co["peers"]]
    sp = co["self_peer"]
    label = co.get("self_peer_label", SHORT[co["key"]])
    tick = co["ticker"].replace(".SH", " CH").replace(".SZ", " CH").replace(".HK", " HK")
    rows.append([label, tick, f(sp[0]), f(sp[1]), f(sp[2])])
    note = co.get("peer_note", "")
    cap = ("Source: StockAnalysis/S&P Global, 12 Oct 2026 (trailing EV/EBITDA and EV/sales; consensus forward P/E)."
           + (" " + note if note else ""))
    return head, rows, cap


def peer_table(co, m):
    head, rows, cap = peer_rows(co, m)
    ths = "".join(f"<th>{esc(h)}</th>" for h in head)
    trs = ["<tr" + (' class="self"' if i == len(rows) - 1 else "") + ">"
           + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for i, r in enumerate(rows)]
    return (f'<table class="peers"><thead><tr>{ths}</tr></thead><tbody>{"".join(trs)}</tbody></table>'
            f'<div class="cap">{esc(cap)}</div>')


def _cell(v, big, dp=None):
    """Amount cell: parentheses for negatives; 1dp for RMB bn, whole numbers for millions."""
    if v is None:
        return "–"
    if big:
        d = 1 if dp is None else dp
        s = f"{abs(v):,.{d}f}"
    else:
        s = f"{abs(v):,.0f}"
    return f"({s})" if v < 0 else s


def _table(head, rows, cls, est_from=None):
    """Generic numeric table. rows = (label, values, row_class). Columns at/after est_from are shaded."""
    ths = "".join(f'<th class="{"e" if est_from is not None and i >= est_from else ""}">{h}</th>'
                  for i, h in enumerate(head[1:]))
    body = []
    for lab, vals, rc in rows:
        tds = "".join(f'<td class="{"e" if est_from is not None and i >= est_from else ""}">{v}</td>'
                      for i, v in enumerate(vals))
        body.append(f'<tr class="{rc}"><th>{lab}</th>{tds}</tr>')
    return (f'<table class="fin {cls}"><thead><tr><th>{head[0]}</th>{ths}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table>')


def bs_data(co, fa):
    big = co["fin_unit"].endswith("bn")
    b = fa["bs"]
    nc = fa["netcash_h"]
    c = lambda xs: [_cell(x, big) for x in xs]
    rows = [
        ("Cash &amp; short-term investments", c(b["cash"]), ""),
        ("Receivables", c(b["recv"]), ""),
        ("Inventory", c(b["inv"]), ""),
        ("PP&amp;E", c(b["ppe"]), ""),
        ("Total assets", c(b["ta"]), "hl"),
        ("Accounts payable", c(b["ap"]), ""),
        ("Total debt", c(b["debt"]), ""),
        ("Equity (attributable)", c(b["eq"]), "hl"),
        ("Minority interests", c(b["mi"]), ""),
        ("Net cash / (net debt)", c(nc), "hl"),
    ]
    head = [f"Balance sheet ({co['fin_unit']})", "FY23A", "FY24A", "FY25A", "Jun-26A"]
    return head, rows, None


def bs_table(co, fa):
    return _table(*bs_data(co, fa)[:2], "bs")


def cf_data(co, m, fa):
    big = co["fin_unit"].endswith("bn")
    cf = fa["cf"]
    c = lambda xs: [_cell(x, big) for x in xs]
    np_row = m["np"][:3] + [None] + m["np"][3:]
    da = cf["da"] + fa["da_e"]
    ocf = cf["ocf"] + fa["ocf_e"]
    capex = cf["capex"] + [-x for x in fa["capex_e"]]
    fcf = fa["fcf_h"] + fa["fcf_e"]
    div = cf["div"] + [-x for x in fa["div_e"]]
    div = [None if x is None else (0.0 if abs(x) < 1e-9 else x) for x in div]
    nc = fa["netcash_h"] + fa["netcash_e"]          # FY23, FY24, FY25, Jun-26 | FY26E-28E
    ocfnp = fa["ocf_np_h"] + [None] + fa["ocf_np_e"]
    np_lab = "Net profit (attributable)" if co["profile"] == "profit" else co["loss_label"]
    show_div = any(v not in (None, 0.0) for v in div)
    rows = [
        (np_lab, c(np_row), ""),
        ("D&amp;A", c(da), "sub"),
        ("Operating cash flow", c(ocf), "hl"),
        ("Capex", c(capex), ""),
        ("Free cash flow", c(fcf), "hl"),
        ("Dividends paid", c(div), ""),
        ("Net cash / (debt), period-end", c(nc), ""),
    ]
    if not show_div:
        rows = [r for r in rows if r[0] != "Dividends paid"]
    ocfnp_s = [("n.m." if v is None or v <= 0 else f"{v:.2f}") for v in ocfnp]
    if any(v != "n.m." for v in ocfnp_s):
        rows.append(("OCF / net profit (x)", ocfnp_s, "sub"))
    head = [f"Cash flow ({co['fin_unit']})", "FY23A", "FY24A", "FY25A", "TTM Jun-26", "FY26E", "FY27E", "FY28E"]
    return head, rows, 4


def cf_table(co, m, fa):
    return _table(*cf_data(co, m, fa)[:2], "cf", est_from=4)


def ratio_data(co, m, fa):
    def p(xs, dp=1):
        def one(v):
            d = 0 if abs(v) >= 100 else dp
            return f"−{abs(v):,.{d}f}%" if v < 0 else f"{v:,.{d}f}%"
        return ["–" if v is None else one(v) for v in xs]

    def x(xs, dp=2):
        return ["–" if v is None else f"{v:.{dp}f}" for v in xs]

    def d(xs):
        return ["–" if v is None else f"{v:.0f}" for v in xs]

    none3 = [None] * 3
    gm = [(None if v is None else v) for v in m["gm"]]
    nm = [None if v is None else v * 100 for v in m["nm"]]
    rg = [None if v is None else v * 100 for v in m["rev_g"]]
    rows = [
        ("Revenue growth", p(rg, 0), ""),
        ("Gross margin", p(gm), ""),
        ("Net margin", p(nm), ""),
        ("ROE (avg. equity)", p(fa["roe_h"] + fa["roe_e"]), "hl"),
        ("ROA (avg. assets)", p(fa["roa_h"] + none3), ""),
        ("Asset turnover (x)", x(fa["at_h"] + none3), ""),
        ("Receivable days", d(fa["recv_d"] + none3), ""),
        ("Inventory days", d(fa["inv_d"] + none3), ""),
        ("Payable days", d(fa["ap_d"] + none3), ""),
        ("Current ratio (x)", x(fa["cr_h"] + none3), ""),
        ("Net debt / equity", p(fa["nd_eq_h"] + fa["nd_eq_e"], 0), "hl"),
        ("Net debt / EBITDA (x)", x(fa["nd_ebitda_h"] + none3, 1), ""),
        ("Capex / revenue", p(fa["capex_r_h"] + fa["capex_r_e"]), ""),
        ("FCF margin", p(fa["fcf_m_h"] + fa["fcf_m_e"]), ""),
    ]
    if co["profile"] == "profit":
        rows.append(("Dividend payout", p(fa["payout"], 0), ""))
    rows = [r for r in rows if any(v != "–" for v in r[1])]      # drop rows with nothing meaningful
    head = ["Key ratios", "FY23A", "FY24A", "FY25A", "FY26E", "FY27E", "FY28E"]
    return head, rows, 3


def ratio_table(co, m, fa):
    return _table(*ratio_data(co, m, fa)[:2], "rt", est_from=3)


def simple_table(head, rows, cls):
    ths = "".join(f"<th>{esc(h)}</th>" for h in head)
    trs = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="txt {cls}"><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>'


def company_section(idx, co, m):
    ph = m["ph"]
    fa = m["fa"]
    t = {k: fill(co[k], ph) for k in ("headline", "summary", "valuation")}
    thesis = "".join(f"<li>{fill(x, ph)}</li>" for x in co["thesis"])
    risks = "".join(f"<li>{esc(fill(x, ph))}</li>" for x in co["risks"])
    cats = "".join(f"<li>{esc(fill(x, ph))}</li>" for x in co["catalysts"])
    tiles = "".join(f'<div class="tile"><div class="tv">{esc(v)}</div><div class="tl">{esc(l)}</div></div>'
                    for v, l in co["tiles"])
    if co.get("mix"):
        side_fig = (f'<div class="side-h">{esc(co["mix_title"])}</div>' + svg_mix(co["mix"]))
    else:
        kp = "".join(f"<tr><th>{esc(a)}</th><td>{esc(b)}</td></tr>" for a, b in co["kpis"])
        side_fig = f'<div class="side-h">Key operating indicators</div><table class="kd kpi">{kp}</table>'
    unit = co["fin_unit"]
    np_title = "Net profit" if co["profile"] == "profit" else co["loss_label"].replace(" (loss)", "")
    fcf_series = fa["fcf_h"][:3] + fa["fcf_e"]
    cw = 228
    charts = (svg_columns(m["rev"], "Revenue", unit, width=cw, height=150)
              + svg_columns(m["np"], np_title, unit, width=cw, height=150)
              + svg_columns(fcf_series, "Free cash flow", unit, width=cw, height=150))
    tp_line = f'{co["ccy"] if co["ccy"] == "HK$" else "RMB"}{tp_str(m["tp"])}'
    risks_title = co.get("risks_title", "Key risks")
    scen = co["scen"]
    scen_note = (f'Bear ({esc(scen["bear"]["desc"])}): {price_fmt(m["bear"], co["ccy"])}. '
                 f'Bull ({esc(scen["bull"]["desc"])}): {price_fmt(m["bull"], co["ccy"])}.')

    paras = lambda xs: "".join(f"<p>{fill(x, ph)}</p>" for x in xs)
    seg_cols = co.get("segments_cols", ("Segment", "Share of revenue", "Key assets / products", "Economics"))
    seg_tbl = simple_table(seg_cols, co["segments"], "seg")
    comp_tbl = simple_table(("Competitor", "Base", "Focus", "Position vs " + SHORT[co["key"]]),
                            co["competitors"], "comp")
    tam_tbl = simple_table(("Market", "Size", "Growth / dynamics", "Source"), co["tam_table"], "tamt")
    miles = "".join(f"<tr><th>{esc(y)}</th><td>{esc(e)}</td></tr>" for y, e in co["milestones"])
    owner = "".join(f"<tr><th>{esc(a)}</th><td>{esc(b)}</td></tr>" for a, b in co["ownership"])
    moat = "".join(f"<li>{esc(x)}</li>" for x in co["moat"])
    frows = "".join(f'<tr><td>{esc(f)}</td><td><span class="lvl lvl-{lv.split()[-1].lower()}">{esc(lv)}</span></td>'
                    f'<td>{a}</td></tr>' for f, lv, a in FORCES[co["key"]])
    forces_tbl = (f'<table class="txt forces"><thead><tr><th>Force</th><th>Intensity</th><th>Assessment</th></tr>'
                  f'</thead><tbody>{frows}</tbody></table>')
    cf_note = ("TTM = twelve months to June 2026; Jun-26 net cash in the TTM column. E = our estimates: OCF = net "
               "profit + D&amp;A − increase in working capital; net cash rolls forward FCF less dividends plus "
               "equity raised.")
    rt_note = ("ROE/ROA on average balances. Days on year-end balances: receivables on revenue, inventory and payables "
               "on cost of sales. Net debt/equity below zero = net cash. "
               + ("Payout = DPS/EPS. " if co["profile"] == "profit" else "")
               + "n.m./– = not meaningful or not modelled.")
    return f"""
<section class="co" id="{co['key']}">
  <div class="band">
    <div class="band-l">
      <div class="kicker">{idx:02d} · {esc(co['theme'])} · {esc(co['sector'])}</div>
      <h2>{esc(SHORT[co['key']])} <span class="cn">{esc(co['cn'])}</span></h2>
      <div class="tick">{esc(co['ticker'])} · Initiation of coverage · {AS_OF}</div>
    </div>
    <div class="band-r">
      {rating_pill(m['rating'])}
      <div class="tp"><span>TP</span> {tp_line}</div>
      <div class="px">Price {price_fmt(co['price'], co['ccy'])} · {pct(m['up'], 0, sign=True)}</div>
    </div>
  </div>
  <h3 class="headline">{t['headline']}</h3>
  <div class="grid1">
    <div class="main">
      <p class="lede">{t['summary']}</p>
      <ul class="thesis">{thesis}</ul>
      <div class="rc1">
        <div class="sec-h">Catalysts</div><ul>{cats}</ul>
        <div class="sec-h">{esc(risks_title)}</div><ul>{risks}</ul>
      </div>
    </div>
    <aside class="side">
      <div class="side-h">Key data</div>
      {key_data(co, m)}
      {side_fig}
    </aside>
  </div>
  <div class="blk"><div class="sec-h">Key financials and valuation</div>{fin_table(co, m)}
    <div class="cap">A = actual (company reports; StockAnalysis/S&amp;P Global), E = our estimates. Multiples at the
    12-Oct-2026 price{'' if co['ccy'] == 'RMB' else ', converted at HK$1 = RMB0.853' if co['fin_unit'].startswith('RMB') else ', converted at US$1 = HK$7.8475'}.</div></div>

  <div class="qual">
  <div class="sec-h">Company background</div>
  {paras(co['background'])}
  <div class="bg-grid">
    <div><div class="tbl-h">Milestones</div><table class="kd ms">{miles}</table></div>
    <div><div class="tbl-h">Ownership and listing</div><table class="kd own">{owner}</table></div>
  </div>

  <div class="sec-h">The business</div>
  {paras(co['business'])}
  <div class="blk"><div class="tbl-h">{esc(co['segments_title'])}</div>{seg_tbl}</div>

  <div class="sec-h">Competitive landscape</div>
  {paras(co['competition'])}
  <div class="blk"><div class="tbl-h">Main competitors</div>{comp_tbl}</div>
  <div class="blk"><div class="tbl-h">Industry structure: five forces</div>{forces_tbl}</div>
  <div class="blk moat"><div class="tbl-h">Moat and vulnerabilities</div><ul>{moat}</ul></div>

  <div class="sec-h">Addressable market (TAM)</div>
  {paras(co['tam'])}
  {tam_tbl}<div class="tiles">{tiles}</div>
  </div>

  <div class="fa">
  <div class="sec-h">Financial analysis</div>
  <div class="charts blk">{charts}</div>
  <p>{fill(co['fin_is'], ph)}</p>
  <div class="fa-grid blk">
    <div>{bs_table(co, fa)}<div class="cap">Source: company filings via StockAnalysis/S&amp;P Global. Jun-26 = latest
    interim balance sheet. Debt includes leases{'' if co['key'] not in ('horizon', 'minimax') else ' and, pre-IPO, preferred shares carried as liabilities'}.</div></div>
    <div><p>{fill(co['fin_bs'], ph)}</p></div>
  </div>
  <div class="blk">{cf_table(co, m, fa)}<div class="cap">{cf_note}</div></div>
  <p>{fill(co['fin_cf'], ph)}</p>
  <div class="fa-grid rt-grid blk">
    <div>{ratio_table(co, m, fa)}<div class="cap">{rt_note}</div></div>
    <div><p>{fill(co['fin_ratios'], ph)}</p></div>
  </div>
  </div>

  <div class="blk"><div class="sec-h">Valuation</div>
    <div class="val-grid">
      <div>{peer_table(co, m)}</div>
      <div>{svg_scenarios(co, m)}<div class="cap">{scen_note}</div></div>
    </div>
    <p>{t['valuation']}</p>
    <div class="src">Sources: {esc(co['sources'])}</div></div>
</section>"""


# ----------------------------------------------------------------------------- front & back matter
def cover(cos):
    nb = sum(1 for c, m in cos if m["rating"] == "Buy")
    nh = sum(1 for c, m in cos if m["rating"] == "Hold")
    ns = sum(1 for c, m in cos if m["rating"] == "Sell")
    buys = sorted([(m["up"], c) for c, m in cos if m["rating"] == "Buy"], key=lambda x: x[0], reverse=True)[:3]
    picks = ", ".join(f"{SHORT[c['key']]} ({pct(u, 0, sign=True)})" for u, c in buys)
    sells = [SHORT[c["key"]] for c, m in cos if m["rating"] == "Sell"]
    return f"""
<section class="cover">
  <div class="cv-top">Equity Research · China &amp; Hong Kong · Initiation of coverage</div>
  <h1>China &amp; Hong Kong:<br/>17 Initiations</h1>
  <div class="cv-sub">Resources, batteries, semiconductors, robotics, medtech and AI models. Company background, the
  business, competition, TAM, a three-statement financial analysis and valuation in up to five pages each.</div>
  <div class="cv-meta">{AS_OF} · Prices as of the 12-Oct-2026 close</div>
  <div class="cv-stats">
    <div class="tile"><div class="tv">{nb}</div><div class="tl">Buy</div></div>
    <div class="tile"><div class="tv">{nh}</div><div class="tl">Hold</div></div>
    <div class="tile"><div class="tv">{ns}</div><div class="tl">Sell</div></div>
  </div>
  <div class="cv-box">
    <p><b>Highest-conviction Buys:</b> {esc(picks)}. Each pairs earnings growth with a valuation the market has
    de-rated during the September sell-off.</p>
    <p><b>Sell:</b> {esc(', '.join(sells))}: a good company priced at ~200x+ forward earnings for a humanoid-robot
    future that is not yet visible in its numbers.</p>
    <p><b>Holds</b> fall into three groups. Lithium and nickel (Tianqi, Ganfeng, Huayou), where prices are turning
    down. Cyclical winners whose peak earnings look priced in (GigaDevice, China Jushi). Turnaround or mix stories
    awaiting proof (Sungrow, Sieyuan). The two LLM developers (Z.AI, MiniMax) we see as binary, with today's price
    close to our risk-weighted value.</p>
  </div>
  <div class="cv-foot">Built from the source pack <i>"17 China/HK Stocks: Business Model, Performance and Outlook"</i> (6 Oct
  2026), updated with company filings, consensus data and market prices to 12 Oct 2026. AI-assisted research for
  information only; not investment advice. See the methodology and disclosures at the end.</div>
</section>"""


def summary_page(cos):
    rows = []
    for i, (c, m) in enumerate(cos, 1):
        if c["profile"] == "profit":
            v26, v27 = mult(m["pe"][3]), mult(m["pe"][4])
            vlab = "P/E"
        else:
            v26, v27 = mult(m["evs"][3]), mult(m["evs"][4])
            vlab = "EV/S"
        short = SHORT[c["key"]]
        rows.append(f"""<tr><td>{i}</td><td class="nm"><a href="#{c['key']}">{esc(short)}</a> <span class="tk">{esc(c['ticker'])}</span></td>
          <td>{rating_pill(m['rating'])}</td><td>{price_fmt(c['price'], c['ccy'])}</td><td>{price_fmt(m['tp'], c['ccy'])}</td>
          <td>{pct(m['up'], 0, sign=True)}</td><td>{m['mcap_usd']:,.1f}</td><td>{vlab} {v26}</td><td>{v27}</td>
          <td class="hl">{esc(fill(c['headline'], m['ph']))}</td></tr>""")
    return f"""
<section class="summary">
  <div class="sec-h big">Summary of ratings and valuation</div>
  <table class="sum">
    <thead><tr><th>#</th><th>Company</th><th>Rating</th><th>Price</th><th>Target</th><th>Return</th>
    <th>Mkt cap US$bn</th><th>FY26E</th><th>FY27E</th><th>One-line view</th></tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table>
  <div class="cap">Prices are 12-Oct-2026 closes (A-shares in RMB; H-shares in HK$). P/E for H-share-rated names uses the
  H-share price. EV/S = enterprise value / sales for loss-making companies. Ratings: Buy ≥ +20% implied return; Sell
  ≤ −10%; Hold otherwise.</div>
</section>"""


def themes_page(cos):
    chart_rows = sorted([(SHORT[c["key"]], m["up"], m["rating"]) for c, m in cos],
                        key=lambda r: r[1], reverse=True)
    return f"""
<section class="themes">
  <div class="sec-h big">Implied 12-month return to target price</div>
  {svg_upside(chart_rows)}
  <div class="sec-h big" style="margin-top:14pt">Cross-cutting themes</div>
  <div class="two">
    <div>
      <h4>1. Strong H1 numbers, de-rated shares</h4>
      <p>Most of the 17 reported strong H1'26 results, yet the source pack notes every stock trades 28–81% below its
      52-week high. China's CSI 300 fell 5.8% in September on worries about tighter policy in major economies and weak
      domestic demand. Several names (CATL, GigaDevice, Han's Laser, Sungrow) now trade at or near multi-year-low
      multiples on forward earnings.</p>
      <h4>2. The AI capex chain has moved down the stack</h4>
      <p>AI servers are pulling through demand for niche memory (GigaDevice), electronic glass-fibre cloth (China
      Jushi), PCB drilling equipment (Han's Laser), grid equipment (Sieyuan) and storage (CATL, Sungrow). The question
      for each is how long pricing power lasts once capacity responds. We are Buy where order books give visibility
      (Han's) and Hold where earnings already look near peak (GigaDevice, Jushi).</p>
      <h4>3. Lithium has turned again</h4>
      <p>China lithium carbonate fell 24% in September to ~RMB122k/t; Wood Mackenzie expects 2026 supply to grow ~28%,
      and a revised SMM inventory methodology added ~175kt to stock estimates. We model lower H2'26 and FY27 prices for
      Tianqi and Ganfeng, below broker forecasts in the source pack.</p>
    </div>
    <div>
      <h4>4. Strong CNY is a quiet earnings headwind</h4>
      <p>USD/CNH is ~6.69. Exporters with dollar receivables (Sany, Sungrow, Sieyuan) booked FX finance losses in H1'26,
      and dollar-priced commodity producers (Zijin) translate fewer renminbi per unit.</p>
      <h4>5. A/H spreads matter</h4>
      <p>Most H-shares trade at large discounts to their A-shares (JL Mag −46%, Ganfeng −45%, Tianqi −44%, Sany −18%),
      but CATL's H-share trades at a ~41% premium. Where both lines exist we name our preferred line in each report.</p>
      <h4>6. Robotics and AI models: real growth, stretched prices</h4>
      <p>Horizon Robotics and Edge Medical combine fast growth with valuations the market has already cut sharply, so
      we rate them Buy. Leaderdrive (Sell), Z.AI and MiniMax (Hold) price in outcomes several years away.</p>
      <h4>Upcoming dates</h4>
      <p>Q3 results: Ganfeng (mid-Oct), China Jushi 20 Oct, Han's Laser 23 Oct, Sieyuan and Huayou 24 Oct, Tianqi 26 Oct,
      JL Mag 28 Oct, Sungrow and GigaDevice 30 Oct, Leaderdrive 31 Oct.</p>
    </div>
  </div>
</section>"""


def back_matter():
    return """
<section class="back">
  <div class="sec-h big">Methodology</div>
  <p><b>Scope.</b> Each of the 17 companies in the source pack gets an initiation of up to five pages: a summary page
  with rating, thesis, catalysts, risks and key financials; at least two pages on company background, the business,
  the competitive landscape and the addressable market (TAM); a financial analysis covering the income statement,
  balance sheet, cash flow statement and key ratios; and a valuation. They are concise initiations, not full models.</p>
  <p><b>Data.</b> Historical financials (FY23–25 and TTM) come from company filings as compiled by StockAnalysis.com
  (S&amp;P Global Market Intelligence data) and from H1'26 interim reports. Consensus estimates, consensus targets and
  peer multiples are from StockAnalysis/S&amp;P Global as of 12 October 2026 unless a broker is named. Share prices,
  52-week ranges, FX and gold/copper futures are from Interactive Brokers (12-Oct-2026). Industry figures (CCMA, SNE
  Research, Wood Mackenzie, Argus, TrendForce, Frost &amp; Sullivan, IFR, Prismark) are cited as reported by the
  sources named in each note.</p>
  <p><b>Estimates.</b> FY26–28E figures are our own simplified projections of revenue, gross margin and attributable net
  profit (adjusted net profit for loss-makers). EPS uses current shares outstanding. Dividends assume the payout ratios
  stated in each report. Cash flow and balance sheet are projected with a simple roll-forward: operating cash flow =
  net profit + D&amp;A (grown at 10–12% a year, faster for capacity builders) − the increase in net working capital
  (receivables + inventory − payables, at the FY25 ratio to revenue or a stated incremental intensity); free cash flow
  = OCF − our capex assumption; year-end net cash = prior net cash + FCF − dividends paid (prior-year DPS) + equity
  raised. For companies that listed or recapitalised in 2026 (Horizon, Edge Medical, Z.AI, MiniMax) the FY26E
  roll-forward starts from the June 2026 balance sheet. Historical ratios are computed from reported statements:
  ROE and ROA on average balances; working-capital days on year-end balances (receivables on revenue, inventory and
  payables on cost of sales); net debt = total debt (including leases) − cash and short-term investments.</p>
  <p><b>Valuation.</b> Profitable companies use target P/E multiples on FY27E EPS, cross-checked against listed peers
  and the bear/bull scenarios shown. Loss-making growth companies use EV/sales on FY27E (Horizon, Edge Medical) or
  FY28E revenue discounted two years at 15% (Z.AI, MiniMax), plus net cash. Leaderdrive uses capitalised FY30E earnings
  discounted three years at 10%. H-share targets convert RMB values at HK$1 = RMB0.8531; MiniMax at US$1 = HK$7.8475.</p>
  <p><b>Ratings.</b> Buy: implied 12-month return ≥ +20%. Hold: between −10% and +20%. Sell: ≤ −10%. Ratings are
  derived mechanically from the target price.</p>

  <div class="sec-h big">Key sources</div>
  <ul class="srcs">
    <li>Source pack: "17 China/HK Stocks: Business Model, Performance and Outlook" (6 October 2026), including citations
    to CMBI, UOB Kay Hian, Futu/Moomoo, Longbridge, Tiger Brokers, Simply Wall St, Gasgoo, Gawin Research, Venture Atlas,
    Magica, The Standard and HKEX filings.</li>
    <li>Company results: Zijin (FY25, H1'26, 2026–28 plan), CATL (FY25, H1'26), Sany (FY25 release), GigaDevice (FY25,
    H1'26), Huayou (FY25, Q1'26), Sungrow (FY25), Sieyuan (FY25 express), Han's Laser (FY25), JL Mag, China Jushi, Tianqi,
    Ganfeng and Leaderdrive (H1'26), Horizon Robotics (FY25 annual results, H1'26 HKEX interim results), Edge Medical
    (H1'26 HKEX interim results), Z.AI (FY25 results via Reuters/SCMP; September 2026 placement and CB terms via
    DealStreetAsia/The Standard), MiniMax (FY25 results release).</li>
    <li>Market data: Interactive Brokers (equity prices, USD/CNH, USD/HKD, COMEX gold and copper); StockAnalysis.com
    (statistics, income statements, forecasts, peer multiples).</li>
    <li>Industry: CCMA excavator data (via Mysteel/Yieh), SNE Research (via company/press), Wood Mackenzie inverter
    rankings and lithium supply, Argus (Indonesian MHP), TrendForce (NOR prices), Frost &amp; Sullivan (specialty memory),
    Trading Economics/SMM (lithium carbonate), Benchmark/SMM (NdPr), IGO ASX quarterlies (Greenbushes/Kwinana).</li>
  </ul>

  <div class="sec-h big">Important disclosures</div>
  <p class="disc">This document was prepared with the assistance of an AI model, using public information and the source
  pack the user provided. It is research and analysis for information only, not personalised financial advice or an
  offer to buy or sell any security. Figures may contain errors, and some inputs (e.g. net cash for recently listed
  companies, segment splits, industry market sizes) are estimates, labelled as such. Estimates, targets and ratings are
  the author's views at the date of publication and may change without notice. Securities discussed may be volatile,
  illiquid or subject to foreign-exchange, regulatory and geopolitical risks; A- and H-share lines of the same company
  can trade at very different prices. Past performance is not a guide to future returns. Readers should verify key
  figures against primary filings and consult a qualified financial adviser before making investment decisions.</p>
</section>"""


CSS = """
@page { size: Letter; margin: 0.62in 0.55in 0.62in 0.55in; }
* { box-sizing: border-box; }
:root { --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --grid:#e1e0d9; --axis:#c3c2b7; --accent:#104281;
        --blue:#2a78d6; --wash:#eef4fc; --page:#ffffff; }
html, body { background: var(--page); color: var(--ink); }
body { font-family: "Inter", system-ui, sans-serif; font-size: 8.55pt; line-height: 1.42; margin: 0;
       font-feature-settings: "ss01" 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
p { margin: 0 0 5pt 0; text-align: left; }
a { color: inherit; text-decoration: none; }
b { font-weight: 600; }
.cn { font-family: "WenQuanYi Zen Hei", sans-serif; font-weight: 400; color: var(--ink2); font-size: 0.72em; margin-left: 4pt;
      white-space: nowrap; }
h1, h2, h3, h4 { margin: 0; font-weight: 600; letter-spacing: -0.01em; }

/* cover */
.cover { break-after: page; padding-top: 1.1in; }
.cv-top { color: var(--accent); font-weight: 600; font-size: 9pt; letter-spacing: 0.04em; text-transform: uppercase; }
.cover h1 { font-size: 34pt; line-height: 1.08; margin: 14pt 0 12pt; color: var(--ink); }
.cv-sub { font-size: 12pt; color: var(--ink2); max-width: 5.6in; line-height: 1.4; }
.cv-meta { margin-top: 12pt; font-size: 9.5pt; color: var(--muted); }
.cv-stats { display: flex; gap: 10pt; margin: 26pt 0 18pt; }
.cv-stats .tile { width: 1.1in; }
.cv-stats .tv { font-size: 24pt; }
.cv-box { border-top: 2px solid var(--accent); padding-top: 10pt; font-size: 10pt; line-height: 1.5; max-width: 6.6in; }
.cv-box p { margin-bottom: 8pt; }
.cv-foot { margin-top: 0.8in; font-size: 8pt; color: var(--muted); max-width: 6.4in; }

/* summary */
.summary, .themes { break-after: page; }
.sec-h { font-weight: 600; font-size: 9.6pt; color: var(--accent); margin: 9pt 0 3pt; padding-bottom: 2pt;
         border-bottom: 1px solid var(--grid); break-after: avoid; }
.sec-h.big { font-size: 13pt; margin: 0 0 8pt; border-bottom: 2px solid var(--accent); }
table { border-collapse: collapse; width: 100%; font-variant-numeric: tabular-nums; }
.sum th, .sum td { padding: 3.2pt 4pt; border-bottom: 1px solid var(--grid); vertical-align: top; text-align: left; font-size: 7.8pt; }
.sum th { color: var(--ink2); font-weight: 600; border-bottom: 1px solid var(--axis); }
.sum td:nth-child(n+4):nth-child(-n+9) { white-space: nowrap; }
.sum .tk { color: var(--muted); font-size: 6.8pt; white-space: nowrap; }
.sum td.nm a { font-weight: 600; }
.sum td.hl { color: var(--ink2); font-size: 7.4pt; }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 20pt; }
.two h4 { font-size: 9.5pt; margin: 8pt 0 3pt; }

/* pill */
.pill { display: inline-block; padding: 1.5pt 7pt; border-radius: 10pt; font-weight: 600; font-size: 7.6pt;
        letter-spacing: 0.02em; }
.pill-buy { background: #e3f3e3; color: #006300; }
.pill-hold { background: #ecebe6; color: #3d3c39; }
.pill-sell { background: #fbe4e4; color: #b02a2a; }

/* company */
.co { break-before: page; }
.band { display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 2.5px solid var(--accent);
        padding-bottom: 6pt; }
.kicker { font-size: 7.4pt; color: var(--accent); font-weight: 600; letter-spacing: 0.03em; text-transform: uppercase; }
.band h2 { font-size: 17pt; margin: 3pt 0 2pt; }
.tick { font-size: 8pt; color: var(--ink2); }
.band-r { text-align: right; min-width: 1.7in; }
.band-r .pill { font-size: 9pt; padding: 2pt 10pt; }
.band-r .tp { font-size: 14pt; font-weight: 600; margin-top: 3pt; }
.band-r .tp span { font-size: 8pt; color: var(--ink2); font-weight: 500; }
.band-r .px { font-size: 8pt; color: var(--ink2); }
.headline { font-size: 11.6pt; margin: 8pt 0 6pt; color: var(--ink); line-height: 1.3; }
.grid1 { display: grid; grid-template-columns: 1fr 2.62in; gap: 14pt; }
.lede { font-size: 8.9pt; }
.thesis { margin: 2pt 0 0 0; padding-left: 12pt; }
.thesis li { margin-bottom: 4.5pt; }
.side { border-left: 1px solid var(--grid); padding-left: 10pt; }
.side-h { font-weight: 600; font-size: 8.2pt; color: var(--accent); margin: 0 0 3pt; }
.side svg { margin-bottom: 4pt; }
.kd th, .kd td { font-size: 7.4pt; padding: 1.6pt 0; border-bottom: 1px solid var(--grid); text-align: left;
                 vertical-align: top; }
.kd th { color: var(--ink2); font-weight: 500; width: 46%; padding-right: 4pt; }
.kd td { font-weight: 500; }
.kd { margin-bottom: 8pt; }
.kpi th { width: 52%; }
.fin th, .fin td { font-size: 7.6pt; padding: 2pt 4pt; border-bottom: 1px solid var(--grid); text-align: right; }
.fin thead th { color: var(--ink2); font-weight: 600; border-bottom: 1px solid var(--axis); }
.fin tbody th { text-align: left; font-weight: 500; color: var(--ink); width: 30%; }
.fin .e { background: var(--wash); }
.fin tr.sub th, .fin tr.sub td { color: var(--ink2); font-size: 7.2pt; }
.fin tr.hl th, .fin tr.hl td { font-weight: 600; }
.cap { font-size: 6.9pt; color: var(--muted); margin-top: 2pt; line-height: 1.35; }
.blk { break-inside: avoid; }
.tiles { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8pt; margin: 4pt 0 2pt; break-inside: avoid; }
.tile { border: 1px solid var(--grid); border-radius: 6pt; padding: 6pt 8pt; background: #fbfbfa; }
.tv { font-size: 12.5pt; font-weight: 600; color: var(--ink); line-height: 1.15; }
.tl { font-size: 7.1pt; color: var(--ink2); margin-top: 2pt; line-height: 1.3; }
.charts { display: flex; justify-content: space-between; margin: 2pt 0 4pt; }
.val-grid { display: grid; grid-template-columns: 1fr 318px; gap: 14pt; align-items: start; margin-bottom: 4pt; }
.peers th, .peers td { font-size: 7.3pt; padding: 2pt 3pt; border-bottom: 1px solid var(--grid); text-align: right; }
.peers th:first-child, .peers td:first-child, .peers th:nth-child(2), .peers td:nth-child(2) { text-align: left; }
.peers thead th { color: var(--ink2); font-weight: 600; border-bottom: 1px solid var(--axis); }
.peers tr.self td { font-weight: 600; background: var(--wash); }
.rc1 ul { margin: 0; padding-left: 12pt; }
.rc1 li { margin-bottom: 1.5pt; font-size: 8pt; }
.rc1 .sec-h { margin-top: 7pt; }
.src { font-size: 6.9pt; color: var(--muted); margin-top: 6pt; border-top: 1px solid var(--grid); padding-top: 3pt; }

/* v2: long-form sections and three-statement tables */
.qual p, .fa p { margin-bottom: 4.5pt; }
.tbl-h { font-weight: 600; font-size: 7.8pt; color: var(--ink2); margin: 5pt 0 2pt; break-after: avoid; }
.bg-grid { display: grid; grid-template-columns: 1.6fr 1fr; gap: 14pt; margin: 0 0 2pt; break-inside: avoid; }
.kd.ms th { width: 0.72in; white-space: nowrap; }
.kd.own th { width: 38%; }
.kd.ms, .kd.own { margin-bottom: 2pt; }
table.txt th, table.txt td { font-size: 7.2pt; padding: 2pt 4pt 2pt 0; border-bottom: 1px solid var(--grid);
                             text-align: left; vertical-align: top; line-height: 1.32; }
table.txt thead th { color: var(--ink2); font-weight: 600; border-bottom: 1px solid var(--axis); }
table.txt tr, .fin tr { break-inside: avoid; }
table.txt td:first-child { font-weight: 600; width: 19%; }
.seg td:nth-child(2) { width: 11%; }
.comp td:nth-child(2) { width: 12%; }
.tamt td:nth-child(2) { width: 19%; }
.tamt td:nth-child(4) { color: var(--ink2); width: 22%; }
.forces td:nth-child(2) { width: 10%; white-space: nowrap; }
.forces td:first-child { width: 15%; }
.lvl { display: inline-block; padding: 0 5pt; border-radius: 8pt; font-size: 6.8pt; font-weight: 600; }
.lvl-high { background: #fbe4e4; color: #b02a2a; }
.lvl-medium { background: #fdf0d8; color: #8a5a00; }
.lvl-low { background: #e3f3e3; color: #006300; }
.moat ul { margin: 0; padding-left: 12pt; }
.moat li { margin-bottom: 1.5pt; }
.fa .charts { margin: 0 0 3pt; }
.fa-grid { display: grid; grid-template-columns: 3.7in 1fr; gap: 12pt; align-items: start; margin: 3pt 0 4pt; }
.rt-grid { grid-template-columns: 4.3in 1fr; }
.fin.bs th, .fin.bs td, .fin.cf th, .fin.cf td, .fin.rt th, .fin.rt td { font-size: 7.2pt; padding: 1.5pt 4pt; }
.fin.bs tbody th { width: 40%; }
.fin.cf tbody th { width: 27%; }
.fin.rt tbody th { width: 33%; }
.fin.cf, .fin.bs, .fin.rt { margin-top: 2pt; }

/* chart text (text tokens, never series colours) */
svg.chart { display: block; overflow: visible; font-family: "Inter", system-ui, sans-serif; }
.t-title { font-size: 8.4px; font-weight: 600; fill: #0b0b0b; }
.t-sub { font-size: 7px; fill: #898781; }
.t-leg { font-size: 7px; fill: #52514e; }
.t-tick { font-size: 6.8px; fill: #898781; font-variant-numeric: tabular-nums; }
.t-lab { font-size: 7.2px; fill: #52514e; }
.t-val { font-size: 7.2px; font-weight: 600; fill: #0b0b0b; font-variant-numeric: tabular-nums; }

/* back matter */
.back { break-before: page; }
.back p { margin-bottom: 6pt; }
.srcs { padding-left: 12pt; }
.srcs li { margin-bottom: 4pt; }
.disc { font-size: 7.8pt; color: var(--ink2); }
"""


def load():
    """All 17 companies in report order as (company dict, computed model) pairs."""
    allc = {c["key"]: c for c in RES + BAT + TECH}
    assert set(allc) == set(ORDER), set(allc) ^ set(ORDER)
    v2 = {**v2_resources.V2, **v2_battery.V2, **v2_semis.V2, **v2_growth.V2}
    assert set(v2) == set(ORDER), set(v2) ^ set(ORDER)
    for k, extra in v2.items():
        allc[k].update(extra)
        for sec, paras in EXTRA.get(k, {}).items():
            allc[k][sec] = list(allc[k][sec]) + paras
    cos = []
    for k in ORDER:
        m = compute(allc[k])
        compute_fin(allc[k], m)
        cos.append((allc[k], m))
    return cos


def main():
    cos = load()
    sections = [company_section(i, c, m) for i, (c, m) in enumerate(cos, 1)]
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>China &amp; HK: 17 Initiations</title>
<style>{CSS}</style></head>
<body>
{cover(cos)}
{summary_page(cos)}
{themes_page(cos)}
{''.join(sections)}
{back_matter()}
</body></html>"""
    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(doc)
    # console summary for checking
    for c, m in cos:
        print(f"{c['key']:12s} {m['rating']:4s} TP {m['tp']:>8} px {c['price']:>8} up {m['up'] * 100:6.1f}%  "
              f"bear {m['bear']:8.2f} bull {m['bull']:8.2f}  eps27 {m['eps'][4]}")


if __name__ == "__main__":
    main()
