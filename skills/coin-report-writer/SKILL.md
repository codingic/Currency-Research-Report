---
name: coin-report-writer
description: Write and save professional cryptocurrency, blockchain network, or stock analysis reports when the user asks for a coin, token, chain, network, stock, equity, or listed company research brief; a latest ecosystem review; roadmap update; tokenomics analysis; AI relevance analysis; value-capture analysis; future development prospects of a chain; the best way a chain should combine with AI; a one-year price outlook; a next-12-month catalyst calendar; or simply sends a coin name, ticker, chain name, or stock ticker such as BTC, ETH, Solana, Base, Arbitrum, ICP, NVDA, AAPL, COIN, or MSTR expecting a full document. Gather fresh web sources, summarize recent X discussion, and produce a markdown report saved in the current workspace.
---

# Coin & Stock Report Writer

## Quick Start

1. Treat a bare coin name, ticker, chain/network name, stock ticker, or listed company name as a request for a full report unless the user explicitly asks for a narrower task.
2. Resolve the exact asset before writing. If the name is ambiguous, use the most likely large-cap/mainstream asset and say which asset you selected, including whether it is `加密资产 / 链 / 股票`.
3. Determine the asset's `主赛道` and optional `次赛道` before drafting so the report uses the right evaluation framework.
4. Gather fresh sources first. This skill depends on recent market, roadmap, and social discussion data, so browse the web before drafting.
5. Create the report file with `python3 scripts/init_coin_report.py "<coin-or-ticker>" --output-dir "<workspace>/reports"`.
6. If the user gives multiple coins, create one file per coin with `python3 scripts/init_coin_report.py BTC ETH SOL --output-dir "<workspace>/reports"`. Do not merge multiple coins into one document unless the user explicitly asks for a comparison report.
7. Fill each generated markdown file in place, delete placeholder text, and leave the finished documents saved in the workspace.

## Research Rules

- Write the final report in Simplified Chinese by default. Only switch to another language if the user explicitly requests it.
- Write like a professional buy-side or research-desk analyst: concise, evidence-driven, and willing to show nuance, disagreement, and uncertainty.
- Be comprehensive and deep by default. Cover the full system around the asset, not just project updates: product, users, token or equity holder economics, governance, competition, liquidity, node/validator set and decentralization when relevant, balance sheet and capital allocation when relevant, policy, macro, and where relevant AI or infrastructure dependencies.
- Include a dedicated `历史大事件与影响意义` section for every asset. Prefer the 3-8 events that most changed adoption, credibility, regulation, token or equity economics, market structure, or the long-term narrative, and explain both the near-term shock and the lasting significance.
- Use exact dates such as `2026-03-17` or `March 17, 2026` instead of relative phrases like "today" or "recently" when precision matters.
- Separate verified facts from inference. Label scenario analysis, probability judgments, and price forecasts as assumptions instead of facts.
- Always classify the asset into a primary sector before writing. This classification determines what metrics matter and what comparisons are valid.
- If the asset is a stock or listed company, treat the report as equity research first: cover business model, revenue drivers, margins, cash flow, balance sheet, valuation, capital allocation, dilution/buybacks, management execution, competition, and sector multiples instead of forcing crypto-native metrics where they do not belong.
- Distinguish clearly between `链的发展前景` and `代币的投资前景`. If the user's wording is chain-centric, prioritize chain adoption, developers, applications, liquidity, security, governance, and ecosystem moat first, then separately assess whether the native token captures that growth.
- If the user asks how a chain should best combine with AI, treat that as a strategy analysis: rank the most promising AI integration paths, explain why they fit this chain, and distinguish real product fit from narrative-only AI positioning.
- Default forecast horizon to the next 12 months. If the user explicitly asks for a calendar year such as `2026` or `2027`, switch the catalyst and price sections to that requested window.
- Treat `股市的影响` as a distinct analytical lens. Explain how broad equity risk appetite, tech-stock performance, sector proxies, ETF flows, and stock-market liquidity conditions may transmit into the asset.
- Treat `国际战争的影响` as a distinct analytical lens. Explain how wars, sanctions, energy shocks, safe-haven demand, cybersecurity risk, payment-fragmentation, and regional instability may transmit into the asset.
- If the same asset has already been covered in this workspace, read the latest prior report first and treat the new report as an update: prioritize newly happened developments, changed sentiment, revised roadmap items, new macro shifts, and new policy signals.
- Prefer primary sources first: official blogs, docs, roadmap pages, governance forums, GitHub, explorer dashboards, foundation statements, exchange disclosures, and direct X posts from the project/founders/core contributors.
- For X discussion, prioritize direct posts and recent community debate. If direct posts are unavailable, fall back to reliable summaries and explicitly say that the point is inferred from secondary discussion coverage.
- Do not fabricate metrics. If a number cannot be verified, say so and continue with qualitative analysis.
- Always analyze unlocks and supply overhang when they matter. When possible, state the most recent material unlock, the next known unlock window, the next 30/90/365 day unlock profile, the recipient buckets, and whether the unlock is cliff-based, linear, programmatic, or already largely absorbed. If reliable unlock data is unavailable or the token is effectively fully circulating, say so explicitly.
- For chain or network assets, always analyze node and validator health when data exists. State total node count, validator count, what class of nodes the number refers to, and any meaningful decentralization context such as geographic/provider concentration, stake concentration, client diversity, or Nakamoto-style concentration indicators. If reliable node data is unavailable or not applicable, say so explicitly.
- For stock assets, always analyze the core equity metrics when data exists: market cap, enterprise value, revenue, growth, gross margin, operating margin, EPS, free cash flow, net cash or debt, diluted share count, valuation multiples, and whether dilution, SBC, convertibles, or buybacks materially change the thesis.
- Prefer direct, declarative analyst prose. Avoid formulaic contrast built around negation; state the real conclusion directly, then explain the mechanism or evidence.
- Because this is financial content, keep a neutral tone and frame price targets as scenarios rather than advice.

