"""Five-forces assessment for the 'Competitive landscape' section: (force, intensity, assessment)."""

RIV, ENT, SUP, BUY, SUB = ("Rivalry", "New entrants", "Supplier power", "Buyer power", "Substitutes")

FORCES = {}

FORCES["zijin"] = [
    (RIV, "Medium", "Metals sell at exchange prices, so producers are price-takers and compete on cost and volume growth. "
     "Rivalry shows up in bidding for deposits, where Zijin meets CMOC, the majors and sovereign funds."),
    (ENT, "Low", "A new copper or gold mine takes 10–15+ years from discovery to output and billions of dollars; "
     "permitting and falling grades keep new supply scarce."),
    (SUP, "Medium", "Host governments own the ore. Royalties, export rules and resource nationalism (DRC, Serbia, "
     "Colombia) can claim a rising share of the rent; energy and labour costs are inflationary."),
    (BUY, "Low", "Smelters, refiners and bullion banks buy at benchmark prices. Copper concentrate treatment charges "
     "are near record lows, which shifts value from smelters to miners."),
    (SUB, "Low", "Aluminium replaces copper in some wiring and cooling at high prices, but grids, EVs and data centres "
     "have few alternatives; gold demand is monetary."),
]

FORCES["sany"] = [
    (RIV, "High", "XCMG, Zoomlion, LiuGong and Sunward compete hard on price and credit terms at home; overseas, "
     "Caterpillar and Komatsu defend share through dense dealer networks."),
    (ENT, "Low", "Scale manufacturing, dealer and service networks and the balance sheet to offer customer finance are "
     "hard to copy; no meaningful new entrant has emerged in a decade."),
    (SUP, "Low", "Steel is a commodity. Hydraulics, engines and controllers once came from Kawasaki, Rexroth and "
     "Cummins; Sany now makes many of these in-house."),
    (BUY, "Medium", "Contractors and rental firms are fragmented but price-sensitive and reliant on vendor finance; "
     "large mining and infrastructure buyers negotiate hard."),
    (SUB, "Low", "There is no substitute for earth-moving equipment. Demand risk comes from the construction cycle and "
     "the stock of used machines."),
]

FORCES["sieyuan"] = [
    (RIV, "Medium", "China's grid tenders are crowded (TBEA, XJ Electric, Pinggao, China XD, Hitachi Energy, Siemens "
     "Energy), which caps domestic margins; overseas markets are tighter."),
    (ENT, "Low", "Utilities require type tests, long qualification and a track record, especially for high-voltage "
     "products and overseas grids; qualification takes years."),
    (SUP, "Medium", "Copper, silicon steel and insulation materials are a large share of cost; Sieyuan passes changes "
     "through with a lag."),
    (BUY, "High", "State Grid and China Southern Grid are near-monopsony buyers at home. Overseas utilities and "
     "data-centre developers face equipment shortages, so suppliers have more pricing power there."),
    (SUB, "Low", "Switchgear, transformers and reactive-power compensation have no substitutes; new technology "
     "(e.g. SF6-free switchgear) favours incumbents that can fund R&amp;D."),
]

FORCES["catl"] = [
    (RIV, "High", "BYD, LG Energy Solution, CALB, Gotion, EVE and Sunwoda compete aggressively; carmakers dual-source "
     "and cell prices fell sharply over 2023–25."),
    (ENT, "Medium", "Carmakers and state-backed newcomers can build cell plants, but cost, quality and scale take years "
     "and Chinese overcapacity deters entry."),
    (SUP, "Low", "Cathode, anode, separator and electrolyte are oversupplied in China. CATL's scale and upstream "
     "stakes give it leverage, and lithium costs are largely passed through."),
    (BUY, "Medium", "Large carmakers negotiate hard and dual-source, but CATL's technology and cost lead keep it the "
     "default supplier for most global programmes."),
    (SUB, "Low", "Fuel cells have not scaled. Sodium-ion and solid-state are battery technologies CATL itself leads; "
     "pumped hydro competes with storage only at the margin."),
]

