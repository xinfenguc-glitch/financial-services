"""Battery, lithium & energy-storage chain: CATL, Sungrow, Huayou, Tianqi, Ganfeng."""

HKD_PER_RMB = 1 / 0.8531  # USD/CNH 6.6943, USD/HKD 7.8475 on 12-Oct-2026 (IBKR)

CATL = dict(
    key="catl", name="Contemporary Amperex Technology (CATL)", cn="宁德时代", ticker="300750.SZ",
    listing="H-share 3750.HK at HK$494.80 (~41% premium to A)",
    sector="Batteries", theme="Battery, lithium & storage",
    ccy="RMB", price=298.38, hi52=468.75, lo52=285.17, ytd=-17.5,
    fin_unit="RMB bn", fx=1.0, shares=4.56,
    mcap_local=1400.0, mcap_ccy="RMB", net_cash=291.2, ev=1140.0,
    profile="profit",
    hist=dict(rev=[400.92, 362.01, 423.70], gm=[19.1, 23.8, 25.1],
              np=[44.12, 50.75, 72.20], eps=[10.05, 11.58, 16.14], dps=[5.03, 4.55, None]),
    est=dict(rev=[600.0, 700.0, 790.0], gm=[24.0, 24.3, 24.5],
             np=[93.0, 108.0, 122.0], payout=0.50),
    tp_method=dict(type="pe", mult=17, yr=1),
    scen=dict(
        bear=dict(type="pe", eps=21.0, mult=12, desc="Share loss to second sources; price war"),
        bull=dict(type="pe", eps=26.0, mult=19, desc="Storage boom; overseas share gains"),
    ),
    cons=dict(tp=548.16, n=29, eps26=20.73, eps27=25.01, ratings="23 Strong Buy / 6 Buy"),
    mix_title="H1'26 revenue mix (%)",
    mix=[("EV batteries", 69.4), ("Energy-storage batteries", 19.2),
         ("Materials, recycling & minerals", 6.8), ("Other", 4.6)],
    tiles=[("661GWh", "CATL battery sales in 2025 (+39%)"),
           ("39.2%", "Global EV battery share in 2025 (SNE Research); No.1 for nine years"),
           ("1,069GWh", "China battery output in H1'26 (+53%)")],
    peers=[("BYD", "002594 CH", 15.5, None, None),
           ("LG Energy Solution", "373220 KS", 43.1, 27.1, 4.9),
           ("EVE Energy", "300014 CH", 13.0, 16.3, 1.6)],
    self_peer=(12.6, 9.4, 2.2),
    headline="Still the cost and technology leader; second-sourcing fears have created an entry point",
    summary=("CATL is the world's largest battery maker, with ~39% of the global EV battery market and a fast-growing "
             "storage business. The A-share fell 24% in September as Chinese automakers added second-source suppliers, "
             "leaving it on {pe27}x FY27E P/E, or ~{pe27x}x excluding RMB291bn of net cash. We initiate at "
             "<b>{rating}</b> with a TP of RMB{tp} ({up} upside) on 17x FY27E EPS. We prefer the A-share to the H-share, "
             "which trades at a ~41% premium."),
    thesis=[
        "<b>Scale and cost leadership.</b> CATL sold 661GWh in 2025 (+39%), ran at 95% utilisation in Q2'26 and targets "
        "1.2TWh of 2026 production. Its ~24–25% gross margin is several points above Korean and Chinese peers.",
        "<b>Storage is the second engine.</b> Storage revenue grew 87.5% in H1'26 to 19% of sales on grid and AI "
        "data-centre demand; China's storage-battery sales rose 83% in the half.",
        "<b>Second-sourcing erodes share; it does not threaten the franchise.</b> Volumes keep growing with the market even "
        "as Li Auto, Xiaomi and Xpeng dual-source. RMB291bn of net cash funds buybacks and a ~50% payout.",
    ],
    background=(
        "CATL (Contemporary Amperex Technology) was founded in 2011 in Ningde, Fujian by Robin Zeng (Zeng Yuqun) and a "
        "team from consumer-battery maker ATL. It listed on Shenzhen's ChiNext board in 2018. Its Hong Kong listing in "
        "May 2025 raised about HK$41bn, the year's largest global listing at the time. SNE Research ranks it the world's "
        "No.1 EV battery supplier for nine straight years. Capacity reached 772GWh at end-2025, with another 321GWh "
        "under construction, including plants in Germany, Hungary, Spain (with Stellantis) and Indonesia."),
    model=(
        "CATL sells cells, modules and cell-to-pack systems to automakers under multi-year supply agreements. Formula "
        "pricing passes lithium and other raw-material costs through with a lag. It also sells storage cells and "
        "containerised systems to integrators and utilities, and earns revenue from lithium mining, materials and "
        "recycling (Brunp). A newer licensing model (licence, royalty and services) lets overseas OEMs build plants with "
        "CATL technology. Profitability rests on purchasing scale, manufacturing yield and R&D (RMB22bn in FY25). The "
        "product ladder spans LFP fast-charge (Shenxing), high-nickel (Qilin) and sodium-ion cells."),
    competition=(
        "BYD (FinDreams) is the clear global No.2, followed by LG Energy Solution, CALB, Gotion, SK On, Panasonic and "
        "Samsung SDI. In storage, EVE, Hithium, BYD and REPT compete hard on price. Chinese automakers increasingly "
        "dual-source to gain bargaining power, which caps CATL's domestic share. Its moat is cost per kWh, quality record "
        "and breadth of chemistries. LGES's ~43x forward P/E reflects trough profits, not stronger positioning. "
        "Geopolitics is the key non-market risk: CATL is on the US Defense Department's 1260H list and exposed to US "
        "'foreign entity of concern' sourcing rules."),
    tam=(
        "Battery demand is growing across EVs and stationary storage. China produced 1,069GWh of batteries in H1'26 "
        "(+53%) and storage-battery sales rose 83%. Industry forecasts put global demand at 4–5TWh by 2030, about twice "
        "today's level. At ~US$70–80/kWh for cells, the global market is already worth ~US$150bn a year. CATL's 661GWh "
        "in 2025 equates to roughly a third of global supply."),
    financials=(
        "Revenue recovered 17% to RMB424bn in FY25 after the FY24 price-led dip, and net profit rose 42% to RMB72.2bn. "
        "H1'26 revenue rose 55% to RMB277bn and net profit 42% to RMB43.3bn, with gross margin down 1.1pt to 23.9% on "
        "mix. Cash generation is exceptional: FY25 operating cash flow was RMB133bn and net cash is RMB291bn (~RMB64 a "
        "share). We forecast revenue of RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of "
        "RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E, slightly below consensus (FY26E EPS RMB20.73) to allow for share "
        "loss and price competition."),
    valuation=(
        "Our TP of RMB{tp} is 17x FY27E EPS of RMB{eps27}, below CATL's five-year average but above BYD (~15.5x) and EVE "
        "(~13x) forward, reflecting superior margins and ~25% ROE. Ex-cash, the stock trades on ~{pe27x}x FY27E. The "
        "consensus average target of RMB548 (29 analysts, all Buy-rated) predates the September sell-off. For the H-share "
        "(3750.HK), a 20% premium to our A-share TP implies ~HK$570, only ~15% upside, so we prefer the A-share. Bear case "
        "RMB{bear}: share loss and a price war. Bull case RMB{bull}: storage boom and overseas share gains."),
    risks=[
        "Customer second-sourcing and domestic price competition.",
        "Geopolitics: US 1260H listing, FEOC sourcing rules, EU tariffs and investment screening.",
        "Lithium price swings that disrupt pass-through timing.",
        "H-share premium could compress as new supply arrives.",
    ],
    catalysts=[
        "Q3'26 results (late October).",
        "Sodium-ion and next-generation LFP launches; storage order wins.",
        "Buyback execution; ramp-up of Hungarian and Spanish plants.",
    ],
    sources="CATL 2025 annual and H1'26 interim reports; SNE Research; Longbridge; Seoul Economic Daily; JPMorgan/CLSA "
            "(via Tiger); StockAnalysis/S&P Global; IBKR; source pack.",
)