## Document Workflow

1. Run `scripts/init_coin_report.py` to create dated markdown file(s) under the chosen `reports/` directory.
2. Read [report-rubric.md](references/report-rubric.md) and follow the section order exactly unless the user requests a different structure.
3. If the same asset was covered before, locate the newest prior report in `reports/` and extract what the last known state was before doing fresh browsing.
4. Read [source-priority.md](references/source-priority.md) before gathering evidence if the request depends on latest information, X discussion, roadmap, or price outlook. That is the normal case for this skill.
5. If the asset is a stock or listed company, verify investor-relations pages, earnings releases, SEC or exchange filings, shareholder letters, earnings transcripts, and consensus or valuation data first. Read [stock-framework.md](references/stock-framework.md) before drafting.
6. If tokenomics matter, verify vesting and unlock information from official tokenomics pages, governance posts, treasury disclosures, or vesting contracts first; use reputable unlock dashboards only as secondary fallback.
7. If the request is chain-centric or the asset is an L1/L2/network, verify node and validator data from official validator pages, explorers, staking dashboards, telemetry sites, or reputable infrastructure trackers. Distinguish validators from full nodes, RPC nodes, or other node classes.
8. Read [sector-frameworks.md](references/sector-frameworks.md) to choose the primary sector and adjust the report emphasis.
9. If the request is chain-centric or the asset is an L1/L2/network, read [chain-analysis.md](references/chain-analysis.md) and make sure chain outlook and token capture are separated.
10. If the user asks about the best AI combination path for a chain, read [chain-ai-fit.md](references/chain-ai-fit.md) and rank the most suitable AI directions before drafting.
11. Read [comparables.md](references/comparables.md) and select the most relevant same-sector peers before writing the report.
12. Read [angle-framework.md](references/angle-framework.md) before writing section `8. 全方位多角度分析`.
13. Read [depth-framework.md](references/depth-framework.md) before drafting the main body so the report answers strong bull, strong bear, priced-in assumptions, market blind spots, and falsification points.
14. Read [report-quality.md](references/report-quality.md) before finalizing the report.
15. Use one asset per report. If the prompt includes multiple assets, create and complete one document per asset.
16. Replace every placeholder in each generated markdown template.
17. End every document with a `## Sources` section containing markdown links.

## Output Standard

