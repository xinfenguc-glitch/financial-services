"""Semis & materials, equipment & robotics, medtech, and AI model developers."""

HKD_PER_RMB = 1 / 0.8531   # 12-Oct-2026 cross via IBKR (USD/CNH 6.6943, USD/HKD 7.8475)
HKD_PER_USD = 7.8475

GIGADEVICE = dict(
    key="gigadevice", name="GigaDevice Semiconductor", cn="兆易创新", ticker="603986.SH",
    listing="H-share 3986.HK at HK$375.60 (~3% premium to A)",
    sector="Semiconductors", theme="Semiconductors & materials",
    ccy="RMB", price=310.84, hi52=846.66, lo52=176.00, ytd=44.3,
    fin_unit="RMB bn", fx=1.0, shares=0.70175,
    mcap_local=218.5, mcap_ccy="RMB", net_cash=17.36, ev=201.4,
    profile="profit",
    hist=dict(rev=[5.76, 7.36, 9.20], gm=[30.3, 35.7, 39.1],
              np=[0.16, 1.10, 1.65], eps=[0.24, 1.66, 2.47], dps=[0.0, 0.34, 0.75]),
    est=dict(rev=[27.0, 31.0, 26.0], gm=[55.0, 56.0, 48.0],
             np=[13.5, 14.0, 10.0], payout=0.20),
    tp_method=dict(type="pe", mult=18, yr=1),
    scen=dict(
        bear=dict(type="pe", eps=12.0, mult=16.7, desc="Prices roll over in 2027; mid-cycle EPS"),
        bull=dict(type="pe", eps=25.0, mult=20, desc="Shortage extends through 2027"),
    ),
    cons=dict(tp=631.74, n=11, eps26=15.89, eps27=15.37, ratings="7 Strong Buy / 3 Buy / 1 Hold"),
    mix_title="Revenue mix by product (%, approx.)",
    mix=[("Memory: NOR, SLC NAND, niche DRAM", 85), ("Microcontrollers (GD32)", 12),
         ("Sensors & analog", 3)],
    tiles=[("US$15.7bn", "Global specialty-memory market, 2025 (Frost & Sullivan)"),
           ("US$3.1bn", "Global NOR flash market, 2025; GigaDevice ~18% share (No.2)"),
           ("+90-110%", "TrendForce forecast for high-capacity NOR price rises in H2'26")],
    peers=[("Winbond", "2344 TT", 4.2, 13.2, 5.6),
           ("Macronix", "2337 TT", 3.8, 15.9, 5.0),
           ("NXP Semiconductors", "NXPI US", 13.6, 12.7, 4.9)],
    peer_note="Winbond and Macronix forward P/Es reflect consensus peak-cycle earnings.",
    self_peer=(16.3, 29.8, 12.1),
    headline="Exceptional earnings, but we would be paying for the top of the memory cycle",
    summary=("GigaDevice is China's leading fabless designer of NOR flash, niche DRAM and microcontrollers. A memory "
             "shortage, as global majors divert capacity to HBM and DDR5, lifted H1'26 net profit twelve-fold to "
             "RMB6.9bn. The shares are already ~63% below their high and {pe26}x FY26E P/E is undemanding, but earnings "
             "are near a cyclical peak. We initiate at <b>{rating}</b>, TP RMB{tp} ({up} upside)."),
    thesis=[
        "Legacy memory is in short supply as leading makers exit NOR, SLC NAND and DDR4 to chase HBM/DDR5. "
        "TrendForce sees high-capacity NOR prices rising another 90-110% in H2'26, and mid-year backlog was RMB9.8bn.",
        "Operating leverage is extreme: memory gross margin jumped to 67.6% from 42.8% in FY25, and TTM group gross "
        "margin is 56%.",
        "Earnings quality and durability are open to question. More than RMB2bn of H1 profit came from fair-value "
        "gains, and we expect earnings to fall in FY28E as new capacity arrives, so we value on a cycle-adjusted 18x "
        "FY27E P/E.",
    ],
    background=(
        "GigaDevice was founded in Beijing in 2005 by Zhu Yiming, who also founded DRAM maker ChangXin Memory (CXMT). "
        "It listed in Shanghai in 2016 and added a Hong Kong H-share listing in early 2026. It started in serial NOR "
        "flash, launched GD32 Arm-based microcontrollers in 2013, and later added sensors (via the Silead acquisition) "
        "and analog chips. Through a partnership with CXMT it sells niche DRAM under its own brand. It is the world's "
        "No.2 NOR flash supplier behind Winbond, with ~18% share."),
    model=(
        "GigaDevice is fabless: it designs chips and outsources wafer fabrication (to foundries such as SMIC and Hua "
        "Hong, and to CXMT for DRAM). It sells through distributors and directly to consumer, industrial, auto, "
        "PC/server and communications customers. Memory (~85% of revenue) is a price-taker business with high operating "
        "leverage: costs are mostly wafer purchases and R&D, so price rises drop straight to profit. MCUs (~12%) are "
        "stickier design-win products with long life cycles. AI servers, AI PCs and edge devices raise both NOR density "
        "and unit demand."),
    competition=(
        "In NOR flash the main rivals are Winbond, Macronix, Puya, XMC and ISSI; in SLC NAND, Kioxia, Winbond and "
        "Macronix; in niche DRAM, Nanya, Winbond and ESMT, as Samsung, SK Hynix and Micron exit DDR4. In MCUs it faces "
        "STMicro, NXP, Infineon, Renesas, Microchip and TI globally, plus local players at home, where it benefits from "
        "domestic substitution. Taiwanese memory peers trade on ~4x forward earnings, which shows how the market "
        "discounts peak-cycle profits."),
    tam=(
        "Frost & Sullivan estimates the global specialty-memory market at US$15.7bn in 2025, of which NOR flash was "
        "US$3.1bn. Both are rising sharply in value in 2026 as prices climb. The MCU market is larger and grows with "
        "industrial automation, EVs and IoT. GigaDevice's TTM revenue of RMB16.6bn (~US$2.5bn) gives it a meaningful "
        "share in each niche."),
    financials=(
        "FY25 revenue rose 25% to RMB9.2bn and net profit 49% to RMB1.65bn. H1'26 revenue jumped 179% to RMB11.6bn and "
        "net profit 1,092% to RMB6.9bn, including more than RMB2bn of fair-value gains (36Kr). Net cash is ~RMB17bn with "
        "almost no debt. We forecast revenue of RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of "
        "RMB{np26}bn/{np27}bn/{np28}bn for FY26-28E, peaking in FY27E and then normalising as capacity returns. Our FY26E "
        "EPS of RMB{eps26} sits between the S&P consensus (RMB15.9) and the Simply Wall St figure (RMB20.9) in the "
        "source pack."),
    valuation=(
        "Our TP of RMB{tp} applies 18x to FY27E EPS of RMB{eps27}. This cycle-adjusted multiple is above NXP (~14x) for "
        "growth and well above Taiwanese memory peers (~4x peak earnings) for MCU diversification and domestic "
        "substitution. At the TP the stock would trade on ~25x our post-peak FY28E EPS. The consensus target of RMB632 "
        "assumes a longer cycle. The H-share (3986.HK) trades close to parity. Bear case RMB{bear}: mid-cycle EPS of "
        "RMB12 at ~17x. Bull case RMB{bull}: the shortage extends through 2027."),
    risks=[
        "Memory price reversal as new capacity arrives (peak-cycle risk).",
        "Volatile fair-value gains on equity holdings.",
        "Dependence on CXMT and escalation of US export controls.",
        "Sentiment swings, e.g. September reports that Beijing may allow Nvidia chip purchases.",
    ],
    catalysts=[
        "Q3'26 results on 30 October.",
        "Monthly NOR/DRAM contract prices (TrendForce).",
        "Index inclusion of the H-share; MCU recovery.",
    ],
    sources="Company FY25 results and H1'26 report; 36Kr; China Biz Insider; TrendForce/Taipei Times; Frost & Sullivan "
            "(via Cailian); StockAnalysis/S&P Global; IBKR; source pack.",
)