SUNGROW = dict(
    key="sungrow", name="Sungrow Power Supply", cn="阳光电源", ticker="300274.SZ",
    listing="Hong Kong H-share IPO filed (refiled April 2026)",
    sector="Solar & Storage Equipment", theme="Battery, lithium & storage",
    ccy="RMB", price=82.35, hi52=208.88, lo52=78.00, ytd=-51.8,
    fin_unit="RMB bn", fx=1.0, shares=2.06,
    mcap_local=169.7, mcap_ccy="RMB", net_cash=28.05, ev=144.7,
    profile="profit",
    hist=dict(rev=[72.25, 77.86, 89.18], gm=[25.5, 29.1, 30.5],
              np=[9.44, 11.04, 13.46], eps=[4.55, 5.32, 6.53], dps=[0.69, 1.08, 1.64]),
    est=dict(rev=[82.0, 98.0, 112.0], gm=[34.5, 33.0, 32.5],
             np=[12.3, 14.5, 16.3], payout=0.25),
    tp_method=dict(type="pe", mult=13.5, yr=1),
    scen=dict(
        bear=dict(type="pe", eps=5.6, mult=11, desc="Storage price war; US access closes"),
        bull=dict(type="pe", eps=8.1, mult=16, desc="H2 storage ramp; margins hold"),
    ),
    cons=dict(tp=146.50, n=20, eps26=6.83, eps27=8.07, ratings="11 Strong Buy / 5 Buy / 3 Hold / 1 Sell"),
    mix_title="H1'26 revenue mix (%)",
    mix=[("Energy-storage systems", 50), ("PV inverters & power electronics", 40),
         ("Project development & other", 10)],
    tiles=[("43GWh", "Sungrow storage shipments in 2025 (+54%)"),
           ("~25%", "Sungrow share of global PV inverter shipments (2024 volumes)"),
           ("73%", "Overseas share of H1'26 revenue")],
    peers=[("Ginlong (Solis)", "300763 CH", 14.9, 15.5, 3.7),
           ("Enphase Energy", "ENPH US", 16.7, 20.9, 3.0),
           ("Fluence Energy", "FLNC US", None, None, 0.6)],
    self_peer=(11.3, 10.0, 1.9),
    headline="Margins are recovering; revenue has to follow before we turn constructive",
    summary=("Sungrow is the world's No.2 solar-inverter maker and a top-tier storage integrator; storage is now half of "
             "revenue and 73% of sales are overseas. H1'26 revenue fell 29% on domestic solar weakness and lower "
             "shipments, yet gross margin rose to 35.9%. At {pe27}x FY27E P/E with net cash the stock is inexpensive, "
             "but we want evidence of an H2 storage ramp. We initiate at <b>{rating}</b>, TP RMB{tp} ({up} upside)."),
    thesis=[
        "<b>Storage has overtaken inverters.</b> Storage shipments rose 54% to 43GWh in 2025 and made up ~50% of H1'26 "
        "revenue, with demand from utility-scale, C&I and data-centre projects.",
        "<b>Margins are the bright spot.</b> Gross margin reached 35.9% in H1'26 and 38.6% in Q2 on overseas mix and "
        "cheaper cells; price increases of 5–15% took effect from 20 September.",
        "<b>The top line is the open question.</b> H1'26 revenue fell 29%, and our FY26E EPS of RMB{eps26} is ~13% below "
        "consensus. Q3 results (30 October) need to show storage deliveries accelerating.",
    ],
    background=(
        "Sungrow was founded in 1997 in Hefei, Anhui by Cao Renxian, then a lecturer at Hefei University of Technology, "
        "to make power electronics for renewables. It listed on Shenzhen's ChiNext board in 2011. Wood Mackenzie ranks it "
        "a global top-two solar-inverter supplier alongside Huawei, and cumulative storage shipments passed 93GWh by "
        "end-2025. It also develops solar and storage projects in China and makes EV drives and hydrogen electrolysers. "
        "A Hong Kong H-share listing was filed in 2025 and refiled in April 2026."),
    model=(
        "Sungrow designs and assembles power-conversion equipment: string and central inverters for utility, commercial "
        "and residential solar. It also sells integrated battery-storage systems (PowerTitan, PowerStack), buying cells "
        "from suppliers such as CATL and EVE and adding power conversion, battery management, thermal and "
        "energy-management systems. Value comes from power electronics, integration, bankability and long-term service. "
        "Cells are largely a pass-through cost, so falling cell prices support margins. A smaller arm builds and sells "
        "solar and storage plants, and the company is moving into data-centre power (solid-state transformers, HVDC)."),
    competition=(
        "In inverters, Huawei is No.1 and Sungrow No.2, followed by Ginlong (Solis), GoodWe, Sineng, SMA, Enphase and "
        "SolarEdge. In storage integration, Tesla (Megapack) leads; Sungrow sits in the top tier with BYD, Fluence, "
        "Hithium, Envision and CATL's own systems, and price competition from Chinese integrators is fierce. Sungrow's "
        "strengths are a two-decade overseas channel, bankability with utilities and in-house power electronics. Its "
        "weaknesses are reliance on bought-in cells and limited access to the US given tariffs and sourcing rules."),
    tam=(
        "Stationary storage is the growth market. China's storage-battery sales rose 83% in H1'26, and grid-scale "
        "deployments are accelerating worldwide as solar penetration, grid congestion and data-centre load rise. The "
        "solar-inverter market is larger but more mature. China's domestic installations have weakened since the 2025 "
        "shift to market-based renewable pricing. With ~43GWh of 2025 storage shipments and ~25% of inverter volumes, "
        "Sungrow already holds a sizeable slice of both pools."),
    financials=(
        "FY25 revenue grew 14.6% to RMB89.2bn and net profit 22% to RMB13.5bn. Q4'25 profit more than halved, however, "
        "on a RMB1bn incentive provision and delivery timing. H1'26 revenue fell 29% to RMB30.9bn and net profit 32% to "
        "RMB5.3bn, hit by domestic solar weakness, lower shipments and FX losses, even as gross margin rose to 35.9%. "
        "Net cash is ~RMB28bn and ROE ~22%. We forecast revenue of RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of "
        "RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E, assuming H2'26 revenue grows ~12% YoY."),
    valuation=(
        "Our TP of RMB{tp} is 13.5x FY27E EPS of RMB{eps27}, a modest discount to Ginlong (~15x) and Enphase (~17x) "
        "forward to reflect the revenue decline. The stock is down 52% YTD and trades on {pe27}x FY27E, so downside is "
        "partly cushioned. We would turn more positive on evidence of H2 storage deliveries and order growth. The "
        "consensus average target is RMB146.5 (20 analysts). Bear case RMB{bear}: storage price war and US access "
        "closes. Bull case RMB{bull}: H2 ramp and margins hold."),
    risks=[
        "Price war among Chinese storage integrators.",
        "US tariffs and foreign-entity-of-concern sourcing rules.",
        "Domestic solar demand and FX losses.",
        "Dilution from the H-share listing.",
    ],
    catalysts=[
        "Q3'26 results on 30 October.",
        "Storage order announcements and shipment data.",
        "H-share listing; data-centre power products.",
    ],
    sources="Company 2025 annual and H1'26 reports; pv magazine; Energy-Storage.news; Wood Mackenzie; Bloomberg; "
            "Simply Wall St; StockAnalysis/S&P Global; IBKR; source pack.",
)