FORCES["sungrow"] = [
    (RIV, "High", "Huawei, Tesla, BYD and many Chinese integrators compete in storage, where system prices have fallen "
     "sharply; in inverters Huawei, Sineng, Ginlong and GoodWe are the main rivals."),
    (ENT, "Medium", "Cell makers (CATL, BYD, EVE) are moving into storage systems. Inverter entry is harder because "
     "utility buyers demand bankability, certification and service history."),
    (SUP, "Low", "Battery cells, the largest cost in a storage system, are oversupplied, and Sungrow sources from "
     "several cell makers; power-semiconductor supply has normalised."),
    (BUY, "High", "Utility-scale developers run competitive tenders and overseas IPPs are sophisticated buyers; "
     "bankability and track record are what protect margins."),
    (SUB, "Low", "Inverters are essential to solar. Storage competes with gas peakers and grid upgrades but is winning "
     "on cost in most markets."),
]

FORCES["huayou"] = [
    (RIV, "High", "Tsingshan, GEM, Lygend, CNGR and Nickel Industries keep adding Indonesian capacity, and Chinese "
     "overcapacity squeezes precursor and cathode processing fees."),
    (ENT, "Medium", "HPAL plants cost billions and need know-how, yet Chinese groups with Indonesian partners have built "
     "them quickly; Indonesia's ore quotas (RKAB) are now the main gate."),
    (SUP, "High", "Indonesia sets ore quotas, royalties and export policy, and the DRC's 2025 cobalt export suspension "
     "and quotas show how quickly host governments can change the economics."),
    (BUY, "Medium", "Battery and cathode makers such as LGES, POSCO and CATL are concentrated buyers; long-term supply "
     "agreements and joint ventures soften this."),
    (SUB, "Medium", "LFP chemistry (no nickel or cobalt) dominates China's EV and storage markets, and sodium-ion is a "
     "further threat; high-nickel holds in premium and ex-China EVs."),
]

FORCES["tianqi"] = [
    (RIV, "High", "Lithium is a commodity. Ganfeng, Albemarle, SQM, Rio Tinto, Pilbara Minerals and many Chinese "
     "lepidolite and brine producers compete, and in surplus the marginal cost sets the price."),
    (ENT, "Medium", "African hard rock, Argentine brine and Chinese lepidolite added supply within 2–4 years in "
     "2022–25; high prices quickly invite new projects."),
    (SUP, "Low", "Greenbushes gives Tianqi its own low-cost spodumene, so the main 'supplier' is its own joint "
     "venture; Western Australian royalties are the external claim."),
    (BUY, "Medium", "Cathode and battery makers (CATL, BYD, LG) are concentrated buyers on index-linked contracts and "
     "control qualification."),
    (SUB, "Medium", "Sodium-ion can replace LFP in storage and small EVs if lithium prices spike; there is no substitute "
     "in high-energy-density cells."),
]

FORCES["ganfeng"] = [
    (RIV, "High", "The same commodity rivalry as Tianqi in lithium chemicals, plus a crowded battery market where "
     "CATL, BYD, EVE and Gotion set the price of storage and consumer cells."),
    (ENT, "Medium", "New lithium supply arrives within 2–4 years when prices rise, and battery capacity in China is "
     "already in surplus."),
    (SUP, "Medium", "Ganfeng still buys part of its feedstock, and its own resources depend on host governments; Mexico "
     "revoked its Sonora concessions and Mali has tightened mining rules."),
    (BUY, "Medium", "Global cathode makers, battery makers and carmakers buy on index-linked long-term agreements; "
     "battery buyers run competitive tenders."),
    (SUB, "Medium", "Sodium-ion threatens lithium demand at the low end; in batteries, Ganfeng's solid-state work is a "
     "hedge against being substituted itself."),
]

