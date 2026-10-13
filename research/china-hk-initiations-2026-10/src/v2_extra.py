"""Additional strategy, competition and market-sizing paragraphs, appended to the v2 sections in build.py.

EXTRA[key][section] -> list of paragraphs (raw HTML; placeholders allowed)."""

EXTRA = {}

EXTRA["sany"] = dict(tam=[
    "Sany has plenty of room to gain share abroad. Caterpillar and Komatsu still hold the largest shares of global "
    "sales, and Chinese brands remain small in North America, Western Europe and Japan, where buyers weigh dealer "
    "networks, brand and resale values most heavily. Sany's overseas growth has therefore come first from emerging "
    "markets, where price, delivery time and financing decide most purchases.",
])

EXTRA["sieyuan"] = dict(business=[
    "In China, management wants to push further into higher-voltage products, where qualification is hardest and "
    "margins are best. Abroad, the planned H-share listing is meant to fund overseas plants and service networks so "
    "that project exports become local market positions in the Middle East, Latin America and Europe. The company is "
    "also adding products that sell to the same customers: storage, reactive-power compensation for renewables and "
    "data-centre power distribution. That last push carries the most risk. Storage earns a 10.5% gross margin, so its "
    "growth dilutes group returns until the business reaches scale.",
])

EXTRA["sungrow"] = dict(tam=[
    "In storage, revenue per GWh matters as much as GWh installed. A utility storage system now sells for a fraction "
    "of its 2023 price because cell prices have collapsed, so industry revenue grows more slowly than installations. "
    "The power-conversion and software content that Sungrow makes itself holds its value better than cells, which is "
    "why its margins rose while system prices fell. We expect growth in the storage market over the next few years to "
    "come from volume, with prices flat to lower.",
])

EXTRA["huayou"] = dict(
    business=[
        "The plan for the next three years is to finish the Indonesian build-out and then harvest it. Pomalaa adds "
        "120ktpa of MHP capacity as it ramps through 2026–27. We assume capex falls from ~RMB15bn in FY26E to ~RMB8bn "
        "by FY28E once it is complete, which is what turns free cash flow positive in our model. The second priority "
        "is selling more nickel outside China's LFP-dominated market, mainly to Korean and European cell makers. US "
        "foreign-entity sourcing rules limit how much Huayou can sell into US supply chains.",
    ],
    tam=[
        "Huayou's three HPAL projects total ~300ktpa of nickel-in-MHP capacity at 100% ownership (less on an "
        "attributable basis), equal to roughly 8% of global nickel supply. That is enough to matter to the market, "
        "though not enough to set prices. Indonesian supply growth has pushed nickel "
        "prices down toward the costs of higher-cost producers elsewhere, so Huayou's returns depend on staying at the "
        "bottom of the cost curve rather than on a price recovery.",
    ],
)

EXTRA["tianqi"] = dict(
    competition=[
        "Position on the cost curve decides who survives a downturn. Greenbushes concentrate is among the cheapest "
        "spodumene in the world to produce, while Jiangxi lepidolite and many African and Australian hard-rock mines sit "
        "at the top of the curve. When prices fall, those high-cost tonnes are the first to close, as they did in 2024. Tianqi's conversion "
        "plants are less advantaged: Chinese converters run on thin processing margins, and Kwinana's problems have "
        "made Western conversion look expensive.",
    ],
    tam=[
        "EV batteries account for the majority of lithium demand. Stationary storage is now the fastest-growing "
        "segment, and consumer electronics and industrial uses (glass, ceramics, greases) make up the rest. The rise "
        "of storage and of LFP cells in EVs shifts demand toward lithium carbonate and away from hydroxide, which is "
        "used in high-nickel cathodes. That matters for Tianqi, because Kwinana was built to make hydroxide.",
    ],
)