JUSHI = dict(
    key="jushi", name="China Jushi", cn="中国巨石", ticker="600176.SH",
    listing="A-share only",
    sector="Advanced Materials", theme="Semiconductors & materials",
    ccy="RMB", price=38.30, hi52=77.20, lo52=14.78, ytd=124.0,
    fin_unit="RMB bn", fx=1.0, shares=4.00,
    mcap_local=152.0, mcap_ccy="RMB", net_cash=-11.47, ev=165.0,
    profile="profit",
    hist=dict(rev=[14.88, 15.86, 18.88], gm=[27.9, 24.8, 33.0],
              np=[3.04, 2.45, 3.29], eps=[0.76, 0.61, 0.82], dps=[0.275, 0.24, 0.36]),
    est=dict(rev=[25.0, 30.5, 33.0], gm=[39.0, 41.0, 40.0],
             np=[6.9, 9.0, 9.8], payout=0.40),
    tp_method=dict(type="pe", mult=20, yr=1),
    scen=dict(
        bear=dict(type="pe", eps=1.75, mult=16, desc="E-cloth prices fade; roving price war"),
        bull=dict(type="pe", eps=2.60, mult=23, desc="AI-driven e-cloth tightness persists"),
    ),
    cons=dict(tp=63.27, n=16, eps26=1.95, eps27=2.39, ratings="11 Strong Buy / 3 Buy / 2 Hold"),
    kpis=[("7628 e-cloth price, H1'26", "RMB6.02/m (+49%)"),
          ("Roving price, H1'26", "Flat YoY"),
          ("Huai'an e-glass line (2026)", "100kt yarn + 390m m cloth"),
          ("Next Huai'an line", "50kt + 320m m (1.5-yr build)"),
          ("Global e-glass fibre share", "~23% → ~28%")],
    tiles=[("8.43Mt", "China glass-fibre yarn output in 2025 (+11.5%)"),
           ("~23% → 28%", "Jushi share of global electronic-grade glass fibre after Huai'an"),
           ("+15-20%", "E-cloth price increases announced in September 2026")],
    peers=[("Sinoma Science & Tech", "002080 CH", 24.9, 22.5, 3.4),
           ("Nitto Boseki", "3110 JP", 26.6, 18.5, 5.1)],
    self_peer=(16.1, 19.5, 7.9),
    headline="AI has turned a commodity producer into a growth story, but pricing still drives earnings",
    summary=("China Jushi is the world's largest glass-fibre maker. AI-server demand for high-layer PCBs has tightened "
             "supply of electronic yarn and cloth, which lifted H1'26 net profit 74%. The stock more than doubled, then "
             "halved from its peak. At {pe27}x FY27E P/E the valuation is fair for a business whose earnings still hinge "
             "on e-cloth pricing. We initiate at <b>{rating}</b>, TP RMB{tp} ({up} upside)."),
    thesis=[
        "Electronic cloth is the main profit driver. The price of 7628 e-fabric averaged RMB6.02/m in H1'26 (+49%) and "
        "rose another 15-20% in September, while roving prices were flat.",
        "New capacity is arriving on time. The 100kt Huai'an e-glass line (with 390m metres of cloth) hit full output "
        "by June. A 50kt/320m-metre line and a Tongxiang project follow and will take global e-glass share from ~23% "
        "toward ~28%.",
        "Much of this is priced in, and supply is responding. Kingboard, Taishan (Sinoma) and others are adding e-yarn "
        "capacity, and Zhenshi Group, the second-largest shareholder, is selling.",
    ],
    background=(
        "China Jushi grew out of a glass-fibre plant in Tongxiang, Zhejiang and has been listed in Shanghai since 1999. It "
        "is controlled by China National Building Material (CNBM), and Zhenshi Group is the second-largest shareholder. "
        "It runs tank-furnace bases in Tongxiang, Jiujiang, Chengdu and Huai'an in China, plus Egypt and the US, and is "
        "the world's largest producer by capacity. Products span roving, chopped strands, yarn and electronic cloth."),
    model=(
        "Glass fibre is made in continuous tank furnaces that run for 8-10 years. The business is capital- and "
        "energy-intensive with high fixed costs, so scale, furnace efficiency and utilisation decide cost position. Jushi "
        "sells roving and chopped strands for wind blades, construction, autos, thermoplastics and pipes. It also sells "
        "electronic yarn and woven cloth to copper-clad-laminate makers, who supply PCB manufacturers. Pricing follows "
        "industry capacity additions. E-cloth demand is now tied to AI-server boards, where thinner, low-dielectric "
        "grades command premiums."),
    competition=(
        "The main rivals are Taishan Fiberglass (Sinoma Science & Technology), Chongqing Polycomp (CPIC), "
        "Saint-Gobain/Vetrotex, Johns Manville and Nippon Electric Glass. In high-end electronic cloth they are Nittobo "
        "(Japan), Taiwan Glass, Grace Fabric and Kingboard. China produces most of the world's glass fibre and Jushi is "
        "the cost leader. Its gap is premium low-dielectric cloth, where Nittobo leads and Jushi is still in customer "
        "certification."),
    tam=(
        "China produced 8.43Mt of glass-fibre yarn in 2025 (+11.5%), the large majority of global output. The "
        "electronic-grade segment is smaller but growing fastest, driven by AI servers, high-speed networking and "
        "automotive electronics. Jushi's FY25 revenue of RMB18.9bn (~US$2.8bn) makes it the global scale leader."),
    financials=(
        "FY25 revenue grew 19% to RMB18.9bn and net profit 34% to RMB3.3bn as gross margin recovered from 24.8% to 33.0%. "
        "H1'26 revenue rose 22.5% to RMB11.2bn and net profit 74% to RMB2.93bn, and TTM gross margin is 38%. Net debt is "
        "~RMB11.5bn and capex is rising (a RMB2.4bn e-cloth project was approved in July). We forecast net profit of "
        "RMB{np26}bn/{np27}bn/{np28}bn for FY26-28E, below consensus (FY26E EPS RMB1.95), because we assume e-cloth "
        "prices plateau in 2027 as new capacity arrives."),
    valuation=(
        "Our TP of RMB{tp} is 20x FY27E EPS of RMB{eps27}, a discount to Sinoma Science & Technology (~25x) and Nittobo "
        "(~27x) forward because more of Jushi's profit comes from commodity roving. The stock is up 124% YTD but 50% "
        "below its RMB77.20 high. The consensus target (RMB63.3) assumes stronger pricing. Bear case RMB{bear}: e-cloth "
        "prices fade and roving enters a price war. Bull case RMB{bull}: AI-driven tightness persists into 2028."),
    risks=[
        "E-yarn and e-cloth capacity additions by peers.",
        "Roving price war; energy costs.",
        "Share overhang from Zhenshi Group selling.",
        "Trade actions on Chinese or Egyptian glass fibre.",
    ],
    catalysts=[
        "Q3'26 results on 20 October.",
        "E-cloth price announcements.",
        "Certification of low-dielectric products.",
    ],
    sources="Company FY25 and H1'26 results; Futu; Yicai Global; CompositesWorld; JEC; StockAnalysis/S&P Global; IBKR; "
            "source pack.",
)

