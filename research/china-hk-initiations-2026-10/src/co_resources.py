"""Industrials & resources: Zijin Mining, Sany Heavy, Sieyuan Electric.

Units: financial figures in RMB bn unless `fin_unit` says otherwise.
Placeholders in text ({tp}, {eps27}, ...) are filled by build.py from the model.
"""

ZIJIN = dict(
    key="zijin", name="Zijin Mining Group", cn="紫金矿业", ticker="601899.SH",
    listing="H-share 2899.HK at HK$32.58 (~8% discount to A)",
    sector="Metals & Mining", theme="Industrials & resources",
    ccy="RMB", price=30.22, hi52=44.29, lo52=24.42, ytd=-11.5,
    fin_unit="RMB bn", fx=1.0, shares=26.6,
    mcap_local=783.6, mcap_ccy="RMB", net_cash=-53.7, ev=904.5,
    profile="profit",
    hist=dict(rev=[293.40, 303.64, 349.08], gm=[15.8, 20.3, 27.7],
              np=[21.12, 32.04, 51.78], eps=[0.80, 1.20, 1.91], dps=[0.25, 0.38, 0.60]),
    est=dict(rev=[405.0, 435.0, 465.0], gm=[34.0, 35.0, 35.0],
             np=[82.0, 92.0, 101.0], payout=0.35),
    tp_method=dict(type="pe", mult=12, yr=1),
    scen=dict(
        bear=dict(type="pe", eps=2.60, mult=10, desc="Gold US$3,500/oz, copper US$11,000/t"),
        bull=dict(type="pe", eps=4.00, mult=13, desc="Gold US$4,800/oz, copper US$16,000/t"),
    ),
    cons=dict(tp=47.90, n=15, eps26=3.10, eps27=3.59, ratings="12 Strong Buy / 3 Buy"),
    mix_title="H1'26 revenue mix by product (%)",
    mix=[("Gold", 41.2), ("Copper", 32.6), ("Refining, trading & other", 19.0),
         ("Zinc / lead", 3.0), ("Lithium", 2.2), ("Silver", 2.0)],
    tiles=[("~US$400bn", "Global refined copper market (~27Mt at ~US$14.9k/t)"),
           ("~US$485bn", "Annual gold mine supply (~3,600t at ~US$4,195/oz)"),
           ("130–140t / 1.5–1.6Mt", "Zijin's 2028 gold / copper output targets")],
    peers=[("Freeport-McMoRan", "FCX US", 19.3, 11.7, 4.3),
           ("Newmont", "NEM US", 13.4, 7.0, 4.6),
           ("CMOC Group", "603993 CH", 11.0, 6.0, 1.5)],
    self_peer=(9.1, 7.4, 2.4),
    headline="Volume growth few miners can match, at a single-digit multiple",
    summary=("Zijin is China's largest diversified miner and one of the few majors still growing mined "
             "copper and gold output by double digits. At {pe26}x FY26E and {pe27}x FY27E P/E it trades at a "
             "steep discount to global peers despite superior growth and moderate leverage. We initiate at "
             "<b>{rating}</b> with a TP of RMB{tp} ({up} upside), based on 12x FY27E EPS."),
    thesis=[
        "Few majors can match Zijin's output growth. The 2026 plan targets ~105t of mined gold (+17%) and 1.2Mt of copper "
        "(+10%), rising to 130–140t and 1.5–1.6Mt by 2028, a ~13% copper CAGR while most Western peers are flat.",
        "Metal prices and cash generation are both at records. Gold at ~US$4,200/oz and COMEX copper at ~US$6.77/lb "
        "(~US$14,900/t) drove H1'26 net profit of RMB39.2bn (+68%) and operating cash flow of RMB55.5bn (+92%).",
        "The valuation gap to global peers looks unjustified. Zijin trades on {pe27}x FY27E vs ~19x for Freeport and "
        "~13x for Newmont, and a 35% payout target supports a ~{dy26} FY26E dividend yield.",
    ],
    background=(
        "Founded in 1993 around the Zijinshan gold-copper deposit in Shanghang, Fujian, Zijin grew under geologist-founder "
        "Chen Jinghe from a county gold mine into a global group with mines on five continents. It listed H-shares in Hong "
        "Kong in 2003 and A-shares in Shanghai in 2008; its largest shareholder is Minxi Xinghang, the Shanghang county "
        "state-asset vehicle. Core assets include Kamoa-Kakula (DRC, with Ivanhoe), the Serbian copper complex (Bor and "
        "Čukaru Peki), Julong copper in Tibet, and gold mines in Colombia, Suriname, Australia and Kazakhstan. In 2025 its "
        "overseas gold assets were spun out as Zijin Gold International in Hong Kong, in which Zijin keeps control."),
    model=(
        "Zijin earns the spread between metal prices and its unit costs on self-mined output, which generates most of its "
        "gross profit. Refining and trading add revenue at thin margins (the 19% 'other' slice in the mix chart). Its edge "
        "is in-house geology and mining engineering. That lets it buy under-developed or distressed deposits cheaply, often "
        "in higher-risk jurisdictions, then build them faster and at lower capital cost than peers. Gold (41% of H1'26 sales) "
        "and copper (33%) dominate; zinc/lead, silver and a fast-growing lithium arm (H1 output up ~5x) make up the rest. "
        "Operating cash flow funds greenfield expansion, bolt-on M&A and a 35% dividend payout."),
    competition=(
        "In copper, Zijin's 1.09Mt of 2025 mined output places it among the world's top five producers, alongside BHP, "
        "Freeport and Codelco; in gold, ~90t (~2.9Moz) puts it in the global top ten behind Newmont, Barrick and Agnico "
        "Eagle. Management targets a top-three ranking in both by 2028. Compared with Western majors, it grows faster, "
        "spends less capital per tonne and has Chinese bank funding. The trade-offs are a riskier footprint (DRC, Serbia, "
        "Colombia, Suriname) and a lower payout. Domestic comparables are CMOC (copper/cobalt) and Shandong Gold/Zhaojin "
        "(gold)."),
    tam=(
        "Zijin's addressable market is global mined copper and gold supply. Refined copper consumption runs at ~27Mt a "
        "year (~US$400bn at current prices). Electrification, grid build-out and AI data-centre power demand are colliding "
        "with declining ore grades and slow mine development, which supports a structural deficit narrative. Annual gold "
        "mine supply of ~3,600t is worth ~US$485bn at today's price, with central-bank and ETF demand underpinning prices. "
        "Zijin's 2026 targets equal roughly 4–5% of world copper and ~3% of world gold mine supply."),
    financials=(
        "Revenue rose from RMB293bn (FY23) to RMB349bn (FY25), but the bigger change is margin. Gross margin expanded "
        "from 15.8% to 27.7%, and to 34.6% on a TTM basis, as prices rose and self-mined volumes grew. Net profit rose "
        "2.5x in two years to RMB51.8bn in FY25. H1'26 delivered RMB39.2bn (+68%) with a reported ROE of 19.6%. Net debt "
        "of ~RMB54bn is only ~0.4x TTM EBITDA of RMB122bn, and S&P projects debt/EBITDA of ~0.9–1.0x. We forecast net "
        "profit of RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E. That assumes flat-to-slightly-lower gold and copper "
        "prices, so volume does the work. Rough sensitivities: US$100/oz on gold moves annual net profit by ~RMB1.6bn "
        "(~2%); US$1,000/t on copper moves it by ~RMB5.5bn (~6%)."),
    valuation=(
        "Our TP of RMB{tp} is 12x FY27E EPS of RMB{eps27}, roughly a 20% discount to the average forward P/E of Freeport, "
        "Newmont and CMOC (~14.6x) to reflect jurisdictional risk. It still implies only ~8x FY27E EV/EBITDA versus ~12x "
        "for Freeport. The consensus average target is RMB47.90 (15 analysts, all Buy-rated). Our bear case (RMB{bear}) "
        "assumes gold at US$3,500/oz and copper at US$11,000/t; our bull case (RMB{bull}) assumes US$4,800/oz and "
        "US$16,000/t. The H-share (2899.HK) gives the same exposure at an ~8% discount."),
    risks=[
        "Metal prices: a 15–20% fall in gold and copper would cut FY27E EPS by roughly a quarter.",
        "Jurisdiction and operating risk in the DRC, Serbia, Colombia and Suriname (permits, export rules, tax).",
        "CNY strength (USD/CNY ~6.69) compresses RMB-reported margins on dollar-priced metal.",
        "M&A discipline: acquisitive growth raises the risk of overpaying near cycle highs.",
    ],
    catalysts=[
        "Q3'26 results (late October) and 2027 production guidance.",
        "Ramp-up of Julong phase II, Kamoa-Kakula expansions and lithium projects.",
        "Dividend delivery against the 35% payout target.",
    ],
    sources="Company interim/annual reports and 2026–28 production plan; S&P Global Ratings; StockAnalysis/S&P Global "
            "(consensus, multiples); IBKR (prices, gold/copper futures); source pack.",
)

