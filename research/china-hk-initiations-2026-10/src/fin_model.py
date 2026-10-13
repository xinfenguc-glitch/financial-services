"""Simplified three-statement analysis: historical ratios from reported statements and FY26-28E
cash-flow / balance-sheet roll-forward driven by the P&L estimates in co_*.py.

Conventions
- Units follow each company's `fin_unit` (RMB bn, RMB m or US$ m); fin_data.py is in millions and is scaled here.
- OCF(E) = net profit + D&A - increase in net working capital (receivables + inventory - payables, held at the
  FY25 ratio to revenue). D&A grows at `da_g` a year. Capex comes from ASSUME.
- Net cash(E) = prior net cash + FCF - dividends paid (prior-year DPS x shares) + equity raised (+ non-cash
  conversion of preferred shares that were carried as debt).
- 'h2' mode (2026 IPOs/recapitalisations): FY26E closing net cash = Jun-26 reported net cash + half of FY26E FCF
  + equity raised in H2'26.
"""

from fin_data import FIN, EBITDA

# Per-company forecast assumptions (fin units). capex = positive spend for FY26E-28E.
ASSUME = dict(
    zijin=dict(capex=[36.0, 38.0, 38.0], da_g=0.12),
    catl=dict(capex=[60.0, 60.0, 55.0], da_g=0.12),
    sany=dict(capex=[3.0, 3.2, 3.4], nwc_inc=0.12),
    sieyuan=dict(capex=[1.2, 1.3, 1.4], nwc_inc=0.25),
    sungrow=dict(capex=[3.5, 3.8, 4.0], nwc_inc=0.15),
    huayou=dict(capex=[15.0, 10.0, 8.0]),
    tianqi=dict(capex=[3.5, 3.5, 3.0], eqiss=[2.6, 0, 0]),
    ganfeng=dict(capex=[6.0, 5.0, 5.0], nwc_inc=0.20),
    gigadevice=dict(capex=[1.8, 1.8, 1.6], eqiss=[4.8, 0, 0], nwc_inc=0.15),
    jushi=dict(capex=[4.0, 4.0, 3.0], nwc_inc=0.25),
    jlmag=dict(capex=[1.0, 1.2, 1.0], nwc_inc=0.20),
    hans=dict(capex=[0.9, 1.0, 1.1], nwc_inc=0.25),
    horizon=dict(capex=[0.6, 0.7, 0.8], mode="h2", nwc_inc=0.40),
    leaderdrive=dict(capex=[250.0, 250.0, 200.0], nwc_inc=0.40),
    edge=dict(capex=[80.0, 100.0, 60.0], mode="h2", nwc_inc=0.40),
    zai=dict(capex=[1500.0, 2500.0, 3000.0], mode="h2", eqiss_h2=40200.0),
    minimax=dict(capex=[250.0, 300.0, 300.0], mode="h2"),
)


def _scale(co):
    return 1000.0 if co["fin_unit"].endswith("bn") else 1.0


def _avg(a, b):
    if a is None or b is None:
        return None
    return (a + b) / 2