JLMAG = dict(
    key="jlmag", name="JL Mag Rare-Earth", cn="金力永磁", ticker="6680.HK",
    listing="A-share 300748.SZ at RMB23.47 (H at ~46% discount)",
    sector="Rare-earth Magnets", theme="Semiconductors & materials",
    ccy="HK$", price=14.75, hi52=28.71, lo52=14.33, ytd=-20.1, a_price=23.47,
    fin_unit="RMB bn", fx=HKD_PER_RMB, shares=1.37,
    mcap_local=29.6, mcap_ccy="RMB", mcap_note="A+H", net_cash=2.26, ev=27.5,
    profile="profit",
    hist=dict(rev=[6.69, 6.76, 7.72], gm=[15.6, 10.4, 20.3],
              np=[0.564, 0.291, 0.706], eps=[0.42, 0.22, 0.52], dps=[0.26, None, 0.40]),
    est=dict(rev=[9.8, 12.0, 14.2], gm=[21.5, 22.0, 22.5],
             np=[0.90, 1.15, 1.40], payout=0.50),
    tp_method=dict(type="pe", mult=19, yr=1),
    scen=dict(
        bear=dict(type="pe", eps=0.65, mult=14.5, desc="Rare-earth prices slide; robot demand slips"),
        bull=dict(type="pe", eps=1.00, mult=21, desc="Humanoid volumes and export recovery"),
    ),
    cons=dict(tp=37.28, tp_ccy="RMB", tp_line="A-share", n=10, eps26=0.66, eps27=0.85,
              ratings="5 Strong Buy / 4 Buy / 1 Strong Sell"),
    mix_title="H1'26 revenue by end-market (%)",
    mix=[("NEVs & auto parts", 56.0), ("Energy-efficient air-con", 24.0),
         ("Robots & servo motors", 6.6), ("Wind power", 6.3), ("Other", 7.1)],
    tiles=[("60kt", "JL Mag magnet capacity target by end-2027 (~40kt in 2025)"),
           ("+96%", "Growth in robot-related sales, H1'26"),
           ("~90%", "China's share of global sintered NdFeB magnet production")],
    peers=[("Ningbo Yunsheng", "600366 CH", 20.9, 16.3, 1.6),
           ("Zhong Ke San Huan", "000970 CH", 56.5, 33.2, 1.8),
           ("MP Materials", "MP US", 130.3, 183.6, 17.9)],
    self_peer=(24.7, 24.4, 3.1), self_peer_label="JL Mag (A-share)",
    headline="The global magnet leader; own it through the discounted H-share",
    summary=("JL Mag is the world's largest maker of high-performance NdFeB rare-earth magnets for EV motors, efficient "
             "air-conditioners, wind turbines and, increasingly, robots. H1'26 net profit rose 52% and gross margin "
             "5.3pt. The H-share trades at a ~46% discount to the A-share, on {pe27}x FY27E P/E with a ~{dy26} yield. We "
             "initiate on the H-share at <b>{rating}</b>, TP HK${tp} ({up} upside)."),
    thesis=[
        "JL Mag's position is strategic. China makes ~90% of the world's sintered NdFeB magnets and controls rare-earth "
        "exports. JL Mag leads on scale and technology; its grain-boundary diffusion process cuts heavy rare-earth use.",
        "New capacity drives growth: it rises from ~40kt (2025) to 60kt by end-2027. Robot-related sales rose 96% in "
        "H1'26, and small-batch humanoid rotor deliveries have started.",
        "The H-share is the cheaper line, on {pe27}x FY27E against ~{pe27a}x for the A-share, with the same earnings "
        "and a dividend yield near {dy26}.",
    ],
    background=(
        "JL Mag was founded in 2008 in Ganzhou, Jiangxi, at the heart of China's ionic-clay heavy rare-earth region, by "
        "chairman Cai Baogui and partners. It listed on Shenzhen's ChiNext board in 2018 and in Hong Kong in January "
        "2022. Its production bases are in Ganzhou, Ningbo and Baotou (Inner Mongolia, close to light rare-earth supply), "
        "and it is building capacity overseas. Customers include leading global automakers, auto-parts suppliers, "
        "air-conditioner makers and wind-turbine OEMs."),
    model=(
        "JL Mag buys rare-earth oxides and metals (PrNd, dysprosium, terbium) from China's state-controlled rare-earth "
        "groups and turns them into sintered magnets made to customer specifications. Pricing is broadly raw-material "
        "cost plus a processing fee, so volume and processing margin drive profit. Rising rare-earth prices bring "
        "inventory gains and falling prices erode them, which explains the FY24 margin trough. Process technology "
        "(diffusion that saves heavy rare earths, recycling) and long qualification cycles with auto and robot customers "
        "create switching costs."),
    competition=(
        "Chinese rivals include Ningbo Yunsheng, Zhong Ke San Huan, Ningbo Jintian, Yantai Zhenghai and Innuovo. "
        "Overseas producers include Proterial, Shin-Etsu, TDK and VAC, and MP Materials is building US magnet capacity "
        "with Department of Defense backing. China's 2025 rare-earth export-licensing regime slows exports but "
        "entrenches Chinese leaders. JL Mag's advantages are scale, cost and a qualified customer base; non-Chinese "
        "buyers, however, are actively seeking to diversify supply."),
    tam=(
        "Industry estimates put high-performance NdFeB demand growth at ~10-15% a year to 2030. The drivers are EV "
        "traction motors (2-3kg of magnet per car), variable-frequency air-conditioners, direct-drive wind turbines and "
        "robotics (roughly 2-4kg per humanoid, on industry estimates). NdPr oxide peaked near US$98k/t in January 2026 and "
        "has eased since (RMB750k/t in July)."),
    financials=(
        "Revenue grew from RMB6.7bn (FY23) to RMB7.7bn (FY25). After a FY24 trough (gross margin 10.4%), FY25 net profit "
        "rose 142% to RMB0.71bn. H1'26 revenue rose 33% to RMB4.65bn and net profit 52% to RMB462m, at a 21.7% gross "
        "margin. Net cash is ~RMB2.3bn. We forecast net profit of RMB{np26}bn/{np27}bn/{np28}bn for FY26-28E, in line "
        "with consensus (FY26E EPS RMB0.66), with capacity growth offset by softer rare-earth prices."),
    valuation=(
        "Our H-share TP of HK${tp} is 19x FY27E EPS of RMB{eps27}, a discount to Ningbo Yunsheng (~21x) and to the "
        "A-share (~{pe27a}x) that reflects the persistent A/H gap. Even at our TP the H-share would sit ~33% below the "
        "A-share. The A-share consensus target is RMB37.3, but at RMB23.47 we see the A-share as fairly valued. Bear case "
        "HK${bear}: rare-earth prices slide and robot demand slips. Bull case HK${bull}: humanoid volumes and an export "
        "recovery."),
    risks=[
        "Rare-earth price volatility (inventory gains and losses).",
        "Export licensing and trade policy.",
        "Customer concentration in NEVs; overseas plant execution.",
        "The A/H discount could persist or widen.",
    ],
    catalysts=[
        "Q3'26 results on 28 October.",
        "Humanoid-robot rotor orders.",
        "Capacity ramp toward 60kt; dividends.",
    ],
    sources="Company H1'26 HKEX interim results; SMM; Benchmark Mineral Intelligence; Simply Wall St; StockAnalysis/"
            "S&P Global; IBKR; source pack.",
)