SANY = dict(
    key="sany", name="Sany Heavy Industry", cn="三一重工", ticker="600031.SH",
    listing="H-share 6031.HK at HK$16.93 (~18% discount to A)",
    sector="Machinery", theme="Industrials & resources",
    ccy="RMB", price=17.52, hi52=24.29, lo52=16.68, ytd=-17.2,
    fin_unit="RMB bn", fx=1.0, shares=9.15,
    mcap_local=158.1, mcap_ccy="RMB", net_cash=38.1, ev=121.1,
    profile="profit",
    hist=dict(rev=[74.02, 78.38, 89.70], gm=[27.0, 26.9, 27.8],
              np=[4.53, 5.96, 8.41], eps=[0.53, 0.70, 0.98], dps=[0.22, 0.36, 0.49]),
    est=dict(rev=[104.5, 117.0, 128.0], gm=[28.0, 28.5, 29.0],
             np=[10.3, 12.8, 14.8], payout=0.50),
    tp_method=dict(type="pe", mult=16, yr=1),
    scen=dict(
        bear=dict(type="pe", eps=1.15, mult=12, desc="Domestic relapse; FX losses persist"),
        bull=dict(type="pe", eps=1.60, mult=17.5, desc="China upcycle plus 20%+ overseas growth"),
    ),
    cons=dict(tp=26.72, n=19, eps26=1.17, eps27=1.52, ratings="12 Strong Buy / 6 Buy / 1 Hold"),
    mix_title="FY25 revenue by region (%, approx.)",
    mix=[("China", 37), ("Asia-Pacific", 27), ("Europe", 14), ("Americas", 12), ("Africa", 9)],
    tiles=[("235,257", "China excavator sales in 2025 (+17%), about half exported"),
           ("+24%", "China excavator sales growth, Jan–Aug 2026 (CCMA)"),
           ("~64%", "Overseas share of Sany revenue, FY25")],
    peers=[("Caterpillar", "CAT US", 27.8, 25.4, 5.5),
           ("Komatsu", "6301 JP", 15.7, 10.4, 1.8),
           ("XCMG", "000425 CH", 8.5, 8.9, 1.0)],
    self_peer=(15.2, 8.4, 1.2),
    headline="A global share-taker at a trough multiple, with overseas now driving earnings",
    summary=("Sany is China's largest construction-machinery maker and one of the world's top five or six OEMs, with "
             "61% of H1'26 revenue earned outside China. Profit quality is improving (H1'26 EBIT +56%), but FX finance "
             "costs masked it at the net line. At {pe27}x FY27E P/E with ~RMB38bn of net cash, we initiate at "
             "<b>{rating}</b> with a TP of RMB{tp} ({up} upside) on 16x FY27E EPS."),
    thesis=[
        "The overseas expansion is structural. Sales outside China were ~64% of FY25 revenue and earned a 32.5% gross "
        "margin in H1'26, above domestic, as Sany takes share from Caterpillar and Komatsu in Asia, Africa and Latin America.",
        "The domestic market is bottoming. Excavator sales rose 17% in 2025 and 24% in Jan–Aug 2026 (CCMA), helped by "
        "replacement of the 2016–21 fleet.",
        "Sany combines operating leverage with cash returns. FY25 operating cash flow rose 35%, a RMB400–800m buyback is "
        "under way, and the payout is ~50%. We expect FY27E EPS of RMB{eps27} (+24% YoY).",
    ],
    background=(
        "Sany was founded in 1989 by Liang Wengen and three partners in Lianyuan, Hunan, and is now headquartered in "
        "Changsha. It began in welding materials before moving into concrete pumps and excavators. It listed in Shanghai "
        "in 2003 and added a Hong Kong H-share listing in 2025; Liang remains the controlling shareholder through Sany "
        "Group. Sany has been China's leading excavator brand since 2011 and sells in more than 180 countries. Its "
        "overseas manufacturing includes Putzmeister in Germany (acquired 2012) and plants in India, Indonesia, the US "
        "and Brazil."),
    model=(
        "Sany makes and sells excavators (~40% of H1'26 revenue), concrete machinery, cranes, piling and road machinery "
        "through dealers and direct sales. It supports sales with customer financing (instalments and leases) and a growing "
        "parts-and-service business. Profitability depends on volume (fixed-cost absorption), mix and pricing discipline: "
        "large excavators, mining equipment and overseas units carry higher margins. Electrified products and digital "
        "fleet management are differentiators. Overseas growth relies on local plants and a dealer network built over the "
        "past decade."),
    competition=(
        "At home Sany competes with XCMG, Zoomlion, LiuGong, SDLG and Sunward, and foreign brands' share of China's "
        "excavator market has shrunk sharply over the past decade. Globally the benchmarks are Caterpillar, Komatsu, Deere, "
        "Volvo CE, Hitachi CM and Liebherr. Sany wins on price (Chinese machines typically sell at a meaningful discount "
        "to Japanese and US brands), product breadth and speed of dealer expansion. Its gaps are brand perception in North "
        "America and Western Europe, after-market density, and exposure to trade barriers. China's excavator exports "
        "now roughly equal domestic sales (116,739 vs 118,518 units in 2025)."),
    tam=(
        "Global construction equipment is roughly a US$200–250bn market in annual OEM sales. China sold 235,257 "
        "excavators in 2025 (+17%), half of them exported, and 191,557 in Jan–Aug 2026 (+24%). Domestic demand rests on "
        "fleet replacement and infrastructure and water-conservancy spending; exports ride emerging-market mining and "
        "infrastructure. Sany's ~US$12.5bn of FY25 revenue is a mid-single-digit share of the global pool, which leaves "
        "room to grow."),
    financials=(
        "FY25 revenue rose 14.7% to RMB89.7bn and net profit 41% to RMB8.4bn, with gross margin up 0.9pt to 27.8%. "
        "H1'26 revenue grew 19.5% to RMB53.5bn and EBIT 56%, but net profit rose only 9% to RMB5.7bn because CNY strength "
        "created FX finance losses on overseas receivables. The balance sheet carries ~RMB38bn of net cash; ROE is a "
        "modest ~11%, which leaves room for improvement. We forecast revenue of RMB{rev26}bn/{rev27}bn/{rev28}bn and "
        "net profit of RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E. Our FY26E EPS of RMB{eps26} is slightly below "
        "consensus (RMB1.17) on FX."),
    valuation=(
        "Our TP of RMB{tp} is 16x FY27E EPS of RMB{eps27}: in line with Komatsu (~15.7x forward), above XCMG (~8.5x) "
        "and well below Caterpillar (~28x). Faster overseas growth and the net-cash balance sheet justify that level. "
        "The H-share (6031.HK) trades at an ~18% discount to the A-share. The consensus average target is RMB26.72 "
        "(19 analysts, 18 Buy-rated). Bear case RMB{bear}: domestic relapse and persistent FX losses. Bull case "
        "RMB{bull}: China upcycle plus 20%+ overseas growth."),
    risks=[
        "China property and infrastructure relapse.",
        "Trade barriers (tariffs, anti-dumping actions) against Chinese machinery.",
        "FX: a stronger CNY creates translation and finance losses.",
        "Credit risk on customer financing and receivables.",
    ],
    catalysts=[
        "Monthly CCMA excavator sales and export data.",
        "Q3'26 results (late October).",
        "Buyback execution (RMB400–800m) and dividend.",
    ],
    sources="Company FY25 results release and H1'26 HKEX results; CMBI; CCMA via Mysteel/Yieh; StockAnalysis/S&P "
            "Global; IBKR; source pack.",
)