- Save reports as markdown in the active workspace, normally under `reports/`.
- Default to one coin per file.
- Use a Chinese title such as `# BTC / Bitcoin 深度分析报告`.
- Include a Chinese `执行摘要` before the numbered sections.
- Add a visible `解锁与供给压力快照` section near the top. State the most recent material unlock, the next known unlock, the next 30/90/365 day unlock pressure when data exists, who receives the tokens, and whether the unlock should matter for market structure. If the token is largely fully circulating or no reliable unlock data exists, say so explicitly.
- Add a visible `节点与验证者概况` section near the top. State the total node count and/or validator count, clarify what kind of nodes the count refers to, describe the most relevant concentration or distribution facts, and explain why that matters for decentralization, liveness, or censorship resistance. If the metric is not applicable or no reliable data exists, say so explicitly.
- Add a visible `股票信息与核心指标` section near the top for stock requests. Include ticker and exchange, core business description, market cap, enterprise value, revenue and growth, gross margin, operating margin, EPS, free cash flow, net cash or debt, diluted share count, valuation multiples such as `P/E`, `EV/Sales`, `EV/EBITDA`, and any material `SBC / buyback / ATM / convertibles` context.
- State the chosen `主赛道` clearly near the top of the report and let it influence which metrics and comparisons are emphasized.
- Include explicit depth sections near the top of the report: `核心投资逻辑`, `反方观点与证伪条件`, and `市场可能忽略的变量`.
- Include a visible `历史大事件与影响意义` section near the top-middle of the report. For each event, explain what happened, why it mattered at the time, what changed afterward, and whether that effect still shapes the current thesis.
- Include a `对标项目比较` section that compares the asset with the closest same-sector chains or projects whenever reasonable peers exist.
- If the request is about a chain's future prospects, make the chain-level outlook the primary narrative and treat token capture as a separate judgment instead of assuming chain success automatically means token upside.
- If the request is about a chain and AI, identify the `最佳结合方向`, `为什么适合这条链`, `落地路径`, `商业化与价值捕获`, and `哪些 AI 方向看起来热闹但其实不适合`.
- Cover all sixteen user-requested numbered dimensions, and also include `解锁与供给压力快照` plus `节点与验证者概况` near the top when applicable:
  `Recent ecosystem progress`, `Recent X discussion`, `Tokenomics`, `Outlook`, `Value capture`, `next-12-month catalysts`, `next-12-month price forecast`, `Multi-angle analysis`, `AI-related analysis`, `Latest roadmap`, `Macroeconomic impact`, `Economic policy impact`, `Stock-market impact`, `International-war impact`, `Block explorer address`, and `Smart contract development language`.
- If the asset is a stock, add `股票信息与核心指标` near the top, translate token-centric discussion into share count, dilution, buybacks, and capital structure where relevant, and mark crypto-only fields such as block explorer or smart contract language as `不适用` unless the company business makes them materially relevant.
- Add a short `Key Risks` section before `Sources`.
- Make the `未来 12 个月价格走势预测` scenario-based with `bear / base / bull` ranges and the assumptions behind each range.
- When AI relevance is weak, say so plainly and explain whether the connection is product-level, infrastructure-level, narrative-level, or negligible.
- In the macro and policy sections, connect the token to liquidity cycles, rate expectations, dollar strength, risk appetite, ETF flows when relevant, jurisdictional regulation, tax/accounting treatment, and sector-specific policy catalysts.
- Go beyond news summarization. Explain why each development matters for adoption, token demand, margins, market structure, or narrative durability.
- For depth, force yourself to cover both bull and bear logic, what is already priced in, what the market may be missing, and what data would falsify the thesis.
- On repeat coverage of the same asset, emphasize deltas first: what is newly shipped, newly debated, newly delayed, newly regulated, or newly repriced since the last report.
- Use the chosen sector to decide what deserves the most space. For example, L1/L2 reports should emphasize developers, users, fees, and ecosystem stickiness, while DeFi reports should emphasize revenue, TVL quality, and token capture.
- Compare with the nearest chains or same-category projects, not arbitrary large-cap names. Explain relative strengths, weaknesses, and whether valuation looks rich or cheap versus peers.
- In the stock-market section, explain whether the asset behaves more like a high-beta tech trade, a liquidity trade, a crypto-native trade, or a partially decorrelated asset, and identify the most relevant equity benchmarks or proxy stocks.
- In the international-war section, explain concrete transmission paths such as sanctions, commodity and energy shocks, safe-haven rotation, payment settlement demand, cyber conflict risk, mining/validator geographic exposure, and regional liquidity disruption.
- In section `8. 全方位多角度分析`, use the multi-angle framework and cover at least 8 materially relevant angles when possible. For angles that do not apply, say `不适用` and explain briefly.
- In the explorer section, provide the main official or most commonly used block explorer URL and explain what users can inspect there.
- In the smart contract language section, name the primary contract language, VM, or developer stack. If the asset does not support general smart contracts, say that explicitly and explain the practical developer path instead.

