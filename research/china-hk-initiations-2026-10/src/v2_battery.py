"""v2 long-form content: CATL, Sungrow, Huayou Cobalt, Tianqi Lithium, Ganfeng Lithium."""

V2 = {}

V2["catl"] = dict(
    background=[
        "Contemporary Amperex Technology (CATL) was founded in December 2011 in Ningde, Fujian, by Robin Zeng (Zeng "
        "Yuqun) and colleagues from ATL, the consumer-battery maker they had built and sold to Japan's TDK. CATL took over "
        "ATL's nascent EV-battery team and won BMW as an early customer, which forced it to meet German quality standards "
        "from the start. When Beijing's EV subsidies and battery 'white list' favoured domestic suppliers in 2015–19, "
        "CATL scaled faster than any rival, and it has been the world's largest EV-battery supplier since 2017. SNE "
        "Research ranks it No.1 for nine consecutive years, with a 39.2% global share in 2025.",
        "CATL listed on Shenzhen's ChiNext board in 2018. In May 2025 it raised about HK$41bn in a Hong Kong listing, the "
        "year's largest global listing at the time, mainly to fund European capacity. Capacity reached 772GWh at end-2025, "
        "with 321GWh under construction. Plants are in China, Germany (Thuringia), Hungary (Debrecen), Spain (a joint "
        "venture with Stellantis) and Indonesia (an integrated mine-to-battery project). The founder-chairman remains "
        "the largest shareholder. In 2025 the US Department of Defense added CATL to its 1260H list of 'Chinese "
        "military companies', and US sourcing rules limit its direct presence in the US market. CATL has therefore "
        "developed a licensing model, under which Ford builds LFP cells in Michigan with CATL technology.",
    ],
    milestones=[
        ("2011", "Founded in Ningde by Robin Zeng and the ATL EV-battery team; BMW becomes an early customer."),
        ("2017", "Becomes the world's largest EV-battery supplier (SNE Research), a rank it has held since."),
        ("2018", "IPO on Shenzhen's ChiNext board (300750.SZ)."),
        ("2022", "First European plant (Thuringia) starts output; launches Qilin cell-to-pack battery."),
        ("2023", "Shenxing fast-charging LFP cell; technology-licensing deal with Ford (US)."),
        ("2025", "Hong Kong listing (~HK$41bn); sells 661GWh; net profit RMB72.2bn (+42%)."),
        ("2026", "Targets 1.2TWh of production; automakers add second-source suppliers."),
    ],
    ownership=[
        ("Largest shareholder", "Founder-chairman Robin Zeng; co-founders hold further large stakes"),
        ("Share classes", "A-share 300750.SZ; H-share 3750.HK (small float, ~41% premium to A)"),
        ("Capital returns", "~50% payout; buybacks under way (Sept 2026)"),
    ],
    business=[
        "CATL makes lithium-ion battery cells and packs. EV batteries were 69% of H1'26 revenue, energy-storage batteries "
        "19%, and materials, recycling and mining 7%. It supplies virtually every major global automaker other than BYD, "
        "including European premium brands and leading Chinese EV makers, and sells storage cells and containerised "
        "systems (TENER) to integrators and utilities. Contracts run for several years, with formula pricing that "
        "passes lithium, nickel and cobalt costs through with a lag. Margins therefore swing temporarily when raw "
        "material prices move sharply, but gross margin has stayed within 19–25% over the cycle.",
        "Its edge is cost and technology at scale. CATL buys more battery materials than anyone, runs highly automated "
        "plants at high utilisation (95% in Q2'26), and spends heavily on R&amp;D (RMB22bn in FY25). The product ladder "
        "spans fast-charging LFP (Shenxing), high-energy NCM cell-to-pack (Qilin), sodium-ion (Naxtra) and long-life "
        "storage cells, so it can serve mass-market and premium EVs and grid storage from one platform. Upstream stakes "
        "(lithium in Yichun, nickel in Indonesia) and recycling through Brunp reduce supply risk.",
        "CATL operates with negative working capital. Customers pay deposits and suppliers are paid on long terms "
        "(payables ~300 days of cost of sales at FY25), so the company takes in cash from working capital as it grows. "
        "Together with ~RMB290bn of net cash, this funds capacity expansion, overseas plants and a ~50% payout "
        "without leverage. New revenue streams include licensing (LRS), battery-swapping (Choco-swap) and "
        "materials sales to third parties.",
        "Growth is shifting toward storage and overseas. Storage revenue grew 87.5% in H1'26 as utilities and data "
        "centres add batteries, and overseas customers made up 31.5% of revenue. The main near-term challenge is "
        "domestic customer diversification: Li Auto, Xiaomi and Xpeng are adding second-source suppliers to gain "
        "pricing leverage.",
    ],
    segments_title="Revenue mix and economics (H1'26)",
    segments=[
        ("EV batteries", "69.4%", "Cells and packs for passenger, commercial vehicles; global OEMs",
         "Formula pricing; volume +55% in Q2'26"),
        ("Energy-storage batteries", "19.2%", "Storage cells and TENER systems for utilities, C&I, data centres",
         "Revenue +87.5% in H1'26; margins at least group average"),
        ("Materials, recycling, minerals", "6.8%", "Brunp recycling, precursors, lithium/nickel resources",
         "Cycle-sensitive; strategic supply security"),
        ("Other", "4.6%", "Licensing, swapping, services", "Small but growing; asset-light"),
    ],
    competition=[
        "The battery industry is highly concentrated at the top. CATL holds about 39% of global EV battery installations. "
        "BYD's FinDreams is a clear No.2, supplying mainly BYD vehicles but increasingly third parties. LG Energy "
        "Solution, Panasonic, Samsung SDI and SK On are the non-Chinese contenders, strongest in the US where Chinese "
        "cells face tariffs and sourcing rules. Second-tier Chinese makers (CALB, Gotion, EVE, Sunwoda, REPT) compete hard "
        "on price and are the main beneficiaries of automakers' dual-sourcing. In storage, EVE, Hithium, BYD and REPT "
        "have pushed cell prices to record lows.",
        "CATL's advantages are cost per kWh, quality record (important to automakers facing recall risk) and "
        "technology breadth. Its margins (~24–25% gross) remain well above second-tier Chinese peers and Korean makers, "
        "whose forward P/Es (LGES ~43x) reflect depressed earnings. The risks are a structural loss of share in China "
        "as OEMs diversify, and exclusion from the US market, which favours LGES, Panasonic and Samsung SDI there.",
    ],
    competitors=[
        ("BYD (FinDreams)", "China", "LFP Blade batteries; vertically integrated", "No.2 globally; mostly captive; strong cost position"),
        ("LG Energy Solution", "Korea", "NCM/LFP cells; US and EU plants", "Leading non-Chinese supplier; US policy advantage; low margins"),
        ("CALB / Gotion / EVE", "China", "EV and storage cells", "Price challengers; main winners from dual-sourcing"),
        ("Panasonic / Samsung SDI / SK On", "Japan / Korea", "Premium NCM cells; US plants",
         "Tesla/US OEM focus; sub-scale vs CATL"),
        ("Hithium / REPT", "China", "Storage cells", "Aggressive storage pricing; limited EV presence"),
    ],
    moat=[
        "The industry's largest purchasing and manufacturing scale; ~95% utilisation and best-in-class yields.",
        "Technology breadth (LFP, NCM, sodium-ion, storage) and a decade-long quality record with global OEMs.",
        "Negative working capital and ~RMB290bn of net cash fund growth and returns without leverage.",
        "Vulnerabilities: OEM dual-sourcing, US/EU policy barriers, price wars in storage.",
    ],
    tam=[
        "Global battery demand from EVs and stationary storage was roughly 2TWh in 2025; CATL's 661GWh of sales "
        "equates to about a third. China produced 1,069GWh in H1'26 alone (+53%), and storage-battery sales rose 83%. "
        "Industry forecasts point to 4–5TWh of global demand by 2030, about twice today's level. EV penetration keeps "
        "rising, commercial vehicles and ships are electrifying, and grid and data-centre storage are scaling quickly.",
        "At ~US$70–80/kWh for cells, the global market is already worth ~US$150bn a year and should keep growing in value "
        "despite price deflation. Storage is the fastest-growing segment and is less concentrated than EVs, so CATL "
        "has room to gain share there. Sodium-ion and solid-state chemistries could open new niches (cold-climate "
        "vehicles, low-cost storage, premium EVs), though they will also bring in new competitors.",
    ],
    tam_table=[
        ("EV + storage batteries", "~2TWh (2025); ~US$150bn", "4–5TWh by 2030 (industry forecasts)", "Our estimate; industry"),
        ("China battery output", "1,069GWh (H1'26)", "+53% YoY", "Industry data"),
        ("Stationary storage", "Fastest-growing segment", "China storage-battery sales +83% in H1'26", "Industry data"),
        ("CATL share", "39.2% of global EV batteries", "No.1 for nine years", "SNE Research"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue fell from RMB401bn (FY23) to RMB362bn (FY24) as lithium deflation cut selling "
        "prices, then recovered to RMB424bn (FY25) and RMB522bn TTM on volume. Gross margin rose from 19.1% (FY23) to "
        "25.1% (FY25), and operating profit grew from RMB51bn to RMB76bn. Net profit reached RMB72.2bn (FY25, +42%), a 17% "
        "net margin, and RMB43.3bn in H1'26 (+42%). We forecast revenue of RMB{rev26}bn/{rev27}bn/{rev28}bn and net "
        "profit of RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E, with gross margin of ~24%."),
    fin_bs=(
        "<b>Balance sheet.</b> Total assets reached RMB975bn at FY25 and RMB1.14tn at June 2026. Cash and short-term "
        "investments of RMB440bn exceed total debt of RMB149bn, leaving net cash of RMB{ncj26}bn (vs RMB{nc23}bn at FY23), "
        "about {ndeq25} of equity. Working capital is structurally negative: receivables equal {recvd25} days of sales "
        "and inventory {invd25} days (inventory rose to RMB131bn by June 2026 ahead of storage deliveries), but payables "
        "run at {apd25} days of cost of sales. Equity attributable rose to RMB337bn at FY25 (BVPS ~RMB74), including "
        "RMB39bn of H-share proceeds. The current ratio is {cr25}."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash flow rose from RMB92.8bn (FY23) to RMB133.2bn (FY25), {ocfnp25} net profit, "
        "because growth releases working capital. Capex of RMB31–42bn a year (~10% of revenue) left free cash flow of "
        "RMB{fcf23}bn, {fcf24}bn and {fcf25}bn over FY23–25, which funded RMB32.6bn of dividends and RMB4.4bn of "
        "buybacks in FY25. With capex stepping up to ~RMB60bn for the 1.2TWh plan, we forecast FCF of "
        "RMB{fcf26}bn/{fcf27}bn/{fcf28}bn, and net cash rising to ~RMB{nc28}bn by FY28E after dividends."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE has held steady at {roe23}–{roe25} even as a growing cash pile dilutes returns, "
        "and we expect ~{roe27} in FY27E. ROA is {roa25}. Excluding net cash, returns on operating capital are "
        "far higher, because working capital is negative. The FY25 payout ratio was {payout25}."),
)

V2["sungrow"] = dict(
    background=[
        "Sungrow Power Supply was founded in 1997 in Hefei, Anhui, by Cao Renxian, then an associate professor of power "
        "electronics at Hefei University of Technology, to make inverters for small wind and solar systems in rural "
        "China. It grew with China's solar industry and listed on Shenzhen's ChiNext board in 2011. Exports drove its "
        "rise to the front rank of global inverter suppliers. Sungrow and Huawei now consistently occupy the top two "
        "positions in Wood Mackenzie's global inverter rankings, with Sungrow holding about a quarter of global "
        "shipments by volume.",
        "Sungrow moved early into battery energy storage, integrating bought-in cells with its own power-conversion, "
        "control and thermal systems. Products such as the liquid-cooled PowerTitan let it win large utility projects in "
        "the Middle East, Europe, Australia and the Americas. Cumulative storage shipments passed 93GWh by end-2025, and "
        "storage overtook inverters as its largest segment that year. The founder remains the largest shareholder. "
        "Sungrow filed for a Hong Kong H-share listing in October 2025 and refiled in April 2026. It also develops solar "
        "and storage plants in China and makes EV motor drives and hydrogen electrolysers.",
    ],
    milestones=[
        ("1997", "Founded in Hefei by Cao Renxian, a power-electronics academic."),
        ("2011", "Lists on Shenzhen's ChiNext board (300274.SZ)."),
        ("2015–16", "Joins the top tier of global PV inverter suppliers by shipments."),
        ("2021–23", "Liquid-cooled PowerTitan storage systems; large utility projects in the Middle East and Europe."),
        ("2025", "Storage (43GWh, +54%) overtakes inverters; net profit RMB13.5bn; files for HK listing."),
        ("2026", "Refiles HK IPO (April); H1 revenue −29%; prices raised 5–15% from 20 September."),
    ],
    ownership=[
        ("Largest shareholder", "Founder Cao Renxian"),
        ("Share classes", "A-share 300274.SZ; Hong Kong H-share listing pending"),
        ("Dividend policy", "Payout ~25% of net profit (FY25 DPS RMB1.64)"),
    ],
    business=[
        "Sungrow has three businesses. Energy-storage systems (about 50% of H1'26 revenue) combine purchased lithium-iron-"
        "phosphate cells with Sungrow's own power-conversion systems, battery management, thermal management and "
        "energy-management software, delivered as containerised blocks for utility-scale, commercial and residential "
        "use. PV inverters and power electronics (about 40%) cover central and string inverters for utility plants and "
        "residential inverters sold through distributors. Renewable project development and other businesses (about "
        "10%) build and sell solar and storage plants in China and include EV drives and electrolysers.",
        "Sungrow earns its margin on power electronics. Cells are largely a pass-through cost, so the 2024–26 collapse in "
        "LFP cell prices widened storage margins even as selling prices fell. Group gross margin rose from 25.5% (FY23) "
        "to 35.9% in H1'26, and 38.6% in Q2. Overseas utility storage projects carry the richest margins; domestic "
        "solar and project development the thinnest. Overseas sales made up 73% of H1'26 revenue.",
        "Customers are utilities, independent power producers and EPC contractors for large projects, plus installers "
        "and distributors for residential products. Projects are lumpy and delivery-driven, so revenue swings with "
        "shipment timing. That, together with the slump in China's domestic solar market after the 2025 shift to "
        "market-based renewable tariffs, explains the 29% fall in H1'26 revenue. Working capital is large: "
        "inventory of RMB32bn at June 2026 reflects systems awaiting delivery, and receivables include project milestone "
        "payments.",
        "New growth avenues include data-centre power (solid-state transformers, HVDC), where Sungrow's power-"
        "electronics know-how is directly relevant, and grid-forming storage for weak grids.",
    ],
    segments_title="Revenue mix and economics (H1'26)",
    segments=[
        ("Energy-storage systems", "~50%", "PowerTitan/PowerStack utility & C&I systems; residential storage",
         "Highest-margin overseas; cell cost pass-through"),
        ("PV inverters & power electronics", "~40%", "Central, string and residential inverters", "Mature, ~30% gross margin range"),
        ("Project development & other", "~10%", "Solar/storage plant development in China; EV drives; hydrogen",
         "Lower margin; lumpy"),
    ],
    competition=[
        "In inverters, Huawei and Sungrow lead globally, followed by Ginlong (Solis), GoodWe, Sineng and TBEA in China "
        "and SMA, Enphase and SolarEdge in the West. Chinese makers dominate utility-scale and much of the residential "
        "market outside the US. Residential demand in Europe has been weak since 2024, which hit Western peers hardest. "
        "Sungrow's breadth (utility to residential) and bankability with utilities set it apart from smaller Chinese "
        "rivals.",
        "In storage integration, Tesla (Megapack) is the global leader. Sungrow sits in the top tier with BYD, Fluence, "
        "Hithium, Envision, Wärtsilä, Trina Storage and CATL's own system business. Competition is intense: "
        "battery makers are integrating forward and pushing system prices down. Sungrow's moat is power electronics "
        "and grid-integration capability (grid-forming, safety certification, long-term service), which buyers value for "
        "multi-hundred-MWh projects. Its weaknesses are dependence on bought-in cells and limited access to the US, "
        "where tariffs and foreign-entity-of-concern rules favour Tesla and Fluence.",
    ],
    competitors=[
        ("Huawei Digital Power", "China (private)", "Inverters; storage; data-centre power", "Inverter No.1; strong brand and tech"),
        ("Tesla Energy", "US", "Megapack utility storage", "Storage No.1; US policy advantage; in-house cells"),
        ("Ginlong / GoodWe", "China", "String and residential inverters", "Smaller; residential focus"),
        ("Fluence", "US", "Storage integration", "US-focused; thin margins (EV/sales ~0.6x)"),
        ("BYD / CATL / Hithium", "China", "Storage systems from cell makers", "Integrating forward; price pressure"),
    ],
    moat=[
        "In-house power electronics and grid-integration know-how across inverters and storage.",
        "Two decades of overseas channels, bankability and service with utilities and IPPs.",
        "Net cash and scale procurement of cells.",
        "Vulnerabilities: cell makers integrating forward; US access; China domestic solar slump.",
    ],
    tam=[
        "Stationary storage is the growth market. Utilities need batteries to absorb solar output and stabilise "
        "grids, commercial users buy them for peak shaving, and AI data centres need them for backup and power "
        "quality. China's storage-battery sales rose 83% in H1'26, and global grid-scale deployments are growing rapidly from a base of "
        "several hundred GWh a year. Sungrow's 43GWh of 2025 shipments suggests a high-single to low-double-digit share "
        "of global system deliveries.",
        "The solar-inverter market is larger in units but more mature. Global solar additions are running at several "
        "hundred GW a year, but China, the biggest market, has slowed since the 2025 pricing reform, and European "
        "residential demand is weak. Data-centre power electronics and grid-forming equipment are new adjacent markets. "
        "Policy risk is significant: US tariffs and sourcing rules effectively ring-fence much of the US market.",
    ],
    tam_table=[
        ("Stationary storage systems", "Several hundred GWh a year", "Rapid growth; China storage sales +83% (H1'26)",
         "Industry data; our estimate"),
        ("PV inverters", "Several hundred GW a year", "Mature; China slowing after 2025 reform", "Industry data"),
        ("Data-centre power electronics", "Emerging", "AI load growth", "Qualitative"),
        ("Sungrow position", "~25% of inverter volumes; 43GWh storage (2025)", "Top-two inverter; top-tier storage",
         "Wood Mackenzie; company"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue grew from RMB72.3bn (FY23) to RMB89.2bn (FY25), then fell to RMB76.6bn TTM. "
        "Gross margin has expanded every year, from 25.5% (FY23) to 30.5% (FY25), 30.9% TTM and 35.9% in H1'26, as "
        "storage mix and cheaper cells offset falling inverter prices. Net profit rose from RMB9.4bn to RMB13.5bn "
        "(FY25), a 15% net margin, but fell 32% in H1'26 to RMB5.3bn on lower volumes and FX losses. We forecast revenue "
        "of RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E."),
    fin_bs=(
        "<b>Balance sheet.</b> Total assets are RMB119bn (FY25), of which working capital is the largest component: "
        "receivables of RMB30.1bn ({recvd25} days of sales) and inventory of RMB27.3bn ({invd25} days), rising to RMB32bn "
        "in June 2026, partly funded by payables of RMB36.6bn ({apd25} days). Debt was cut from RMB14.2bn (FY24) to "
        "RMB7.2bn, so net cash rose from RMB{nc23}bn (FY23) to RMB{nc25}bn (FY25) and RMB{ncj26}bn (June 2026), ~{ndeq25} "
        "of equity. Equity attributable is RMB46.6bn (BVPS ~RMB23), and the current ratio is {cr25}."),
    fin_cf=(
        "<b>Cash flow.</b> Cash conversion has improved markedly: OCF rose from RMB7.0bn (FY23) to RMB16.9bn (FY25), "
        "{ocfnp25} net profit, and held at RMB17.2bn TTM despite the profit decline. Capex is light at RMB2.7–3.0bn a year "
        "(~{capexr25} of revenue), so FCF reached RMB{fcf25}bn in FY25 and RMB{fcfttm}bn TTM. Dividends rose to RMB4.4bn. "
        "We forecast FCF of RMB{fcf26}bn/{fcf27}bn/{fcf28}bn, lifting net cash to ~RMB{nc28}bn by FY28E before any "
        "H-share proceeds."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE has been very high ({roe23} in FY23, {roe25} in FY25) but is falling as profits dip "
        "and cash builds; we expect ~{roe27} in FY27E. ROA is {roa25}. Inventory days ({invd25}) are the ratio to watch: "
        "they will fall quickly if H2 storage deliveries accelerate. The FY25 payout ratio was {payout25}."),
)

V2["huayou"] = dict(
    background=[
        "Zhejiang Huayou Cobalt was founded in 2002 in Tongxiang, Zhejiang, by Chen Xuehua, who still chairs the company. "
        "It began as a cobalt refiner. Its early bet was to secure ore at the source: in the 2000s it built cobalt-copper "
        "mining and processing operations in the Democratic Republic of Congo, the world's dominant cobalt supplier. "
        "Huayou listed on the Shanghai Stock Exchange in 2015 and used the EV boom to move downstream into battery "
        "materials.",
        "From 2018, in partnership with Tsingshan, Huayou built high-pressure acid leaching (HPAL) plants in "
        "Indonesia that turn low-grade laterite nickel into mixed hydroxide precipitate "
        "(MHP) for batteries: Huayue (60ktpa) and Huafei (120ktpa) in the IMIP and IWIP industrial parks. A third "
        "project at Pomalaa with Vale and Ford (120ktpa) is starting up, and a fourth (Sorowako, with Vale) is planned. "
        "Huayou bought the Arcadia lithium mine in Zimbabwe and control of cathode maker Bamo in 2021. It also runs "
        "precursor and cathode joint ventures with Korean partners and a recycling arm, and has agreed to acquire "
        "Atlantic Lithium (Ghana). That makes it one of the most vertically integrated battery-materials groups in the "
        "world, and one of the most capital-intensive.",
    ],
    milestones=[
        ("2002", "Founded in Tongxiang, Zhejiang by Chen Xuehua as a cobalt refiner."),
        ("2000s", "Builds cobalt-copper mining and processing in the DRC."),
        ("2015", "Lists on the Shanghai Stock Exchange (603799.SH)."),
        ("2018–23", "Indonesian HPAL nickel with Tsingshan: Huayue (60ktpa), Huafei (120ktpa)."),
        ("2021", "Acquires Arcadia lithium (Zimbabwe) and control of cathode maker Bamo."),
        ("2025", "Record net profit of RMB6.1bn (+47%)."),
        ("2026", "Pomalaa HPAL (Vale, Ford) ramps; Huafei maintenance; agrees to buy Atlantic Lithium."),
    ],
    ownership=[
        ("Largest shareholder", "Founder-chairman Chen Xuehua and affiliates"),
        ("Main partners", "Tsingshan, Vale, Ford (Indonesia); Korean cathode/precursor JV partners"),
        ("Capital returns", "Buying back ~0.8% of shares; DPS RMB0.50"),
    ],
    business=[
        "Huayou earns money at each step from mine to cathode. Upstream, it mines cobalt and copper in the DRC and "
        "lithium in Zimbabwe, and processes Indonesian laterite nickel into MHP. Midstream, it refines nickel, cobalt and "
        "lithium into battery-grade chemicals. Downstream, it makes ternary (NCM) precursors and cathodes, and some "
        "LFP, for cell makers. Recycling feeds used battery metals back into the chain. In FY25, nickel products were RMB25.9bn of revenue, cathode "
        "materials RMB15.0bn, and nickel intermediates RMB11.8bn, with cobalt, copper, lithium, precursors and trading "
        "making up the rest.",
        "Upstream assets earn most of the profit. Indonesian HPAL produces nickel at among the lowest cash costs globally, and "
        "when nickel or cobalt prices rise, Huayou's mining and refining margins expand quickly. Processing earns "
        "steadier fees but thinner margins. Integration lowers cost and secures supply, but it also concentrates risk. "
        "Results depend on four commodity prices (nickel, cobalt, lithium, copper) and on input costs, notably sulfur and "
        "sulfuric acid for HPAL. Sulfur spikes forced maintenance at Huafei in 2026. Cobalt volumes are subject to DRC "
        "export quotas, and shipments fell 24% in H1'26.",
        "The model is capital-hungry. PP&amp;E has grown to RMB74bn, capex reached RMB16bn TTM for Pomalaa, and net debt "
        "is ~RMB54bn, about 3x EBITDA. Minority interests are sizeable because Indonesian projects are jointly owned. "
        "Customers are major Korean and Chinese cell makers. Many of the relationships are formalised in joint ventures, "
        "which give Huayou volume visibility but limit pricing power.",
    ],
    segments_title="FY25 revenue by product",
    segments_cols=("Product", "RMB bn / share", "What it is", "Economics"),
    segments=[
        ("Nickel products", "25.9 / 32%", "Battery-grade nickel sulfate and refined nickel", "Margin tied to nickel price; HPAL cost advantage"),
        ("Cathode materials", "15.0 / 18.5%", "NCM (and some LFP) cathodes via Bamo and JVs", "Processing fees; volume growth"),
        ("Nickel intermediates", "11.8 / 14.6%", "MHP from Indonesian HPAL", "Low cash cost; main profit driver"),
        ("Cobalt, copper, lithium, other", "28.3 / 34.9%", "DRC cobalt/copper; Zimbabwe lithium; precursors; trading",
         "Cobalt quota-dependent; lithium price-exposed"),
    ],
    competition=[
        "Huayou competes in several overlapping arenas. In Indonesian nickel, the main players are Tsingshan (its "
        "partner and the world's largest nickel producer), Nickel Industries, Harita (with Lygend), GEM and CNGR. Several "
        "of them are adding HPAL capacity, which Argus expects to nearly double Indonesian MHP capacity in 2026. In "
        "cobalt, CMOC is the world's largest producer and Glencore the other major. In precursors and cathodes, CNGR, GEM, "
        "Ronbay and Easpring are direct rivals.",
        "The structural problem is that LFP, which needs no nickel or cobalt, now accounts for roughly 80% of China's "
        "EV battery installations, so nickel-based cathodes are growing only in premium and overseas EVs. Huayou's "
        "response is to sell nickel to Korean and Western cell makers, add LFP and lithium, and lean on its cost "
        "advantage. Integration and low upstream cost are its competitive strengths; leverage, complexity and exposure "
        "to Indonesian policy (ore quotas and royalties) are its weaknesses.",
    ],
    competitors=[
        ("Tsingshan", "China (private)", "Indonesian nickel (NPI, HPAL), stainless", "World's largest nickel producer; partner and rival"),
        ("CMOC Group", "China", "Cobalt and copper (DRC)", "Cobalt No.1; lower leverage"),
        ("GEM / CNGR", "China", "Indonesian HPAL; precursors; recycling", "Direct precursor rivals; similar integration"),
        ("Harita / Lygend", "Indonesia / China", "HPAL nickel (Obi island)", "Low-cost MHP; capacity growth"),
        ("Glencore / Vale", "Switzerland / Brazil", "Nickel, cobalt, copper", "Western majors; Vale also a Huayou partner"),
    ],
    moat=[
        "Mine-to-cathode integration with low-cost Indonesian HPAL nickel.",
        "Long-term partnerships with Tsingshan, Vale, Ford and Korean cell makers.",
        "Scale in cobalt refining and a recycling loop.",
        "Vulnerabilities: commodity prices, LFP substitution, leverage and Indonesian/DRC policy.",
    ],
    tam=[
        "Huayou's markets are large but cyclical. Global nickel demand is ~3.5–3.7Mt a year (worth ~US$60bn at ~US$16.9k/t), "
        "driven by stainless steel with batteries the growth segment. Indonesia supplies more than half and is expanding "
        "further. Cobalt is a ~250–300kt market (mostly DRC), tightened by export quotas since 2025. Lithium is ~1.5Mt "
        "LCE and oversupplied in 2026.",
        "Downstream, cathode and precursor demand grows with EV and storage batteries, but nickel-based chemistries are "
        "losing share to LFP in China. Huayou's addressable market is therefore growing more slowly than the overall "
        "battery market. Its growth comes from Indonesian volume and from share gains with overseas cell makers; "
        "nickel intensity in batteries is not rising.",
    ],
    tam_table=[
        ("Nickel", "~3.5–3.7Mt / ~US$60bn", "Batteries growing; Indonesian oversupply", "Industry; our calc. at US$16.9k/t"),
        ("Indonesian MHP capacity", "862ktpa (2026E)", "Nearly double 2025", "Argus"),
        ("Cobalt", "~250–300kt", "Tighter on DRC export quotas", "Industry estimates"),
        ("Ternary cathode share (China EV)", "~20%", "Losing share to LFP (~80%)", "Industry data"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue moved from RMB66.3bn (FY23) to RMB60.9bn (FY24) on lower nickel and cobalt "
        "prices, then to RMB81.0bn (FY25, +33%) and RMB99.4bn TTM as Indonesian volumes ramped. Gross margin improved from "
        "13.6% to 17.4% (FY25) and 19.0% TTM, and operating profit doubled from RMB5.0bn to RMB9.7bn. Net profit rose 47% "
        "to RMB6.1bn in FY25. H1'26 net profit of RMB3.5bn (+29%) masks a sharp slowdown: Q1 earned RMB2.5bn, Q2 RMB1.0bn. "
        "We forecast revenue of RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of RMB{np26}bn/{np27}bn/{np28}bn."),
    fin_bs=(
        "<b>Balance sheet.</b> Total assets rose from RMB126bn (FY23) to RMB186bn (June 2026), a heavy base that "
        "includes PP&amp;E of RMB74bn and inventory of RMB32bn ({invd25} days of cost of sales at FY25, up from 100). "
        "Leverage is high: total debt is RMB75.8bn against cash of RMB22.0bn, giving net debt of RMB{ncj26}bn "
        "(RMB{nc25}bn at FY25), ~{ndeq25} of equity and {ndebitda25} EBITDA. The current ratio is below 1 ({cr25}). Equity attributable is "
        "RMB48.3bn (FY25; BVPS ~RMB26), and minority interests of RMB12.5bn reflect jointly owned Indonesian projects."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash flow is volatile and often below profit plus D&amp;A because of inventory "
        "build: RMB3.5bn, RMB12.4bn and RMB4.0bn over FY23–25 (OCF/net profit {ocfnp25} in FY25). Capex has been heavy "
        "(RMB16.8bn in FY23, RMB10.8bn in FY25, RMB16.2bn TTM), so free cash flow was negative in two of the last three "
        "years (FY25: −RMB{fcf25}bn; TTM −RMB{fcfttm}bn), funded by debt. We forecast FCF of −RMB{fcf26}bn in FY26E, "
        "turning positive at RMB{fcf27}bn/{fcf28}bn in FY27–28E as Pomalaa capex ends. Net debt only edges down to "
        "~RMB{nc28}bn by FY28E."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE improved from {roe23} (FY23) to {roe25} (FY25), and we expect ~{roe27} by FY27E: "
        "respectable, but earned with high leverage. ROA is only {roa25}. Net debt/EBITDA of {ndebitda25} and a current "
        "ratio below 1 are the main constraints; any further acquisitions (Atlantic Lithium) would delay deleveraging. "
        "Payout was {payout25} on FY25 EPS."),
)

V2["tianqi"] = dict(
    background=[
        "Tianqi Lithium traces its roots to the state-owned Shehong lithium-salt plant in Sichuan, set up in 1992. "
        "Entrepreneur Jiang Weiping took control in 2004, and the company listed in Shenzhen in 2010. In 2013 it "
        "acquired a controlling stake in Talison Lithium, owner of the Greenbushes mine in Western Australia, which is "
        "still its main asset. Greenbushes is the world's largest and highest-grade hard-rock lithium deposit, with "
        "Rockwood (now Albemarle) holding the remaining 49%.",
        "In 2018, at the top of the previous lithium cycle, Tianqi bought ~24% of Chile's SQM from Nutrien for ~US$4.1bn, "
        "largely with debt. When lithium prices collapsed in 2019–20, it faced a liquidity crisis. It restructured by "
        "selling 49% of its Australian holding company (which owns its Greenbushes interest and the Kwinana hydroxide "
        "plant) to IGO for ~US$1.4bn in 2021, and by listing H-shares in Hong Kong in July 2022, near the peak of the "
        "next upcycle. Profit hit RMB24.1bn in FY22 before another collapse produced a RMB7.9bn loss in FY24. The "
        "company today is leaner but still exposed: its effective Greenbushes interest is ~26%, Kwinana has "
        "under-performed, and Chile's Supreme Court rejected its challenge to SQM's partnership with Codelco.",
    ],
    milestones=[
        ("1992", "Shehong lithium-salt plant established in Sichuan (state-owned)."),
        ("2004 / 2010", "Jiang Weiping takes control; Shenzhen listing (002466.SZ)."),
        ("2013", "Acquires 51% of Talison (Greenbushes); Rockwood/Albemarle holds 49%."),
        ("2018", "Buys ~24% of SQM for ~US$4.1bn, largely debt-funded."),
        ("2021", "Sells 49% of its Australian holding company to IGO (~US$1.4bn) to deleverage."),
        ("2022", "Hong Kong listing (9696.HK); record net profit RMB24.1bn."),
        ("2024–26", "RMB7.9bn loss in FY24; H1'26 profit RMB4.2bn; H-share placement and CB."),
    ],
    ownership=[
        ("Controlling shareholder", "Jiang Weiping and family"),
        ("Main associates", "Greenbushes (~26% effective, with IGO and Albemarle); SQM (~22%)"),
        ("Share classes", "A-share 002466.SZ; H-share 9696.HK (~44% discount to A)"),
    ],
    business=[
        "Tianqi has three earnings streams. First, its share of Greenbushes mining profits. The mine sells spodumene "
        "concentrate to its two owners at market-linked prices, and Tianqi resells part of its share as concentrate "
        "(42% of H1'26 revenue). Second, conversion. Tianqi turns the rest into lithium carbonate and hydroxide at plants "
        "in Shehong (Sichuan), Zhangjiagang (Jiangsu) and Kwinana (Australia), and sells them to cathode and battery "
        "makers (58% of revenue). Third, equity income from its SQM stake, which taps Chile's low-cost Atacama brine.",
        "Mining generates most of the profit. Greenbushes delivered a 74% mining gross margin in H1'26, and its cash cost sits in "
        "the bottom quartile of the industry. Conversion margins are thinner and volatile. Because Tianqi buys "
        "concentrate at lagged market prices and sells chemicals at spot, falling prices can generate inventory "
        "losses, as in FY24. Kwinana, Australia's first lithium hydroxide plant, has struggled with commissioning and "
        "ran at ~15% of nameplate in the June 2026 quarter.",
        "Earnings are almost entirely a function of the lithium price, volumes at Greenbushes (where the CGP3 "
        "expansion was interrupted by a fire in June 2026), and SQM's results. Development projects include the "
        "Cuola spodumene mine in Sichuan. The balance sheet has been repaired since 2021, but the A-share and H-share "
        "valuations differ widely (H at a ~44% discount).",
    ],
    segments_title="Revenue mix and economics (H1'26)",
    segments=[
        ("Lithium chemicals", "58%", "Carbonate and hydroxide from Sichuan, Jiangsu and Kwinana plants",
         "Conversion margin; inventory-lag risk"),
        ("Lithium concentrate", "42%", "Spodumene from Greenbushes (~26% effective interest)", "74% gross margin in H1'26"),
        ("Equity income (not in revenue)", "–", "~22% of SQM (Chile brine); associates", "Lithium-price driven"),
    ],
    competition=[
        "Lithium supply is split between hard-rock spodumene (Australia, Africa, China) and brine (Chile, Argentina, "
        "China's Qinghai and Tibet), with lepidolite in Jiangxi as a high-cost swing source. Tianqi's peers include "
        "Albemarle (its Greenbushes partner), SQM, Pilbara Minerals, Mineral Resources and Rio Tinto (which bought "
        "Arcadium). In China its rivals are Ganfeng, Yahua, Zangge, Sinomine and battery makers that have integrated "
        "upstream, such as CATL in Yichun.",
        "Producers are price-takers, so their returns depend on cost position. Greenbushes is among the lowest-cost sources "
        "worldwide, which protects Tianqi in downturns and gives it high leverage in upturns. Its relative weaknesses "
        "are a minority position in its main asset (Albemarle and IGO are co-owners), under-performing downstream "
        "conversion, and limited growth projects of its own compared with Ganfeng or Pilbara. African supply "
        "(Zimbabwe, Mali, Ghana) and Chinese lepidolite restarts are the marginal tonnes that set prices.",
    ],
    competitors=[
        ("Albemarle", "US", "Greenbushes (49%), Chile brine, conversion", "Largest Western producer; co-owner of Greenbushes"),
        ("SQM", "Chile", "Atacama brine (with Codelco from 2025)", "Lowest-cost brine; Tianqi owns ~22%"),
        ("Pilbara Minerals", "Australia", "Pilgangoora spodumene", "Pure-play hard rock; growth projects"),
        ("Ganfeng Lithium", "China", "Diversified resources, chemicals, batteries", "More diversified; higher debt"),
        ("Zangge / Yahua / CATL (Yichun)", "China", "Brine, conversion, lepidolite", "Domestic cost-curve swing supply"),
    ],
    moat=[
        "Interest in Greenbushes, the world's largest high-grade hard-rock lithium mine (bottom-quartile cost).",
        "Exposure to SQM's low-cost Atacama brine through its ~22% stake.",
        "Repaired balance sheet (net debt ~RMB6bn at June 2026).",
        "Vulnerabilities: price-taker economics, Kwinana under-performance, minority position in its main assets.",
    ],
    tam=[
        "The lithium market is driven by batteries. We estimate demand of ~1.5Mt LCE in 2026, growing 20–25% a year with "
        "EVs and storage. At China's spot price of RMB122k/t (~US$18k/t), the market is worth roughly US$27bn. Prices "
        "fell 24% in September as Wood Mackenzie forecast 2026 supply growth of ~28%, and as a revised SMM inventory "
        "methodology added ~175kt to China's stock estimates. Prices are nonetheless still ~66% higher than a year ago.",
        "Over the long run, demand growth looks secure, but supply responds quickly when prices rise: African "
        "spodumene, Chinese lepidolite and Argentine brine can add tonnes within 1–3 years. Tianqi's earnings "
        "therefore track the lithium price more than market growth. On our estimates, each RMB10k/t move in price "
        "changes annual net profit by roughly RMB0.7–0.9bn.",
    ],
    tam_table=[
        ("Lithium demand (LCE)", "~1.5Mt / ~US$27bn (2026E)", "+20–25% a year", "Our estimate"),
        ("Lithium supply", "–", "+27.9% in 2026", "Wood Mackenzie"),
        ("China lithium carbonate", "RMB122,350/t (9 Oct 2026)", "+66% YoY; −24% in Sept", "Trading Economics/SMM"),
        ("Tianqi sensitivity", "~RMB0.7–0.9bn net profit per RMB10k/t", "–", "Our estimate"),
    ],
    fin_is=(
        "<b>Income statement.</b> Tianqi's P&amp;L follows the lithium price. Revenue fell from RMB40.5bn (FY23) to "
        "RMB13.1bn (FY24) and RMB10.3bn (FY25) before rebounding to RMB17.8bn TTM. Gross margin swung from 83% to 37% "
        "and back to 57% TTM. Net profit went from RMB7.3bn (FY23) to a RMB7.9bn loss (FY24, inventory write-downs and "
        "impairments), RMB0.46bn (FY25) and RMB4.2bn in H1'26 alone. We forecast net profit of RMB{np26}bn/{np27}bn/{np28}bn "
        "for FY26–28E on lithium carbonate averaging ~RMB130k/t in 2026 and ~RMB110k/t in 2027."),
    fin_bs=(
        "<b>Balance sheet.</b> Total assets are RMB83bn (June 2026). About half are long-term investments: the SQM stake "
        "and Greenbushes-related assets. PP&amp;E is RMB22bn. Debt rose from RMB11.8bn (FY23) to RMB17.5bn, but cash "
        "recovered to RMB11.8bn after the 2026 H-share placement, so net debt fell from RMB{nc25}bn (FY25) to "
        "RMB{ncj26}bn (June 2026), ~{ndeq25} of equity at FY25. Liquidity is strong (current ratio {cr25}). Equity "
        "attributable is RMB48.3bn (BVPS ~RMB28, A-share P/B ~1.1x, H-share ~0.6x). Minority interests (RMB11.1bn) "
        "represent IGO's share of the Australian holding company."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash flow collapsed from RMB22.7bn (FY23) to RMB5.6bn (FY24) and RMB3.0bn (FY25). "
        "With capex of RMB3.6–4.5bn a year, free cash flow fell from RMB{fcf23}bn to roughly break-even (FY25: "
        "−RMB{fcf25}bn), and dividends were cut from RMB5.6bn to RMB0.75bn. The H-share placement added ~RMB2.6bn of "
        "equity in 2026. We forecast FCF of RMB{fcf26}bn/{fcf27}bn/{fcf28}bn as H1'26 profits turn into cash, taking the "
        "company to roughly net-cash neutral by FY28E."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE swung from {roe23} (FY23) to {roe24} (FY24) and {roe25} (FY25); we expect {roe26} in "
        "FY26E, easing to ~{roe27}. Asset turnover is very low (0.15x in FY25) because of the SQM stake. Net debt/EBITDA "
        "was {ndebitda25} at FY25 but falls below 1x on TTM EBITDA (~RMB10.5bn). Receivable and inventory days rose in "
        "FY25 ({recvd25} and {invd25})."),
)

V2["ganfeng"] = dict(
    background=[
        "Ganfeng Lithium was founded in 2000 in Xinyu, Jiangxi, by Li Liangbin (chairman) and Wang Xiaoshen. It started "
        "as a maker of lithium metal and specialty lithium compounds, and it remains the world's largest lithium-metal "
        "producer, a material used in pharmaceuticals, alloys and next-generation batteries. It listed in Shenzhen in "
        "2010 and in Hong Kong in 2018, and used both markets to fund a decade of resource acquisitions.",
        "Ganfeng built one of the most diversified lithium resource portfolios worldwide. It holds Mt Marion spodumene "
        "in Australia (with Mineral Resources), the Cauchari-Olaroz brine in Argentina (with Lithium Argentina; first "
        "production in 2023), the Mariana brine (Argentina), the Goulamina spodumene mine in Mali (fully owned after "
        "buying out Leo Lithium in 2024; production from late 2024), and lepidolite and brine assets in China. Some bets "
        "have run into trouble: Mexico revoked its Sonora lithium-clay concessions in 2023, and Mali's military government has "
        "tightened mining rules. In parallel, Ganfeng LiEnergy has grown into a sizeable battery business making "
        "consumer cells, storage systems and power batteries. It is one of China's leading developers of solid-state "
        "batteries, with 400Wh/kg cells validated and 500Wh/kg cells in small-batch production in 2026.",
    ],
    milestones=[
        ("2000", "Founded in Xinyu, Jiangxi; starts with lithium metal and compounds."),
        ("2010 / 2018", "Shenzhen listing (002460.SZ); Hong Kong listing (1772.HK)."),
        ("2015–17", "Secures Mt Marion (Australia) and Cauchari-Olaroz (Argentina) interests."),
        ("2023", "Cauchari-Olaroz produces first carbonate; Mexico revokes Sonora concessions."),
        ("2024", "Takes full control of Goulamina (Mali); first spodumene; FY24 loss RMB2.1bn."),
        ("2026", "400Wh/kg solid-state cell validated; 500Wh/kg small-batch production; H1 profit RMB4.3bn."),
    ],
    ownership=[
        ("Founders", "Li Liangbin (chairman) and Wang Xiaoshen are the largest shareholders"),
        ("Share classes", "A-share 002460.SZ; H-share 1772.HK (~45% discount to A)"),
        ("Battery subsidiary", "Ganfeng LiEnergy (consumer, storage, power and solid-state cells)"),
    ],
    business=[
        "Ganfeng has two businesses. The lithium business (RMB14.2bn, 62% of H1'26 revenue) mines and buys spodumene, "
        "brine and lepidolite and converts it into lithium carbonate, hydroxide, chloride, metal and organolithium "
        "compounds for cathode, battery, pharmaceutical and industrial customers. It earns a conversion margin on "
        "everything it processes and a mining margin on the share it mines itself. Self-sufficiency is rising as "
        "Goulamina, Mariana and Cauchari-Olaroz ramp.",
        "The battery business (RMB7.8bn, 34% of revenue; about 20GWh in H1'26) makes small-format consumer cells (1.5m "
        "cells a day across two bases), storage cells and 5MWh containerised systems, and power batteries for "
        "commercial vehicles and two-wheelers. Margins are lower than in lithium at the top of the cycle but more "
        "stable, and the business gives Ganfeng a captive outlet for its lithium. The solid-state programme (lithium-"
        "metal anodes, sulfide electrolytes) targets premium EVs, eVTOLs and robots; it is strategically important "
        "but does not yet earn revenue at scale.",
        "Economically, Ganfeng is more diversified than Tianqi but has a higher-cost, more geopolitically exposed "
        "resource base and more debt. FY25 gross margin was only 14.6%, recovering to 31.2% in H1'26. Heavy "
        "development capex in Mali and Argentina (RMB7–9bn a year over FY23–25) pushed net debt to ~RMB29bn. Recycling "
        "and lithium-sulfide supply for solid-state electrolytes add smaller revenue streams.",
    ],
    segments_title="Revenue mix and economics (H1'26)",
    segments=[
        ("Lithium products", "62% (RMB14.2bn)", "Carbonate, hydroxide, metal, compounds; own mines in Mali, Argentina, Australia",
         "Price-driven; rising self-sufficiency"),
        ("Batteries", "34% (RMB7.8bn)", "Consumer cells, storage systems, power batteries (~20GWh)", "Lower, steadier margins"),
        ("Other", "4%", "Recycling, materials", "Small"),
    ],
    competition=[
        "In lithium chemicals Ganfeng competes with Tianqi, Albemarle, SQM, Rio Tinto (Arcadium), Yahua and Zangge, and "
        "with integrated battery makers such as CATL. Its scale and product breadth (especially lithium metal and "
        "specialty compounds) are distinctive. Its resource portfolio is diversified but on average higher-cost than "
        "Greenbushes, and it carries more country risk.",
        "In batteries, Ganfeng is a mid-sized player competing with CATL, BYD, EVE, Gotion and many smaller firms for "
        "storage and consumer cells. Ganfeng's edge is upstream integration and its solid-state technology, where it "
        "is among China's leaders alongside CATL, WeLion and QingTao. The risk is that storage price wars compress "
        "margins before scale benefits arrive.",
    ],
    competitors=[
        ("Tianqi Lithium", "China", "Greenbushes interest, conversion, SQM stake", "Lower-cost resource; less diversified"),
        ("Albemarle / SQM", "US / Chile", "Hard rock and brine; conversion", "Global incumbents; SQM lowest cost"),
        ("Rio Tinto (Arcadium)", "UK/Australia", "Argentina brine, Australian/Canadian hard rock", "Major's balance sheet; long-term builder"),
        ("CATL / EVE", "China", "Batteries; CATL also upstream lithium", "Battery scale leaders"),
        ("WeLion / QingTao", "China", "Solid-state batteries", "Rivals in next-generation cells"),
    ],
    moat=[
        "Broadest lithium product range (metal, compounds) and diversified global resources.",
        "Captive battery business and leadership in solid-state development.",
        "Long relationships with global cathode and battery customers.",
        "Vulnerabilities: higher-cost/riskier resources (Mali, Argentina), net debt ~RMB27–29bn, price-taker economics.",
    ],
    tam=[
        "Ganfeng shares Tianqi's lithium market, ~1.5Mt LCE (~US$27bn) in 2026 on our estimates, growing 20–25% a "
        "year in demand but oversupplied near term. Management itself now expects a balanced market in 2027 with "
        "20–25% supply growth, a retreat from its earlier view of prices above RMB200k/t.",
        "The battery arm opens additional markets: storage (China storage-battery sales +83% in H1'26), consumer cells, "
        "and potentially solid-state batteries for premium EVs, eVTOLs and humanoid robots. These have much larger "
        "revenue pools than lithium chemicals, but Ganfeng is a small participant today.",
    ],
    tam_table=[
        ("Lithium demand (LCE)", "~1.5Mt / ~US$27bn (2026E)", "Supply +20–25% into 2027 (mgmt)", "Our estimate; company"),
        ("Storage batteries", "Fast-growing", "China sales +83% (H1'26)", "Industry data"),
        ("Solid-state batteries", "Pre-commercial", "Small-batch 500Wh/kg cells (2026)", "Company"),
        ("Ganfeng battery output", "~20GWh (H1'26)", "Growing", "UOB Kay Hian"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue fell from RMB33.0bn (FY23) to RMB18.9bn (FY24), with a RMB2.1bn loss, then "
        "recovered to RMB23.1bn and a RMB1.6bn profit in FY25 and RMB37.8bn TTM. FY23 profit (RMB4.9bn) was flattered "
        "by investment gains; operating profit was only RMB0.4bn. Gross margin troughed at ~9% in FY23–24, then recovered "
        "to 14.6% (FY25) and 31.2% in H1'26, when net profit reached RMB4.3bn. We forecast revenue of "
        "RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of RMB{np26}bn/{np27}bn/{np28}bn, below UOB's RMB9.2bn for "
        "FY26E."),
    fin_bs=(
        "<b>Balance sheet.</b> Total assets grew from RMB92bn (FY23) to RMB122bn (June 2026), driven by PP&amp;E "
        "(RMB37.6bn) for Mali and Argentina and by working capital. Inventory reached RMB15.2bn and receivables RMB12.7bn "
        "(FY25: {invd25} and {recvd25} days). Debt rose from RMB27.6bn to RMB40.1bn, so net debt is RMB{ncj26}bn (June "
        "2026), ~{ndeq25} of FY25 equity and {ndebitda25} FY25 EBITDA. The current ratio is {cr25}. Equity attributable is "
        "RMB48.2bn (BVPS ~RMB23; H-share P/B ~1.0x)."),
    fin_cf=(
        "<b>Cash flow.</b> Ganfeng has burned cash for three years. OCF was RMB0.1bn, RMB5.2bn and RMB2.9bn over FY23–25, "
        "against capex of RMB8.6bn, 9.2bn and 7.4bn, so FCF was negative each year (FY25 −RMB{fcf25}bn), funded by debt "
        "and a RMB2.3bn equity raise. TTM FCF improved to −RMB{fcfttm}bn as capex fell. We forecast FCF of "
        "−RMB{fcf26}bn in FY26E, then RMB{fcf27}bn/{fcf28}bn as capex normalises at ~RMB5bn, trimming net debt to "
        "~RMB{nc28}bn by FY28E."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE was {roe23}, {roe24} and {roe25} over FY23–25; we expect {roe26} in FY26E and ~{roe27} "
        "thereafter. ROA is low ({roa25} in FY25) because of the large asset base. Net debt/EBITDA of {ndebitda25} (FY25) "
        "is the main risk metric, though it falls to ~3x on TTM EBITDA. Inventory days ({invd25}) are elevated."),
)