HUAYOU = dict(
    key="huayou", name="Zhejiang Huayou Cobalt", cn="华友钴业", ticker="603799.SH",
    listing="A-share only",
    sector="Battery Materials & Metals", theme="Battery, lithium & storage",
    ccy="RMB", price=34.53, hi52=82.17, lo52=33.89, ytd=-49.4,
    fin_unit="RMB bn", fx=1.0, shares=1.90,
    mcap_local=65.4, mcap_ccy="RMB", net_cash=-53.8, ev=134.7,
    profile="profit",
    hist=dict(rev=[66.30, 60.95, 81.02], gm=[13.6, 16.7, 17.4],
              np=[3.35, 4.16, 6.11], eps=[2.05, 2.39, 3.33], dps=[1.00, 0.50, 0.50]),
    est=dict(rev=[106.0, 118.0, 128.0], gm=[18.0, 18.5, 18.8],
             np=[5.9, 7.0, 8.0], payout=0.17),
    tp_method=dict(type="pe", mult=10.5, yr=1),
    scen=dict(
        bear=dict(type="pe", eps=2.8, mult=9, desc="Nickel oversupply; sulfur costs persist"),
        bull=dict(type="pe", eps=4.3, mult=12, desc="Pomalaa ramps smoothly; cobalt stays tight"),
    ),
    cons=dict(tp=61.06, n=6, eps26=3.06, eps27=None, ratings="3 Strong Buy / 2 Buy / 1 Hold"),
    mix_title="FY25 revenue mix by product (%)",
    mix=[("Cobalt, copper, lithium, trading & other", 34.9), ("Nickel products", 32.0),
         ("Cathode materials", 18.5), ("Nickel intermediates", 14.6)],
    tiles=[("~300ktpa", "Huayou Indonesian HPAL nickel capacity incl. Pomalaa (Ni in MHP)"),
           ("862ktpa", "Indonesian MHP capacity expected in 2026, nearly double 2025 (Argus)"),
           ("~80%", "LFP share of China EV battery installations, a headwind for nickel cathodes")],
    peers=[("CMOC Group", "603993 CH", 11.0, 6.0, 1.5),
           ("GEM", "002340 CH", 13.4, 10.6, 1.7),
           ("CNGR Advanced Material", "300919 CH", 18.0, 9.1, 1.1)],
    self_peer=(8.8, 7.4, 1.4),
    headline="Cheap for a reason: the integration is real, but earnings quality has slipped",
    summary=("Huayou is an integrated nickel, cobalt, lithium and battery-materials group, spanning Indonesian and African "
             "mining through refining to precursors and cathodes. The shares are down 49% YTD after Q2 profit fell 31% "
             "and consensus FY26 EPS was cut by a third. At {pe27}x FY27E P/E and ~1x book the valuation is "
             "undemanding, but leverage and commodity headwinds keep us at <b>{rating}</b>, TP RMB{tp} ({up} upside)."),
    thesis=[
        "<b>Integration is a genuine cost advantage.</b> Low-cost Indonesian HPAL nickel (~300ktpa including Pomalaa) "
        "feeds precursor and cathode plants; cathode and precursor shipments nearly doubled in H1'26.",
        "<b>Earnings quality weakened in Q2.</b> Sulfur-cost spikes forced maintenance at Huafei, cobalt shipments fell 24% "
        "under DRC export quotas, and Q2 net profit fell 31% YoY to ~RMB1.0bn.",
        "<b>The balance sheet limits flexibility.</b> Net debt of ~RMB54bn (~3x TTM EBITDA) and the Atlantic Lithium "
        "acquisition add risk as nickel and lithium prices soften.",
    ],
    background=(
        "Founded in 2002 in Tongxiang, Zhejiang by Chen Xuehua, Huayou began as a cobalt refiner buying ore from the "
        "Democratic Republic of Congo and listed in Shanghai in 2015. Over the past decade it has built a vertically "
        "integrated chain: DRC cobalt-copper mining, and Indonesian laterite nickel processed by high-pressure acid "
        "leaching (HPAL) with partners Tsingshan, Vale and Ford. It also owns lithium in Zimbabwe (Arcadia), precursor "
        "and cathode plants in China and abroad (including joint ventures with Korean materials makers), and battery "
        "recycling."),
    model=(
        "Huayou earns a margin at each step of the chain. The main profit pool is mining and HPAL refining, where it "
        "produces mixed hydroxide precipitate at low cash cost. Next come refined nickel and cobalt products, and "
        "processing fees on precursors and cathodes sold to battery makers. Integration lowers cost and secures supply, "
        "but it ties results to nickel, cobalt and lithium prices and to inputs such as sulfur and sulfuric acid. Growth "
        "comes from new Indonesian capacity (Pomalaa, 120ktpa), lithium, and cathode volumes for Korean and Chinese cell "
        "makers."),
    competition=(
        "In Indonesian nickel, Huayou competes with Tsingshan, Nickel Industries, Harita (Lygend), GEM and CNGR. In cobalt "
        "its rivals are CMOC (the world's largest producer) and Glencore; in precursors and cathodes, CNGR, GEM, Ronbay "
        "and Easpring. The structural problem is chemistry: lithium iron phosphate (LFP) now accounts for about 80% of "
        "China's EV battery installations. That limits growth in nickel-based cathodes outside premium and overseas "
        "models. Huayou wins on cost position and customer relationships but is capital-intensive."),
    tam=(
        "The global nickel market is ~3.5–3.7Mt a year, with Indonesia supplying more than half. Argus expects Indonesian "
        "MHP capacity to nearly double to 862ktpa in 2026, which points to continued oversupply. Cobalt (~250–300kt a "
        "year) is tighter because of DRC export quotas. Battery-materials demand grows with EVs and storage, but "
        "nickel's share is shrinking as LFP dominates in China."),
    financials=(
        "FY25 revenue rose 33% to RMB81.0bn and net profit 47% to RMB6.1bn as Indonesian volumes ramped. H1'26 revenue "
        "rose 49% to RMB55.6bn and net profit 29% to RMB3.5bn, but the quarterly split matters: Q1 earned RMB2.5bn "
        "(+99%) and Q2 only ~RMB1.0bn (−31%). Gross margin has improved from 13.6% (FY23) to ~19% TTM. Net debt of "
        "~RMB54bn is large against a ~RMB65bn market cap, though a 0.8% buyback is under way. We forecast net profit of "
        "RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E, in line with the reduced consensus (FY26E EPS RMB3.06)."),
    valuation=(
        "Our TP of RMB{tp} is 10.5x FY27E EPS of RMB{eps27}, a discount to CMOC (~11x) and GEM (~13x) forward for higher "
        "leverage and weaker earnings momentum. On EV/EBITDA the stock already trades at ~7.4x TTM, between CMOC (~6x) "
        "and GEM (~11x). The consensus average target (RMB61) has not caught up with the estimate cuts. Bear case "
        "RMB{bear}: nickel oversupply and sulfur costs persist. Bull case RMB{bull}: Pomalaa ramps smoothly and cobalt "
        "stays tight."),
    risks=[
        "Nickel oversupply from Indonesian capacity additions.",
        "Indonesian policy (ore quotas, royalties) and DRC cobalt export quotas.",
        "Input costs (sulfur, sulfuric acid) and high leverage.",
        "LFP substituting for nickel-based cathodes.",
    ],
    catalysts=[
        "Q3'26 results on 24 October: is upstream nickel recovering?",
        "Pomalaa ramp-up and Huafei restart.",
        "Buyback completion; Atlantic Lithium deal terms.",
    ],
    sources="Company FY25 and H1'26 results; Stock Analysis; Simply Wall St; SMM; Argus; Project Blue; StockAnalysis/"
            "S&P Global; IBKR; source pack.",
)