## Reusable Resources

### `scripts/init_coin_report.py`

Create a dated markdown report from the bundled template. Use it whenever you are starting a new report file.

### `references/report-rubric.md`

Use this rubric to keep the report structure consistent and sufficiently deep.

### `references/source-priority.md`

Use this to decide what sources to trust and how to write scenario analysis without overstating confidence.

### `references/sector-frameworks.md`

Use this to classify the asset's main sector and choose the right evaluation framework and metrics.

### `references/chain-analysis.md`

Use this when the request is chain-centric or the asset is primarily a blockchain network. Separate chain growth from token capture.

### `references/chain-ai-fit.md`

Use this when the user asks how a chain should best combine with AI. Rank the best-fit AI directions and explain why they do or do not fit the chain.

### `references/stock-framework.md`

Use this when the asset is a stock or listed company. It explains which equity metrics matter and how to map the report structure away from token-native language.

### `references/comparables.md`

Use this to choose the right peer set and compare against similar chains or same-category projects.

### `references/angle-framework.md`

Use this to turn `全方位多角度分析` into a concrete coverage matrix instead of generic commentary.

### `references/depth-framework.md`

Use this to make the report genuinely deep: strong bull case, strong bear case, priced-in assumptions, market blind spots, and falsification points.

### `references/report-quality.md`

Use this as the final quality gate so the report has enough source diversity, freshness, and analytical depth.

### `assets/report-template.md`

This is the report scaffold used by `init_coin_report.py`. Update it only when the report format should change for every future run.

## Final Checklist

- The file is saved in the workspace.
- Each requested coin has its own standalone document unless the user explicitly asked for a comparison report.
- The document is written in Simplified Chinese unless the user explicitly asked for another language.
- All sixteen requested sections are present and non-empty.
- The report explicitly states a `主赛道`, and the chosen metrics/comparables match that sector.
- The report includes `对标项目比较` and the peer set is genuinely comparable.
- If the request is chain-centric, the report clearly separates `链的发展前景` from `代币价值捕获`.
- If the request is about chain + AI fit, the report clearly ranks AI integration paths by fit and explains why the top path is better than the alternatives.
- The metadata lines correctly state whether the report is `首次覆盖` or `更新版`, and reference the previous report when one exists.
- If the asset has a prior report, the new document clearly identifies what changed since the last version instead of repeating old points at the same weight.
- The report includes `关键指标快照` and `未证实但值得跟踪的问题`.
- The report includes `解锁与供给压力快照`, or explicitly states why unlock analysis is not applicable.
- The report includes `节点与验证者概况`, or explicitly states why node analysis is not applicable or unavailable.
- If the asset is a stock, the report includes `股票信息与核心指标` and uses actual equity metrics instead of generic crypto placeholders.
- The report includes `核心投资逻辑`, `反方观点与证伪条件`, and `市场可能忽略的变量`.
- The report includes `历史大事件与影响意义`, and each event includes both the impact at that time and the longer-term significance.
- The `全方位多角度分析` section covers at least 8 relevant angles or marks some as `不适用` with a reason.
- The X discussion section reflects recent discourse rather than generic sentiment.
- The roadmap and next-12-month catalyst sections contain concrete dates or windows when available.
- The price forecast is clearly scenario-based and not framed as certainty.
- The macro and policy sections explain transmission mechanisms instead of giving generic market commentary.
- The stock-market section explains equity-market transmission paths instead of generic correlation claims.
- The international-war section explains geopolitical transmission paths instead of generic fear/risk-off commentary.
- The analysis explains second-order effects, not just headline events.
- The explorer section includes a usable URL.
- The smart contract section states the exact language or clearly explains why smart contracts are not applicable.
- The `Sources` section contains clickable markdown links.