EXTRA["ganfeng"] = dict(
    business=[
        "Ganfeng is integrating in both directions. Upstream, it is lifting self-sufficiency in "
        "lithium resources as Goulamina, Mariana and Cauchari-Olaroz ramp, which should lower its cost position "
        "through the cycle. Downstream, it uses the battery business and solid-state technology to capture more of the "
        "value chain, accepting lower margins today for a position in next-generation cells. We assume capex slows to "
        "RMB5–6bn a year in FY26–28E, from RMB7–9bn in FY23–25, which is what allows free cash flow to turn positive.",
    ],
    competition=[
        "Ganfeng's position is stronger in lithium metal than in mainstream chemicals. It is the world's largest "
        "producer of lithium metal, which feeds pharmaceutical, alloy and next-generation battery uses, and its "
        "high-purity metal and organolithium compounds face fewer competitors and steadier prices. Solid-state "
        "batteries with lithium-metal anodes would turn that niche into a much larger market, an option that pure "
        "miners do not have.",
    ],
    tam=[
        "At around RMB122k/t, much higher-cost lepidolite and African supply is profitable again, and restarts could "
        "cap prices over the next 18 months. Ganfeng's earnings are less sensitive to "
        "the lithium price than Tianqi's: it buys more of its feedstock at market-linked prices, and its battery "
        "business dilutes the commodity exposure.",
    ],
)

EXTRA["gigadevice"] = dict(
    business=[
        "Management is using the 2026 memory upcycle to fund higher-value products: higher-density NOR for AI servers, "
        "automotive-grade memory, and DDR4/LPDDR4 parts as the majors exit. In MCUs it is pushing into automotive and "
        "high-performance industrial uses, including RISC-V cores, where a design win can last a decade. The H-share "
        "proceeds go to R&amp;D and strategic stakes. With record cash flow on top, we estimate net cash reaches "
        "~RMB{nc26}bn by FY26E.",
    ],
    competition=[
        "Shortages also reshape customer behaviour. When legacy memory is scarce, buyers put supply security first "
        "and qualify second sources. GigaDevice's domestic wafer partners give Chinese customers a local supply chain "
        "that is insulated from export controls. Our bull case assumes the share GigaDevice gains in the shortage "
        "stays with it after prices normalise, which would make the memory franchise worth more than its peak-cycle "
        "earnings suggest.",
    ],
)

EXTRA["jlmag"] = dict(
    business=[
        "JL Mag plans to lift capacity from ~40kt in 2025 to 60kt by end-2027, including the Baotou base next to light "
        "rare-earth supply and overseas capacity for customers that want supply outside China. It is shifting output "
        "toward robots, servo motors and humanoid joint motors, where specifications are tighter and processing fees "
        "higher. Its grain-boundary diffusion process and low-heavy-rare-earth grades also cut its need for dysprosium "
        "and terbium, the materials most exposed to export controls.",
    ],
    tam=[
        "Humanoid robots will add little tonnage. At 2–4kg of magnets per robot, one million humanoids a year would add "
        "only 2–4kt of magnet demand, small next to EVs. The money is in the higher processing fees for precision rotor "
        "assemblies, which is why JL Mag sells finished rotors as well as magnet blocks into this market.",
    ],
    competition=[
        "Since April 2025 China has required export licences for seven medium and heavy rare earths and for magnets "
        "that contain them. Over time that pushes Western automakers to qualify non-Chinese suppliers. In the near term "
        "it favours established Chinese producers with licences, long customer relationships and overseas plants, such "
        "as JL Mag.",
    ],
)

EXTRA["hans"] = dict(tam=[
    "Semiconductor and advanced-packaging equipment is the next adjacency. Laser dicing, grooving and annealing "
    "tools are dominated by Japanese and European suppliers, and Chinese chipmakers want domestic alternatives. Han's "
    "revenue there is still small, so this is upside to our forecasts rather than part of them.",
])

EXTRA["horizon"] = dict(business=[
    "Management's priorities for 2026–28 are to scale HSD on mid-priced cars, keep licensing revenue growing faster "
    "than chip shipments, and widen the customer base outside China through Toyota programmes, Denso and AUMOVIO. Each "
    "raises content per vehicle and the share of high-margin software and licence revenue. The path to the 2028 "
    "breakeven target depends mostly on R&amp;D: if spending stays near RMB5bn while revenue rises 2.5x to "
    "RMB{rev28}bn by FY28E, as we forecast, operating losses narrow sharply.",
])