HANS = dict(
    key="hans", name="Han's Laser Technology", cn="大族激光", ticker="002008.SZ",
    listing="A-share; PCB-equipment arm Han's CNC listed separately",
    sector="Industrial Equipment", theme="Equipment, robotics & medtech",
    ccy="RMB", price=70.18, hi52=168.08, lo52=34.43, ytd=70.8,
    fin_unit="RMB bn", fx=1.0, shares=1.03,
    mcap_local=72.3, mcap_ccy="RMB", net_cash=5.76, ev=70.4,
    profile="profit",
    hist=dict(rev=[14.09, 14.77, 18.76], gm=[31.4, 30.4, 32.2],
              np=[0.82, 1.69, 1.19], eps=[0.78, 1.62, 1.15], dps=[0.20, 0.35, 0.20]),
    est=dict(rev=[27.5, 34.0, 39.0], gm=[34.5, 35.0, 35.0],
             np=[2.75, 3.90, 4.60], payout=0.15),
    tp_method=dict(type="pe", mult=25, yr=1),
    scen=dict(
        bear=dict(type="pe", eps=3.0, mult=17, desc="AI capex pause; PCB orders digest"),
        bull=dict(type="pe", eps=4.5, mult=28, desc="AI PCB capex keeps accelerating"),
    ),
    cons=dict(tp=157.23, n=11, eps26=3.11, eps27=4.88, ratings="8 Strong Buy / 2 Buy / 1 Hold"),
    mix_title="FY25 revenue mix (%)",
    mix=[("Industrial lasers, new-energy & other", 56), ("PCB equipment", 31),
         ("Consumer-electronics, display & semi equipment", 13)],
    tiles=[("RMB27bn+", "Han's 2026 revenue guidance (+44%)"),
           ("RMB19bn + RMB9bn", "New orders plus backlog cited by management"),
           ("+73%", "PCB-equipment revenue growth in FY25 (to RMB5.8bn)")],
    peers=[("HGTECH (Huagong)", "000988 CH", 38.6, 61.6, 5.9),
           ("Wuxi Lead Intelligent", "300450 CH", 19.8, 20.3, 3.1),
           ("IPG Photonics", "IPGP US", 38.1, 23.7, 2.3)],
    self_peer=(16.9, 19.7, 2.9),
    headline="An AI-capex winner with clear order visibility; the sell-off is an entry point",
    summary=("Han's Laser is Asia's largest laser and smart-manufacturing equipment maker. AI-server PCBs need far more "
             "drilling and processing, and its PCB-equipment arm now leads the group's growth: H1'26 revenue rose 76% and "
             "net profit 164%. The stock is ~58% below its high (−7% on 12 October). At {pe27}x FY27E P/E, with RMB28bn of "
             "new orders and backlog, we initiate at <b>{rating}</b>, TP RMB{tp} ({up} upside)."),
    thesis=[
        "AI-server PCBs are a multi-year growth driver. High-layer, high-density boards need more mechanical and laser "
        "drilling, exposure and testing; FY25 PCB-equipment revenue rose 73% to RMB5.8bn.",
        "Order visibility is unusually good. Management guides FY26 revenue of at least RMB27bn (+44%) and cites RMB19bn "
        "of new orders plus a RMB9bn backlog.",
        "Operating leverage is lifting margins. H1'26 gross margin rose 4pt to 34.9%; we forecast FY27E EPS of "
        "RMB{eps27} (+42%).",
    ],
    background=(
        "Han's Laser was founded in Shenzhen in 1996 by Gao Yunfeng, who remains chairman and controlling shareholder "
        "(he trimmed his stake in September 2026). It listed in Shenzhen in 2004 and has become Asia's largest "
        "industrial-laser equipment group, selling more than 54,000 machines in FY25. Its businesses include Han's CNC "
        "(PCB drilling and processing, separately listed), consumer-electronics automation (a long-standing Apple "
        "supply-chain vendor), lithium-battery equipment, semiconductor and display equipment, and high-power cutting "
        "and welding lasers."),
    model=(
        "Han's sells capital equipment, so revenue tracks customers' capex cycles: PCB makers (now driven by AI "
        "servers), consumer-electronics assemblers (Apple product cycles), battery makers and general metal fabricators. "
        "It sells systems that integrate in-house lasers, motion control and software, plus spare parts and service. "
        "Margins depend on mix, since PCB and precision equipment earn more than general cutting lasers, and on "
        "utilisation. Working capital rises in upcycles."),
    competition=(
        "In PCB equipment, Han's CNC competes with Japan's Via Mechanics and Mitsubishi Electric (laser drilling), "
        "Germany's Schmoll and Taiwanese makers, and leads in China. In industrial lasers the global rivals are Trumpf, "
        "Coherent, IPG and Bystronic, with HGTECH (Huagong) and Hymson at home; in battery equipment, Lead Intelligent "
        "and Yinghe. Han's edge is breadth, closeness to customers in Shenzhen's electronics cluster, and cost."),
    tam=(
        "Global PCB output is roughly US$75-80bn a year (Prismark). AI-server and high-speed networking boards are the "
        "fastest-growing segment, prompting capacity additions in China, Taiwan and Southeast Asia. Industrial laser "
        "processing is a broader, more cyclical market. Han's FY26E revenue of ~RMB27bn (~US$4bn) places it among the "
        "largest players in both."),
    financials=(
        "FY25 revenue rose 27% to RMB18.8bn. Reported net profit fell 30% to RMB1.19bn against a 2024 base inflated by "
        "RMB1.25bn of one-off gains, while core profit rose 82% to RMB0.81bn. H1'26 revenue rose 76% to RMB13.4bn and net "
        "profit 164% to RMB1.29bn. Net cash is ~RMB5.8bn. We forecast revenue of RMB{rev26}bn/{rev27}bn/{rev28}bn and "
        "net profit of RMB{np26}bn/{np27}bn/{np28}bn for FY26-28E. Our FY26E is close to the forecast cited in the source "
        "pack (RMB2.65bn), but our FY27E is below both that and the S&P consensus."),
    valuation=(
        "Our TP of RMB{tp} is 25x FY27E EPS of RMB{eps27}: a premium to Lead Intelligent (~20x forward) for AI exposure, "
        "but below HGTECH (~39x). UOB's target is RMB153.2 and the consensus average RMB157, both on higher FY27 "
        "earnings. Bear case RMB{bear}: an AI capex pause and PCB order digestion. Bull case RMB{bull}: AI PCB capex keeps "
        "accelerating."),
    risks=[
        "AI capex slowdown or PCB capacity digestion.",
        "Apple and consumer-electronics cycle.",
        "Further share sales by the controlling shareholder.",
        "Minority leakage from listed subsidiaries.",
    ],
    catalysts=[
        "Q3'26 results on 23 October.",
        "Large PCB-equipment orders.",
        "FY27 guidance and AI-server PCB capex data.",
    ],
    sources="Company FY25 results release and H1'26 report; Longbridge; UOB Kay Hian; Futu; MarketScreener; "
            "StockAnalysis/S&P Global; IBKR; source pack.",
)