TIANQI = dict(
    key="tianqi", name="Tianqi Lithium", cn="天齐锂业", ticker="9696.HK",
    listing="A-share 002466.SZ at RMB39.23 (H at ~44% discount)",
    sector="Lithium", theme="Battery, lithium & storage",
    ccy="HK$", price=25.92, hi52=69.15, lo52=25.92, ytd=-50.8,
    fin_unit="RMB bn", fx=HKD_PER_RMB, shares=1.70,
    mcap_local=63.1, mcap_ccy="RMB", mcap_note="A+H", net_cash=-5.7, ev=79.9,
    profile="profit",
    hist=dict(rev=[40.50, 13.06, 10.35], gm=[83.2, 40.6, 36.6],
              np=[7.30, -7.91, 0.46], eps=[4.45, -4.82, 0.28], dps=[1.35, 0.0, 0.0]),
    est=dict(rev=[23.0, 21.0, 22.5], gm=[58.0, 52.0, 52.0],
             np=[6.5, 4.8, 5.2], dps=[0.0, 0.30, 0.40]),
    tp_method=dict(type="pe", mult=9, yr=1),
    scen=dict(
        bear=dict(type="pe", eps=1.6, mult=9.5, desc="Lithium carbonate ~RMB80k/t"),
        bull=dict(type="pe", eps=4.0, mult=9, desc="Lithium carbonate ~RMB160k/t"),
    ),
    cons=dict(tp=64.20, tp_ccy="RMB", tp_line="A-share", n=17, eps26=3.67, eps27=2.95,
              ratings="7 Strong Buy / 4 Buy / 5 Hold / 1 Strong Sell"),
    mix_title="H1'26 revenue mix (%)",
    mix=[("Lithium chemicals", 58), ("Lithium concentrate", 42)],
    tiles=[("~26%", "Tianqi's effective stake in Greenbushes, the largest hard-rock lithium mine"),
           ("RMB122k/t", "China lithium carbonate, 9 Oct 2026 (+66% YoY, −24% in Sept)"),
           ("+28%", "2026 global lithium supply growth (Wood Mackenzie)")],
    peers=[("Albemarle", "ALB US", 10.9, 8.3, 2.1),
           ("SQM", "SQM US", 8.2, 6.4, 2.9),
           ("Pilbara Minerals", "PLS AU", 11.5, 9.4, 5.3),
           ("Ganfeng Lithium (A)", "002460 CH", 13.3, 12.9, 3.0)],
    self_peer=(10.1, 7.8, 4.5), self_peer_label="Tianqi (A-share)",
    headline="A world-class asset in a commodity-price trade; the H-share discount is the cushion",
    summary=("Tianqi owns about a quarter of Greenbushes, the world's largest and highest-grade hard-rock lithium mine, "
             "plus ~22% of Chile's SQM. H1'26 profit rebounded to RMB4.2bn on higher lithium prices, but lithium "
             "carbonate fell 24% in September and supply is set to grow ~28% in 2026. The H-share trades on only "
             "{pe27}x FY27E P/E, a ~44% discount to the A-share. We initiate at <b>{rating}</b> with a TP of HK${tp} "
             "({up} upside)."),
    thesis=[
        "<b>Bottom-quartile cost position.</b> Greenbushes delivered a 74% mining gross margin in H1'26 and generates "
        "cash even at much lower lithium prices.",
        "<b>Operating leverage cuts both ways.</b> Revenue rose 154% and profit swung from RMB87m to RMB4.2bn in H1'26; "
        "we expect FY27E EPS to fall ~26% as prices normalise.",
        "<b>The H-share has a valuation cushion.</b> At ~0.6x book and {pe27}x FY27E P/E it discounts a lot of bad news; "
        "the A-share (~14x FY27E) looks fuller.",
    ],
    background=(
        "Tianqi traces its roots to a state-owned lithium-salt plant founded in Shehong, Sichuan in 1992 and privatised "
        "under chairman Jiang Weiping in 2004. It listed in Shenzhen in 2010 and in Hong Kong in July 2022. Its 51%-owned "
        "joint venture with IGO holds 51% of Greenbushes owner Talison (Albemarle holds 49%), giving Tianqi a ~26% "
        "effective interest in the Western Australian mine. It also owns ~22% of SQM in Chile, the Kwinana lithium "
        "hydroxide plant (with IGO) and conversion plants in Sichuan and Jiangsu."),
    model=(
        "Tianqi is a vertically integrated lithium producer. It buys spodumene concentrate from Greenbushes at "
        "market-linked prices, sells part of it as concentrate (42% of H1'26 revenue) and converts the rest into lithium "
        "carbonate and hydroxide in China (58%). Its share of Greenbushes mining profit and equity income from SQM drive "
        "earnings. Results swing hard with lithium prices. Lags between concentrate purchases and chemical sales have "
        "caused large inventory write-downs in past downturns (FY24 loss of RMB7.9bn). The Kwinana hydroxide plant ran at "
        "~15% of nameplate in the June quarter."),
    competition=(
        "Hard-rock peers include Albemarle (Tianqi's Greenbushes partner), Pilbara Minerals, Mineral Resources and Rio "
        "Tinto (via Arcadium). Brine peers include SQM; Chinese peers include Ganfeng, Zangge, Yahua, Sinomine and CATL's "
        "lepidolite operations. Greenbushes sits at the bottom of the cost curve, so Tianqi is a price-taker with a "
        "durable cost edge. Its weak spots are downstream conversion (Kwinana) and Chile, where the Supreme Court "
        "dismissed its challenge to SQM's partnership with Codelco."),
    tam=(
        "Lithium demand comes from EV and storage batteries: about 1.5Mt LCE in 2026 on our estimates, growing 20–25% a "
        "year. Supply is growing faster. Wood Mackenzie forecasts +27.9% in 2026 as African and Chinese projects ramp, "
        "and a revised SMM inventory method added ~175kt to Chinese stock estimates in September. China spot carbonate "
        "was RMB122,350/t on 9 October, up 66% YoY but down 24% in September."),
    financials=(
        "Revenue collapsed from RMB40.5bn (FY23) to RMB10.3bn (FY25) as prices fell, with a RMB7.9bn loss in FY24 and a "
        "small profit in FY25. H1'26 revenue rose 154% to RMB12.2bn and net profit reached RMB4.2bn (vs RMB87m). Net debt "
        "is modest at ~RMB5.7bn after a 2026 H-share placement and convertible bond. We forecast net profit of "
        "RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E, assuming lithium carbonate averages ~RMB130k/t in 2026 and "
        "~RMB110k/t in 2027. That is well below the broker forecasts in the source pack (RMB7.6bn/9.3bn)."),
    valuation=(
        "Our TP of HK${tp} is 9x FY27E EPS of RMB{eps27} (at HK$1 = RMB0.853), in line with SQM (~8x) and below "
        "Albemarle and Pilbara (~11x forward), to reflect conversion-asset risk. Even at the TP the H-share is only ~0.7x "
        "book. The A-share consensus target is RMB64.2, and a broker H-share target in the source pack is HK$49.42; both "
        "assume higher prices than we do. Bear case HK${bear}: carbonate ~RMB80k/t. Bull case HK${bull}: ~RMB160k/t."),
    risks=[
        "Lithium price: each RMB10k/t moves annual net profit by roughly RMB0.7–0.9bn (our estimate).",
        "Greenbushes operations (CGP3 fire in June) and Kwinana under-performance.",
        "SQM/Codelco outcome and Chilean policy.",
        "Upside risk: supply discipline or a demand surprise reverses the price slide.",
    ],
    catalysts=[
        "Q3'26 results on 26 October.",
        "Greenbushes CGP3 restart and Kwinana fixes.",
        "Chinese inventory data and GFEX lithium futures.",
    ],
    sources="Company H1'26 HKEX results; IGO ASX quarterlies; Wood Mackenzie; Trading Economics/SMM; StockAnalysis/S&P "
            "Global; IBKR; source pack (Futu broker forecasts).",
)

