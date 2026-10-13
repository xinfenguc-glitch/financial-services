"""v2 long-form content: Horizon Robotics, Leaderdrive, Edge Medical, Z.AI, MiniMax."""

V2 = {}

V2["horizon"] = dict(
    background=[
        "Horizon Robotics was founded in Beijing in July 2015 by Yu Kai, a machine-learning researcher who had built and "
        "led Baidu's Institute of Deep Learning, with co-founder and CTO Huang Chang. Its thesis was that autonomous "
        "driving would need purpose-built AI processors designed together with the algorithms they run. China, with "
        "no domestic automotive AI-chip supplier at the time, was the natural first market. Its first automotive-grade "
        "processor, Journey 2, entered mass production in 2019–20, and successive generations (Journey 3, 5 and the "
        "2024 Journey 6 family) moved it from entry-level driver assistance to highway and urban navigate-on-autopilot "
        "(NOA).",
        "Horizon raised capital from automakers, Tier-1s and global investors. In 2022 it formed CARIZON, a software "
        "joint venture with Volkswagen's CARIAD, one of the largest foreign investments in China's auto-tech sector. "
        "It listed in Hong Kong in October 2024 at HK$3.99 under a weighted-voting-rights structure that keeps control "
        "with the founder, and raised about RMB10bn more through placements in 2025. Horizon shipped more than 4 "
        "million Journey chip sets in 2025 (+39%), launched its full-stack urban driving system HSD in November 2025, "
        "and has nearly 500 model design wins. In March 2026 it deconsolidated its robotics affiliate, D-Robotics, which "
        "licenses its technology to more than 400 robot makers. The shares are back at the IPO price.",
    ],
    milestones=[
        ("2015", "Founded in Beijing by Yu Kai (ex-Baidu IDL) and Huang Chang."),
        ("2019–20", "Journey 2, its first automotive-grade AI chip, enters mass production."),
        ("2022", "Journey 5 in production; CARIZON software JV with Volkswagen's CARIAD."),
        ("2024", "Journey 6 family launched; Hong Kong IPO at HK$3.99 (October)."),
        ("2025", ">4m Journey sets shipped (+39%); HSD urban NOA in production (Nov); ~RMB10bn placements."),
        ("2026", "D-Robotics deconsolidated; Journey 6B wins Toyota, Denso, AUMOVIO; Journey 7 for 2027."),
    ],
    ownership=[
        ("Control", "Founder-CEO Yu Kai, via weighted voting rights"),
        ("Strategic shareholders", "Chinese automakers and Tier-1s; Volkswagen (via CARIAD JV)"),
        ("Listing", "Hong Kong only (9660.HK)"),
    ],
    business=[
        "Horizon calls its model 'ARM + Android' for intelligent driving. It sells three layers that customers can "
        "combine as they wish. Journey system-on-chips are designed in-house and manufactured by foundries; they are "
        "sold with reference solutions for ADAS and highway/urban NOA. HSD (Horizon SuperDrive) is a complete urban "
        "driving system, software included, for automakers without large in-house teams. Licensing covers processor "
        "IP, algorithms, the toolchain and foundation models, for OEMs and Tier-1s that build their own stacks.",
        "The economics differ sharply by layer. Products and solutions (45% of H1'26 revenue, RMB926m, +15%) carry "
        "hardware-like gross margins of roughly 35–40%. Licensing and services (55%, RMB1.13bn, +53%) earned a 90% gross "
        "margin in H1'26. Licence income scales with partners' vehicle volumes and new programmes, while unit shipments "
        "(2.22m Journey SoCs in H1'26, +12%) drive product revenue. Group gross margin was 66% in H1'26.",
        "Customers are almost every major Chinese automaker plus a growing list of international brands and Tier-1s. "
        "Toyota programmes, Denso and AUMOVIO are developing on Journey 6B. Design wins for nearly 500 models (about 130 "
        "with advanced NOA) provide a multi-year revenue pipeline. The cost base is dominated by R&amp;D (RMB5.2bn in "
        "FY25, more than 1.3x revenue), which funds new chip generations, HSD and foundation models. Management "
        "targets breakeven in 2028. Working capital is significant (receivables ~180 days and inventory ~290 days at "
        "FY25) because chips are built ahead of OEM ramps.",
    ],
    segments_title="Revenue mix and economics (H1'26)",
    segments=[
        ("Licensing & services", "55% (RMB1.13bn, +53%)", "Processor IP, algorithms, toolchain, foundation-model licences",
         "90.4% gross margin; scales with partner volumes"),
        ("Products & solutions", "45% (RMB0.93bn, +15%)", "Journey SoCs with ADAS/NOA reference solutions; HSD",
         "~36% gross margin; 2.22m units (+12%)"),
    ],
    competition=[
        "At the high end, Nvidia's Orin and Thor platforms power many premium Chinese EVs, often running software from "
        "Momenta or the automakers' own teams. Huawei sells a vertically integrated stack (chips, software, sensors) "
        "through its Qiankun brand and HIMA alliance. In mainstream ADAS, Mobileye and Qualcomm (Snapdragon Ride) "
        "compete globally, and Black Sesame is a smaller Chinese rival. Several leading EV makers (NIO, Xpeng, BYD and "
        "Li Auto) are developing in-house driving chips to control costs and differentiation.",
        "Horizon's advantages are cost-optimised silicon designed for China's mass market, a large installed base and "
        "toolchain that lowers development costs for OEMs, and an open licensing model that lets automakers keep "
        "ownership of their software. Its strongest position is in cars priced below ~RMB200k, where Nvidia is too "
        "expensive and in-house chips are uneconomic. The main threats are price competition in a shrinking domestic car "
        "market, large OEMs going in-house, and Nvidia or Qualcomm pushing cheaper platforms.",
    ],
    competitors=[
        ("Nvidia (Orin/Thor)", "US", "High-end ADAS/AD compute", "Performance leader; costly; export-control exposure"),
        ("Huawei (Qiankun)", "China (private)", "Full-stack ADS; HIMA brands", "Integrated rival; competes for OEM control"),
        ("Mobileye / Qualcomm", "Israel/US / US", "Mainstream ADAS SoCs", "Global incumbents; weaker in China NOA"),
        ("OEM in-house (NIO, Xpeng, BYD, Li Auto)", "China", "Self-developed driving chips", "Captive; limits Horizon's share at top OEMs"),
        ("Black Sesame / Momenta", "China", "ADAS chips / driving software", "Smaller chip rival; software partner/competitor"),
    ],
    moat=[
        "China's largest automotive AI-chip installed base, with nearly 500 model design wins.",
        "Licensing model (90% gross margin) that monetises IP across OEMs and Tier-1s.",
        "Cost-optimised hardware and toolchain tailored to China's mass-market price points.",
        "Vulnerabilities: OEM in-house chips, auto price war, cash burn, foundry and export-control risk.",
    ],
    tam=[
        "China sells more than 20m passenger cars a year, and driver assistance is moving rapidly down the price ladder. "
        "Highway NOA is now standard on many mid-priced EVs, and HSD targets urban NOA in cars around RMB70–150k. "
        "Frost & Sullivan, cited in Horizon's prospectus, projected China's ADAS/AD solutions market to grow from "
        "~RMB60bn in 2023 to more than RMB1tn by 2030 as content per vehicle rises from a few hundred to several "
        "thousand RMB.",
        "Horizon's revenue (RMB4.3bn TTM) is a single-digit share of today's market, so share gains plus rising content "
        "per car drive growth. International OEMs (Toyota, Volkswagen through CARIZON) and robotics (through D-Robotics "
        "licences) extend the addressable market beyond China.",
    ],
    tam_table=[
        ("China passenger cars", ">20m units a year", "Retail −20% in H1'26; NOA penetration rising", "Industry data"),
        ("China ADAS/AD solutions", "~RMB60bn (2023) → >RMB1tn (2030E)", "~50% CAGR", "Frost & Sullivan via prospectus"),
        ("Horizon shipments", "2.22m Journey SoCs (H1'26)", "~5m in 2026, >7m in 2027 (guidance)", "Company"),
        ("Robotics licensing", "400+ customers (D-Robotics)", "Early stage", "Company"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue grew from RMB1.55bn (FY23) to RMB2.38bn (FY24) and RMB3.76bn (FY25, +58%), and "
        "RMB2.06bn in H1'26 (+33%). Gross margin fell from 77% (FY24) to 64.5% (FY25) as hardware grew faster, then held "
        "at 66% in H1'26 as licensing recovered. R&amp;D rose 63% to RMB5.2bn in FY25, so the adjusted operating loss "
        "widened from RMB1.5bn to RMB2.4bn and the adjusted net loss from RMB1.7bn to RMB2.8bn. Reported results swing "
        "with fair-value items: −RMB10.5bn in FY25, +RMB3.8bn in H1'26. We forecast revenue of "
        "RMB{rev26}bn/{rev27}bn/{rev28}bn and adjusted net losses of RMB{np26}bn/{np27}bn/{np28}bn."),
    fin_bs=(
        "<b>Balance sheet.</b> Cash and short-term deposits fell from RMB20.8bn (FY25) to RMB15.0bn (June 2026). Reported "
        "'debt' (RMB8.5bn) mostly consists of preferred shares and other financial liabilities at fair value, not bank "
        "borrowings (RMB1.4bn). On StockAnalysis's basis, net cash was RMB{nc25}bn at FY25 and RMB{ncj26}bn at June 2026, "
        "plus RMB4.1bn of fair-value investments. We use ~RMB10bn in our valuation. Receivables rose to RMB2.5bn ({recvd25} "
        "days at FY25) and inventory to RMB1.3bn. Equity attributable is RMB16.4bn, and the current ratio was {cr25} at "
        "FY25."),
    fin_cf=(
        "<b>Cash flow.</b> Horizon burns cash: OCF was −RMB1.7bn (FY23), roughly zero (FY24, helped by licence "
        "prepayments) and −RMB2.1bn (FY25), and −RMB2.8bn TTM. With capex of RMB0.3–0.5bn, FCF was −RMB{fcf25}bn in FY25 "
        "and −RMB{fcfttm}bn TTM, funded by RMB5.4bn of IPO proceeds (FY24) and RMB10.1bn of placements (FY25). We forecast "
        "FCF of −RMB{fcf26}bn/−RMB{fcf27}bn/−RMB{fcf28}bn. On StockAnalysis's net cash basis that leaves ~RMB{nc28}bn by "
        "FY28E before monetising investments, so another capital raise before breakeven is likely."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE and ROA are negative (FY25 ROA {roa25}), and R&amp;D runs at ~137% of revenue. The ratios "
        "to watch are licensing share of revenue (55%), gross margin (~64–66%), receivable days ({recvd25}) and cash "
        "burn relative to cash. Our forecasts imply the adjusted loss narrows from ~59% of revenue in FY26E to ~2% in "
        "FY28E."),
)

V2["leaderdrive"] = dict(
    background=[
        "Leader Harmonious Drive Systems (Leaderdrive) was founded in Suzhou in 2011 by Zuo Yuyu, who had spent years "
        "developing strain-wave (harmonic) gearing at a time when Chinese robot makers relied almost entirely on "
        "imports from Japan's Harmonic Drive Systems. Harmonic reducers are compact, zero-backlash gears that sit in "
        "the smaller joints of industrial robots, collaborative robots and, increasingly, humanoid robots. They require "
        "extremely precise machining of thin-walled flexible components. Leaderdrive mastered the tooth profile, "
        "materials and heat treatment, and built many of its own machine tools to control quality and cost.",
        "As China became the world's largest industrial-robot market, Leaderdrive displaced imports with products priced "
        "materially below Japanese equivalents. It listed on Shanghai's STAR Market in August 2020. Profits peaked at "
        "RMB189m in FY21, fell to RMB56m in FY24 as robot demand slowed and prices were cut, and recovered in FY25 "
        "on humanoid-robot development and industrial share gains. A ~RMB1.4bn placement in 2024 funded new capacity. In "
        "2026 the company announced plans for a Hong Kong H-share listing and a robotics joint venture with SKF. With "
        "humanoid makers such as Agibot and UBTech among its customers, the stock has become one of China's purest "
        "listed plays on humanoid robots.",
    ],
    milestones=[
        ("2011", "Founded in Suzhou by Zuo Yuyu after years of in-house harmonic-drive development."),
        ("2020", "IPO on Shanghai's STAR Market (688017.SH)."),
        ("2021", "Record net profit of RMB189m in the industrial-robot boom."),
        ("2023–24", "Profit falls to RMB84m, then RMB56m, on weaker demand and price cuts; ~RMB1.4bn placement."),
        ("2025", "Revenue +47% to RMB571m on industrial and humanoid demand."),
        ("2026", "Plans HK H-share listing and SKF robotics JV; H1 revenue +39%; Q2 results miss."),
    ],
    ownership=[
        ("Control", "Founder-chairman Zuo Yuyu and family"),
        ("Share classes", "A-share 688017.SH (STAR); H-share listing planned"),
        ("Key customers", "Industrial/collaborative robot makers; humanoid developers (e.g. Agibot, UBTech)"),
    ],
    business=[
        "Leaderdrive manufactures harmonic reducers (flexspline, circular spline and wave generator) in standard and "
        "custom sizes, plus precision metal parts. Together these were 82.7% of H1'26 revenue. Electromechanical "
        "actuators (15.7%) integrate reducer, frameless motor, encoder, brake and drive into a complete joint module, "
        "which raises content per joint and suits humanoid and collaborative-robot designers who want to buy "
        "modules rather than components.",
        "Its edge is manufacturing. The company designs tooth profiles and processes in-house, builds much of its own "
        "precision grinding and machining equipment, and controls heat treatment. That lets it sell at materially "
        "lower prices than Harmonic Drive Systems while keeping gross margins around 30%. Margins have fallen from ~50% "
        "in FY21 as it cut prices to win share and absorbed new capacity.",
        "Customers include Chinese industrial and collaborative robot makers, CNC machine-tool builders, semiconductor "
        "and medical equipment makers, and humanoid-robot developers. Humanoids are still a small share of revenue but "
        "dominate the investment case: a humanoid can use ~14–20 harmonic reducers. Revenue is small (RMB571m in FY25), "
        "so profit is sensitive to utilisation of new capacity and to interest income on its ~RMB2bn of cash, which "
        "makes up a meaningful share of pre-tax profit.",
    ],
    segments_title="Revenue mix and economics (H1'26)",
    segments=[
        ("Harmonic reducers & metal parts", "82.7%", "Strain-wave reducers for robot joints, machine tools, equipment",
         "~30% gross margin; price below Japanese rivals"),
        ("Electromechanical actuators", "15.7%", "Integrated joint modules (reducer + motor + encoder + drive)",
         "Higher content per joint; humanoid focus"),
        ("Other", "1.6%", "Hydraulic and other precision parts", "Small"),
    ],
    competition=[
        "The global benchmark is Harmonic Drive Systems (Japan), which invented commercial strain-wave gearing and still "
        "leads in premium industrial and aerospace applications. Nidec-Shimpo is another Japanese supplier. In China, "
        "Leaderdrive is the largest of a growing field that includes Laifual, Zhongda Leader, KOFON, Beijing CTKM and "
        "Han's Motion (part of Han's Laser). JPMorgan estimates Leaderdrive's share of China's harmonic-reducer market "
        "at 30–40%.",
        "Two competitive risks loom over the humanoid opportunity. Designers may favour other transmissions for some "
        "joints, such as planetary gears, RV reducers (Nabtesco, Shuanghuan) or planetary roller screws. And large robot "
        "makers, including Tesla, may produce reducers in-house or squeeze suppliers on price as volumes grow. "
        "Leaderdrive's lead rests on precision, yield and scale, but harmonic reducers are increasingly a contested "
        "component.",
    ],
    competitors=[
        ("Harmonic Drive Systems", "Japan", "Harmonic reducers and actuators", "Global leader; ~80x forward P/E"),
        ("Nabtesco", "Japan", "RV reducers (large joints)", "Complementary/alternative; ~22x forward P/E"),
        ("Zhejiang Shuanghuan", "China", "RV reducers, gears", "Domestic RV leader; ~20x forward P/E"),
        ("Laifual / Zhongda Leader / KOFON", "China", "Harmonic reducers", "Price challengers"),
        ("Han's Motion (Han's Laser)", "China", "Harmonic reducers, motion control", "Group-backed entrant"),
    ],
    moat=[
        "Largest Chinese harmonic-reducer maker (30–40% domestic share) with in-house machine tools and process know-how.",
        "Early design-ins with humanoid developers; integrated actuator modules.",
        "Net cash of ~RMB2bn funds capacity without leverage.",
        "Vulnerabilities: alternative transmissions, customer in-sourcing, price competition, small earnings base.",
    ],
    tam=[
        "China installs about 300k industrial robots a year (IFR), the world's largest market. Each uses several harmonic "
        "reducers in its wrist and smaller joints, alongside RV reducers in larger joints. Collaborative robots, "
        "semiconductor equipment and medical devices add further demand. This core market is growing at mid-single to "
        "low-double digits.",
        "Humanoids could be transformational. At ~14–20 harmonic reducers per robot, annual production of one million "
        "humanoids would require 14–20 million reducers, many times today's market. Humanoid output is currently only in "
        "the tens of thousands, however, and timing, design choices and price points are uncertain. The valuation "
        "depends on that future market, not on today's addressable market.",
    ],
    tam_table=[
        ("China industrial robots", "~300k units a year", "Mid-single to low-double-digit growth", "IFR"),
        ("Harmonic reducers per humanoid", "~14–20", "Design-dependent", "Industry estimates"),
        ("Humanoid production", "Tens of thousands today", "Scenario: 1m a year → 14–20m reducers", "Our scenario"),
        ("Leaderdrive China share", "30–40%", "Contested by new entrants", "JPMorgan estimate"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue fell from RMB446m (FY22) to RMB356m (FY23), then rose to RMB387m (FY24), "
        "RMB571m (FY25, +47%) and RMB668m TTM. Gross margin compressed from 49.5% (FY21) to 28.7% (FY24) before "
        "recovering to 31.7% (FY25). Operating profit was only RMB90m in FY25; net profit of RMB124m was helped by "
        "interest income and subsidies. H1'26 revenue rose 39% and net profit 31% to RMB70m, with Q2 margins down. We "
        "forecast revenue of RMB{rev26}m/{rev27}m/{rev28}m and net profit of RMB{np26}m/{np27}m/{np28}m."),
    fin_bs=(
        "<b>Balance sheet.</b> The balance sheet is conservative: RMB2.17bn of cash and short-term investments (June 2026) "
        "against negligible debt, so net cash is RMB{ncj26}m (RMB{nc25}m at FY25), ~{ndeq25} of equity. PP&amp;E is rising "
        "(RMB611m at FY25, RMB752m by June 2026) as capacity is built. Receivables ({recvd25} days) and inventory "
        "({invd25} days) are long for a component maker. Equity attributable is RMB3.6bn (BVPS ~RMB20), and the stock "
        "trades at ~13x book. The current ratio is {cr25}."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash flow is small and erratic (RMB149m, RMB28m and RMB152m over FY23–25), and capex "
        "has stepped up (RMB177m TTM), so FCF was RMB{fcf25}m in FY25 and −RMB{fcfttm}m TTM. The 2024 placement "
        "(~RMB1.4bn) funds the expansion. We forecast FCF of −RMB{fcf26}m, −RMB{fcf27}m and RMB{fcf28}m in FY26–28E, "
        "with net cash still ~RMB{nc28}m by FY28E."),
    fin_ratios=(
        "<b>Key ratios.</b> Returns are low: ROE was {roe23}, {roe24} and {roe25} over FY23–25, and we forecast only "
        "~{roe27} in FY27E and ~{roe28} in FY28E because of the large cash and equity base. ROA is {roa25}. A P/E of "
        "~{pe27}x FY27E on single-digit ROE is the core of our Sell call."),
)

V2["edge"] = dict(
    background=[
        "Shenzhen Edge Medical was founded in May 2017 in Longgang, Shenzhen, by Dr Wang Jianchen, who remains chairman "
        "and CEO. The company set out to build a full family of endoscopic surgical robots for laparoscopic surgery, "
        "rather than a single me-too system. In China and globally that market has been dominated by Intuitive "
        "Surgical's da Vinci. Edge developed a multi-port robot (MP1000), a single-port robot (SP1000) and a "
        "natural-orifice (bronchoscopy) robot. It became the first Chinese company, and only the second globally, to have "
        "all three types approved.",
        "Rather than wait for China's hospital purchase quotas, Edge pursued overseas registrations aggressively. By "
        "mid-2026 MP1000 was approved in 37 overseas jurisdictions, and most placements were going abroad. Edge also "
        "built a telesurgery capability, with more than 500 remote procedures by end-2025, a selling point in "
        "geographically dispersed markets. After two earlier Hong Kong IPO filings (2022, 2023), Edge listed on 8 "
        "January 2026 at HK$43.24, raising ~HK$1.1bn with cornerstones including ADIA, UBS Asset Management, OrbiMed "
        "and Tencent. It is preparing an A-share listing. By June 2026 it had installed or delivered 158 robots (55 in "
        "China, 103 overseas).",
    ],
    milestones=[
        ("2017", "Founded in Shenzhen by Dr Wang Jianchen."),
        ("2022–23", "Multi-port (MP1000) and China's first single-port (SP1000) endoscopic robots approved."),
        ("2024–25", "CE mark and overseas launches; FY25 revenue RMB456m (+185%); >500 telesurgery cases."),
        ("Jan 2026", "Hong Kong IPO at HK$43.24 (~HK$1.1bn); cornerstones ADIA, UBS AM, OrbiMed, Tencent."),
        ("H1 2026", "58 robots placed (49 overseas); revenue +114%; net loss narrows 78% to RMB19m."),
        ("2026", "~350-unit plant under construction; A-share listing in preparation."),
    ],
    ownership=[
        ("Founder", "Dr Wang Jianchen (chairman and CEO)"),
        ("Notable investors", "Tencent, OrbiMed, LYFE Capital; IPO cornerstones ADIA, UBS AM"),
        ("Listing", "H-share 2675.HK; A-share listing in preparation"),
    ],
    business=[
        "Edge designs, manufactures and sells endoscopic surgical robots, used mainly in urology, gynaecology, general and "
        "thoracic surgery. Systems made up 99.6% of H1'26 revenue, sold directly to hospitals in China and through "
        "distributors abroad (Italy, Spain and other European markets, Asia, the Middle East, Africa and Latin America). "
        "Overseas sales were 69.8% of H1'26 revenue (RMB223m), unusual for a Chinese medtech company.",
        "The long-term model is razor and blade. Each robot placed generates recurring revenue from instruments "
        "(limited-use, replaced every few procedures), consumables and service contracts, as at Intuitive, where most "
        "revenue is recurring. Edge is still early: recurring revenue is below 1% of sales, so revenue today is "
        "lumpy and driven by system placements. On our calculation, H1'26 revenue averaged ~RMB5.5m per robot placed, "
        "well below typical da Vinci list prices, which is central to Edge's pitch to price-sensitive hospitals.",
        "Gross margin is already high (~64–66%) for a company of its size, and operating costs have fallen as "
        "development programmes matured (H1'26 R&amp;D −44%), bringing the company close to breakeven. Production "
        "capacity is more than 100 units a year, and a ~350-unit plant is under construction. Working capital is "
        "meaningful because overseas distributors receive credit terms: receivables were ~196 days of sales at FY25.",
    ],
    segments_title="Revenue mix and installed base (H1'26)",
    segments=[
        ("Overseas", "69.8% (RMB223m)", "49 units placed in H1; 103 cumulative; distributors in Europe, Asia, ME, LatAm",
         "Faster approvals; price-sensitive markets"),
        ("Mainland China", "30.2% (RMB96m)", "9 units placed in H1; 55 cumulative; direct hospital sales",
         "Purchase quotas limit placements"),
        ("Instruments, consumables, service", "<1%", "Per-procedure instruments; service contracts",
         "Recurring; grows with installed base"),
    ],
    competition=[
        "Intuitive Surgical dominates the global market with da Vinci, including the da Vinci 5 and the single-port SP, "
        "backed by a vast installed base, training ecosystem and clinical evidence. Medtronic (Hugo), Johnson & Johnson "
        "(Ottava, in development) and CMR Surgical (Versius) are the main Western challengers. None has yet dented "
        "Intuitive's position in its core markets.",
        "In China, MicroPort MedBot (Toumai) is Edge's main domestic rival and is also exporting aggressively, including "
        "telesurgery. Kangduo, Shurui and other start-ups compete in niches. Edge differentiates on price, the "
        "breadth of its multi-port/single-port/bronchoscopy family, telesurgery, and speed of overseas registration. "
        "Its disadvantages are a small installed base, limited long-term clinical data and a recurring-revenue stream "
        "that is barely started. Distributor-led sales abroad also mean less control over service quality.",
    ],
    competitors=[
        ("Intuitive Surgical (da Vinci)", "US", "Multi-port and single-port robots; global", "Dominant; ~13x EV/sales"),
        ("MicroPort MedBot (Toumai)", "China", "Laparoscopic, orthopaedic robots; telesurgery", "Main domestic rival; ~30x trailing sales"),
        ("Medtronic (Hugo) / J&J (Ottava)", "US", "Multi-port robots", "Large medtech challengers"),
        ("CMR Surgical (Versius)", "UK (private)", "Modular robots", "Emerging-market focus"),
        ("Kangduo / Shurui", "China", "Laparoscopic, single-port robots", "Smaller domestic rivals"),
    ],
    moat=[
        "Full robot family (multi-port, single-port, bronchoscopy) with approvals in China and 37 overseas jurisdictions.",
        "Cost structure that allows pricing well below da Vinci while keeping ~65% gross margin.",
        "Telesurgery capability and an export-led channel that avoids China's purchase quotas.",
        "Vulnerabilities: small scale, distributor reliance, early-stage recurring revenue, Intuitive and MicroPort competition.",
    ],
    tam=[
        "Intuitive's annual revenue of roughly US$10bn and installed base of ~10,000 systems are the best gauge of "
        "today's global robotic-surgery market. Penetration of eligible laparoscopic procedures remains low outside "
        "the US, especially in emerging markets where da Vinci's price is a barrier. China is still early: "
        "large-equipment purchase quotas have limited placements, but domestic robots are now eligible and cheaper.",
        "For Edge, the most relevant addressable market is price-sensitive hospitals in Asia, Europe, the Middle East "
        "and Latin America, plus China as quotas loosen. DBS projects a 49% revenue CAGR to 2030 (source pack). Over "
        "time, instruments and service revenue per installed robot, rather than system sales, should drive the value of "
        "the market.",
    ],
    tam_table=[
        ("Global robotic surgery", "~US$10bn (Intuitive revenue proxy)", "Double-digit growth", "Intuitive disclosures"),
        ("Installed base", "~10,000 da Vinci systems", "Low penetration outside US", "Intuitive"),
        ("Edge installed base", "158 robots (Jun 2026)", "58 placed in H1'26", "Company"),
        ("Edge revenue CAGR", "~49% to 2030 (DBS)", "–", "Source pack"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue grew from RMB48m (FY23) to RMB160m (FY24) and RMB456m (FY25), and RMB319m in "
        "H1'26 (+114%), as overseas placements took off. Gross margin was ~66% in FY25 and 64.1% in H1'26. Operating "
        "costs have stabilised, so the net loss narrowed from RMB219m (FY24) to RMB89m (FY25) and RMB19m in H1'26. We "
        "forecast revenue of RMB{rev26}m/{rev27}m/{rev28}m and net profit of RMB{np26}m/{np27}m/{np28}m, with "
        "breakeven in FY26E."),
    fin_bs=(
        "<b>Balance sheet.</b> IPO proceeds doubled the balance sheet: cash and short-term investments rose from RMB923m "
        "(FY25) to RMB1.86bn (June 2026), and equity from RMB1.2bn to RMB2.3bn. Debt is negligible, so net cash is "
        "RMB{ncj26}m. Receivables have grown with overseas distributor sales (RMB245m at FY25, {recvd25} days; RMB286m "
        "by June 2026), and inventory is RMB158m. The current ratio was {cr25} at FY25. The company is lightly capitalised "
        "in fixed assets (PP&amp;E ~RMB95m) ahead of the new plant."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash outflow narrowed from RMB320m (FY23) to RMB194m (FY25) but remained −RMB214m "
        "TTM, because receivables absorb cash even as losses shrink. Capex has been minimal. FCF was −RMB{fcf25}m in FY25. "
        "We forecast FCF of −RMB{fcf26}m and −RMB{fcf27}m in FY26–27E, turning positive at RMB{fcf28}m in FY28E as "
        "profits grow and the new plant is completed. Net cash stays comfortably above RMB1.6bn (~RMB{nc28}m by FY28E)."),
    fin_ratios=(
        "<b>Key ratios.</b> Edge's ratios are those of a company crossing breakeven: gross margin ~64–66%, net margin "
        "rising from −19% (FY25) to ~12% in FY27E and ~17% in FY28E on our forecasts, and ROE turning positive from FY26E. "
        "Receivable days ({recvd25} at FY25) and recurring-revenue share are the metrics to watch."),
)

V2["zai"] = dict(
    background=[
        "Knowledge Atlas Technology, better known as Zhipu AI and internationally as Z.AI, was spun out of Tsinghua "
        "University's Knowledge Engineering Group in 2019 by professors Tang Jie and Li Juanzi; Zhang Peng is CEO. "
        "The team had built AMiner, an academic knowledge graph, and developed the GLM (General Language Model) "
        "pre-training framework. In 2022 it open-sourced GLM-130B, one of the first large bilingual models, and in 2023 "
        "released ChatGLM-6B, an open-weight model that became widely used by Chinese developers, alongside a consumer "
        "chatbot (Qingyan).",
        "Zhipu raised capital from Chinese internet groups (including Alibaba, Tencent and Meituan) and state-backed "
        "funds. In January 2025 the US added it to the Entity List, restricting access to US technology, which pushed "
        "it toward domestic chips such as Huawei Ascend. Its GLM-4.5/4.6/5 series (2025–26) became known for strong "
        "coding and agentic performance, and it rebranded internationally as Z.AI. On 8 January 2026 it became Hong "
        "Kong's first listed LLM developer (IPO at HK$116.20). It then raised money aggressively as the shares soared: "
        "~US$4.0bn in July at HK$1,588 a share, and ~US$5bn in September (a US$2bn placement at HK$714 plus a "
        "RMB20.1bn zero-coupon convertible). A Shanghai A-share listing is planned.",
    ],
    milestones=[
        ("2019", "Spun out of Tsinghua's Knowledge Engineering Group by Tang Jie and Li Juanzi."),
        ("2022–23", "Open-sources GLM-130B and ChatGLM-6B; launches Qingyan chatbot."),
        ("Jan 2025", "Added to the US Entity List; shifts toward domestic AI chips."),
        ("2025", "GLM-4.5/4.6 coding and agent models; international Z.AI brand; revenue RMB724m."),
        ("Jan 2026", "Hong Kong IPO at HK$116.20; first listed LLM developer."),
        ("Jul–Sep 2026", "~US$9bn raised via placements and a RMB20.1bn CB; GLM-5.3 on AWS, Alibaba, Huawei clouds."),
    ],
    ownership=[
        ("Founders / management", "Tang Jie, Li Juanzi (Tsinghua); CEO Zhang Peng"),
        ("Pre-IPO investors", "Chinese internet groups (incl. Alibaba, Tencent, Meituan) and state-backed funds"),
        ("Capital structure", "RMB20.1bn zero-coupon CB due Sep-2027 (conversion HK$892.50)"),
    ],
    business=[
        "Z.AI develops and sells the GLM family of foundation models (language, coding, vision, agents). It monetises them "
        "in two main ways. The cloud/API business (86.5% of H1'26 revenue, up from 26% in FY25) charges developers and "
        "enterprises per token through its own platform, sells fixed-price coding subscription plans (popular with "
        "developers globally), and earns revenue shares when GLM is offered on hyperscaler clouds (AWS, Alibaba Cloud, "
        "Huawei Cloud). The on-premise business (13.5% of H1'26 revenue but 74% in FY25) installs models on customers' "
        "own servers for state-owned enterprises, government and regulated industries. These deals are larger but "
        "lumpier, and often run on domestic hardware.",
        "The economics are those of a compute-intensive software business at an early stage. Gross margin fell from ~50% "
        "to 26.4% in H1'26 as low-margin cloud traffic grew. Every token served consumes GPU or NPU time, and price "
        "competition in China has been fierce. Moving inference to domestic chips cut unit cost by 80%, which is "
        "key to margin recovery. R&amp;D, mostly training compute and researcher pay, exceeded RMB3bn in FY25, about "
        "four times revenue.",
        "Management targets annual recurring revenue (ARR) of US$3.0bn by end-2026, roughly ten times the H1'26 revenue "
        "run-rate. Whether that is reached depends on coding-plan subscriptions and international API demand. The "
        "~US$9.5bn raised since the IPO gives Z.AI one of the largest war chests among Chinese AI labs, to fund "
        "GLM-6.0 and compute.",
    ],
    segments_title="Revenue mix and economics",
    segments_cols=("Business", "H1'26 share (FY25)", "What it is", "Economics"),
    segments=[
        ("Cloud / API (MaaS, coding plans)", "86.5% (26%)", "Per-token API, coding subscriptions, hyperscaler revenue share",
         "Fast growth; lower margin; GM fell to 26%"),
        ("On-premise deployment", "13.5% (74%)", "Private deployments for SOEs, government, regulated industries",
         "Higher margin; lumpy contracts"),
        ("Consumer (Qingyan)", "Small", "Chatbot app", "Mostly free; brand and data"),
    ],
    competition=[
        "China's foundation-model market is crowded. DeepSeek's open-weight models set a low price benchmark in 2025. "
        "Alibaba (Qwen), ByteDance (Doubao/Seed), Tencent (Hunyuan) and Baidu (ERNIE) bundle models with cloud services "
        "and can subsidise them. Independent labs such as Moonshot (Kimi), MiniMax and StepFun compete for developers "
        "and enterprises. Globally, OpenAI, Anthropic and Google lead on frontier capability. The domestic API market has "
        "been in a price war, though DeepSeek's August 2026 price increase hints at rationalisation.",
        "Z.AI's differentiation is coding and agentic capability, the trust of enterprise and government buyers "
        "(important for on-premise deals), its distribution through international hyperscalers, and now its balance "
        "sheet. Its disadvantages are the Entity-List constraint on hardware, dependence on expensive compute, and the "
        "risk that hyperscalers' own models commoditise third-party APIs.",
    ],
    competitors=[
        ("DeepSeek", "China (private)", "Open-weight LLMs; low-price API", "Price-setter; strong reasoning models"),
        ("Alibaba (Qwen) / ByteDance (Doubao)", "China", "LLMs bundled with cloud/apps", "Deep pockets; can subsidise"),
        ("Moonshot (Kimi) / StepFun", "China (private)", "LLMs; consumer and API", "Independent rivals"),
        ("MiniMax", "China (0100.HK)", "Multimodal models; consumer apps; API", "Listed peer; more consumer-oriented"),
        ("OpenAI / Anthropic / Google", "US", "Frontier models and APIs", "Global leaders; set capability frontier"),
    ],
    moat=[
        "Strong coding/agentic models and early open-source developer community (ChatGLM).",
        "Enterprise and government trust for on-premise deployments; distribution via AWS, Alibaba and Huawei clouds.",
        "~US$9.5bn raised since IPO: one of the best-funded Chinese AI labs.",
        "Vulnerabilities: price war, compute costs, Entity-List hardware constraints, dilution.",
    ],
    tam=[
        "Enterprise and developer spending on foundation models in China is at an early stage, but growing quickly as "
        "coding assistants, customer-service agents and document workflows move into production. Leading US labs report "
        "annualised revenues in the tens of billions of US dollars, which illustrates the potential scale of the "
        "global market once models become embedded in enterprise software.",
        "Z.AI's ARR target of US$3bn (~RMB20bn) for end-2026 would make it one of the largest independent model "
        "providers outside the US. Distribution through AWS and Alibaba Cloud extends its reach internationally. The "
        "addressable market is large; the uncertainty is the share and price Z.AI can capture against hyperscaler "
        "models and open-weight alternatives.",
    ],
    tam_table=[
        ("Global LLM APIs and subscriptions", "Tens of US$bn (leading US labs' annualised revenue)", "Very rapid growth",
         "Company disclosures (US labs)"),
        ("China enterprise LLM spend", "Early stage", "Rapid growth; price competition", "Qualitative"),
        ("Z.AI ARR target", "US$3.0bn (end-2026)", "~10x H1'26 run-rate", "Management (source pack)"),
        ("Z.AI H1'26 revenue", "RMB954m", "+400% YoY", "Company"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue rose from RMB124m (FY23) to RMB312m (FY24), RMB724m (FY25, +132%) and RMB954m "
        "in H1'26 (+400%), though H1 missed the ~RMB1.35bn consensus. Gross margin fell from ~50% to 26.4% as cloud "
        "volumes grew. The FY25 net loss was RMB4.7bn (adjusted RMB3.2bn) on R&amp;D of RMB3.2bn, and the H1'26 adjusted "
        "loss was RMB1.96bn. We forecast revenue of RMB{rev26}m/{rev27}m/{rev28}m and adjusted net losses of "
        "RMB{np26}m/{np27}m/{np28}m, with breakeven in 2028–29."),
    fin_bs=(
        "<b>Balance sheet.</b> Before the IPO, Z.AI's preferred shares were carried as liabilities, so reported equity "
        "was negative (−RMB8.1bn at FY25). After conversion and the IPO, equity was RMB4.4bn at June 2026, with cash and "
        "short-term investments of RMB4.6bn and debt of RMB2.6bn (net cash RMB{ncj26}m). The July and September raises "
        "added ~RMB40bn of equity plus the RMB20.1bn convertible. We estimate ~RMB{nc26}m of net cash at FY26E (cash of "
        "~RMB60bn+ less ~RMB23bn of debt). Receivables jumped to RMB875m by June 2026 with on-premise contracts."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash burn has accelerated: −RMB0.6bn (FY23), −RMB2.2bn (FY24 and FY25) and −RMB4.3bn "
        "TTM. Capex has been low but is rising for compute (RMB0.6bn TTM). We forecast FCF of −RMB{fcf26}m, "
        "−RMB{fcf27}m and −RMB{fcf28}m in FY26–28E, so net cash declines from ~RMB{nc26}m to ~RMB{nc28}m by FY28E. That "
        "is still ample runway, but it assumes losses narrow. The convertible matures in September 2027 unless it "
        "converts (HK$892.50, ~44% above the current price)."),
    fin_ratios=(
        "<b>Key ratios.</b> Conventional returns ratios are not meaningful. The metrics that matter are revenue growth "
        "(+400% in H1'26), gross margin (26% and falling), R&amp;D intensity (~4x revenue in FY25), cash runway (more than "
        "three years at our forecast burn) and dilution (share count up ~10% since the IPO, plus potential CB conversion)."),
)

V2["minimax"] = dict(
    background=[
        "MiniMax was founded in Shanghai in early 2022 by Yan Junjie, a computer-vision researcher who had been a "
        "vice-president at SenseTime. It set out to build general multimodal models (text, voice, video) and to "
        "monetise them through its own consumer products as well as an API. Its first hit was a companion-chat app, "
        "launched overseas as Talkie and in China as Xingye, which grew a large user base among young users. Hailuo AI, "
        "its video-generation product, followed in 2024, along with MiniMax Speech/Voice. Early backers included "
        "Chinese gaming company miHoYo, Tencent and Alibaba, which led a large 2024 funding round.",
        "In 2025 MiniMax shifted toward open-weight frontier models. MiniMax-01 introduced a 'lightning attention' "
        "architecture with very long context, followed by the M1 reasoning model and M2. It listed in Hong Kong on 9 "
        "January 2026 at HK$165 (top of the range), raising ~HK$4.8bn. The shares more than doubled on debut and peaked "
        "above HK$1,300. They then fell as much as 77% from 1 June after a lukewarm reception for the M3 model, and as "
        "the July lock-up expiry lifted the free float from 5.4% to 54.4%. About 61% of revenue now comes from outside "
        "mainland China.",
    ],
    milestones=[
        ("2022", "Founded in Shanghai by Yan Junjie (ex-SenseTime vice-president)."),
        ("2023", "Launches Talkie (overseas) and Xingye (China) companion apps."),
        ("2024", "Hailuo AI video generation; Alibaba-led funding round."),
        ("2025", "Open-weight MiniMax-01, M1 and M2; FY25 revenue US$79m (+159%); 236m users."),
        ("Jan 2026", "Hong Kong IPO at HK$165 (~HK$4.8bn); shares later peak above HK$1,300."),
        ("Jun–Jul 2026", "M3 reception lukewarm; shares −77% from 1 June; free float rises to 54% after lock-up."),
    ],
    ownership=[
        ("Founder", "Yan Junjie (CEO)"),
        ("Pre-IPO investors", "Including Alibaba, Tencent and miHoYo"),
        ("Free float", "54.4% after July 2026 lock-up expiry"),
    ],
    business=[
        "MiniMax runs two businesses on top of its own foundation models. The Open Platform and enterprise services "
        "(63.4% of H1'26 revenue, US$74m, +703%) sell API access to text, speech and video models, priced per token, "
        "per character of speech or per video, plus subscriptions and licences for developers and enterprises. "
        "AI-native consumer apps (36.6%, US$43m) monetise through subscriptions and in-app credits. These are Talkie and "
        "Xingye (AI companions), Hailuo AI (video generation) and MiniMax Voice/Audio.",
        "The consumer apps gave MiniMax scale (236m users across 200+ countries by FY25) and data, but they are "
        "expensive: user acquisition and inference costs are high, and companion apps face content-regulation risk. "
        "The 2026 shift toward enterprise and API revenue is strategically sensible, because marginal costs are lower "
        "and customers stickier. Gross margin was 25.4% in FY25 and 17.9% in H1'26, still low because of heavy "
        "inference costs and price competition.",
        "R&amp;D (US$297m in H1'26) is about 2.5x revenue and the dominant cost, mostly training compute. MiniMax is "
        "known for cost-efficient architectures, but it competes against far larger budgets. Capex jumped in 2026 (US$188m "
        "TTM) as it built its own compute. Cash of ~US$1.2bn at June 2026 is modest against an annual burn of ~US$0.6bn.",
    ],
    segments_title="Revenue mix and economics (H1'26)",
    segments=[
        ("Open Platform & enterprise", "63.4% (US$74m, +703%)", "APIs for text, speech, video models; enterprise licences",
         "Lower marginal cost; fastest growth"),
        ("AI-native apps", "36.6% (US$43m)", "Talkie/Xingye companions, Hailuo video, MiniMax Voice",
         "Subscriptions/credits; high acquisition and inference cost"),
        ("Geography", "60.8% outside mainland China", "US, Europe, Asia users and developers", "Global reach; regulatory exposure"),
    ],
    competition=[
        "MiniMax competes on two fronts. In models and APIs, its rivals are DeepSeek, Moonshot (Kimi), Z.AI and StepFun "
        "among independents, and Alibaba, ByteDance, Tencent and Kuaishou among large platforms in China. Globally it "
        "faces OpenAI, Google and Anthropic. JPMorgan (Neutral, HK$260) flags this competition, particularly from Kimi, "
        "DeepSeek, ByteDance and Kuaishou, as the key risk.",
        "In consumer AI, Talkie competes with Character.AI and general chatbots. Hailuo competes with Kuaishou's Kling, "
        "ByteDance's Seedance/Jimeng, Google's Veo and OpenAI's Sora in video generation, and MiniMax Voice competes with "
        "ElevenLabs in speech. MiniMax's edges are multimodal breadth, international distribution and efficient model "
        "design. Its weaknesses are scale of compute budget versus platform rivals, monetisation per user, and the "
        "binary nature of each model launch (M3's reception showed how quickly sentiment can turn).",
    ],
    competitors=[
        ("ByteDance (Doubao, Seedance) / Kuaishou (Kling)", "China", "Chatbots, video generation", "Platform scale; can subsidise"),
        ("DeepSeek / Moonshot (Kimi)", "China (private)", "LLMs and APIs", "Strong models; price pressure"),
        ("Z.AI (Zhipu)", "China (2513.HK)", "LLMs; coding; on-premise", "Listed peer; enterprise-oriented"),
        ("Character.AI / ElevenLabs", "US", "AI companions / voice", "Consumer and voice rivals abroad"),
        ("OpenAI / Google", "US", "Frontier models; Sora/Veo video", "Global leaders"),
    ],
    moat=[
        "Multimodal model breadth (text, voice, video) with efficient architectures and open-weight credibility.",
        "International consumer distribution (236m users; ~61% of revenue outside China).",
        "Fast-growing enterprise API business with lower marginal cost.",
        "Vulnerabilities: compute budget vs. platforms, burn rate, content regulation, share overhang.",
    ],
    tam=[
        "MiniMax addresses two growing pools. The first is the global market for foundation-model APIs and enterprise "
        "subscriptions, which leading US labs show can reach tens of billions of US dollars of annualised revenue. The "
        "second is consumer AI subscriptions in companions, video generation and voice, among the fastest-monetising "
        "categories in consumer software.",
        "Both markets are early and growing rapidly, so size is not the constraint: MiniMax's FY25 revenue of US$79m "
        "is a tiny fraction of either. The constraint is competitiveness. Each model generation has to stay near the "
        "frontier at a fraction of rivals' compute budgets, and consumer products have to convert users into paying "
        "subscribers.",
    ],
    tam_table=[
        ("Global LLM APIs and subscriptions", "Tens of US$bn", "Very rapid growth", "Company disclosures (US labs)"),
        ("Consumer AI (companions, video, voice)", "Multi-US$bn", "Fast-monetising categories", "Qualitative"),
        ("MiniMax revenue", "US$79m (FY25); US$117m (H1'26)", "+283% in H1'26", "Company"),
        ("MiniMax users", "236m in 200+ countries", "–", "Company (FY25)"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue rose from US$3.5m (FY23) to US$30.5m (FY24), US$79.0m (FY25, +159%) and "
        "US$116.6m in H1'26 (+283%). Gross margin improved from 12.2% (FY24) to 25.4% (FY25) but dipped to 17.9% in H1'26. "
        "The adjusted net loss was ~US$244m (FY24) and ~US$251m (FY25), and widened to US$293m in H1'26 alone. The IFRS "
        "loss (~US$1.9bn in FY25) was inflated by preferred-share revaluation. We forecast revenue of "
        "US${rev26}m/{rev27}m/{rev28}m and adjusted net losses of US${np26}m/{np27}m/{np28}m."),
    fin_bs=(
        "<b>Balance sheet.</b> Pre-IPO preferred shares were carried as debt (US$3.6bn at FY25), giving negative equity "
        "(−US$2.6bn). After conversion and the IPO, equity was US$1.35bn at June 2026, with US$1.22bn of cash and "
        "short-term investments and US$137m of debt (net cash US${ncj26}m). PP&amp;E jumped to US$79m as MiniMax began "
        "building its own compute. Working capital is small: receivables are minimal and payables include compute "
        "suppliers."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash burn rose from US$64m (FY23) to US$258m (FY24), US$280m (FY25) and US$429m TTM, "
        "and capex jumped to US$188m TTM, so FCF was −US${fcfttm}m TTM. We forecast FCF of −US${fcf26}m, −US${fcf27}m "
        "and −US${fcf28}m in FY26–28E. On these numbers net cash falls to ~US${nc26}m by FY26E and is effectively "
        "exhausted during FY28E, so MiniMax will probably need to raise capital in 2027 unless losses narrow faster "
        "than we assume."),
    fin_ratios=(
        "<b>Key ratios.</b> Returns ratios are not meaningful. The key metrics are revenue growth (+283% in H1'26), "
        "enterprise share of revenue (63%), gross margin (18–25%), R&amp;D intensity (~2.5x revenue) and cash runway "
        "(~1.5–2 years at the current burn rate)."),
)