SIEYUAN = dict(
    key="sieyuan", name="Sieyuan Electric", cn="思源电气", ticker="002028.SZ",
    listing="H-share listing (up to 15% of share capital) pending",
    sector="Electrical Equipment", theme="Industrials & resources",
    ccy="RMB", price=120.65, hi52=239.12, lo52=100.32, ytd=-22.0,
    fin_unit="RMB bn", fx=1.0, shares=0.7826,
    mcap_local=94.4, mcap_ccy="RMB", net_cash=7.03, ev=87.7,
    profile="profit",
    hist=dict(rev=[12.46, 15.46, 21.54], gm=[29.4, 31.1, 30.8],
              np=[1.56, 2.05, 3.15], eps=[2.02, 2.64, 4.01], dps=[0.40, 0.50, 0.70]),
    est=dict(rev=[26.5, 32.5, 38.5], gm=[29.3, 29.5, 29.8],
             np=[3.65, 4.55, 5.50], payout=0.18),
    tp_method=dict(type="pe", mult=24, yr=1),
    scen=dict(
        bear=dict(type="pe", eps=5.00, mult=19, desc="Storage dilution deepens; tender prices fall"),
        bull=dict(type="pe", eps=6.60, mult=28, desc="Orders beat target; overseas margins hold"),
    ),
    cons=dict(tp=209.54, n=12, eps26=5.11, eps27=6.77, ratings="9 Strong Buy / 2 Buy / 1 Hold"),
    mix_title="H1'26 revenue mix by product (%)",
    mix=[("Switchgear", 40.1), ("Protection, automation, EPC & other", 26.1),
         ("Transformers", 20.9), ("Energy storage", 12.9)],
    tiles=[("RMB5tn+", "China grid investment planned for 2026–30 (source pack)"),
           ("US$9.0bn", "China transformer exports in 2025 (+35%)"),
           ("RMB37.5bn", "Sieyuan 2026 new-order target (+30%)")],
    peers=[("GE Vernova", "GEV US", 47.8, 65.9, 6.3),
           ("HD Hyundai Electric", "267260 KS", 18.4, 16.9, 4.6),
           ("XJ Electric", "000400 CH", 16.1, 11.9, 1.1),
           ("TBEA", "600089 CH", 12.3, 10.4, 1.4)],
    self_peer=(20.3, 21.3, 3.7),
    headline="A quality private-sector grid franchise; storage mix and valuation cap the upside",
    summary=("Sieyuan is China's leading privately owned transmission-and-distribution equipment maker and benefits from "
             "record grid investment at home and a global transformer shortage abroad. Revenue grew 27% in H1'26 but profit "
             "only 13% as low-margin storage diluted the mix. At {pe27}x FY27E P/E much of the growth is priced in; we "
             "initiate at <b>{rating}</b> with a TP of RMB{tp} ({up} upside)."),
    thesis=[
        "Demand for grid equipment is structural. China's grid capex is at record levels (more than RMB5tn planned for "
        "2026–30), and overseas utilities face multi-year transformer lead times.",
        "Sieyuan has a consistent execution record. Revenue grew at a 27% CAGR and net profit at 37% over FY22–25, with "
        "a steady ~30% gross margin and net cash throughout.",
        "The mix is turning against margins. Storage revenue (10.5% gross margin) grew 231% in H1'26 and FX losses "
        "weighed. Our FY26E EPS of RMB{eps26} is ~9% below consensus.",
    ],
    background=(
        "Founded in Shanghai in 1993 by Dong Zengping, Sieyuan started in power-system test equipment and capacitors. "
        "It now offers a full T&D portfolio: high-voltage switchgear (GIS), transformers, reactors, protection and "
        "automation, reactive-power compensation (SVG/STATCOM), energy storage and EPC. It listed in Shenzhen in 2004. "
        "As a privately controlled company it competes against State Grid-affiliated SOEs. In December 2025 it announced "
        "a Hong Kong H-share listing of up to 15% of its share capital, which still awaits completion."),
    model=(
        "Sieyuan sells mainly through competitive tenders run by State Grid, China Southern Grid, power generators and "
        "industrial users, and increasingly to overseas utilities and EPC contractors (29.5% of H1'26 revenue). Revenue "
        "follows order intake with a 6–18-month lag; the 2026 target is RMB37.5bn of new orders (+30%) and RMB27bn of "
        "revenue (+25%). Switchgear (40% of H1'26 revenue) and transformers (21%) earn gross margins around or above "
        "30%. Storage systems (13%) are a low-margin integration business. Working capital is meaningful, but the "
        "company has stayed net cash."),
    competition=(
        "At home Sieyuan competes with State Grid-affiliated Pinggao and XJ Electric, China XD Electric, TBEA "
        "(transformers) and NARI (secondary equipment). Abroad it faces Hitachi Energy, Siemens Energy, GE Vernova, "
        "Schneider, HD Hyundai Electric, Hyosung and LS Electric. Its edge is breadth, delivery speed and cost. China's "
        "transformer exports rose 35% to US$9.0bn in 2025 because Western capacity could not keep up. The main pressure "
        "points are price in domestic tenders and the commoditised storage segment."),
    tam=(
        "China's grid spending is at record highs: State Grid alone plans more than RMB650bn a year, and the 15th "
        "Five-Year Plan points to over RMB5tn for 2026–30. Globally, renewables integration, electrification and AI "
        "data-centre load are driving a multi-year upcycle in transformers and switchgear, with US and European lead "
        "times of two years or more. Sieyuan's FY25 revenue of RMB21.5bn is a small slice of this pool, so share "
        "gains abroad are the swing factor."),
    financials=(
        "FY25 revenue rose ~39% to RMB21.5bn and net profit 54% to RMB3.15bn, with gross margin steady at 30.8%. H1'26 "
        "revenue grew 27% to RMB10.8bn but net profit only 13% to RMB1.46bn, reflecting storage mix (231% growth at a "
        "10.5% gross margin) and FX losses. Net cash is ~RMB7bn and ROE ~23%. We forecast revenue of "
        "RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E. We assume gross "
        "margin drifts down by about a point as storage grows."),
    valuation=(
        "Our TP of RMB{tp} is 24x FY27E EPS of RMB{eps27}. That is a premium to domestic SOE peers (XJ Electric ~16x, "
        "TBEA ~12x forward) and HD Hyundai Electric (~18x) for Sieyuan's ~25% EPS CAGR, net cash and overseas growth, "
        "but far below GE Vernova (~48x). It is close to UBS's RMB142 target; the consensus average of RMB209.5 looks "
        "stale after cuts to ratings. Bear case RMB{bear}: deeper storage dilution and weaker tender pricing. Bull case "
        "RMB{bull}: orders beat the RMB37.5bn target and overseas margins hold."),
    risks=[
        "Storage-mix dilution and price competition in domestic tenders.",
        "FX and execution risk on overseas EPC projects.",
        "Dilution from the planned H-share issue (up to 15%).",
        "Upside risk: faster overseas order conversion and richer UHV/GIS mix.",
    ],
    catalysts=[
        "Q3'26 results on 24 October.",
        "Completion of the Hong Kong H-share listing.",
        "State Grid UHV/transformer tender awards and overseas orders.",
    ],
    sources="Company 2025 performance express and H1'26 report; Gawin Research; CITIC (via Futu); UBS (via "
            "MarketScreener); SCMP; StockAnalysis/S&P Global; IBKR; source pack.",
)

COMPANIES = [ZIJIN, SANY, SIEYUAN]