FORCES["gigadevice"] = [
    (RIV, "High", "Winbond, Macronix and Puya in NOR; ST, NXP, Renesas, Microchip and many Chinese start-ups in MCUs; "
     "Nanya, Winbond and ESMT in niche DRAM."),
    (ENT, "Medium", "The fabless model lowers barriers and state funds created many MCU and NOR start-ups, but auto and "
     "industrial qualification takes years."),
    (SUP, "High", "GigaDevice relies on foundries (SMIC, Hua Hong, TSMC) and on CXMT for DRAM wafers; foundry capacity "
     "and pricing drive its gross margin."),
    (BUY, "Medium", "Customers are spread across consumer, industrial, auto and computing and mostly served through "
     "distributors; large handset and PC makers negotiate hard."),
    (SUB, "Medium", "NOR competes with embedded flash in SoCs and with NAND for larger code storage; MCUs compete with "
     "SoCs; niche DRAM competes with legacy DRAM from the majors."),
]

FORCES["jushi"] = [
    (RIV, "Medium", "Taishan Fiberglass (Sinoma), Chongqing Polycomp, Owens Corning and NEG are the main rivals; "
     "capacity additions in China periodically trigger price wars."),
    (ENT, "Low", "A tank furnace costs over RMB1bn and takes about two years to build, and electronic-grade yarn needs "
     "process know-how; new capacity mostly comes from incumbents."),
    (SUP, "Low", "Pyrophyllite, kaolin and limestone are abundant and partly self-supplied; natural gas and electricity "
     "are the main cost variables."),
    (BUY, "Medium", "Wind-blade and copper-clad-laminate makers are large and negotiate; construction, auto and "
     "industrial demand is fragmented."),
    (SUB, "Low", "Carbon fibre substitutes at the top end (e.g. long blade spars) at a large cost premium; steel and "
     "aluminium compete in some composite uses."),
]

FORCES["jlmag"] = [
    (RIV, "High", "Ningbo Yunsheng, Zhong Ke San Huan, AT&amp;M and Zhenghai at home, and Shin-Etsu, TDK and Proterial "
     "in Japan; Chinese capacity is growing fast."),
    (ENT, "Medium", "US and EU policy supports ex-China magnet plants (MP Materials, Neo, VAC), while Chinese entrants "
     "need rare-earth allocations and auto qualification."),
    (SUP, "High", "Feedstock (NdPr, dysprosium, terbium) is controlled by state groups under quotas; JL Mag's "
     "grain-boundary diffusion cuts its heavy rare-earth use."),
    (BUY, "Medium", "Buyers in EVs, wind, appliances and industrial motors are large and negotiate processing fees; "
     "pricing is largely cost-plus on raw materials."),
    (SUB, "Medium", "Ferrite magnets and rare-earth-free motors can replace NdFeB where performance allows; China's 2025 "
     "export controls have accelerated substitution work abroad."),
]

FORCES["hans"] = [
    (RIV, "High", "Via Mechanics and Mitsubishi Electric in PCB drilling; Trumpf, HGTech and Hymson in laser processing; "
     "Lead Intelligent and others in battery equipment."),
    (ENT, "Medium", "Low-power laser markers and cutters are commoditised, but high-end PCB drilling and semiconductor "
     "tools need years of process know-how."),
    (SUP, "Medium", "Laser sources, scanners and controllers come partly from third parties (IPG, Raycus); falling "
     "fibre-laser prices have helped margins."),
    (BUY, "High", "PCB, battery and consumer-electronics makers are concentrated, cyclical capex buyers that run "
     "competitive bids."),
    (SUB, "Medium", "Mechanical and laser drilling substitute for each other (Han's sells both); plasma and waterjet "
     "compete in cutting."),
]