GANFENG = dict(
    key="ganfeng", name="Ganfeng Lithium Group", cn="赣锋锂业", ticker="1772.HK",
    listing="A-share 002460.SZ at RMB43.68 (H at ~45% discount)",
    sector="Lithium & Batteries", theme="Battery, lithium & storage",
    ccy="HK$", price=27.96, hi52=91.20, lo52=27.96, ytd=-48.8,
    fin_unit="RMB bn", fx=HKD_PER_RMB, shares=2.08,
    mcap_local=81.5, mcap_ccy="RMB", mcap_note="A+H", net_cash=-27.1, ev=115.2,
    profile="profit",
    hist=dict(rev=[32.97, 18.91, 23.08], gm=[8.7, 9.0, 14.6],
              np=[4.95, -2.07, 1.61], eps=[2.46, -1.03, 0.79], dps=[0.80, 0.15, 0.15]),
    est=dict(rev=[46.0, 48.0, 54.0], gm=[27.0, 24.0, 24.0],
             np=[7.0, 5.6, 6.4], dps=[0.30, 0.30, 0.35]),
    tp_method=dict(type="pe", mult=10, yr=1),
    scen=dict(
        bear=dict(type="pe", eps=1.5, mult=11, desc="Lithium carbonate ~RMB80k/t"),
        bull=dict(type="pe", eps=4.0, mult=9.5, desc="~RMB160k/t plus solid-state traction"),
    ),
    cons=dict(tp=77.92, tp_ccy="RMB", tp_line="A-share", n=20, eps26=3.17, eps27=3.00,
              ratings="10 Strong Buy / 7 Buy / 2 Hold / 1 Strong Sell"),
    mix_title="H1'26 revenue mix (%)",
    mix=[("Lithium products", 62), ("Batteries", 34), ("Other", 4)],
    tiles=[("~20GWh", "Ganfeng battery output in H1'26 (RMB7.8bn revenue)"),
           ("+20–25%", "Supply growth management expects into a 'balanced' 2027"),
           ("500Wh/kg", "Solid-state cells in small-batch production (May 2026)")],
    peers=[("Albemarle", "ALB US", 10.9, 8.3, 2.1),
           ("SQM", "SQM US", 8.2, 6.4, 2.9),
           ("Pilbara Minerals", "PLS AU", 11.5, 9.4, 5.3),
           ("Tianqi Lithium (A)", "002466 CH", 10.1, 7.8, 4.5)],
    self_peer=(13.3, 12.9, 3.0), self_peer_label="Ganfeng (A-share)",
    headline="More diversified than Tianqi, but management's own price view caps the upside",
    summary=("Ganfeng is China's most diversified lithium group: chemicals from mines in Australia, Argentina and Mali, "
             "plus a fast-growing battery business. H1'26 revenue rose 177% and profit swung to RMB4.3bn, but "
             "management now expects only a balanced market in 2027 and net debt is rising. The H-share trades on "
             "{pe27}x FY27E P/E at a ~45% discount to the A-share. We initiate at <b>{rating}</b>, TP HK${tp} "
             "({up} upside)."),
    thesis=[
        "<b>The diversification is real.</b> Batteries (consumer, storage and power; ~20GWh in H1'26) were 34% of revenue, "
        "cushioning lithium-price swings, and 400–500Wh/kg solid-state cells are entering small-batch production.",
        "<b>The resource ramp lifts self-sufficiency.</b> Goulamina (Mali) and Mariana/Cauchari-Olaroz (Argentina) are "
        "ramping, which cuts third-party concentrate purchases.",
        "<b>But the cycle is turning.</b> Management has dropped its earlier >RMB200k/t price view and now expects a balanced "
        "2027 with 20–25% supply growth; we model FY27E EPS down ~20%.",
    ],
    background=(
        "Ganfeng was founded in 2000 in Xinyu, Jiangxi by Li Liangbin (chairman) and Wang Xiaoshen. It began in lithium "
        "metal and compounds and listed in Shenzhen in 2010 and Hong Kong in 2018. It is the world's largest lithium-metal "
        "producer and one of the largest lithium-chemical producers. Its resources include Mt Marion (Australia, with "
        "Mineral Resources), Cauchari-Olaroz and Mariana (Argentina), Goulamina (Mali), and Chinese lepidolite and brine. "
        "Its subsidiary Ganfeng LiEnergy makes consumer, power and storage batteries and is developing solid-state "
        "technology."),
    model=(
        "The lithium business buys and mines spodumene, brine and lepidolite and converts them into carbonate, hydroxide "
        "and metal for battery and industrial customers. It earns a conversion margin plus a mining margin on its own "
        "resources, so profit depends on lithium prices and the share of feedstock it mines itself. The battery business "
        "sells cells, packs and 5MWh storage cabins. It earns lower margins but sees steadier demand, and it gives Ganfeng "
        "a captive outlet for lithium. Recycling and solid-state electrolyte materials (lithium sulfide) add optionality."),
    competition=(
        "In lithium chemicals Ganfeng competes with Tianqi, Albemarle, SQM, Rio Tinto (Arcadium), Yahua and Zangge; in "
        "batteries, with CATL, BYD, EVE and Gotion for storage and consumer cells. Against Tianqi, its edge is "
        "diversification and a global resource portfolio; against pure battery makers, upstream integration. Its "
        "weakness relative to Greenbushes-backed Tianqi is a higher-cost, more geopolitically exposed resource base "
        "(Mali, Argentina, Mexico)."),
    tam=(
        "Ganfeng shares Tianqi's lithium market: ~1.5Mt LCE of demand in 2026 on our estimates, growing 20–25% a year, "
        "with supply growing faster near term. The battery arm addresses storage and consumer cells, and China's "
        "storage-battery sales rose 83% in H1'26. Solid-state batteries are a longer-dated option for premium EVs, "
        "eVTOLs and robots."),
    financials=(
        "Revenue fell from RMB33.0bn (FY23) to RMB18.9bn (FY24), with a RMB2.1bn loss, before recovering to RMB23.1bn and "
        "a RMB1.6bn profit in FY25. H1'26 revenue rose 177% to RMB22.9bn, with a 31.2% gross margin and RMB4.3bn of net "
        "profit. Net debt has risen to ~RMB27bn on capex in Mali and Argentina. We forecast net profit of "
        "RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E, below UOB's RMB9.2bn for FY26E, on lower H2 lithium prices."),
    valuation=(
        "Our TP of HK${tp} is 10x FY27E EPS of RMB{eps27}: a small premium to our Tianqi multiple for diversification, "
        "and in line with Albemarle (~11x) and Pilbara (~11.5x) forward. It implies ~0.9x book for the H-share. UOB's "
        "HK$75 target and the A-share consensus (RMB77.9) both embed higher lithium prices. Bear case HK${bear}: "
        "carbonate ~RMB80k/t. Bull case HK${bull}: ~RMB160k/t plus solid-state traction."),
    risks=[
        "Lithium prices and rising leverage.",
        "Political and fiscal risk in Mali, Argentina and Mexico.",
        "Battery price competition.",
        "Upside: faster solid-state commercialisation or industry supply cuts.",
    ],
    catalysts=[
        "Q3'26 results (mid-October).",
        "Goulamina and Mariana ramp-up data.",
        "Solid-state battery customer orders.",
    ],
    sources="Company H1'26 interim report; UOB Kay Hian; CnEVPost/CarNewsChina; Tiger Brokers; StockAnalysis/S&P "
            "Global; IBKR; source pack.",
)

COMPANIES = [CATL, SUNGROW, HUAYOU, TIANQI, GANFENG]
