"""v2 long-form content: Zijin Mining, Sany Heavy, Sieyuan Electric.

Fields: background, milestones, ownership, business, segments(+segments_title/cols), competition, competitors, moat,
tam, tam_table, fin_is, fin_bs, fin_cf, fin_ratios.  Placeholders ({fcf25}, {roe25}, ...) are filled by build.py.
"""

V2 = {}

V2["zijin"] = dict(
    background=[
        "Zijin Mining grew out of the Zijinshan gold-copper deposit in Shanghang county, western Fujian, a low-grade "
        "orebody that state geologists had explored in the 1980s and that larger operators considered uneconomic. The "
        "company was formally established in 1993. Under geologist Chen Jinghe it pioneered large-scale heap leaching of "
        "low-grade ore, and Zijinshan became one of China's largest gold mines. That early experience shaped a culture "
        "that still defines the group: buy or develop deposits others overlook, then lower their cost through in-house "
        "geology, mining and metallurgical engineering. The company became a joint-stock company in 2000, listed H-shares "
        "in Hong Kong in 2003 and A-shares in Shanghai in 2008. Its largest shareholder is Minxi Xinghang, the investment "
        "vehicle of the Shanghang county government.",
        "Overseas expansion began in the mid-2000s and accelerated after 2015 through counter-cyclical acquisitions bought "
        "when sellers were under pressure. These included a 49.5% stake in Ivanhoe's Kamoa-Kakula copper project in the "
        "DRC, Nevsun (owner of the Timok project) and the RTB Bor complex in Serbia, Continental Gold's Buriticá mine in "
        "Colombia, Guyana Goldfields, Neo Lithium's 3Q brine in Argentina, and Rosebel in Suriname. At home, the Julong "
        "copper project in Tibet became a growth engine. In 2025 the group spun its overseas gold assets into Zijin Gold "
        "International, listed in Hong Kong, which it still controls. Zijin now operates on five continents and targets a "
        "global top-three position in both gold and copper by 2028.",
    ],
    milestones=[
        ("1993", "Company established to develop the Zijinshan gold-copper deposit in Fujian."),
        ("2003 / 2008", "H-share listing in Hong Kong; A-share listing in Shanghai."),
        ("2015", "Acquires 49.5% of Kamoa Holding (Kamoa-Kakula copper, DRC) from Ivanhoe."),
        ("2018", "Buys Nevsun (Timok, Serbia) and 63% of RTB Bor, Serbia's state copper complex."),
        ("2019–23", "Adds Buriticá (Colombia), Guyana Goldfields, 3Q lithium (Argentina), Rosebel (Suriname)."),
        ("2025", "Lists Zijin Gold International in Hong Kong; net profit RMB51.8bn (+62%)."),
        ("2026", "Three-year plan: 130–140t gold and 1.5–1.6Mt copper by 2028; lithium up to 320kt LCE."),
    ],
    ownership=[
        ("Largest shareholder", "Minxi Xinghang State-owned Assets Investment (Shanghang county), ~23%"),
        ("Share classes", "A-share 601899.SH; H-share 2899.HK"),
        ("Key listed subsidiary", "Zijin Gold International (2259.HK): overseas gold assets"),
        ("Dividend policy", "Target payout of ~35% of net profit"),
    ],
    business=[
        "Zijin is an integrated miner. It owns and operates mines, processes ore into concentrate, doré or cathode, and "
        "runs smelting and refining plants that also treat third-party material. Revenue therefore mixes two very "
        "different businesses. Self-mined gold, copper, zinc, silver and lithium carry high margins and generate the "
        "large majority of gross profit. Refining and trading of purchased material (about 19% of H1'26 revenue) adds "
        "volume but earns thin margins. The jump in group gross margin from 15.8% in FY23 to 34.6% on a TTM basis "
        "reflects both higher metal prices and a rising share of self-mined output.",
        "Its competitive edge is cost and capital efficiency. Zijin's in-house exploration teams, mine designers and "
        "metallurgists let it value deposits independently, build mines with its own engineering arm, and run "
        "difficult or low-grade orebodies profitably. Management describes this as an integrated 'ore-flow' model "
        "linking geology, mining, processing and refining. The company is willing to operate in frontier jurisdictions "
        "such as the DRC, Serbia, Colombia, Suriname and Tibet, where Western majors often hesitate, and Chinese "
        "policy-bank and bond-market funding lowers its cost of capital.",
        "Copper is the strategic priority. Mined copper was 1.09Mt in 2025 and is targeted at 1.2Mt in 2026 and "
        "1.5–1.6Mt by 2028, led by Julong (Tibet), the Serbian operations and Kolwezi (DRC). Zijin's ~40% interest in "
        "Kamoa-Kakula is equity-accounted, so its profits appear as investment income rather than revenue. Gold output "
        "(~90t in 2025) is growing toward 105t in 2026 and 130–140t by 2028. Lithium (3Q in Argentina, Lakkor Tso in "
        "Tibet, Manono North-East in the DRC and hard rock in Hunan) is the third leg, with output up ~5x in H1'26 but "
        "exposed to the 2026 lithium-price slide.",
        "Capital allocation balances three uses: RMB25–35bn a year of capex on organic growth, opportunistic M&A "
        "(RMB15bn of acquisitions in FY25), and a payout target of ~35%. Large minority interests (RMB62bn at FY25) "
        "reflect partly owned mines and Zijin Gold International's outside shareholders.",
    ],
    segments_title="Revenue mix and economics (H1'26)",
    segments=[
        ("Gold (mined + refined)", "41.2%", "Mines in China, Colombia, Suriname, Guyana, Australia, Kazakhstan; "
         "refining of doré", "Highest margin at current prices; overseas mines via Zijin Gold International"),
        ("Copper", "32.6%", "Julong (Tibet), Bor/Čukaru Peki (Serbia), Kolwezi (DRC), Duobaoshan (Heilongjiang)",
         "1.09Mt mined in 2025; Kamoa-Kakula equity-accounted"),
        ("Refining, trading & other", "19.0%", "Smelting and refining of third-party concentrate; metals trading",
         "Low single-digit margins; inflates revenue"),
        ("Zinc/lead and silver", "5.0%", "Polymetallic mines and by-products", "Small, high-margin by-products"),
        ("Lithium", "2.2%", "3Q brine (Argentina), Lakkor Tso (Tibet), Manono NE (DRC), Hunan",
         "Ramping up; exposed to falling lithium prices"),
    ],
    competition=[
        "Mining is a price-taking business, so competition is about cost position, reserve life and the ability to grow "
        "volumes. In copper, Zijin's 1.09Mt places it among the top five global producers alongside Freeport-McMoRan, BHP "
        "and Codelco; in gold its ~90t (~2.9Moz) ranks it in the global top ten behind Newmont, Barrick and Agnico Eagle. "
        "Few of those peers are growing. Western majors face declining grades, permitting delays and shareholder "
        "pressure to return cash rather than build. Zijin's copper output is planned to rise by ~40–50% by 2028.",
        "Its main competitive disadvantages are jurisdictional and reputational. Several key assets sit in countries "
        "with resource nationalism (DRC export rules, Serbian environmental scrutiny, Colombian security), and Chinese "
        "ownership can complicate approvals in OECD markets. Domestically, CMOC (copper/cobalt in the DRC) is the closest "
        "comparable and a rival for African assets; Shandong Gold and Zhaojin are larger domestic gold peers by reserves "
        "in China but have little overseas growth.",
    ],
    competitors=[
        ("Freeport-McMoRan", "US", "Copper (Grasberg, Americas), gold by-product",
         "Larger copper producer; slower growth; premium valuation"),
        ("BHP / Codelco", "Australia / Chile", "Copper (Escondida; Chilean state mines)",
         "Scale leaders; flat volumes; Codelco constrained by grades"),
        ("Newmont / Barrick", "US / Canada", "Gold (plus copper at Barrick)",
         "Bigger gold output; mature portfolios; higher payouts"),
        ("CMOC Group", "China", "Copper and cobalt (DRC), molybdenum",
         "Closest Chinese peer; competes for African assets"),
        ("Shandong Gold / Zhaojin", "China", "Domestic gold mining", "Strong local reserves; limited overseas growth"),
    ],
    moat=[
        "Low-cost, long-life orebodies plus in-house exploration and engineering that cut capital intensity.",
        "Willingness and ability to operate in frontier jurisdictions with state-bank and bond-market funding.",
        "A visible volume-growth pipeline (copper +40–50% by 2028) that few peers can match.",
        "Vulnerabilities: geopolitical, permitting and ESG risk; acquisitions bought near cycle highs.",
    ],
    tam=[
        "Zijin's addressable market is the global supply of mined copper, gold and lithium. Refined copper consumption "
        "runs at about 27Mt a year, worth ~US$400bn at the current COMEX price of ~US$6.77/lb (~US$14,900/t). Demand is "
        "growing at 2–3% a year from electrification, grids, renewables and AI data centres, while mine supply is "
        "constrained by falling grades and a decade of under-investment. That supports a structural deficit narrative "
        "and high prices.",
        "Annual gold mine supply of ~3,600t is worth ~US$485bn at US$4,195/oz. Supply is broadly flat, and central-bank "
        "buying and ETF inflows have driven prices. Lithium is a smaller (~1.5Mt LCE, ~US$27bn) but faster-growing market "
        "that is currently oversupplied. Zijin's 2026 targets equal roughly 4–5% of world copper and ~3% of world gold "
        "mine supply, so growth comes from volume, not share of a fixed pie.",
    ],
    tam_table=[
        ("Refined copper", "~27Mt / ~US$400bn", "Volume +2–3% a year; deficit risk from grade decline",
         "Industry estimates; our calc. at US$14.9k/t"),
        ("Gold mine supply", "~3,600t / ~US$485bn", "Flat supply; price set by central-bank and ETF demand",
         "Industry estimates; our calc. at US$4,195/oz"),
        ("Lithium (LCE)", "~1.5Mt / ~US$27bn", "Demand +20–25% a year; supply +28% in 2026",
         "Wood Mackenzie; our estimate"),
        ("Zijin share", "~4–5% copper; ~3% gold", "Targets top-three in both by 2028", "Company plan (Feb 2026)"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue rose from RMB293bn (FY23) to RMB349bn (FY25, +15%) and RMB376bn TTM, but the "
        "real story is margin. Gross margin expanded from 15.8% to 27.7% in FY25 and 34.6% TTM, and operating profit more "
        "than doubled from RMB31.6bn to RMB75.0bn as gold and copper prices rose and self-mined volumes grew. Net profit "
        "attributable rose 2.5x in two years to RMB51.8bn (14.8% net margin). H1'26 brought RMB39.2bn (+68%). We forecast "
        "net profit of RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E, driven by volume growth with flat-to-slightly-lower "
        "metal prices, which keeps net margin around 20–22%."),
    fin_bs=(
        "<b>Balance sheet.</b> Total assets grew from RMB343bn to RMB512bn over FY23–25, led by PP&amp;E (RMB165bn) and "
        "mining rights, as new mines were built and acquired. Leverage has fallen fast. Net debt dropped from "
        "RMB{nc23}bn (FY23) to RMB{nc25}bn (FY25) and RMB{ncj26}bn at June 2026, taking net debt/equity from ~109% to "
        "{ndeq25} and net debt/EBITDA to {ndebitda25}. Liquidity is adequate (current ratio {cr25}) with RMB111bn of cash "
        "and short-term investments at June 2026 against RMB165bn of debt, much of it long-term. Minority interests "
        "(RMB62bn) are large, so investors should focus on attributable figures. Inventory days have drifted up to "
        "{invd25} as lithium and concentrate stocks build."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash flow doubled from RMB36.9bn (FY23) to RMB75.4bn (FY25) and RMB102bn TTM, "
        "comfortably above net profit (OCF/net profit {ocfnp25} in FY25) thanks to RMB16bn of D&amp;A. Capex has run at "
        "RMB25–34bn a year (8–10% of revenue), so free cash flow rose from RMB{fcf23}bn to RMB{fcf25}bn and RMB{fcfttm}bn "
        "TTM. That funded RMB17.8bn of dividends and RMB15.4bn of acquisitions in FY25 while still cutting net debt. We "
        "forecast FCF of RMB{fcf26}bn/{fcf27}bn/{fcf28}bn after capex of RMB36–38bn a year. On those numbers Zijin "
        "moves to a net cash position of ~RMB{nc28}bn by FY28E, before any acquisitions."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE has climbed from {roe23} (FY23) to {roe25} (FY25) and should peak around {roe26} in "
        "FY26E before easing as equity builds. ROA of {roa25} is high for a miner. Asset turnover is falling (larger, "
        "capital-heavy asset base), while receivable days are short ({recvd25} days) because metals are sold for cash. The "
        "payout ratio of {payout25} on FY25 EPS leaves room to raise dividends toward the 35% target."),
)

V2["sany"] = dict(
    background=[
        "Sany was founded in 1989 in Lianyuan, Hunan, by Liang Wengen and three partners (Tang Xiuguo, Mao Zhongwu and "
        "Yuan Jinhua) as a welding-materials business. In the 1990s it moved to Changsha and into construction machinery, "
        "starting with truck-mounted concrete pumps, a market then dominated by imported German and Japanese equipment. "
        "It won share by selling reliable machines at lower prices, backed by fast service. It then broadened into "
        "excavators, crawler and truck cranes, rotary piling rigs and road machinery.",
        "Sany Heavy Industry listed on the Shanghai Stock Exchange in 2003. It became China's best-selling excavator "
        "brand in 2011, overtaking Japanese and Korean rivals, and in 2012 bought Putzmeister, the German "
        "concrete-pump leader, which gave it a European base and technology. The 2012–16 downturn after China's "
        "stimulus boom forced deep cost cuts. The following upcycle took revenue to a record RMB107bn in FY21 before "
        "the property-led slump. Since then Sany has leaned into exports, electrification and 'lighthouse' digital "
        "factories, and in 2025 it completed a Hong Kong H-share listing to fund globalisation. Related businesses "
        "(Sany Heavy Energy in wind turbines and Sany International in mining and port machinery) are separately listed "
        "and are not part of this entity.",
    ],
    milestones=[
        ("1989", "Founded in Lianyuan, Hunan by Liang Wengen and partners."),
        ("1990s", "Moves to Changsha; launches concrete pumps, then excavators and cranes."),
        ("2003", "Lists on the Shanghai Stock Exchange (600031.SH)."),
        ("2011", "Becomes China's No.1 excavator brand."),
        ("2012", "Acquires Putzmeister (Germany), the global concrete-pump leader."),
        ("2021", "Record revenue of RMB107bn at the peak of China's construction cycle."),
        ("2025", "Hong Kong H-share listing (6031.HK); net profit +41% to RMB8.4bn; overseas ~64% of sales."),
    ],
    ownership=[
        ("Controlling shareholder", "Sany Group, controlled by founder Liang Wengen"),
        ("Share classes", "A-share 600031.SH; H-share 6031.HK (listed 2025)"),
        ("Sister companies (not consolidated)", "Sany Heavy Energy (688349.SH); Sany International (0631.HK)"),
        ("Capital returns", "RMB400–800m buyback in progress; ~50% payout"),
    ],
    business=[
        "Sany designs, manufactures and sells construction machinery. Excavators are the largest line (~40% of H1'26 "
        "revenue), followed by concrete machinery (pumps, mixer trucks), cranes, piling rigs and road machinery. Machines "
        "are sold through a network of independent dealers in China and abroad, supplemented by direct sales to large "
        "contractors and miners. To support demand, Sany offers customer financing through instalment sales and finance "
        "leases. This lifts volumes but leaves sizeable receivables and credit risk on the balance sheet (receivables of "
        "RMB40bn, ~164 days of sales, at FY25).",
        "Profitability depends on three levers. Volume drives fixed-cost absorption in large plants. Mix matters because "
        "large excavators, mining equipment and overseas units carry higher margins (H1'26 overseas gross margin "
        "32.5%). Pricing discipline is the third lever, which in China depends on how aggressively XCMG, Zoomlion and "
        "others chase share. After-market parts and services are a growing, higher-margin, less cyclical revenue stream "
        "as the installed base ages.",
        "Globalisation is the strategic core. Overseas revenue was ~US$7.8bn in FY25 (+15%), about 64% of sales, led by "
        "Asia-Pacific and fast-growing Africa (+55%). Sany localises production in India, Indonesia, the US, Germany "
        "(Putzmeister) and Brazil to shorten delivery times and reduce tariff exposure. Electrification (electric "
        "excavators, mixers and trucks) and digitalised 'lighthouse' factories are differentiators that improve cost "
        "and position Sany for emission rules in developed markets.",
        "The domestic business is a replacement and infrastructure story rather than a property story. China's "
        "2016–21 boom left a large fleet now reaching replacement age, and water-conservancy, urban-renewal and "
        "mining spending support demand. That is why China excavator sales grew 17% in 2025 despite a weak property "
        "market.",
    ],
    segments_title="FY25 revenue by region (main business, company release)",
    segments_cols=("Region", "US$bn", "Growth / share", "Comment"),
    segments=[
        ("Mainland China", "~4.7", "~37% of sales", "Replacement cycle, infrastructure, mining; recovering from 2021–23 trough"),
        ("Asia-Pacific", "3.34", "+16.2% YoY", "Largest overseas region; India and Indonesia plants"),
        ("Europe", "1.75", "+1.5% YoY", "Putzmeister base; mature, price-competitive market"),
        ("Americas", "1.56", "+8.5% YoY", "US plant in Georgia; Brazil; tariff exposure in the US"),
        ("Africa", "1.16", "+55.3% YoY", "Fastest-growing; mining and infrastructure demand"),
    ],
    competition=[
        "Construction machinery is a global oligopoly at the top with a long tail of regional players. Caterpillar and "
        "Komatsu lead on brand, dealer density and after-market. Deere, Volvo CE, Hitachi Construction Machinery and "
        "Liebherr follow, with Sany and XCMG now in the same revenue league. In China, foreign brands' share of "
        "excavators has collapsed over the past decade as Sany, XCMG, LiuGong, SDLG and Sunward improved quality while "
        "keeping a price advantage.",
        "Sany's advantages are cost (Chinese machines typically sell at a meaningful discount to Japanese and US brands), "
        "breadth across product lines, and speed of dealer expansion and localisation. Its main gaps are brand "
        "perception and service density in North America and Western Europe, where buyers value resale prices and "
        "uptime, and exposure to trade barriers (tariffs and anti-dumping actions against Chinese machinery). The "
        "domestic market remains prone to price wars when demand falls.",
    ],
    competitors=[
        ("Caterpillar", "US", "Full line; mining; dominant dealer network", "Premium brand and after-market; far higher valuation"),
        ("Komatsu", "Japan", "Excavators, mining equipment", "Strong in Asia and mining; Sany's main overseas excavator rival"),
        ("XCMG", "China", "Cranes, excavators, road machinery", "Largest domestic rival; similar export push; lower valuation"),
        ("Zoomlion", "China", "Concrete machinery, cranes", "Strong in cranes and concrete; competes in exports"),
        ("Volvo CE / Hitachi CM / Liebherr", "Europe / Japan", "Excavators, wheel loaders, cranes",
         "Established in developed markets; higher cost base"),
    ],
    moat=[
        "Cost leadership from scale, localised supply chains and highly automated plants.",
        "Broad product line and a dealer network now spanning 180+ countries.",
        "Customer financing and after-market service that lock in dealers and fleets.",
        "Vulnerabilities: cyclical demand, receivable credit risk, trade barriers, weaker brand in developed markets.",
    ],
    tam=[
        "Global construction equipment is a roughly US$200–250bn market in annual OEM sales and highly cyclical. China "
        "is the largest single market by units. It sold 235,257 excavators in 2025 (+17%), of which 116,739 were "
        "exported, and 191,557 in Jan–Aug 2026 (+24%), with exports again outgrowing domestic sales. Emerging markets "
        "(Southeast Asia, Africa, the Middle East, Latin America) are growing fastest, driven by mining, "
        "infrastructure and urbanisation, and are where Chinese brands are gaining most share.",
        "Two structural shifts expand the addressable market. Electrification, first in China and then in emission-"
        "regulated developed markets, raises content per machine and favours manufacturers with in-house batteries and "
        "drivetrains. Mining equipment (large excavators, mining trucks) offers higher margins and stickier customers. "
        "Sany's ~US$12.5bn of FY25 revenue implies a mid-single-digit global share, which leaves ample room to gain "
        "share abroad.",
    ],
    tam_table=[
        ("Global construction equipment", "~US$200–250bn OEM sales", "Cyclical; mid-single-digit long-run growth",
         "Industry estimates"),
        ("China excavators", "235,257 units (2025, +17%)", "Jan–Aug 2026 +24%; replacement cycle", "CCMA"),
        ("  of which exports", "116,739 units (2025, +16%)", "Aug-26 exports +33%", "CCMA"),
        ("Electric construction machinery", "Early stage", "Policy-driven adoption, China first", "Qualitative"),
        ("Sany share", "~5% of global OEM sales", "Gaining share overseas", "Our estimate"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue fell from RMB107bn (FY21) to RMB74bn (FY23) in China's downturn and has since "
        "recovered to RMB89.7bn (FY25, +14.7%) and RMB98.4bn TTM. Gross margin has held at 27–28% through the cycle. "
        "Operating profit nearly doubled from RMB5.1bn (FY23) to RMB10.0bn (FY25) on operating leverage and mix, and net "
        "profit rose 41% to RMB8.4bn. In H1'26, EBIT rose 56% but net profit only 9% because CNY appreciation created FX "
        "finance losses on dollar receivables. We forecast revenue of RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of "
        "RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E."),
    fin_bs=(
        "<b>Balance sheet.</b> The balance sheet has de-risked markedly. Net debt of RMB3.3bn at FY23 turned into net "
        "cash of RMB{nc25}bn at FY25 and RMB{ncj26}bn at June 2026, helped by strong cash generation and ~RMB14.5bn of "
        "H-share proceeds. Total debt fell from RMB37.2bn to RMB20.6bn. Working capital remains the key watch-point: "
        "receivables of RMB40.2bn equal {recvd25} days of sales, reflecting customer financing, while inventory days are "
        "{invd25} and payable days have stretched to {apd25}. Equity attributable rose to RMB88.3bn (BVPS ~RMB10), and "
        "the current ratio is a comfortable {cr25}."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash flow rose from RMB5.7bn (FY23) to RMB20.0bn (FY25), or {ocfnp25} net profit, as "
        "receivables were collected and payables extended. Capex has fallen to ~RMB2.8bn ({capexr25} of revenue) after the "
        "2019–22 factory build-out, so FY25 free cash flow reached RMB{fcf25}bn. Dividends of RMB6.1bn and buybacks were "
        "well covered. We expect OCF to normalise below FY25's level as working capital rebuilds with growth. We forecast "
        "FCF of RMB{fcf26}bn/{fcf27}bn/{fcf28}bn, still enough to grow net cash to ~RMB{nc28}bn by FY28E after "
        "dividends."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE recovered from {roe23} (FY23) to {roe25} (FY25) and we expect {roe27} by FY27E: better, "
        "but still below the 20%+ of the last upcycle, which leaves room for upside if China recovers. ROA is {roa25} "
        "and asset turnover 0.55x. Net cash is equal to ~{ndeq25} of equity. The payout ratio on FY25 EPS was {payout25}, "
        "including a special element."),
)

V2["sieyuan"] = dict(
    background=[
        "Sieyuan Electric was founded in Shanghai in 1993 by Dong Zengping and a group of power-engineering colleagues. "
        "From a narrow initial range of grid products it expanded, mostly through in-house development, into one of the "
        "broadest transmission-and-distribution (T&D) portfolios in China. That portfolio now spans high-voltage "
        "gas-insulated switchgear (GIS) and circuit breakers, power and special transformers, reactors and capacitors, "
        "reactive-power compensation (SVG/STATCOM), protection and substation automation, battery energy-storage systems "
        "and turnkey EPC. It listed on the Shenzhen Stock Exchange in 2004 (002028.SZ).",
        "What makes Sieyuan unusual is ownership. China's grid-equipment industry is dominated by State Grid-affiliated "
        "and central SOEs, such as Pinggao, XJ Electric, NARI and China XD. Sieyuan is privately controlled by its founder, "
        "and has won share on product quality, delivery speed and cost. It has grown into a meaningful exporter, with "
        "equipment and EPC projects in Mexico, Saudi Arabia, the Philippines, Belgium, Brazil, Italy, Ecuador and Australia. "
        "In December 2025 it announced a Hong Kong H-share listing of up to 15% of its share capital to fund overseas "
        "expansion. In 2026 it is investing RMB480m to expand special-transformer capacity in Jiangsu.",
    ],
    milestones=[
        ("1993", "Founded in Shanghai by Dong Zengping."),
        ("2004", "Lists on the Shenzhen Stock Exchange (002028.SZ)."),
        ("2010s", "Builds out GIS, transformers, SVG and protection/automation lines."),
        ("2020s", "Expands overseas and enters battery energy storage."),
        ("2025", "Revenue RMB21.5bn (+39%), net profit RMB3.15bn (+54%); announces H-share plan."),
        ("2026", "Targets RMB37.5bn of new orders (+30%); RMB480m transformer capacity expansion."),
    ],
    ownership=[
        ("Control", "Privately controlled; founder Dong Zengping is the largest shareholder"),
        ("Share classes", "A-share 002028.SZ; H-share listing (≤15% of capital) pending"),
        ("Dividend policy", "Payout ~15–18% of net profit"),
    ],
    business=[
        "Sieyuan sells grid equipment to four customer groups. State Grid and China Southern Grid buy through "
        "centralised competitive tenders. Power generators and renewables developers need substations and grid "
        "connections. Industrial users and data centres buy in-house substations. Overseas utilities and EPC "
        "contractors made up 29.5% of H1'26 revenue. Revenue follows orders with a 6–18-month lag, so management's "
        "2026 targets of RMB37.5bn of new orders (+30%) and RMB27bn of revenue (+25%) give reasonable visibility.",
        "Primary equipment (switchgear and transformers) forms the profit core. Switchgear was 40% of H1'26 revenue and "
        "transformers 21%, both with gross margins around or above 30%. Secondary equipment (protection, automation, "
        "compensation) adds higher-value technology content. Energy storage (13% of revenue) is a newer integration "
        "business with a gross margin of only 10.5%. It grew 231% in H1'26 and is diluting group margins. EPC projects "
        "carry lower margins but help win overseas equipment orders.",
        "The business is asset-light relative to its revenue (PP&amp;E of RMB3.4bn against RMB21.5bn of sales) but "
        "working-capital intensive. Grid customers pay in stages, with retention money held until warranty expiry, so "
        "receivables run at ~190 days of sales. Sieyuan offsets this with supplier credit (payables ~200 days of cost of "
        "sales), and it has remained net cash throughout its growth phase.",
    ],
    segments_title="Revenue mix and economics (H1'26)",
    segments=[
        ("Switchgear (GIS, breakers)", "40.1%", "High-voltage switchgear for grid and industrial substations",
         "~30%+ gross margin; core State Grid tender product"),
        ("Protection, automation, SVG, EPC & other", "26.1%", "Secondary systems, reactive compensation, turnkey projects",
         "Mixed margins; EPC supports overseas wins"),
        ("Transformers & reactors", "20.9%", "Power and special transformers, reactors",
         "Tight global supply; capacity being expanded"),
        ("Energy storage", "12.9%", "PCS and integrated battery systems", "10.5% gross margin; +231% in H1'26"),
    ],
    competition=[
        "In China, Sieyuan competes in State Grid tenders against affiliated or state-owned suppliers: Pinggao and XJ "
        "Electric (both State Grid subsidiaries), China XD Electric (switchgear and transformers), TBEA (transformers) "
        "and NARI (protection and automation). Tender rules weight price and technical scores, so share moves with "
        "product breadth, quality record and willingness to bid aggressively. Sieyuan has steadily gained share as a "
        "private challenger.",
        "Overseas, the incumbents are Hitachi Energy, Siemens Energy, GE Vernova, Schneider and ABB, plus Korean "
        "exporters HD Hyundai Electric, Hyosung and LS Electric, which have been the main winners from the US "
        "transformer shortage. Chinese suppliers win on delivery time and price, especially in the Middle East, Latin "
        "America and Southeast Asia. Access to the US is limited by tariffs and security concerns. In storage, Sieyuan "
        "faces dozens of Chinese integrators and battery makers, and margins are commodity-like.",
    ],
    competitors=[
        ("Pinggao / XJ Electric", "China (State Grid)", "GIS, DC equipment, protection", "Parent-affiliated; strong in UHV tenders"),
        ("China XD Electric", "China (SOE)", "Switchgear, transformers", "Large UHV supplier; slower-growing"),
        ("TBEA", "China", "Transformers, cables (plus polysilicon)", "Transformer scale leader; diversified"),
        ("Hitachi Energy / Siemens Energy", "Switzerland/Japan / Germany", "Full T&D portfolio worldwide",
         "Global brand and HVDC leadership; capacity-constrained"),
        ("HD Hyundai Electric / Hyosung", "Korea", "Transformers, switchgear", "Main winners in the US shortage; premium valuations"),
    ],
    moat=[
        "Broadest private-sector T&D portfolio in China, from primary to secondary equipment.",
        "Track record in State Grid tenders plus growing overseas references and certifications.",
        "Agility and cost discipline of a founder-led private company; net cash balance sheet.",
        "Vulnerabilities: tender price pressure, low-margin storage growth, overseas execution and FX.",
    ],
    tam=[
        "Grid spending is the demand driver. State Grid has been investing more than RMB650bn a year, and the 15th "
        "Five-Year Plan points to more than RMB5tn of grid investment over 2026–30, covering ultra-high-voltage "
        "lines that carry western renewables east, distribution upgrades, and connections for new energy and data "
        "centres. China Southern Grid, provincial utilities and industrial users add to this.",
        "Abroad, renewables integration, electrification and AI data-centre load are driving a multi-year upcycle in "
        "transformers and switchgear, with lead times of two years or more in the US and Europe. China's transformer "
        "exports rose 35% to US$9.0bn in 2025. The storage market is growing even faster (China's storage-battery sales "
        "+83% in H1'26) but is fiercely competitive. Sieyuan's FY25 revenue of RMB21.5bn is a small share of these pools, "
        "so growth depends on share gains rather than market size.",
    ],
    tam_table=[
        ("China grid investment", ">RMB650bn a year (State Grid); >RMB5tn over 2026–30", "Rising; UHV and distribution upgrades",
         "State Grid; source pack"),
        ("China transformer exports", "US$9.0bn (2025)", "+35% in 2025", "Industry data"),
        ("Global transformers & switchgear", "Structural shortage", "≥2-year lead times in US/EU", "Industry reports"),
        ("China storage batteries", "Fast-growing", "Sales +83% in H1'26", "Industry data (via Ganfeng)"),
        ("Sieyuan order target", "RMB37.5bn (2026)", "+30% YoY", "Company"),
    ],
    fin_is=(
        "<b>Income statement.</b> Revenue compounded at ~27% a year from RMB10.5bn (FY22) to RMB21.5bn (FY25), with gross "
        "margin steady at 29–31% and net margin rising from 12.5% (FY23) to 14.6% (FY25). FY25 net profit rose 54% to "
        "RMB3.15bn. The mix is now turning: H1'26 revenue grew 27% but net profit only 13%, as low-margin storage "
        "surged and FX losses weighed. We forecast revenue of RMB{rev26}bn/{rev27}bn/{rev28}bn and net profit of "
        "RMB{np26}bn/{np27}bn/{np28}bn for FY26–28E, with gross margin ~1pt lower than FY25."),
    fin_bs=(
        "<b>Balance sheet.</b> Total assets rose from RMB18.7bn to RMB29.8bn over FY23–25, mostly working capital: "
        "receivables reached RMB11.0bn ({recvd25} days) and inventory RMB4.1bn ({invd25} days), rising to RMB6.0bn by June "
        "2026 as storage projects built. Supplier credit (payables RMB8.2bn, {apd25} days) funds much of this. Debt is "
        "negligible (RMB0.5bn), so net cash was RMB{nc25}bn at FY25 and RMB{ncj26}bn at June 2026, ~{ndeq25} of equity. "
        "The current ratio is {cr25}. Equity attributable has grown to RMB15.5bn (BVPS ~RMB20)."),
    fin_cf=(
        "<b>Cash flow.</b> Operating cash flow has not kept pace with profits: RMB2.3bn/2.5bn/2.2bn over FY23–25 against "
        "net profit of RMB1.6bn/2.0bn/3.2bn, so OCF/net profit fell to {ocfnp25} in FY25 as receivables grew 39%. TTM OCF "
        "recovered to RMB3.2bn. Capex of RMB0.7–0.9bn a year keeps FCF at ~RMB1.4–1.5bn (RMB{fcf25}bn in FY25), and "
        "dividends absorb only ~RMB0.4bn. We forecast FCF of RMB{fcf26}bn/{fcf27}bn/{fcf28}bn as capacity spending rises, "
        "with net cash growing to ~RMB{nc28}bn by FY28E before any H-share proceeds."),
    fin_ratios=(
        "<b>Key ratios.</b> ROE has risen from {roe23} (FY23) to {roe25} (FY25), and we expect it to hold at ~{roe27}. "
        "ROA is {roa25} and asset turnover has improved to 0.81x. Cash conversion is the weak point: OCF/net profit of "
        "{ocfnp25} in FY25, and our forecasts assume ~0.7x. Payout is low ({payout25} on FY25 EPS), leaving capacity to "
        "fund growth internally."),
)