HORIZON = dict(
    key="horizon", name="Horizon Robotics", cn="地平线机器人", ticker="9660.HK",
    listing="Hong Kong only (IPO October 2024 at HK$3.99)",
    sector="Auto Semiconductors & Software", theme="Equipment, robotics & medtech",
    ccy="HK$", price=3.995, hi52=9.80, lo52=3.60, ytd=-54.1,
    fin_unit="RMB bn", fx=HKD_PER_RMB, shares=15.87,
    mcap_local=63.4, mcap_ccy="HK$", net_cash=10.0, ev=44.1,
    profile="loss", loss_label="Adj. net profit (loss)",
    hist=dict(rev=[1.55, 2.38, 3.76], gm=[70.5, 77.3, 64.5], np=[None, -1.68, -2.81]),
    est=dict(rev=[5.1, 7.0, 9.3], gm=[64.0, 63.0, 62.0], np=[-3.0, -1.8, -0.2]),
    tp_method=dict(type="evs", mult=8, yr=1),
    scen=dict(
        bear=dict(type="evs", rev=6.0, mult=3.5, desc="3.5x on FY27E revenue of RMB6.0bn"),
        bull=dict(type="evs", rev=8.5, mult=10, desc="10x on FY27E revenue of RMB8.5bn"),
    ),
    cons=dict(tp=8.15, n=None, eps26=None, eps27=None, ratings="Consensus Buy (target HK$8.2-8.6)"),
    mix_title="H1'26 revenue mix (%)",
    mix=[("Licensing & services (~90% GM)", 55), ("Products & solutions", 45)],
    tiles=[("2.22m", "Journey SoC shipments in H1'26 (+12%) while China car retail fell 20%"),
           ("~500 / ~130", "Cumulative design wins: all models / advanced-NOA models"),
           ("RMB1tn+", "China ADAS/AD solutions market by 2030 (F&S, via prospectus)")],
    peers=[("Mobileye", "MBLY US", 16.6, None, 2.3),
           ("Ambarella", "AMBA US", 73.0, None, 6.5),
           ("Black Sesame", "2533 HK", None, None, 4.5)],
    peer_note="EV/sales on trailing revenue; Black Sesame approximated by P/S.",
    self_peer=(None, None, 9.5),
    headline="An 'ARM + Android' play on driver assistance, back at its IPO price; the market is overlooking licensing",
    summary=("Horizon designs automotive AI processors and licenses its chip IP, algorithms and software to automakers "
             "and Tier-1s. Licensing reached 55% of H1'26 revenue at a 90% gross margin even as China car sales fell 20%. "
             "The shares are back at the 2024 IPO price, which values the company at ~{evs27}x FY27E EV/sales. We initiate "
             "at <b>{rating}</b>, TP HK${tp} ({up} upside), though losses run to 2028 and the H1 cash draw was "
             "steep."),
    thesis=[
        "Horizon is taking share in a falling market. Journey SoC shipments rose 12% to 2.2m in H1'26 while China "
        "passenger-car retail fell 20%, and design wins are near 500 models, including ~130 with advanced NOA.",
        "Licensing changes the economics of the business. Licence and service revenue rose 53% to RMB1.13bn at a 90% "
        "gross margin, and Toyota programmes and global Tier-1s (Denso, AUMOVIO) are adopting Journey 6B.",
        "Several catalysts fall in 2026-27: HSD urban NOA is ramping, integrated cockpit-driving mass production starts "
        "in Q4, Journey 7 is due in 2027, and FY26 revenue guidance is above RMB5bn.",
    ],
    background=(
        "Horizon Robotics was founded in Beijing in 2015 by Yu Kai, former head of Baidu's Institute of Deep Learning. "
        "It listed in Hong Kong in October 2024 at HK$3.99, roughly where the shares trade today. Strategic shareholders "
        "include major Chinese automakers, and it runs CARIZON, a software joint venture with Volkswagen's CARIAD. Its "
        "Journey processors power driver-assistance features for most major Chinese OEMs and, increasingly, "
        "international brands. In March 2026 it deconsolidated its robotics affiliate, D-Robotics."),
    model=(
        "Horizon sells three layers. First, Journey system-on-chips plus reference solutions for ADAS and highway/urban "
        "navigate-on-autopilot (NOA). Second, the full-stack HSD (Horizon SuperDrive) urban driving system. Third, "
        "licences for its processor IP, algorithms, toolchain and foundation models. Products and solutions (45% of "
        "H1'26 revenue) carry hardware margins; licensing and services (55%) carry ~90% margins and scale with "
        "partners' volumes. Heavy R&D (RMB5.2bn in FY25) keeps the company loss-making, with breakeven targeted for "
        "2028."),
    competition=(
        "Horizon competes with Nvidia (Orin/Thor) at the high end, Mobileye and Qualcomm in mainstream ADAS, Huawei's "
        "vertically integrated Qiankun stack, Black Sesame, and automakers' in-house chips (NIO, Xpeng, BYD). Software "
        "specialists such as Momenta compete for the stack on Nvidia or Qualcomm silicon. Horizon's edge is cost-optimised "
        "silicon for China's mass market plus an open licensing model OEMs can customise. The risk is that large OEMs take "
        "more of the stack in-house."),
    tam=(
        "China sells more than 20m passenger cars a year, and driver assistance is moving fast down the price ladder: "
        "HSD targets cars around RMB70-150k. Frost & Sullivan, cited in Horizon's prospectus, projected China's ADAS/AD "
        "solutions market to grow from ~RMB60bn in 2023 to more than RMB1tn by 2030. Robotics licensing via D-Robotics "
        "adds optionality."),
    financials=(
        "Revenue rose from RMB1.55bn (FY23) to RMB3.76bn (FY25, +58%) at a 64.5% gross margin. Reported results swing with "
        "fair-value items: a RMB10.5bn loss in FY25, then a RMB3.8bn profit in H1'26, mostly from fair-value and "
        "deconsolidation gains. The adjusted net loss was RMB2.81bn in FY25 and RMB1.67bn in H1'26. Cash fell from "
        "RMB20.2bn to RMB14.9bn in the half; we estimate net cash of ~RMB13.7bn after borrowings. We forecast revenue of "
        "RMB{rev26}bn/{rev27}bn/{rev28}bn, with the adjusted loss narrowing to near breakeven in FY28E."),
    valuation=(
        "Our TP of HK${tp} applies 8x EV/sales to FY27E revenue of RMB{rev27}bn and adds net cash. The multiple is above "
        "Mobileye (~2.3x) and Ambarella (~6.5x) because over half of revenue is high-margin licensing growing more than "
        "50%. The consensus target is ~HK$8.2-8.6. Bear case HK${bear}: 3.5x on lower FY27E revenue (RMB6.0bn). Bull "
        "case HK${bull}: 10x on RMB8.5bn."),
    risks=[
        "China auto price war and OEM in-house chips.",
        "Competition from Nvidia, Qualcomm and Huawei.",
        "Cash burn and dilution; foundry or export-control restrictions.",
        "Execution on HSD and Journey 7.",
    ],
    catalysts=[
        "Q4'26 start of integrated cockpit-driving mass production.",
        "HSD model launches and shipment updates.",
        "Journey 7 tape-out; L4 robotaxi pilot.",
    ],
    sources="Company FY25 annual results and H1'26 HKEX interim results; earnings call; Business Insider; Gasgoo; "
            "StockAnalysis; IBKR; source pack.",
)

LEADERDRIVE = dict(
    key="leaderdrive", name="Leader Harmonious Drive Systems (Leaderdrive)", cn="绿的谐波", ticker="688017.SH",
    listing="STAR Market; Hong Kong H-share listing planned",
    sector="Robotics Components", theme="Equipment, robotics & medtech",
    ccy="RMB", price=252.02, hi52=495.66, lo52=139.62, ytd=31.2,
    fin_unit="RMB m", fx=1.0, shares=183.3,
    mcap_local=46.2, mcap_ccy="RMB", net_cash=2170.0, ev=44040.0,
    profile="profit",
    hist=dict(rev=[356.2, 387.4, 570.7], gm=[36.1, 28.7, 31.7],
              np=[84.2, 56.2, 124.4], eps=[0.50, 0.33, 0.69], dps=[0.30, 0.10, 0.21]),
    est=dict(rev=[780.0, 1100.0, 1550.0], gm=[31.0, 32.0, 33.0],
             np=[150.0, 225.0, 330.0], payout=0.30),
    tp_method=dict(type="fut_pe", np=1000.0, mult=40, years=3, rate=0.10),
    scen=dict(
        bear=dict(type="fut_pe", np=600.0, mult=35, years=3, rate=0.10, desc="FY30E profit RMB0.6bn at 35x"),
        bull=dict(type="fut_pe", np=1800.0, mult=45, years=3, rate=0.10, desc="FY30E profit RMB1.8bn at 45x"),
    ),
    cons=dict(tp=322.66, n=15, eps26=0.93, eps27=1.41,
              ratings="4 Strong Buy / 3 Buy / 4 Hold / 2 Sell / 2 Strong Sell"),
    mix_title="H1'26 revenue mix (%)",
    mix=[("Harmonic reducers & metal parts", 82.7), ("Electromechanical actuators", 15.7), ("Other", 1.6)],
    tiles=[("30-40%", "Leaderdrive share of China's harmonic-reducer market (JPMorgan est.)"),
           ("~14-20", "Harmonic reducers per humanoid robot (industry estimates)"),
           ("~300k", "Industrial robots installed in China each year (IFR)")],
    peers=[("Harmonic Drive Systems", "6324 JP", 79.9, 50.9, 9.3),
           ("Nabtesco", "6268 JP", 21.9, 11.8, 1.7),
           ("Zhejiang Shuanghuan", "002472 CH", 19.9, 13.3, 3.4)],
    self_peer=(226.0, 278.3, 65.9),
    headline="A good company priced for a humanoid future that has not yet arrived",
    summary=("Leaderdrive is China's leading maker of harmonic reducers, the precision gears in robot joints, and a major "
             "supplier to humanoid-robot developers. Growth is solid (H1'26 revenue +39%), but at ~{pe26}x FY26E and "
             "~{pe27}x FY27E P/E the shares discount mass humanoid adoption years ahead of the evidence. We initiate at "
             "<b>{rating}</b> with a TP of RMB{tp} ({upabs} downside)."),
    thesis=[
        "Leaderdrive's franchise is strong. With an estimated 30-40% of China's harmonic-reducer market, it has displaced "
        "Japanese imports at materially lower prices and supplies humanoid makers such as Agibot and UBTech.",
        "The absolute numbers are still small. FY25 revenue was RMB571m and H1'26 net profit RMB70m. In Q2, margins "
        "fell and results missed forecasts.",
        "The shares are priced for perfection. Our TP capitalises FY30E net profit of RMB1.0bn (8x FY25) at 40x and "
        "discounts it back three years, and even our bull case (RMB{bull}) needs a humanoid boom.",
    ],
    background=(
        "Leaderdrive was founded in Suzhou in 2011 by chairman Zuo Yuyu, who developed strain-wave gearing in-house when "
        "China depended on Japanese imports. It listed on Shanghai's STAR Market in 2020 and is widely regarded as "
        "China's largest harmonic-reducer maker. It serves industrial and collaborative robot makers, humanoid "
        "developers, CNC machine tools, semiconductor equipment and medical devices. It plans a Hong Kong H-share listing "
        "and a robotics joint venture with SKF."),
    model=(
        "Leaderdrive makes harmonic reducers (flexspline, circular spline and wave generator) and related precision metal "
        "parts, which were 83% of H1'26 revenue. It also sells integrated electromechanical joint actuators (16%) that "
        "combine reducer, motor, encoder and drive and raise content per joint. Building its own machine tools and "
        "process know-how gives it a cost edge. Gross margin has fallen from ~50% (FY21) to ~31% as it cut prices to win "
        "share and invested in capacity."),
    competition=(
        "The global benchmark is Harmonic Drive Systems (Japan), alongside Nidec-Shimpo. Domestic rivals include Laifual, "
        "Zhongda Leader, KOFON and Han's Motion. For heavier joints, RV reducers (Nabtesco, Shuanghuan) and planetary or "
        "roller-screw designs compete. A key risk is that humanoid designs shift to alternative transmissions, or that "
        "robot makers bring reducers in-house."),
    tam=(
        "China installs ~300k industrial robots a year (IFR), each with several harmonic reducers in its smaller joints. "
        "Humanoids could add a much larger pool: at ~14-20 reducers per robot, one million humanoids a year would need "
        "14-20 million units, many times today's market. Timing and design choices remain highly uncertain, and humanoid "
        "output today is in the tens of thousands of units."),
    financials=(
        "Revenue fell from RMB443m (FY21) to RMB356m (FY23) before recovering to RMB571m in FY25 (+47%), with net profit of "
        "RMB124m. H1'26 revenue rose 39% to RMB349m and net profit 31% to RMB70m, but Q2 margins fell as expenses rose. "
        "Net cash is ~RMB2.2bn. We forecast revenue of RMB{rev26}m/{rev27}m/{rev28}m and net profit of "
        "RMB{np26}m/{np27}m/{np28}m for FY26-28E, below consensus (FY26E EPS RMB0.93)."),
    valuation=(
        "Our TP of RMB{tp} capitalises FY30E net profit of RMB1.0bn at 40x, discounts it back three years at 10% and adds "
        "net cash. Harmonic Drive Systems, the global leader, trades on ~80x forward earnings and ~9x EV/sales, against "
        "~66x EV/sales for Leaderdrive. The consensus target is RMB323, but ratings are split (7 Buy, 4 Hold, 4 Sell). "
        "Bear case RMB{bear}: FY30E profit of RMB0.6bn at 35x. Bull case RMB{bull}: RMB1.8bn at 45x on a humanoid boom."),
    risks_title="Risks to our Sell call",
    risks=[
        "Faster humanoid mass production (e.g. Tesla Optimus, Unitree, Agibot) re-rates the theme.",
        "The H-share listing and SKF joint venture broaden the investor base.",
        "Thematic liquidity in STAR-market robotics names.",
        "Downside: price competition; a Q3 miss on 31 October.",
    ],
    catalysts=[
        "Q3'26 results on 31 October.",
        "Hong Kong H-share listing.",
        "Humanoid-robot order announcements.",
    ],
    sources="Company FY25 annual and H1'26 reports; Gasgoo; Investing.com; Simply Wall St; JPMorgan (via "
            "humanoid.guide); 36Kr; StockAnalysis/S&P Global; IBKR; source pack.",
)

