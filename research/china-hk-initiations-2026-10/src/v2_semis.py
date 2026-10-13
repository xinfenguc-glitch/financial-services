"""v2 long-form content: GigaDevice, China Jushi, JL Mag Rare-Earth, Han's Laser."""

V2 = {}

V2["gigadevice"] = dict(
    background=[
        "GigaDevice was founded in Beijing's Zhongguancun district in 2005 by Zhu Yiming, a Tsinghua-trained engineer "
        "who had worked in Silicon Valley. It started with serial (SPI) NOR flash, the small memory chips that store boot "
        "code in almost every electronic device. It won share from Taiwanese and US suppliers on price and service to "
        "China's electronics makers. In 2013 it launched the GD32 family, one of China's first 32-bit Arm Cortex-M "
        "microcontroller lines, which became its second pillar. GigaDevice listed on the Shanghai Stock Exchange in 2016.",
        "From 2017 Zhu also led the creation of ChangXin Memory (CXMT), the Hefei-based DRAM maker, and GigaDevice "
        "became CXMT's partner for niche DRAM. It designs and sells DDR3/DDR4 and low-power DRAM under its own brand "
        "using CXMT wafers, launched in 2021. It added fingerprint and touch sensors through the 2019 acquisition of "
        "Silead, plus analog and power-management chips. GigaDevice is now the world's No.2 NOR flash supplier with ~18% "
        "share, behind Winbond, and China's largest general-purpose MCU vendor. It completed a Hong Kong H-share listing "
        "in January 2026, just as a shortage of legacy memory, created by global majors moving capacity to HBM and DDR5, "
        "sent its profits to record highs.",
    ],
    milestones=[
        ("2005", "Founded in Beijing by Zhu Yiming; focuses on SPI NOR flash."),
        ("2013", "Launches GD32, one of China's first Arm Cortex-M MCU families."),
        ("2016", "Lists on the Shanghai Stock Exchange (603986.SH)."),
        ("2017", "Partners with the Hefei DRAM project that becomes CXMT."),
        ("2019", "Acquires sensor designer Silead."),
        ("2021", "Launches own-brand DDR4 DRAM made on CXMT wafers."),
        ("2026", "Hong Kong H-share listing (3986.HK); H1 net profit RMB6.9bn (+1,092%)."),
    ],
    ownership=[
        ("Founder", "Zhu Yiming (also founder and chairman of CXMT), largest individual shareholder"),
        ("Share classes", "A-share 603986.SH; H-share 3986.HK (near parity with A)"),
        ("Key related party", "CXMT: DRAM wafer supply partner"),
    ],
    business=[
        "GigaDevice is a fabless chip designer. It designs memory, microcontroller, sensor and analog chips, outsources "
        "wafer fabrication (NOR and MCU wafers to foundries such as SMIC and Hua Hong, DRAM wafers to CXMT) and outsources "
        "packaging and testing. Its costs are therefore mostly wafer purchases and R&amp;D, and capital intensity is low "
        "(capex ~6% of revenue). It sells through distributors and directly to consumer-electronics, industrial, "
        "automotive, PC/server and communications customers, with a large and loyal customer base in China.",
        "Memory, about 85% of revenue, is a price-taker business. NOR flash (from 512Kb to 2Gb) stores boot code and "
        "firmware for PCs, servers, AI accelerators, displays, wearables, IoT and cars. SLC NAND and niche DRAM serve "
        "set-top boxes, networking, industrial and automotive systems that cannot use leading-edge memory. When prices "
        "rise, as they did in 2026 when Samsung, SK Hynix and Micron exited legacy products, revenue and margins explode. "
        "Memory gross margin jumped to 67.6% in H1'26 from 42.8% in FY25. When prices fall, the reverse happens, as in "
        "FY23, when net profit fell to RMB0.16bn.",
        "Microcontrollers (~12% of revenue) are a steadier, design-win business. GD32 offers hundreds of Arm and "
        "RISC-V parts for industrial control, motor drives, consumer devices and increasingly automotive, where "
        "qualification cycles are long but customers are sticky. Domestic substitution of STMicro, NXP and Renesas "
        "parts is the main growth driver. Sensors and analog chips (~3%) are small.",
        "GigaDevice carries large inventories (~220 days of cost of sales) as a strategic buffer and holds equity "
        "stakes in other chip companies. Those stakes generate volatile fair-value gains: more than RMB2bn of H1'26 "
        "profit came from this source.",
    ],
    segments_title="Revenue mix and economics",
    segments=[
        ("Memory: NOR, SLC NAND, niche DRAM", "~85%", "Boot/code storage for PCs, servers, IoT, auto; DDR3/DDR4/LPDDR4",
         "Price-taker; memory GM 67.6% in H1'26 vs 42.8% FY25"),
        ("Microcontrollers (GD32)", "~12%", "Arm/RISC-V MCUs for industrial, consumer, automotive",
         "Sticky design wins; domestic substitution"),
        ("Sensors & analog", "~3%", "Fingerprint/touch sensors (Silead), PMIC", "Small; competitive"),
    ],
    competition=[
        "Specialty memory is an oligopoly of mid-sized Asian suppliers. In NOR flash, Winbond (No.1), GigaDevice (No.2, "
        "~18%) and Macronix lead, with Puya, XMC and ISSI behind. In SLC NAND, Kioxia, Winbond and Macronix are the main "
        "rivals. In niche DRAM, Nanya, Winbond and ESMT compete as the big three DRAM makers exit DDR4. Product "
        "differentiation is limited, so share depends on cost, capacity access and customer relationships. Taiwanese "
        "peers trade at ~4x forward earnings, a reminder that the market capitalises peak memory profits cautiously.",
        "In MCUs, GigaDevice competes with STMicroelectronics, NXP, Infineon, Renesas, Microchip and TI globally, and with "
        "Chinese rivals such as Nations Technologies, Chipsea and Artery at home. Its advantages are breadth (one of the "
        "largest Arm MCU catalogues in China), pin-compatibility with Western parts, and price. Its gaps are automotive "
        "qualification depth and global sales coverage. The CXMT link is both a strength (secure DRAM supply) and a risk "
        "(related-party dependence, US export-control exposure).",
    ],
    competitors=[
        ("Winbond", "Taiwan", "NOR, SLC NAND, niche DRAM", "NOR No.1; own fabs; ~4x forward P/E"),
        ("Macronix", "Taiwan", "NOR, ROM, SLC NAND", "Strong in automotive/industrial NOR; own fabs"),
        ("Nanya / ESMT", "Taiwan", "Niche/legacy DRAM", "Direct niche-DRAM rivals"),
        ("STMicro / NXP / Renesas", "Europe / Japan", "General-purpose MCUs", "Global MCU leaders; GigaDevice substitutes"),
        ("Puya / XMC / Nations", "China", "NOR flash; MCUs", "Domestic price competitors"),
    ],
    moat=[
        "No.2 global NOR position and China's broadest MCU catalogue, with deep local customer relationships.",
        "Fabless model with diversified foundry access plus secure DRAM supply via CXMT.",
        "Net cash of ~RMB17bn and almost no debt.",
        "Vulnerabilities: memory price cycles, related-party and export-control exposure, fair-value volatility.",
    ],
    tam=[
        "Frost & Sullivan estimates the global specialty-memory market (NOR, SLC NAND, niche DRAM) at US$15.7bn in 2025, "
        "including US$3.1bn for NOR flash. Both are rising sharply in value in 2026: TrendForce expects high-capacity NOR "
        "prices to rise another 90–110% in H2'26, as AI servers and AI PCs need more and larger code-storage chips and "
        "supply shrinks. The general-purpose MCU market is larger (roughly US$20–25bn) and grows with industrial "
        "automation, EVs and IoT.",
        "GigaDevice's TTM revenue of RMB16.6bn (~US$2.5bn) implies a mid-teens share of its combined addressable markets. "
        "The key question is not market size but price durability: the legacy-memory shortage will last only until "
        "supply responds, from Chinese and Taiwanese capacity or from majors returning to profitable niches.",
    ],
    tam_table=[
        ("Specialty memory", "US$15.7bn (2025)", "Sharp price-led growth in 2026", "Frost & Sullivan"),
        ("NOR flash", "US$3.1bn (2025)", "High-capacity NOR +90–110% in H2'26", "Frost & Sullivan; TrendForce"),
        ("General-purpose MCUs", "~US$20–25bn", "Mid-single-digit growth; domestic substitution", "Industry estimates"),
        ("GigaDevice NOR share", "~18% (No.2)", "Gaining with AI-server NOR", "Industry estimate"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue fell from RMB8.1bn (FY22) to RMB5.8bn (FY23) in the memory downturn, then "
        "recovered to RMB9.2bn (FY25) and RMB16.6bn TTM. Gross margin moved from 30.3% (FY23) to 39.1% (FY25) and 56.1% "
        "TTM. Operating profit went from RMB0.1bn (FY23) to RMB1.4bn (FY25) and RMB6.7bn TTM, showing the operating "
        "leverage in a fabless memory model. Net profit of RMB6.9bn in H1'26 included >RMB2bn of fair-value gains. We "
        "forecast revenue of RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of RMB{np26}bn/{np27}bn/{np28}bn, peaking in "
        "FY27E."),
    fin_bs=(
        "<b>Balance sheet.</b> Total assets doubled from RMB21.4bn (FY25) to RMB42.4bn (June 2026), reflecting H1 profits, "
        "H-share proceeds and revalued equity investments. Cash and short-term investments rose to RMB17.4bn against "
        "only RMB0.1bn of debt, so net cash is RMB{ncj26}bn (RMB{nc25}bn at FY25). Inventory is the main operating asset: "
        "RMB3.4bn at FY25 ({invd25} days of cost of sales) and RMB4.2bn in June 2026. Receivables are tiny ({recvd25} "
        "days) because distributors pay quickly. Equity attributable reached RMB37.3bn (BVPS ~RMB53), and the current "
        "ratio of {cr25} is very high."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash flow was RMB1.2–2.1bn a year over FY23–25 (OCF/net profit {ocfnp25} in FY25) "
        "and jumped to RMB7.2bn TTM. Capex is modest (RMB0.3–1.6bn), so FCF rose from RMB{fcf23}bn (FY23) to "
        "RMB{fcfttm}bn TTM. Dividends are small (FY25 DPS RMB0.75). We forecast FCF of RMB{fcf26}bn/{fcf27}bn/{fcf28}bn; "
        "net cash would reach ~RMB{nc28}bn by FY28E, giving flexibility for buybacks, M&amp;A or higher payouts after the "
        "cycle peaks."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE swung from {roe23} (FY23) to {roe25} (FY25) and should spike to ~{roe26} in FY26E before "
        "normalising to ~{roe28} in FY28E, a textbook cyclical profile. ROA is {roa25}. Inventory days ({invd25}) are high "
        "by design. Payout was only {payout25} on FY25 EPS."),
)

V2["jushi"] = dict(
    background=[
        "China Jushi traces its roots to a township glass-fibre workshop in Tongxiang, Zhejiang, in the 1970s that grew "
        "into Jushi Group, formally established in 1993. The listed entity joined the Shanghai Stock Exchange in 1999 "
        "as China Fiberglass, with state-owned China National Building Material (CNBM) as its controlling shareholder, "
        "and was renamed China Jushi in 2016. The Zhenshi Group, the vehicle of Jushi's founding management, is the "
        "second-largest shareholder and has been selling shares.",
        "Jushi grew into the world's largest glass-fibre producer by building ever-larger tank furnaces and pushing down "
        "energy and raw-material costs. It went abroad early, building a plant in Egypt's Suez economic zone from the "
        "early 2010s to serve Europe and the Middle East tariff-free, then a plant in South Carolina, US, in 2019. Its "
        "Chinese bases are in Tongxiang, Jiujiang, Chengdu and Huai'an. A long-standing issue is horizontal competition "
        "with Taishan Fiberglass, owned by sister company Sinoma Science & Technology, which is also controlled by CNBM. "
        "In 2026 Jushi started a 100kt electronic-grade glass-fibre line in Huai'an (with 390m metres of cloth capacity) "
        "and approved further e-cloth investments to serve AI-server circuit boards.",
    ],
    milestones=[
        ("1993", "Jushi Group established in Tongxiang, Zhejiang (roots in a 1970s township plant)."),
        ("1999", "Listed in Shanghai as China Fiberglass (600176.SH); CNBM is the controlling shareholder."),
        ("Early 2010s", "First overseas plant in Egypt (Suez) to serve Europe and the Middle East."),
        ("2016", "Renamed China Jushi."),
        ("2019", "US plant in South Carolina starts production."),
        ("2021–22", "Cycle peak: net profit RMB6.0bn and RMB6.6bn."),
        ("2026", "100kt Huai'an e-glass line at full output; e-cloth price +49%; RMB2.4bn e-cloth project."),
    ],
    ownership=[
        ("Controlling shareholder", "China National Building Material (CNBM, state-owned), ~29%"),
        ("Second-largest shareholder", "Zhenshi Group (founding management), ~15%, selling"),
        ("Sister company", "Sinoma Science & Technology (Taishan Fiberglass), also CNBM-controlled"),
    ],
    business=[
        "Glass fibre is made by melting silica-rich minerals in continuous tank furnaces and drawing the melt through "
        "platinum-rhodium bushings into fine filaments. Furnaces run non-stop for 8–10 years before a cold repair, so "
        "the business is capital- and energy-intensive with high fixed costs. Scale, furnace efficiency, energy prices "
        "and utilisation determine cost position, and Jushi is the industry cost leader with its own mineral mines, "
        "large furnaces and automated lines.",
        "Products fall into two families. Reinforcement fibre (direct and assembled roving, chopped strands, mats and "
        "fabrics), the bulk of volume, goes into wind-turbine blades, construction materials, pipes and tanks, "
        "automotive thermoplastics and consumer goods. Pricing follows the capacity cycle and was flat in H1'26. "
        "Electronic yarn and woven electronic cloth go to copper-clad-laminate makers (Kingboard, Shengyi, Nan Ya and "
        "others), who make the base material for printed circuit boards. This is the profit engine today: AI servers "
        "and high-speed networking boards use more layers and more cloth, standard 7628 cloth averaged RMB6.02/m in "
        "H1'26 (+49%), and further 15–20% increases followed in September.",
        "Jushi sells mostly direct to industrial customers in China and abroad (Egypt and US plants serve Europe and "
        "North America). Working capital is moderate (receivables ~116 days, inventory ~100 days at FY25), and the "
        "balance sheet carries ~RMB11bn of net debt from successive capacity builds. The strategic task now is to move "
        "up the e-cloth value chain into thin and low-dielectric grades, where Japan's Nittobo leads. Jushi's "
        "low-dielectric products are in customer certification.",
    ],
    segments_title="Products, end-markets and 2026 price trend",
    segments_cols=("Product family", "End-markets", "2026 price trend", "Economics"),
    segments=[
        ("Direct / assembled roving", "Wind blades, pipes, construction", "Flat (H1'26)", "Bulk volume; cost leadership decisive"),
        ("Chopped strands & thermoplastics", "Autos, appliances, consumer goods", "Stable", "Mid margins"),
        ("Electronic yarn & cloth", "Copper-clad laminates → PCBs (AI servers)", "7628 cloth +49%; +15–20% in Sept",
         "Profit engine; capacity expanding"),
        ("Low-dielectric e-cloth", "High-speed / AI server boards", "Premium", "In certification; Nittobo leads"),
    ],
    competition=[
        "China produces the large majority of the world's glass fibre, and the industry is concentrated: Jushi, Taishan "
        "Fiberglass (Sinoma S&amp;T) and Chongqing Polycomp (CPIC) are the big three. Outside China, the main producers "
        "are Saint-Gobain/Vetrotex, Johns Manville and Nippon Electric Glass. Competition is mostly on price and "
        "delivery for standard roving, and cost leadership lets Jushi win share in downturns. The main risk is "
        "capacity additions: every price spike draws new furnaces, which then depress prices for years.",
        "Electronic yarn and cloth have a different set of rivals: Kingboard (which commissioned a 70kt e-yarn line and "
        "is adding cloth), Taiwan Glass, Grace Fabric and Honghe at the standard end, and Nittobo (Japan) in premium "
        "low-dielectric and low-CTE cloth. Jushi expects to lift its share of global electronic-grade fibre from ~23% "
        "to ~28% with Huai'an. Its advantage is scale and cost; its gap is the top-end grades used in the most "
        "advanced AI boards.",
    ],
    competitors=[
        ("Taishan Fiberglass (Sinoma S&T)", "China (CNBM)", "Roving, e-yarn, wind materials", "No.2; sister company under CNBM"),
        ("Chongqing Polycomp (CPIC)", "China", "Roving, e-yarn", "No.3; regional cost base"),
        ("Nitto Boseki (Nittobo)", "Japan", "Premium low-Dk / low-CTE e-cloth", "Technology leader in AI-grade cloth"),
        ("Kingboard / Taiwan Glass / Grace Fabric", "HK / Taiwan / China", "E-yarn and e-cloth", "Adding capacity"),
        ("Saint-Gobain / Johns Manville / NEG", "Europe / US / Japan", "Reinforcement fibre", "Higher cost; regional strongholds"),
    ],
    moat=[
        "Industry-lowest cost from scale, large furnaces, own minerals and automation.",
        "Global footprint (Egypt, US) that mitigates trade barriers.",
        "Integrated yarn-to-cloth chain and fast capacity execution in electronic grades.",
        "Vulnerabilities: capacity cycles, energy costs, Zhenshi share overhang, lag in premium low-Dk cloth.",
    ],
    tam=[
        "China produced 8.43Mt of glass-fibre yarn in 2025 (+11.5%), most of global output. Demand grows roughly with "
        "industrial production plus structural drivers: lightweighting in autos, wind-turbine blades, infrastructure "
        "composites and electronics. The reinforcement market is large but low-growth and cyclical. At a few thousand "
        "RMB per tonne, it is a market worth tens of billions of RMB, where share is won on cost.",
        "Electronic-grade fibre is a smaller but faster-growing and higher-value segment. AI servers, 800G networking and "
        "automotive electronics use thicker, multi-layer boards with more and better cloth. Jushi's Huai'an line alone "
        "represents ~9% of global e-cloth capacity, and its share of electronic-grade fibre should rise to ~28%. The "
        "addressable market's value is being driven by price as much as volume, which makes the outlook sensitive "
        "to capacity additions by peers.",
    ],
    tam_table=[
        ("China glass-fibre yarn output", "8.43Mt (2025)", "+11.5% in 2025", "Industry data"),
        ("Electronic-grade glass fibre", "Jushi ~23% → ~28% share", "AI-server and networking boards", "Company/press"),
        ("7628 electronic cloth price", "RMB6.02/m (H1'26)", "+49% YoY; +15–20% in Sept", "Futu/industry"),
        ("Huai'an e-glass line", "100kt + 390m metres", "~9% of global e-cloth capacity", "China Daily/company"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue fell from RMB20.2bn (FY22) to RMB14.9bn (FY23) as glass-fibre prices slumped, "
        "then recovered to RMB18.9bn (FY25) and RMB20.9bn TTM. Gross margin bottomed at 24.8% (FY24) and rebounded to "
        "33.0% (FY25) and 38.1% TTM. Operating profit rose from RMB2.6bn (FY23) to RMB4.6bn (FY25), and net profit from "
        "RMB2.4bn (FY24) to RMB3.3bn (FY25) and RMB2.9bn in H1'26 alone (+74%). We forecast revenue of "
        "RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E."),
    fin_bs=(
        "<b>Balance sheet.</b> The balance sheet is asset-heavy: PP&amp;E of RMB36–38bn is two-thirds of total assets "
        "(RMB57.6bn in June 2026). Debt has been stable at ~RMB14.6bn and cash at ~RMB3bn, so net debt has held around "
        "RMB{nc25}bn (FY25) and RMB{ncj26}bn (June 2026), ~{ndeq25} of equity and {ndebitda25} EBITDA. Working capital "
        "improved as inventory days fell from 154 (FY23) to {invd25} (FY25) while receivable days are {recvd25}. The "
        "current ratio is only {cr25}, reflecting short-term borrowings. Equity attributable is RMB33.2bn (BVPS ~RMB8.3)."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash flow rose from RMB0.9bn (FY23) to RMB4.2bn (FY25) and RMB5.2bn TTM as prices "
        "recovered and inventory was released. With maintenance-level capex of RMB1.3–1.5bn, FCF went from "
        "−RMB{fcf23}bn (FY23) to RMB{fcf25}bn (FY25), but capex has since stepped up to RMB3.2bn TTM for the new "
        "e-glass lines. Dividends (RMB1.4–2.5bn) and a RMB0.54bn buyback absorbed most FCF. We forecast FCF of "
        "RMB{fcf26}bn/{fcf27}bn/{fcf28}bn with capex of RMB3–4bn, eliminating net debt by FY28E."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE was {roe23}, {roe24} and {roe25} over FY23–25, well below the ~20%+ of the 2021–22 peak. "
        "We expect ~{roe26} in FY26E and ~{roe27} in FY27E as e-cloth profits flow through. ROA is {roa25}, and asset "
        "turnover is low (0.35x), typical for a furnace-based business. The payout ratio was {payout25} on FY25 EPS."),
)

V2["jlmag"] = dict(
    background=[
        "JL Mag Rare-Earth was founded in 2008 in Ganzhou, Jiangxi, by Cai Baogui, who remains chairman and controls the "
        "company. Ganzhou is the centre of China's ionic-clay deposits of heavy rare earths (dysprosium, terbium), which "
        "are critical for high-temperature magnets. JL Mag set out to make the highest grades of sintered "
        "neodymium-iron-boron (NdFeB) magnets for demanding applications, rather than competing in commodity grades.",
        "The bet paid off as EVs, inverter air-conditioners and direct-drive wind turbines took off. JL Mag qualified with "
        "global automakers and Tier-1 suppliers, wind-turbine OEMs and appliance makers, and built a reputation for "
        "grain-boundary diffusion. This process deposits heavy rare earths only at grain boundaries, cutting their use "
        "and cost while keeping performance. It listed on Shenzhen's ChiNext board in 2018 and in Hong Kong in January "
        "2022. It now runs bases in Ganzhou, Ningbo and Baotou (Inner Mongolia, near light rare-earth supply) and is "
        "building overseas capacity. Capacity reached ~40kt in 2025 and is targeted at 60kt by end-2027. Small-batch "
        "deliveries of humanoid-robot rotors began in 2026.",
    ],
    milestones=[
        ("2008", "Founded in Ganzhou, Jiangxi by Cai Baogui."),
        ("2018", "ChiNext IPO (300748.SZ)."),
        ("2022", "Hong Kong listing (6680.HK)."),
        ("2023–25", "Baotou and Ningbo bases expand; capacity ~40kt in 2025."),
        ("2025", "Net profit +142% to RMB0.71bn as rare-earth prices recover."),
        ("2026", "Small-batch humanoid-robot rotor deliveries; robot sales +96% in H1; 60kt target for 2027."),
    ],
    ownership=[
        ("Controlling shareholder", "Founder-chairman Cai Baogui"),
        ("Share classes", "A-share 300748.SZ; H-share 6680.HK (~46% discount to A)"),
        ("Raw-material suppliers", "China Northern Rare Earth, China Rare Earth Group (state-controlled)"),
    ],
    business=[
        "JL Mag makes sintered NdFeB permanent magnets, the strongest commercially available magnets, which allow "
        "smaller, lighter and more efficient electric motors and generators. The process runs from alloy melting and "
        "strip casting through hydrogen decrepitation, jet milling, pressing in a magnetic field, sintering, machining "
        "and coating, with grain-boundary diffusion for high-coercivity grades. Each customer program needs custom "
        "specifications and lengthy qualification, especially in automotive.",
        "End-markets in H1'26 were NEVs and auto parts (56% of revenue: traction motors, EPS, other motors), "
        "energy-efficient air-conditioners (24%: inverter compressors), robots and industrial servo motors (6.6%), wind "
        "power (6.3%), and consumer electronics and others. Robot-related sales nearly doubled (+96%) and are the "
        "fastest-growing line.",
        "Pricing is broadly raw-material cost (PrNd, Dy, Tb oxides and metals) plus a processing fee, adjusted "
        "periodically. JL Mag's profit therefore comes from volume and processing margin, plus inventory gains or "
        "losses when rare-earth prices move. That explains the swing from a 10.4% gross margin in FY24, when prices "
        "fell, to 21.7% in H1'26. Raw materials come from China's state-controlled rare-earth groups. Export licensing "
        "since 2025 adds administrative friction for overseas customers but reinforces China's dominance. Working "
        "capital is substantial: receivables and inventory each run at ~160 days.",
    ],
    segments_title="Revenue by end-market and economics (H1'26)",
    segments=[
        ("NEVs & auto parts", "56.0%", "Traction motors, EPS and auxiliary motors", "Largest; long qualification cycles"),
        ("Energy-efficient air-conditioners", "24.0%", "Inverter compressor motors", "Stable volume"),
        ("Robots & servo motors", "6.6%", "Industrial servo, humanoid joints/rotors", "+96% in H1'26; highest growth"),
        ("Wind power", "6.3%", "Direct-drive / semi-direct generators", "Lumpy; large magnets"),
        ("Other", "7.1%", "Consumer electronics, elevators, industrial motors", "Diversified"),
    ],
    competition=[
        "China makes roughly 90% of the world's sintered NdFeB magnets. Domestic competitors include Ningbo Yunsheng, "
        "Zhong Ke San Huan, Ningbo Jintian, Yantai Zhenghai, Innuovo (Hengdian DMEGC) and Galaxy Magnetic, plus many "
        "smaller producers of lower grades. JL Mag is the largest in high-performance grades and has the deepest "
        "automotive qualification list.",
        "Outside China, Proterial (formerly Hitachi Metals) and Shin-Etsu in Japan, TDK and VAC (Germany, building in the "
        "US) are established; MP Materials (US) and Neo Performance (Estonia) are building Western supply chains with "
        "government support. Those efforts are small relative to China and much higher-cost, but over time they will "
        "take share of Western automakers' purchases. JL Mag's counter-strategy is overseas capacity and long-term "
        "contracts.",
    ],
    competitors=[
        ("Ningbo Yunsheng", "China", "Sintered NdFeB, broad grades", "Smaller; ~21x forward P/E"),
        ("Zhong Ke San Huan", "China", "NdFeB (Chinese Academy of Sciences roots)", "Lower margins; ~57x forward P/E"),
        ("Proterial / Shin-Etsu / TDK", "Japan", "High-grade NdFeB", "Technology peers; higher cost"),
        ("VAC", "Germany/US", "NdFeB and specialty alloys", "Building US plant for automakers"),
        ("MP Materials", "US", "Mine-to-magnet (Texas)", "Policy-backed Western supply; ~18x EV/sales"),
    ],
    moat=[
        "Scale leader in high-performance NdFeB, with grain-boundary diffusion know-how.",
        "Deep qualification with global automakers and Tier-1s; robot and humanoid design wins.",
        "Location near both heavy (Ganzhou) and light (Baotou) rare-earth supply.",
        "Vulnerabilities: rare-earth price swings, export licensing, Western supply-chain diversification.",
    ],
    tam=[
        "Industry estimates put high-performance NdFeB demand growth at ~10–15% a year to 2030. EV traction motors use "
        "2–3kg of magnet per car; inverter air-conditioners and industrial motors are switching to permanent-magnet "
        "designs for efficiency; direct-drive wind turbines use hundreds of kilograms per MW; and humanoid robots "
        "could each need roughly 2–4kg in joint motors on industry estimates.",
        "The value of the market also depends on rare-earth prices, since magnets are priced cost-plus. NdPr oxide "
        "peaked near US$98k/t in January 2026 (Baotou February average RMB850k/t) and eased to ~RMB750k/t by July. "
        "JL Mag's planned 60kt capacity would be a high-teens share of global high-performance supply on our rough "
        "estimates.",
    ],
    tam_table=[
        ("High-performance NdFeB demand", "–", "~10–15% a year to 2030", "Industry estimates"),
        ("China share of sintered NdFeB", "~90%", "Stable; export licensing since 2025", "Industry estimates"),
        ("NdPr oxide price", "~RMB750k/t (Jul 2026)", "Peak ~US$98k/t in Jan 2026", "SMM; Benchmark"),
        ("JL Mag capacity", "~40kt (2025) → 60kt (2027E)", "+50%", "Company"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue was flat at ~RMB6.7bn in FY23–24 as rare-earth prices fell, then rose to RMB7.7bn "
        "(FY25) and RMB8.9bn TTM. Gross margin troughed at 10.4% (FY24) and recovered to 20.3% (FY25) and 22.7% TTM. Net "
        "profit fell to RMB0.29bn in FY24 before rebounding to RMB0.71bn (FY25) and RMB0.46bn in H1'26 (+52%). We "
        "forecast revenue of RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E, "
        "as capacity growth offsets softer rare-earth prices."),
    fin_bs=(
        "<b>Balance sheet.</b> Total assets are RMB16.5bn (June 2026), dominated by working capital. Receivables of "
        "RMB3.4bn ({recvd25} days at FY25) and inventory of RMB2.8–3.6bn ({invd25} days) are partly funded by payables "
        "({apd25} days). PP&amp;E is modest at RMB3.3bn. Net cash shrank from RMB{nc23}bn (FY23) to RMB{nc25}bn (FY25) as "
        "borrowing rose to fund inventory, then recovered to RMB{ncj26}bn in June 2026. Equity attributable is RMB7.8bn "
        "(BVPS ~RMB5.7), the current ratio {cr25}."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash flow fell from RMB1.5bn (FY23) to RMB0.35bn (FY25) as rising rare-earth prices "
        "inflated inventory and receivables (OCF/net profit {ocfnp25} in FY25), then recovered to RMB2.1bn TTM. With "
        "capex of RMB0.5–0.8bn, FCF was slightly negative in FY24–25 (FY25 −RMB{fcf25}bn) but RMB{fcfttm}bn TTM. "
        "Dividends of RMB0.45–0.63bn a year are generous for this cash flow. We forecast FCF of −RMB{fcf26}bn, "
        "−RMB{fcf27}bn and RMB{fcf28}bn in FY26–28E as capex rises toward 60kt, so the company moves to small net "
        "debt (~RMB{nc28}bn by FY28E)."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE fell from {roe23} (FY23) to {roe24} (FY24) and recovered to {roe25} (FY25); we expect "
        "~{roe27} by FY27E and ~{roe28} by FY28E. ROA is {roa25}. Cash conversion is the weak spot ({ocfnp25} in FY25, "
        "~0.6–0.7x in our forecasts). Payout was {payout25} on FY25 EPS."),
)

V2["hans"] = dict(
    background=[
        "Han's Laser was founded in Shenzhen in 1996 by Gao Yunfeng, who started by selling laser marking machines to "
        "the Pearl River Delta's electronics factories. It listed on the Shenzhen SME board in 2004 and grew into Asia's "
        "largest industrial-laser equipment group by following its customers. It moved into laser cutting and welding "
        "for metal fabricators, then PCB drilling and processing, consumer-electronics production lines (it has long "
        "been an Apple supply-chain vendor), lithium-battery equipment, and display and semiconductor equipment.",
        "The group is organised as a holding company with several specialist subsidiaries. The most important today is "
        "Han's CNC, the PCB-equipment maker listed separately on ChiNext since 2022. Han's sold more than 54,000 "
        "machines in FY25. FY24 reported profit was inflated by ~RMB1.25bn of one-off disposal gains, which makes FY25's "
        "reported decline misleading; core profit rose 82%. The founder's holding company remains the controlling "
        "shareholder but trimmed its stake in September 2026. AI servers have transformed the company's growth "
        "profile: high-layer, high-density boards require far more drilling, exposure and testing equipment, and "
        "Han's entered 2026 with RMB19bn of new orders and a RMB9bn backlog.",
    ],
    milestones=[
        ("1996", "Founded in Shenzhen by Gao Yunfeng; laser marking machines."),
        ("2004", "Listed on the Shenzhen SME board (002008.SZ)."),
        ("2000s–10s", "Expands into cutting/welding, PCB equipment and Apple-chain automation."),
        ("2022", "PCB-equipment subsidiary Han's CNC lists on ChiNext (301200.SZ)."),
        ("2024", "One-off disposal gains (~RMB1.25bn) lift reported net profit to RMB1.69bn."),
        ("2025", "Revenue +27% to RMB18.8bn; PCB equipment +73% to RMB5.8bn."),
        ("2026", "Guides revenue ≥RMB27bn (+44%); H1 net profit +164%; founder trims stake (Sept)."),
    ],
    ownership=[
        ("Controlling shareholder", "Han's Holding Group, controlled by founder Gao Yunfeng (trimmed stake Sept 2026)"),
        ("Listed subsidiary", "Han's CNC (301200.SZ): PCB drilling and processing equipment"),
        ("Dividend policy", "Low payout (~15–20%)"),
    ],
    business=[
        "Han's makes capital equipment built around lasers and precision motion control. FY25 revenue split into "
        "information-industry equipment (RMB8.2bn, 44%) and industrial lasers, new-energy and other equipment (RMB10.5bn, "
        "56%). Within the first, PCB equipment (RMB5.8bn, 31% of group revenue) covers mechanical and laser drilling, "
        "exposure, routing and testing for printed circuit boards. Consumer-electronics, display and semiconductor "
        "equipment made up the remaining 13%. The second group spans high-power fibre-laser cutting and welding systems "
        "for sheet-metal fabricators, equipment for lithium-battery production, and small and medium-power lasers for "
        "marking and micro-processing.",
        "Revenue tracks customers' capex cycles, so visibility comes from orders and backlog. PCB makers are investing "
        "heavily in capacity for AI-server and high-speed networking boards in China, Taiwan and Southeast Asia, "
        "which needs more and more precise drilling. Apple product cycles drive consumer-electronics line orders, "
        "battery makers' expansion drives new-energy equipment, and general industry drives the cutting-laser "
        "business.",
        "Margins depend on mix. PCB and precision equipment earn higher gross margins than commoditised cutting "
        "lasers, and group gross margin rose 4pt to 34.9% in H1'26. Working capital is heavy, because customers pay in "
        "instalments with acceptance-based final payments: receivables run at ~230 days of sales. The holding "
        "structure means some profit leaks to minorities in listed subsidiaries.",
    ],
    segments_title="Revenue mix and economics (FY25)",
    segments=[
        ("PCB equipment (Han's CNC)", "31% (RMB5.8bn, +73%)", "Mechanical/laser drilling, exposure, testing for PCBs",
         "Highest growth; AI-server driven"),
        ("Consumer-electronics, display & semi equipment", "13%", "Automation lines for smartphones/wearables; display, semi tools",
         "Apple-cycle dependent"),
        ("Industrial lasers, new-energy & other", "56%", "High-power cutting/welding; battery equipment; marking",
         "Competitive; lower margins"),
    ],
    competition=[
        "In PCB equipment, Han's CNC competes with Japan's Via Mechanics (mechanical drilling leader) and Mitsubishi "
        "Electric (laser drilling), Germany's Schmoll and several Taiwanese makers. It is the leader in China and has "
        "been taking share in high-end drilling as Chinese PCB makers win AI-server work. The top-end laser-drilling "
        "segment for advanced substrates remains dominated by Japanese suppliers.",
        "In industrial lasers, the global leaders are Trumpf, Coherent, IPG Photonics and Bystronic. Domestic "
        "competition is fierce from HGTECH (Huagong), Hymson, Golden Laser and Raycus (laser sources), and has pushed "
        "down prices of fibre-laser cutting systems. In battery equipment, Lead Intelligent and Yinghe are the main "
        "rivals. Han's advantages are breadth, its installed base, closeness to customers in Shenzhen's electronics "
        "cluster and cost. Its weaknesses are exposure to cyclical capex and a still-small presence at the very high "
        "end of semiconductor and substrate equipment.",
    ],
    competitors=[
        ("Via Mechanics / Mitsubishi Electric", "Japan", "PCB mechanical and laser drilling", "High-end leaders"),
        ("HGTECH (Huagong)", "China", "Lasers, sensors, optical modules", "Domestic laser rival; ~39x forward P/E"),
        ("Trumpf / Coherent / IPG", "Germany / US", "Industrial lasers and systems", "Technology leaders; premium pricing"),
        ("Lead Intelligent / Yinghe", "China", "Lithium-battery equipment", "Leaders in battery lines"),
        ("Bystronic / Golden Laser", "Switzerland / China", "Sheet-metal laser cutting", "Price competition"),
    ],
    moat=[
        "Broadest laser and precision-equipment portfolio in Asia, with a large installed base and service network.",
        "Leadership in China PCB equipment as AI-server boards drive capacity investment.",
        "Customer intimacy with Apple-chain and Shenzhen electronics makers.",
        "Vulnerabilities: capex cyclicality, price competition in lasers, controlling-shareholder selling.",
    ],
    tam=[
        "Global printed-circuit-board output is roughly US$75–80bn a year (Prismark), and AI servers and high-speed "
        "networking are the fastest-growing segments. They need more layers, finer features and more holes per board. "
        "That is prompting large capacity additions by Chinese, Taiwanese and Southeast Asian PCB makers, and equipment "
        "spending is growing much faster than PCB output.",
        "China is also the world's largest market for industrial laser processing, where fibre lasers are displacing "
        "plasma and mechanical cutting, though it is mature and price-competitive. Han's FY26E revenue of ~RMB27bn "
        "(~US$4bn) makes it a top-tier participant in both markets. Upside comes from share gains in high-end PCB "
        "drilling and semiconductor equipment rather than market growth alone.",
    ],
    tam_table=[
        ("Global PCB output", "~US$75–80bn", "AI-server/networking boards fastest-growing", "Prismark"),
        ("PCB equipment capex", "Rising faster than PCB output", "AI-driven capacity additions", "Company/industry"),
        ("Industrial laser equipment", "China is the largest market", "Mature; price-competitive", "Industry"),
        ("Han's order book", "RMB19bn new orders + RMB9bn backlog", "FY26 revenue ≥RMB27bn", "Company"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue moved from RMB14.1bn (FY23) to RMB14.8bn (FY24), RMB18.8bn (FY25) and RMB24.6bn "
        "TTM. Gross margin improved from 30.4% (FY24) to 32.2% (FY25) and 34.1% TTM. Operating profit tripled from "
        "RMB0.4bn (FY24) to RMB1.35bn (FY25) and RMB3.0bn TTM. Reported net profit (RMB0.82bn/1.69bn/1.19bn over FY23–25) "
        "was distorted by FY24 one-offs; H1'26 net profit was RMB1.29bn (+164%). We forecast revenue of "
        "RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E."),
    fin_bs=(
        "<b>Balance sheet.</b> Total assets jumped from RMB38.2bn (FY25) to RMB47.4bn (June 2026) as receivables "
        "(RMB16.1bn) and inventory (RMB7.2bn) grew with orders. At FY25, receivable days were {recvd25} and inventory "
        "days {invd25}, partly offset by payable days of {apd25}. Debt fell to RMB4.4bn and cash rose to RMB10.1bn, so "
        "net cash is RMB{ncj26}bn (RMB{nc25}bn at FY25), ~{ndeq25} of equity. Equity attributable rose to RMB21.5bn "
        "(BVPS ~RMB21), and minority interests jumped to RMB3.9bn after capital raising at subsidiaries. The current "
        "ratio is {cr25}."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash flow has been steady at RMB1.1–1.5bn a year, lagging profit growth because "
        "working capital absorbs cash. Capex fell from RMB1.4–1.5bn (FY23–24) to RMB0.6bn (FY25), so FCF turned "
        "positive at RMB{fcf25}bn in FY25 after −RMB{fcf23}bn/−RMB{fcf24}bn in FY23–24. Dividends are small. We forecast "
        "FCF of RMB{fcf26}bn/{fcf27}bn/{fcf28}bn as working-capital growth slows relative to profits, lifting net cash to "
        "~RMB{nc28}bn by FY28E."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE was {roe23}, {roe24} and {roe25} over FY23–25; we expect it to more than double to "
        "~{roe27} by FY27E on higher margins and volumes. ROA was {roa25} in FY25. Receivable days of {recvd25} are the "
        "key working-capital risk in an AI capex slowdown. Payout was {payout25} on FY25 EPS."),
)