def fin_analysis(co, m):
    """Returns dict of historical BS/CF tables, ratios and FY26-28E cash-flow/BS roll-forward."""
    key = co["key"]
    f = FIN[key]
    s = _scale(co)
    a = ASSUME[key]
    bs = {k: [None if v is None else v / s for v in vals] for k, vals in f["bs"].items()}
    cf = {k: [None if v is None else v / s for v in vals] for k, vals in f["cf"].items()}
    rev, gm, npf = m["rev"], m["gm"], m["np"]
    shares = co["shares"]

    # ---------------- history (FY23A, FY24A, FY25A) ----------------
    netcash_h = [c - d for c, d in zip(bs["cash"], bs["debt"])]          # FY23, FY24, FY25, Jun-26
    fcf_h = [o + c for o, c in zip(cf["ocf"], cf["capex"])]             # FY23, FY24, FY25, TTM
    cogs = [r * (1 - g / 100) if (r is not None and g is not None) else None for r, g in zip(rev, gm)]

    def days(num, den):
        return [None if (n is None or d in (None, 0)) else n / d * 365 for n, d in zip(num, den)]

    recv_d = days(bs["recv"][:3], rev[:3])
    inv_d = days(bs["inv"][:3], cogs[:3])
    ap_d = days(bs["ap"][:3], cogs[:3])
    eq = bs["eq"]
    ta = bs["ta"]
    roe_h, roa_h = [], []
    for i in range(3):
        e_avg = eq[i] if i == 0 else _avg(eq[i - 1], eq[i])
        t_avg = ta[i] if i == 0 else _avg(ta[i - 1], ta[i])
        roe_h.append(npf[i] / e_avg * 100 if (npf[i] is not None and e_avg and e_avg > 0) else None)
        roa_h.append(npf[i] / t_avg * 100 if (npf[i] is not None and t_avg) else None)
    cr_h = [ca / cl if cl else None for ca, cl in zip(bs["ca"][:3], bs["cl"][:3])]
    nd_eq_h = [(-nc / e * 100) if (e and e > 0) else None for nc, e in zip(netcash_h[:3], eq[:3])]
    ebitda = EBITDA.get(key)
    nd_ebitda_h = ([(-nc / (eb / s)) if eb and eb > 0 else None for nc, eb in zip(netcash_h[:3], ebitda)]
                   if ebitda else [None] * 3)
    ocf_np_h = [o / n if (n and n > 0) else None for o, n in zip(cf["ocf"][:3], npf[:3])]
    fcf_m_h = [fc / r * 100 if r else None for fc, r in zip(fcf_h[:3], rev[:3])]
    capex_r_h = [-c / r * 100 if r else None for c, r in zip(cf["capex"][:3], rev[:3])]
    at_h = []
    for i in range(3):
        t_avg = ta[i] if i == 0 else _avg(ta[i - 1], ta[i])
        at_h.append(rev[i] / t_avg if t_avg else None)

    # ---------------- forecasts (FY26E-28E) ----------------
    nwc25 = bs["recv"][2] + bs["inv"][2] - bs["ap"][2]
    nwc_pct = nwc25 / rev[2] if rev[2] else 0
    nwc_inc = a.get("nwc_inc", nwc_pct)          # incremental NWC intensity on revenue growth
    da = [cf["da"][2]]
    for _ in range(3):
        da.append(da[-1] * (1 + a.get("da_g", 0.10)))
    da = da[1:]
    capex = a["capex"]
    eqiss = a.get("eqiss", [0, 0, 0])
    dps = m["dps"]
    ocf_e, fcf_e, div_e, netcash_e, eq_e = [], [], [], [], []
    prev_rev = rev[2]
    prev_nc = netcash_h[2]
    prev_eq = eq[2]
    mode = a.get("mode", "fy")
    for i in range(3):
        r, n = rev[3 + i], npf[3 + i]
        d_nwc = nwc_inc * (r - prev_rev)
        ocf = n + da[i] - d_nwc
        fcf = ocf - capex[i]
        prev_dps = dps[2 + i]
        div = (prev_dps or 0) * shares
        if mode == "h2" and i == 0:
            nc = netcash_h[3] + 0.5 * fcf + a.get("eqiss_h2", 0)
            e_close = eq[3] + 0.5 * n + a.get("eqiss_h2", 0)
        else:
            nc = prev_nc + fcf - div + eqiss[i]
            e_close = prev_eq + n - div + eqiss[i]
        ocf_e.append(ocf)
        fcf_e.append(fcf)
        div_e.append(div)
        netcash_e.append(nc)
        eq_e.append(e_close)
        prev_rev, prev_nc, prev_eq = r, nc, e_close

    roe_e = []
    eq_series = [eq[2]] + eq_e
    for i in range(3):
        avg = _avg(eq_series[i], eq_series[i + 1])
        n = npf[3 + i]
        roe_e.append(n / avg * 100 if (avg and avg > 0 and n > 0 and co["profile"] == "profit") else None)
    nd_eq_e = [(-nc / e * 100) if e > 0 else None for nc, e in zip(netcash_e, eq_e)]
    ocf_np_e = [o / n if n > 0 else None for o, n in zip(ocf_e, npf[3:])]
    fcf_m_e = [fc / r * 100 for fc, r in zip(fcf_e, rev[3:])]
    capex_r_e = [c / r * 100 for c, r in zip(capex, rev[3:])]
    bvps = [e / shares for e in eq_e]

    return dict(
        bs=bs, cf=cf, netcash_h=netcash_h, fcf_h=fcf_h,
        recv_d=recv_d, inv_d=inv_d, ap_d=ap_d, roe_h=roe_h, roa_h=roa_h, cr_h=cr_h, nd_eq_h=nd_eq_h,
        nd_ebitda_h=nd_ebitda_h, ocf_np_h=ocf_np_h, fcf_m_h=fcf_m_h, capex_r_h=capex_r_h, at_h=at_h,
        nwc_pct=nwc_pct * 100, da_e=da, capex_e=capex, ocf_e=ocf_e, fcf_e=fcf_e, div_e=div_e,
        netcash_e=netcash_e, eq_e=eq_e, roe_e=roe_e, nd_eq_e=nd_eq_e, ocf_np_e=ocf_np_e, fcf_m_e=fcf_m_e,
        capex_r_e=capex_r_e, bvps_e=bvps,
    )