EDGE = dict(
    key="edge", name="Shenzhen Edge Medical", cn="精锋医疗", ticker="2675.HK",
    listing="Hong Kong (IPO 8 Jan 2026 at HK$43.24); A-share listing in preparation",
    sector="Medical Devices", theme="Equipment, robotics & medtech",
    ccy="HK$", price=32.88, hi52=73.70, lo52=31.26, ytd=None, since_ipo=-24.0,
    fin_unit="RMB m", fx=HKD_PER_RMB, shares=389.6,
    mcap_local=12.81, mcap_ccy="HK$", net_cash=1800.0, ev=9130.0,
    profile="loss", loss_label="Net profit (loss)",
    hist=dict(rev=[48.0, 160.0, 455.7], gm=[None, None, 66.0], np=[-212.9, -218.5, -88.6]),
    est=dict(rev=[780.0, 1100.0, 1500.0], gm=[64.5, 65.0, 66.0], np=[15.0, 130.0, 250.0]),
    tp_method=dict(type="evs", mult=11, yr=1),
    scen=dict(
        bear=dict(type="evs", rev=850.0, mult=7, desc="7x on FY27E revenue of RMB850m"),
        bull=dict(type="evs", rev=1300.0, mult=14, desc="14x on FY27E revenue of RMB1.3bn"),
    ),
    cons=dict(tp=60.65, n=5, eps26=None, eps27=None, ratings="5 analysts, consensus Strong Buy"),
    mix_title="H1'26 revenue by region (%)",
    mix=[("Overseas", 69.8), ("Mainland China", 30.2)],
    tiles=[("158", "Robots installed or delivered by June 2026 (103 overseas)"),
           ("37", "Overseas jurisdictions with MP1000 approval"),
           ("~350 units", "Annual capacity of the new plant under construction (>100 today)")],
    peers=[("Intuitive Surgical", "ISRG US", 37.5, 34.6, 13.1),
           ("MicroPort MedBot", "2252 HK", None, None, 30.0)],
    peer_note="EV/sales on trailing revenue; MicroPort MedBot approximated by P/S at its last available price (31 Aug).",
    self_peer=(75.3, None, 13.3),
    headline="An export-led surgical-robot challenger at breakeven: small and volatile, but worth owning",
    summary=("Edge Medical makes multi-port and single-port laparoscopic surgical robots and, unusually for a Chinese "
             "medtech, sells most of them abroad (70% of H1'26 revenue). Revenue more than doubled in H1'26 and losses "
             "all but disappeared. The stock trades 24% below its January IPO price, at ~{evs27}x FY27E EV/sales versus "
             "~13x for Intuitive Surgical. We initiate at <b>{rating}</b>, TP HK${tp} ({up} upside)."),
    thesis=[
        "Exports drive growth: 49 of the 58 robots placed in H1'26 went overseas (Asia, Europe, the Middle East, "
        "Latin America), and MP1000 is approved in 37 overseas jurisdictions.",
        "Edge is close to turning a profit. Gross margin is ~64% and the H1 net loss narrowed 78% to RMB19m; we "
        "expect breakeven in FY26E and RMB{np28}m of profit in FY28E.",
        "The long-term upside is in recurring revenue. Instruments and service are <1% of revenue today. As the "
        "installed base (158 units) grows, an Intuitive-style razor-and-blade model should lift earnings quality.",
    ],
    background=(
        "Shenzhen Edge Medical was founded in Shenzhen in 2017 by Dr Wang Jianchen, its chairman and CEO. It is the first "
        "Chinese company with approvals for multi-port, single-port and natural-orifice (bronchoscopy) surgical robots. "
        "It listed in Hong Kong on 8 January 2026 at HK$43.24, raising ~HK$1.1bn with cornerstones including ADIA, UBS "
        "AM, OrbiMed and Tencent, and is preparing an A-share listing. By end-2025, surgeons in China had performed more "
        "than 14,000 robot-assisted procedures on its systems, plus over 500 telesurgery cases."),
    model=(
        "Edge sells robotic systems (99.6% of H1'26 revenue) to hospitals, directly and through overseas distributors, "
        "priced well below Intuitive's da Vinci. Each placement then drives recurring sales of instruments, consumables "
        "and service contracts, which are tiny today but carry high margins. Telesurgery capability and a single-port "
        "platform set it apart from domestic rivals. Capacity is >100 units a year, with a ~350-unit plant under "
        "construction."),
    competition=(
        "Intuitive Surgical dominates globally with the da Vinci platform, including the single-port SP. Medtronic "
        "(Hugo), J&J (Ottava, in development) and CMR (Versius) are the other global challengers. In China, MicroPort "
        "MedBot (Toumai) is the main domestic rival, alongside Kangduo and Shurui. Edge competes on price, single-port "
        "and telesurgery capability, and speed of overseas registration. Hospital purchase quotas and pricing reforms "
        "shape demand in China."),
    tam=(
        "Intuitive's ~US$10bn of annual revenue is the best proxy for today's global market, and robotic penetration of "
        "laparoscopic surgery outside the US remains low. China is still early, with large-equipment purchase quotas "
        "limiting placements. Emerging markets in Asia, the Middle East and Latin America are under-penetrated and "
        "price-sensitive, which suits Edge's offer. DBS projects a 49% revenue CAGR to 2030 (source pack)."),
    financials=(
        "Revenue grew from RMB48m (FY23) to RMB160m (FY24) and RMB456m (FY25), with a 66% gross margin and the net loss "
        "narrowing from RMB219m to RMB89m. H1'26 revenue rose 114% to RMB319m at a 64.1% gross margin, and the net loss "
        "narrowed to RMB19m as R&D fell 44% with programmes maturing. Cash was RMB1.26bn at end-June after the IPO. We "
        "forecast revenue of RMB{rev26}m/{rev27}m/{rev28}m, with profits from FY26E."),
    valuation=(
        "Our TP of HK${tp} applies 11x EV/sales to FY27E revenue of RMB{rev27}m and adds net cash. That is a discount to "
        "Intuitive (~13x) for scale and recurring-revenue mix, and far below MicroPort MedBot (~30x trailing sales). The "
        "consensus target is ~HK$61 (5 analysts). Bear case HK${bear}: 7x on lower FY27E revenue (RMB850m). Bull case "
        "HK${bull}: 14x on RMB1.3bn."),
    risks=[
        "Small cap (~US$1.6bn), thin liquidity and post-IPO volatility.",
        "Competition from Intuitive and MicroPort; pricing pressure.",
        "Overseas regulatory, reimbursement and distributor execution risk.",
        "Slow build-up of recurring revenue.",
    ],
    catalysts=[
        "Progress on the A-share listing.",
        "New country approvals, including US/EU registrations.",
        "FY26 results confirming a first full-year profit.",
    ],
    sources="Company H1'26 HKEX interim results and prospectus-era disclosures; Cleary Gottlieb; MassDevice; Simply "
            "Wall St; Bitget (DBS); StockAnalysis; IBKR; source pack.",
)