FORCES["horizon"] = [
    (RIV, "High", "Nvidia (Orin/Thor) at the high end, Mobileye at the low end, Huawei's full-stack offer and Black "
     "Sesame, plus carmakers' own chips."),
    (ENT, "Medium", "Xpeng, Nio and Li Auto design their own chips, and Chinese chip start-ups keep appearing, but an "
     "auto-grade SoC takes 3–5 years and heavy R&amp;D."),
    (SUP, "High", "As a fabless company Horizon depends on TSMC and on EDA tools; US export controls could restrict "
     "advanced-node access."),
    (BUY, "High", "Chinese carmakers are concentrated, price-sensitive and increasingly able to design chips in-house."),
    (SUB, "Medium", "In-house silicon and Nvidia or Huawei full-stack solutions substitute at the top end; cheaper "
     "camera-only systems compete at the low end."),
]

FORCES["leaderdrive"] = [
    (RIV, "High", "Harmonic Drive Systems leads globally and Nabtesco dominates RV reducers; at home a long tail of "
     "makers (e.g. Laifual) competes on price."),
    (ENT, "High", "Humanoid-robot excitement has drawn many new reducer and actuator makers. Precision machining slows "
     "them down but does not keep them out."),
    (SUP, "Low", "Inputs are specialty steel, bearings and machine tools; Leaderdrive builds much of its own grinding "
     "equipment and does its own heat treatment."),
    (BUY, "High", "Robot makers (Estun, Inovance, Efort) and humanoid developers are price-sensitive and dual-source; "
     "large humanoid makers may integrate vertically."),
    (SUB, "Medium", "Planetary gears, cycloidal drives, roller screws and quasi-direct-drive actuators compete for "
     "humanoid joints, and actuator designs are not yet settled."),
]

FORCES["edge"] = [
    (RIV, "High", "Intuitive Surgical dominates globally; MicroPort MedBot, Shurui and Kangduo compete in China, and "
     "Medtronic (Hugo) and J&amp;J are entering."),
    (ENT, "Medium", "Regulatory approval and clinical evidence take years, but well-funded start-ups and medtech majors "
     "keep entering."),
    (SUP, "Medium", "Precision motors, optics and some electronics are imported or specialised; Edge's scale is still "
     "small."),
    (BUY, "High", "Hospitals buy through tenders and budget approvals; provincial pricing rules and possible "
     "volume-based procurement of instruments can cut consumable prices."),
    (SUB, "Medium", "Conventional laparoscopy and open surgery remain cheaper; robots must prove outcome and efficiency "
     "benefits to win share."),
]

FORCES["zai"] = [
    (RIV, "Very high", "DeepSeek, Alibaba's Qwen, ByteDance's Doubao, Moonshot, MiniMax, Baidu and Tencent compete; "
     "open-weight releases and price wars push API prices toward cost."),
    (ENT, "Medium", "Frontier training costs keep rising, limiting new labs to well-funded players, but open models "
     "lower the bar for application-layer rivals."),
    (SUP, "High", "GPUs, cloud capacity and AI talent are scarce; US export controls limit Nvidia supply, and Z.AI has "
     "been on the US Entity List since January 2025."),
    (BUY, "High", "Government and enterprise customers run competitive procurement; consumers switch freely; "
     "on-premise deployments need costly customisation."),
    (SUB, "High", "Free open-weight models (DeepSeek, Qwen) and in-house models at large platforms substitute for paid "
     "APIs."),
]

FORCES["minimax"] = [
    (RIV, "Very high", "Domestic model labs plus Kuaishou's Kling and ByteDance's Seedance in video, and Character.AI "
     "and others in AI companions."),
    (ENT, "Medium", "Frontier training is costly, but open models let app-layer start-ups launch competing products "
     "quickly."),
    (SUP, "High", "MiniMax rents much of its compute; US chip export controls and GPU scarcity raise costs and limit "
     "scale."),
    (BUY, "Medium", "Consumer subscribers (Talkie, Hailuo) are fragmented but price-sensitive; API developers switch "
     "models easily."),
    (SUB, "High", "Free apps from platforms with huge distribution (Doubao, Qwen) and open-weight models are close "
     "substitutes."),
]