EXTRA["leaderdrive"] = dict(
    business=[
        "Leaderdrive is moving from selling components to selling modules, and electromechanical actuators already "
        "contribute ~16% of revenue. The SKF joint venture and the planned H-share listing are meant to fund capacity for humanoid and "
        "collaborative-robot joint modules, where content per robot is far higher than for a reducer alone. The "
        "trade-off is capital intensity: capex of ~RMB250m a year in our forecasts is large against FY26E revenue of "
        "RMB{rev26}m, so free cash flow stays negative until volumes arrive.",
    ],
    tam=[
        "Today's humanoid pilot volumes are worth little to reducer makers: at an illustrative RMB1,000–2,000 "
        "per reducer, 50,000 humanoids a year would need RMB0.7–2.0bn of harmonic reducers across the whole industry. "
        "A million-unit market would be worth RMB14–40bn a year, but prices per reducer would probably fall as volumes "
        "rise. At ~{pe27}x FY27E P/E, Leaderdrive's share price already assumes something close to the million-unit "
        "market.",
    ],
    competition=[
        "Customer qualification is the main barrier to entry. Robot makers test reducers for accuracy, stiffness and "
        "life over thousands of hours, and humanoid developers now run similar programmes. Leaderdrive's long record "
        "with Chinese industrial-robot makers gives it a head start, but humanoid designers are qualifying several "
        "suppliers at once.",
    ],
)

EXTRA["edge"] = dict(
    business=[
        "Over the next three years Edge wants to turn placements into recurring revenue. It plans to raise procedure "
        "volumes per robot through surgeon training and clinical programmes and to sell more instruments and service. "
        "The ~350-unit plant adds capacity, so system prices can fall further without hurting margins. The "
        "planned A-share listing would add domestic capital and raise Edge's profile with Chinese hospitals.",
    ],
    tam=[
        "On illustrative numbers, an installed base of 1,000 robots, each performing ~300 procedures a year with ~RMB10,000 of instruments and service per procedure, "
        "would generate ~RMB3bn of recurring revenue a year, several times Edge's FY25 revenue of RMB456m. Most of "
        "Intuitive's revenue already comes from instruments and service, and Edge is trying to copy that model.",
    ],
)

EXTRA["zai"] = dict(
    business=[
        "Z.AI's management plans to spend the war chest on next-generation models (GLM-6.0), domestic compute and "
        "international growth through coding plans and hyperscaler marketplaces. We "
        "model capex of RMB1.5–3.0bn a year and operating cash outflows of RMB4–6bn a year. On that basis the "
        "~RMB{nc26}m of net cash we expect at FY26E covers several years of investment without further raises.",
    ],
    competition=[
        "Benchmark leads change hands every few weeks, so distribution, developer loyalty and cost per token last "
        "longer as advantages. Z.AI's coding subscriptions and integrations with developer tools give it a direct "
        "relationship with users, and its move to domestic inference chips cuts unit cost.",
    ],
    tam=[
        "Policy also shapes China's market. The State Council's 'AI+' initiative encourages adoption across industry "
        "and the public sector, and state-owned buyers often prefer domestic models deployed on their own servers, "
        "which plays to Z.AI's strengths in on-premise work.",
    ],
)

EXTRA["minimax"] = dict(
    business=[
        "Management aims to keep its models near the frontier at a fraction of rivals' budgets by using efficient "
        "architectures. It wants the higher-margin Open Platform to grow faster than consumer apps, and it is building "
        "some of its own compute to cut inference costs (capex of US$250–300m a year in our forecasts). Money limits all "
        "of this. With ~US${ncj26}m of net cash at June 2026 and annual burn of ~US$0.6bn, MiniMax will probably need to "
        "raise capital again by 2028 unless losses narrow faster than we expect.",
    ],
    competition=[
        "Video generation is the most contested category. Kling, Seedance, Veo and Sora are backed by platforms with "
        "large video libraries and distribution, while Hailuo competes on model quality and price. Voice is a relative "
        "strength: MiniMax's speech models are among the better-regarded on public text-to-speech leaderboards, which "
        "gives the Open Platform a differentiated product.",
    ],
)