ZAI = dict(
    key="zai", name="Knowledge Atlas (Zhipu AI / Z.AI)", cn="智谱", ticker="2513.HK",
    listing="Hong Kong (IPO 8 Jan 2026 at HK$116.20); Shanghai A-share listing planned",
    sector="AI Foundation Models", theme="AI large-model developers",
    ccy="HK$", price=619.00, hi52=2980.0, lo52=116.10, ytd=None, since_ipo=433.0,
    fin_unit="RMB m", fx=HKD_PER_RMB, shares=466.0,
    mcap_local=288.2, mcap_ccy="HK$", net_cash=40000.0, ev=205900.0,
    profile="loss", loss_label="Adj. net profit (loss)",
    hist=dict(rev=[124.5, 312.4, 724.3], gm=[None, None, None], np=[None, None, -3180.0]),
    est=dict(rev=[5000.0, 14000.0, 26000.0], gm=[28.0, 32.0, 38.0], np=[-5500.0, -4500.0, -1500.0]),
    tp_method=dict(type="evs", mult=10, yr=2, disc_years=2, rate=0.15),
    scen=dict(
        bear=dict(type="evs", rev=14000.0, mult=7, disc_years=2, rate=0.15, desc="7x on FY28E revenue of RMB14bn"),
        bull=dict(type="evs", rev=40000.0, mult=12, disc_years=2, rate=0.15, desc="12x on FY28E revenue of RMB40bn"),
    ),
    cons=dict(tp=1564.83, n=None, eps26=None, eps27=None,
              ratings="Goldman HK$1,560; Morgan Stanley HK$1,700"),
    mix_title="H1'26 revenue mix (%)",
    mix=[("Cloud / API (MaaS, coding plans)", 86.5), ("On-premise deployment", 13.5)],
    tiles=[("US$3.0bn", "Management's end-2026 ARR target"),
           ("~US$9.5bn", "Equity and convertible raised since the January 2026 IPO"),
           ("−80%", "Unit inference cost after moving to domestic chips")],
    peers=[("MiniMax", "0100 HK", None, None, 49.0),
           ("SenseTime", "0020 HK", None, None, 6.6),
           ("iFlytek", "002230 CH", 90.9, None, 3.4)],
    peer_note="EV/sales on trailing revenue; SenseTime approximated by P/S.",
    self_peer=(None, None, 117.0),
    headline="Real traction and a large war chest, but the share price already assumes a great deal",
    summary=("Z.AI (Zhipu) develops the GLM family of large language models and sells them mainly through cloud APIs and "
             "coding subscriptions, plus on-premise deployments for enterprises and government. H1'26 revenue rose 400% "
             "to RMB954m but missed expectations, and losses remain large. After raising ~US$9.5bn since its January "
             "IPO, it trades at ~{evs27}x FY27E EV/sales. We initiate at <b>{rating}</b>, TP HK${tp} ({up} vs "
             "current)."),
    thesis=[
        "Z.AI has commercial traction. Cloud/API is 86.5% of revenue, GLM-5.3 ships on AWS, Alibaba Cloud and Huawei "
        "Cloud under revenue-share deals, and management targets US$3.0bn of ARR by end-2026.",
        "The company is well funded. The ~US$9.5bn raised in nine months (IPO, July placement, September placement plus "
        "a RMB20bn convertible) pays for GLM-6.0 and compute, and domestic chips cut unit inference cost by 80%.",
        "The valuation already assumes success. H1 revenue missed (RMB954m vs RMB1.35bn expected), gross margin fell "
        "to 26% and each raise dilutes holders, so we see the risk/reward as balanced.",
    ],
    background=(
        "Zhipu was spun out of Tsinghua University's Knowledge Engineering Group in 2019 by professors Tang Jie and Li "
        "Juanzi; Zhang Peng is CEO. Its ChatGLM/GLM models were among China's earliest open-weight LLMs, and the US added "
        "the company to its Entity List in January 2025. On 8 January 2026 it became Hong Kong's first listed LLM "
        "developer (IPO price HK$116.20). It operates internationally as Z.AI and plans a Shanghai A-share listing."),
    model=(
        "Z.AI monetises GLM models in two ways. Cloud/API (86.5% of H1'26 revenue) covers per-token model-as-a-service "
        "pricing, GLM coding subscription plans popular with developers, and revenue-share distribution through "
        "hyperscalers. On-premise deployments for state-owned enterprises, government and regulated industries often "
        "run on Huawei Ascend hardware; contracts are larger but revenue is lumpier. Gross margin fell from ~50% to 26% "
        "as mix shifted to cloud. Compute is the main cost, which makes inference efficiency and chip access strategic."),
    competition=(
        "In China, Z.AI competes with DeepSeek (an open-weight price-setter), Alibaba's Qwen, ByteDance's Doubao/Seed, "
        "Moonshot's Kimi, MiniMax, StepFun, Baidu ERNIE and Tencent Hunyuan; globally, with OpenAI, Anthropic and Google. "
        "The domestic API market has been in a price war, and DeepSeek's August price increase is an encouraging sign of "
        "rationalisation. Z.AI's differentiation is coding capability, enterprise and government trust, and the most "
        "commercial traction among independent Chinese labs."),
    tam=(
        "Enterprise and developer spending on LLMs in China is at an early stage. Leading US labs report annualised "
        "revenues in the tens of billions of US dollars, which shows the potential scale of the global market. Z.AI's "
        "US$3bn ARR target (~RMB20bn) for end-2026 would make it one of the larger Chinese model providers, and "
        "distribution through AWS and Alibaba Cloud extends its reach beyond China."),
    financials=(
        "Revenue grew from RMB312m (FY24) to RMB724m (FY25, +132%) and RMB954m in H1'26 (+400% YoY). The FY25 net loss was "
        "RMB4.7bn (adjusted RMB3.2bn) on R&D of RMB3.2bn, and the H1'26 adjusted loss widened to RMB1.96bn. We estimate "
        "~RMB45bn of net cash after the September raise, net of the RMB20.1bn zero-coupon convertible (conversion price "
        "HK$892.50). We forecast revenue of RMB{rev26}m/{rev27}m/{rev28}m, well below the Goldman forecasts in the source "
        "pack (RMB8.2bn/26.7bn for FY26/27), with breakeven in 2028-29."),
    valuation=(
        "We value Z.AI at 10x EV/sales on FY28E revenue of RMB{rev28}m, discounted back two years at 15%, plus net cash, "
        "for a TP of HK${tp}. Broker targets (Goldman HK$1,560, Morgan Stanley HK$1,700) assume much faster revenue "
        "growth. Bear case HK${bear}: RMB14bn of FY28E revenue at 7x. Bull case HK${bull}: RMB40bn at 12x, i.e. the ARR "
        "target is met and keeps growing."),
    risks=[
        "Price war and rising compute costs.",
        "Further dilution (equity and convertible).",
        "US export controls and Entity-List constraints on chips.",
        "Execution on GLM-6.0 and the ARR target (upside if it is met).",
    ],
    catalysts=[
        "GLM-6.0 release.",
        "ARR disclosures and quarterly revenue run-rate.",
        "Shanghai A-share listing.",
    ],
    sources="Company FY25 results (via Reuters/SCMP) and H1'26 interim report; Magica; Futu; Tiger; The Standard; "
            "DealStreetAsia; Venture Atlas; StockAnalysis; IBKR; source pack.",
)

MINIMAX = dict(
    key="minimax", name="MiniMax Group", cn="稀宇科技", ticker="0100.HK",
    listing="Hong Kong (IPO 9 Jan 2026 at HK$165)",
    sector="AI Foundation Models", theme="AI large-model developers",
    ccy="HK$", price=214.00, hi52=1330.0, lo52=186.20, ytd=None, since_ipo=29.7,
    fin_unit="US$ m", fx=HKD_PER_USD, shares=349.2,
    mcap_local=74.7, mcap_ccy="HK$", net_cash=1000.0, ev=8520.0,
    profile="loss", loss_label="Adj. net profit (loss)",
    hist=dict(rev=[3.5, 30.5, 79.0], gm=[None, 12.2, 25.4], np=[None, -244.2, -250.9]),
    est=dict(rev=[270.0, 600.0, 1050.0], gm=[20.0, 30.0, 38.0], np=[-560.0, -480.0, -280.0]),
    tp_method=dict(type="evs", mult=10, yr=2, disc_years=2, rate=0.15),
    scen=dict(
        bear=dict(type="evs", rev=600.0, mult=7, disc_years=2, rate=0.15, desc="7x on FY28E revenue of US$0.6bn"),
        bull=dict(type="evs", rev=1700.0, mult=13, disc_years=2, rate=0.15, desc="13x on FY28E revenue of US$1.7bn"),
    ),
    cons=dict(tp=588.71, n=23, eps26=None, eps27=None, ratings="Consensus Buy; CMBI HK$570, JPMorgan HK$260"),
    mix_title="H1'26 revenue mix (%)",
    mix=[("Open Platform & enterprise", 63.4), ("AI-native apps (Talkie/Xingye, Hailuo, Voice)", 36.6)],
    tiles=[("236m", "Users across 200+ countries and regions (FY25)"),
           ("60.8%", "Share of H1'26 revenue from outside mainland China"),
           ("54.4%", "Free float after the July lock-up expiry (from 5.4%)")],
    peers=[("Z.AI (Zhipu)", "2513 HK", None, None, 117.0),
           ("SenseTime", "0020 HK", None, None, 6.6),
           ("iFlytek", "002230 CH", 90.9, None, 3.4)],
    peer_note="EV/sales on trailing revenue; SenseTime approximated by P/S.",
    self_peer=(None, None, 49.0),
    headline="Global consumer reach and a fast-growing API business, but losses are three times revenue",
    summary=("MiniMax builds text, video and voice foundation models and sells them through an API platform and consumer "
             "apps (Talkie, Hailuo, MiniMax Voice); ~61% of revenue comes from outside mainland China. H1'26 revenue "
             "rose 283% to US$117m, yet the adjusted loss was US$293m. After a 77% fall from June, the stock trades at "
             "~{evs27}x FY27E EV/sales. We initiate at <b>{rating}</b>, TP HK${tp} ({up} vs current)."),
    thesis=[
        "The mix is shifting to enterprise: Open Platform and enterprise revenue grew 703% in H1'26 to 63% of sales.",
        "MiniMax has global distribution that most Chinese labs lack, with 236m users across 200+ countries and strong "
        "positions in AI video (Hailuo) and voice.",
        "Cash burn and the share overhang will dominate the near term. H1 R&D (US$297m) was 2.5x revenue, and the July "
        "lock-up expiry lifted free float from 5.4% to 54.4%. After M3's lukewarm reception, the next model (M3 Pro) is a "
        "binary swing factor.",
    ],
    background=(
        "MiniMax was founded in Shanghai in early 2022 by Yan Junjie, formerly a vice-president at SenseTime; its backers "
        "include Alibaba and Tencent. It listed in Hong Kong on 9 January 2026 at HK$165 (top of the range), raising "
        "~HK$4.8bn. The shares more than doubled on debut and peaked above HK$1,300, then fell 77% from 1 June. Products "
        "include the MiniMax-M text models, Hailuo AI video generation, MiniMax Voice/Audio, and the Talkie (overseas) and "
        "Xingye (China) companion apps."),
    model=(
        "Revenue comes from two streams. The Open Platform and enterprise services (63% of H1'26 revenue) charge "
        "per-token, per-video and per-character API fees plus subscriptions and licences for developers and "
        "enterprises. AI-native consumer apps (37%) charge subscriptions and in-app credits in Talkie/Xingye, Hailuo and "
        "Voice. Consumer apps bring scale and data but carry high user-acquisition and inference costs, while the "
        "enterprise API scales at lower marginal cost. Compute and R&D dominate the cost base."),
    competition=(
        "MiniMax competes at home with Kimi, DeepSeek, Z.AI, ByteDance (Doubao, Seedance) and Kuaishou (Kling); abroad, "
        "with OpenAI, Google (Veo), Character.AI and ElevenLabs in consumer and media AI. JPMorgan (Neutral, HK$260) "
        "flags this competition as the key risk. MiniMax's edges are multimodal breadth, international consumer "
        "distribution and cost-efficient model architectures."),
    tam=(
        "MiniMax addresses both the global API market for foundation models and consumer AI subscriptions (companions, "
        "video generation, voice), and both are growing rapidly from a small base. Consumer AI video and voice are among "
        "the fastest-monetising categories, while enterprise API spending in China is still early. FY25 revenue of US$79m "
        "is a tiny share of either pool."),
    financials=(
        "Revenue rose from US$30.5m (FY24) to US$79.0m (FY25, +159%), with gross margin improving from 12.2% to 25.4% and "
        "an adjusted net loss of ~US$251m. In H1'26, revenue rose 283% to US$116.6m, gross margin dipped to 17.9% and the "
        "adjusted net loss widened to US$293m. Cash was US$1.05bn at end-2025, plus US$0.62bn of IPO proceeds; we "
        "estimate ~US$1.4bn of net cash today. We forecast revenue of US${rev26}m/{rev27}m/{rev28}m, close to CMBI for "
        "FY26 (US$285m) but below it for FY27 (US$743m)."),
    valuation=(
        "We use the same method as for Z.AI: 10x EV/sales on FY28E revenue of US${rev28}m, discounted back two years at "
        "15%, plus net cash. That gives a TP of HK${tp}, below both JPMorgan (HK$260) and CMBI (HK$570). Bear case "
        "HK${bear}: US$0.6bn of FY28E revenue at 7x. Bull case HK${bull}: US$1.7bn at 13x."),
    risks=[
        "Model competitiveness (M3 Pro) and price war.",
        "Cash burn and potential dilution.",
        "Content regulation for companion apps; data rules abroad.",
        "Share overhang after the lock-up expiry (upside if enterprise API scales faster).",
    ],
    catalysts=[
        "M3 Pro and next-generation video/voice model launches.",
        "FY26 results and enterprise customer wins.",
        "API pricing moves by DeepSeek and peers.",
    ],
    sources="Company FY25 results release and H1'26 interim report; CMBI; JPMorgan (via Futu); Tiger; DealStreetAsia; "
            "Jiemian; StockAnalysis; IBKR; source pack.",
)

COMPANIES = [GIGADEVICE, JUSHI, JLMAG, HANS, HORIZON, LEADERDRIVE, EDGE, ZAI, MINIMAX]
