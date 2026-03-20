# AAVE / Aave 深度分析报告

- 报告日期：2026-03-19
- 分析标的：AAVE / Aave
- 文件标识：aave
- 报告类型：首次覆盖
- 上一版报告：无

## 与上次相比的关键变化

首次覆盖。这篇报告的重点，不是重复 “Aave 是 DeFi 借贷龙头” 这个老结论，而是判断 `2025-2026 这轮变化是否让 Aave 从“最大借贷协议”升级为“链上信用基础设施”，并且让 AAVE 从“治理代币”进一步走向“带真实回购与更低排放的资产”。`

最关键的新变量有六个：

- `2025-03-04`：`Aavenomics Part One` 提案发布，正式把 `buyback、Umbrella、LEND chapter close、Anti-GHO 路线` 推到执行层。
- `2025-06-05`：Umbrella 升级生效，Safety Module 风险与排放结构重构。
- `2025-08`：Aave Horizon 上线，把 Aave 扩展到 RWA 抵押借贷市场。
- `2025` 全年：Aave V4 完成测试网与代码公开，官方明确 `2026` 主网上线。
- `2025-10-22`：长期 buyback 计划提议设定 `5000 万美元年预算`，并在 `2025-11-02` 通过 ARFC Snapshot。
- `2026-03-11`：wstETH CAPO 风险预言机参数错配引发错误清算，暴露出服务商流程与风控协同风险，但协议无坏账，DAO 正在推进赔付。

一句话结论：`Aave 协议层面比过去更强，收入和生态分发也更像基础设施；AAVE 代币层面的价值捕获比过去明显改善，但还没有强到能被当作“纯现金流资产”来定价。`

## 关键指标快照

以下数据主要来自 `2026-03-19` 前后的 CoinGecko、DefiLlama、Aave 官方博客与治理论坛。

| 指标 | 最新快照 | 解释 |
| --- | --- | --- |
| 价格 | `约 115.82 美元` | CoinGecko 快照 |
| 市值 | `约 17.58 亿美元` | 仍属大型 DeFi 蓝筹 |
| FDV | `约 18.52 亿美元` | 市值与 FDV 差距已不大 |
| 流通量 | `15.184M AAVE` | 约占总量 `94.9%` |
| 总量 / 最大供应 | `16M AAVE` | 固定上限，长期无再增发空间 |
| TVL | `约 247.5-248.9 亿美元` | DeFi 借贷龙头体量 |
| Borrowed | `约 175.6 亿美元` | 真实借贷使用深度很高 |
| 协议年化 Fees | `约 5.79 亿美元` | 资金使用非常真实 |
| 年化 Revenue | `约 7823 万美元` | 属于 DeFi 中已较成熟的收入规模 |
| 年化 Holders Revenue | `约 7809 万美元` | 对 AAVE 价值捕获最重要 |
| Treasury | `约 1.03 亿美元` | DAO 财政仍然健康 |
| Staked | `约 3.51 亿美元` | 约占市值 `19.8%` |
| 24h 成交额 | `约 3.94 亿美元` | 流动性优秀 |
| Buyback 合约持仓 | `约 191,565 AAVE` | CoinGecko 口径，按现价约 `2219 万美元` |
| 协议市值 / TVL | `约 0.07x` | 协议资产底盘远大于 token 市值 |
| 市值 / 年化 Revenue | `约 22.5x` | 已不是便宜资产，但也不离谱 |
| 市值 / 年化 Fees | `约 3.0x` | 说明大量费用最终仍未直接完全流向持币人 |

还可以补三组很关键的定性指标：

- Aave `2025` 年末占 `61.5%` 的活跃借贷市场份额、`52.4%` 的借贷板块 TVL、`43.2%` 的借贷板块收入。
- 官方 `2026` 研究文章写到：Aave 拥有 `约 200 亿美元` 的稳定币存款，占借贷协议稳定币流动性的 `70-90%`。
- Horizon 在 `2026-03` 官方博客口径下已有 `450M+` 净存款、`约 135M` 借款量，是目前最大的 RWA 借贷市场。

这些数字共同说明一件事：`Aave 不是靠叙事硬撑的协议，它已经是链上信用与稳定币流动性的核心基础设施。`

## 解锁与供给压力快照

AAVE 的供给结构，现在已经比绝大多数 DeFi 代币清晰得多。

- 总量上限是 `16,000,000 AAVE`。
- CoinGecko 快照显示，当前流通量 `15.184M`，约占总量 `94.9%`。
- 主要非流通部分包括：
  - `Aave Ecosystem Reserve`：约 `663,810 AAVE`，约占总量 `4.15%`
  - `LEND Migration contract`：约 `303,373 AAVE`
  - `Rewards contract`：约 `321,042 AAVE`
  - `BuyBack contract`：约 `191,565 AAVE`

近未来 `30/90/365 天` 的结论：

- 典型 VC cliff：`无`
- 线性解锁表：`无公开、清晰、近月型释放时间表`
- 结构性通胀：`无新上限扩张`
- 真正需要关注的是 `Reserve 如何被治理使用，以及 buyback 与 emissions 的净效应`

这里最重要的变化，不是 “有没有解锁”，而是：

`AAVE 正在从“靠排放维护安全与流动性”的旧模型，转向“降低排放 + 程序化买回 + 国库回收”的新模型。`

几个关键事实：

- `2025-03-04` 的 Aavenomics Part One 提案授权 `前 6 个月按每周 100 万美元` 速度执行 buyback。
- `2025-09-10` 的 Umbrella emission update 提到：Safety Module 日排放已从 `2025` 年初的 `820 AAVE/day` 逐步降到 `300 AAVE/day`。
- 同一提案里，若按当时价格测算，buyback 速度大约为 `476 AAVE/day`，意味着 DAO 在净持仓层面开始 `净增 AAVE`。

因此，我对供给压力的判断是：

- `短期解锁压力：低`
- `中期稀释风险：低于大多数 DeFi 代币`
- `长期供给方向：更偏通缩 / 回收，而不是继续释放`

但也必须补一句：`buyback 目前主要回收到 reserve，不等于直接 burn。`

## 节点与验证者概况

对 AAVE 这个资产本身来说，这一项 `严格意义上不适用`。

- Aave 是多链部署的借贷协议，不是一条独立 L1/L2，因此不存在一个统一的原生 validator set。
- 它运行在 Ethereum、Base、Arbitrum、Avalanche、Aptos 等多条链上，实际安全性依赖各底层链、预言机、风控参数和治理执行。
- 如果要看 “协议安全节点”，核心并不是看验证者数量，而是看：
  - 底层链安全性
  - Oracle 体系
  - 风险服务商配置
  - 治理与应急权限

`2026-03-11` 的 wstETH CAPO 事故也再次证明：Aave 的关键风险更多来自 `参数配置、风控执行、服务商协同`，而不是来自“原生节点不够多”。

因此，对 AAVE 更有意义的安全观察指标是：

- 是否出现坏账
- 清算系统是否稳定
- 风险参数调整是否及时
- 预言机与 risk steward 流程是否稳健

## 股票信息与核心指标

不适用。AAVE 是加密资产，不是股票。

## 赛道定位

- 主赛道：`DeFi 借贷 / 链上信用基础设施`
- 次赛道：`稳定币流动性层 / RWA 借贷 / 嵌入式 DeFi 基础设施`

这是评估 Aave 最准确的框架，因为今天的 Aave 已经不是单纯的 “借贷 App”，而更像：

- 链上稳定币利率基准层
- 钱包与 fintech 的底层收益接口
- 新型资产与链的默认信用引擎
- RWA 抵押借贷市场的制度化入口

所以，对 Aave 的判断不能只停留在 “TVL 高不高”，而要看它是否已经变成 `默认信用层`。

## 核心投资逻辑

- `Aave 已经是链上信用的默认基础设施。` 这体现在规模、收入、稳定币流动性深度、分发集成和市场份额上。
- `Aave 的产品边界正在扩张。` V4、Horizon、Aave App、MetaMask/Kraken 等嵌入式分发让它从 DeFi 协议走向“信用操作系统”。
- `AAVE 的 tokenomics 明显改善。` 排放下降、buyback 持续、Umbrella 改造、未来 Anti-GHO，都让 AAVE 从“弱捕获治理币”往“更有财务抓手的资产”转。
- `市场真正要赌的是两件事。` 第一，Aave 能不能继续扩大在 stablecoins、RWA、embedded finance 里的基础设施地位；第二，这些增长能不能继续转成更强的 AAVE 回购和更明确的持币价值。

## 反方观点与证伪条件

最强的反方观点不是 “Aave 不行”，而是：

`Aave 协议极强，但 AAVE 代币的价值捕获仍不够直接；买回回到 reserve，不是分红，也不是彻底 burn。`

具体反方逻辑包括：

- `反方一：token capture 仍不如协议强度。`
  协议年化 fees 接近 `5.8 亿美元`，但持币人真正可感知的价值回流仍然偏间接。
- `反方二：竞争没有结束。`
  Morpho、Spark、Sky、Euler 等都在不同维度切走份额，尤其在资本效率和定制市场方面。
- `反方三：治理与服务商复杂度提高了操作风险。`
  `2026-03-11` 的 CAPO 事故就不是黑客，而是配置与流程问题。
- `反方四：AAVE 不是低估到离谱。`
  当前市值 / 年化 holders revenue 约 `22.5x`，不能再按“完全没有 capture”的价格来买。

证伪条件也比较清晰：

- 如果未来 12 个月 buyback 节奏明显放缓，或者 Aavenomics Part Two 长期不落地，AAVE 的 token 重估逻辑会削弱。
- 如果 V4 主网上线明显延后、Horizon 增长停滞、Aave App/embedded distribution 不见放量，那么 “信用操作系统” 叙事会降级。
- 如果协议出现坏账、连续风控事故或重大监管压制，Aave 作为“机构级 DeFi 基础设施”的溢价会被打掉。

## 市场可能忽略的变量

- `Aave 已经越来越像“稳定币基础设施”，而不只是借贷协议。`
  这类定位的护城河比单一 DeFi 产品更深。
- `Aave 的分发能力正在外部化。`
  MetaMask、Kraken、Bitget Wallet、Ledger、拉美 fintech 接入，意味着用户很多时候甚至不需要“先成为 Aave 原生用户”，也能给 Aave 带来存款。
- `Horizon 可能是 Aave 的第二增长曲线。`
  如果 RWA 真正上链，Aave 比多数 DeFi 协议更有制度和产品准备。
- `buyback 是重要拐点，但不是终点。`
  现在的关键争论不再是 “有没有 buyback”，而是 “reserve accumulation 最终会如何反映到每个 AAVE 上”。
- `最近的 CAPO 事故可能反而强化治理改进。`
  这类事故短期伤害情绪，但也可能迫使 Aave 在服务商责任、风控流程和参数验证上更制度化。

## 对标项目比较

对 AAVE 最合理的对标，不是 BTC 或 ETH，而是其他 `借贷 / 信用协议与相关价值捕获代币`。

我选择：

- `Morpho`
- `SKY / Spark`
- `COMP / Compound`

原因分别是：

- `Morpho` 代表新一代模块化、资本效率更高的借贷架构
- `SKY / Spark` 代表与稳定币财政深度绑定、价值捕获更直接的信用体系
- `COMP` 代表老牌治理型借贷 token 的历史参照

| 对标对象 | 为什么可比 | Aave 相对优势 | Aave 相对劣势 |
| --- | --- | --- | --- |
| `Morpho` | 同属借贷 / 信用基础设施 | 规模更大、资产更全、品牌与风控体系更成熟、机构叙事更强 | Morpho 在定制市场、模块化效率和轻资产扩张上更灵活 |
| `SKY / Spark` | 稳定币与借贷的深度绑定体系 | Aave 更中立、更跨资产、更跨链，分发更广 | SKY / Spark 的 token economics 与稳定币利润联动更直接 |
| `COMP` | 历史蓝筹借贷治理币 | Aave 在收入、产品迭代、生态分发和心智上全面领先 | 几乎无明显劣势，除非认为更复杂也意味着更多执行风险 |

我的相对估值判断是：

- 相对 `COMP`，AAVE 应该长期享受 `显著溢价`。
- 相对 `Morpho`，AAVE 的规模与安全溢价有道理，但不能忽略 Morpho 的资本效率优势。
- 相对 `SKY / Spark`，AAVE 在“协议质量”上可以给溢价，但在“当前直接 token capture”上未必应该给过大溢价。

一句话说：`AAVE 是高质量借贷龙头，值得比旧式治理币贵，但如果只看当前直接回流，它还没贵到可以毫无保留地给极端溢价。`

## 执行摘要

Aave 仍是链上借贷和稳定币流动性的绝对龙头，而且 `2025-2026` 的发展让它开始从“最大借贷协议”升级为“链上信用基础设施”。Aave V4、Horizon、Aave App、embedded finance 分发，以及 MetaMask/Kraken/fintech 集成，把 Aave 的增长路径从单一 DeFi 用户扩展到稳定币发行方、机构、钱包和移动端储蓄产品。AAVE 代币层面也确实发生了关键改善：排放下降、buyback 持续、Umbrella 改造落地，历史上“协议强、代币弱”的矛盾正在被修复。问题在于，`修复` 不等于 `完全解决`。当前 buyback 更多回流到 reserve，而不是等价于直接分红或彻底 burn，因此 AAVE 的价值捕获依然比协议层面间接。`2026-03-11` 的 CAPO 事故也提醒市场：Aave 的主要风险不再是是否有 PMF，而是作为系统级基础设施，治理、参数和服务商流程必须越来越机构化。我的总判断是：`Aave 协议前景为强，AAVE 代币前景为中性偏强；想要进一步重估，必须继续看到 V4、Horizon 和 buyback 三条线同时兑现。`

## 历史大事件与影响意义

### 1. 2017-11：ETHLend 诞生与 ICO

发生了什么：Aave 的前身 ETHLend 在 ICO 时代诞生。  
当时的直接影响：项目最初以点对点借贷为主，定位仍偏早期实验。  
长期意义：它为后续从 P2P 借贷转向池化借贷奠定了起点。  
延续影响：Aave 今天的开放金融定位，仍保留了早期“无许可信用市场”的基因。

### 2. 2020-01 到 2020-12：ETHLend 重品牌为 Aave，LEND 向 AAVE 迁移，Aave V2 推出

发生了什么：项目完成品牌重塑，推出 Aave V2，并完成从 `LEND` 向 `AAVE` 的迁移。  
当时的直接影响：Aave 从旧时代 ICO 项目升级为 DeFi 核心基础设施，并通过 flash loans、credit delegation 等功能迅速建立差异化。  
长期意义：这确立了 Aave 作为 DeFi 借贷蓝筹的核心位置。  
延续影响：AAVE 的固定上限、迁移合约尾巴、治理架构都来自这一阶段。

### 3. 2023-07：GHO 稳定币上线

发生了什么：Aave 推出原生超额抵押稳定币 GHO。  
当时的直接影响：Aave 第一次把“借贷协议收入”延伸到“稳定币财政收入”。  
长期意义：这让 Aave 的商业模式从单纯收取 reserve factor，扩展到可持续的自有货币收益。  
延续影响：今天 Aavenomics、Anti-GHO、sGHO 和 buyback 逻辑，都离不开 GHO 的利润池。

### 4. 2024-07 到 2024-08：Aavenomics 更新 temp check 获批

发生了什么：Aavenomics 更新被温度检查与治理通过。  
当时的直接影响：市场第一次比较清晰地看到，Aave 准备系统性调整 Safety Module、排放、buyback 与 revenue redistribution。  
长期意义：这标志着 AAVE 不再满足于“协议强、token 一般”的旧状态。  
延续影响：2025-2026 的 buyback 和 Umbrella 改造，都是这次更新的延伸。

### 5. 2025-03 到 2025-09：Aavenomics Part One、Umbrella、排放下调与 buyback 落地

发生了什么：`2025-03-04` 发布 Aavenomics Part One；`2025-06-05` Umbrella 生效；`2025-09-10` 提案把 Safety Module 日排放进一步压到 `300 AAVE/day`，同时 buyback 已经买入 `84,640 AAVE`。  
当时的直接影响：AAVE 的经济模型开始从高排放防御，转向低排放 + buyback + reserve accumulation。  
长期意义：这是真正改变 AAVE 代币估值框架的事件。  
延续影响：未来 12 个月市场看 AAVE，核心就是看这条链路能否继续深化。

### 6. 2025-08：Aave Horizon 上线

发生了什么：Aave Labs 推出 Horizon，把 RWA 作为抵押品引入链上借贷。  
当时的直接影响：Aave 不再只服务 crypto-native collateral，也开始服务 tokenized treasuries 与机构资产。  
长期意义：这为 Aave 打开了更大的潜在 TAM，也把机构与合规叙事做实。  
延续影响：今天 Horizon 已成为 Aave 第二增长曲线的核心候选。

### 7. 2025-12：Aave V4 测试网与代码公开，官方指向 2026 主网

发生了什么：Aave V4 完成测试网阶段，Hub-and-Spoke 架构公开。  
当时的直接影响：市场开始把 Aave 理解为“统一流动性 + 风险隔离”的信用操作系统。  
长期意义：V4 是 Aave 未来几年继续扩大协议边界的关键技术基础。  
延续影响：2026 年主网兑现与否，将深刻影响 AAVE 的下一阶段估值。

### 8. 2026-03-11：wstETH CAPO 事故与赔付提案

发生了什么：wstETH CAPO 风险预言机参数错配引发 34 个账户的错误清算；DAO 推出用户赔付提案。  
当时的直接影响：短期打击了市场对“机构级风控”的信心。  
长期意义：这提醒市场，Aave 的系统性风险更多来自配置与治理流程，而不是单纯合约漏洞。  
延续影响：未来服务商责任、风控 QA 与参数管理机制可能被进一步制度化。

## 1. 最近生态进展

2025-2026 的 Aave 生态进展，可以概括为一句话：

`Aave 正从 DeFi 借贷龙头，扩展为稳定币、RWA、钱包和 fintech 默认接入的信用底层。`

最值得关注的进展有：

- `Aave Horizon`：
  `2025-08` 上线，启动时就支持 Circle、Superstate、Centrifuge 等资产与机构网络；`2026-03` 官方表示 Horizon 已有 `450M+` 净存款与 `约 135M` 借款量，是最大的 RWA 借贷市场。
- `Aave V4`：
  `2025` 年测试网与代码上线，官方在年终回顾中明确写到 `2026` 主网上线；核心是 Hub-and-Spoke、统一流动性与风险隔离。
- `Aave App`：
  提供 `最高 9% APY`、`12,000+` 银行入金、`100 万美元` balance protection，且 Push Virtual Assets Ireland Limited 已拿到 MiCAR/CASP 牌照。
- `嵌入式分发`：
  Aave 已成为 MetaMask Stablecoin Earn、Kraken DeFi Earn、Bitget Wallet、Ledger、Tangem、以及拉美 fintech 的底层收益接口。
- `稳定币基础设施化`：
  官方研究文章写到 Aave 拥有 `200 亿美元` 稳定币存款、`130 亿美元` 稳定币借款，是稳定币发行方扩张的首选场所。
- `Aptos 部署`：
  Aave V3 在 Aptos 上线，说明协议正在尝试超越 EVM 单一边界。
- `风险事件与善后`：
  `2026-03-11` wstETH CAPO 事故暴露流程问题，但也显示了 DAO 有能力快速推进赔付与恢复信任。

这些进展的意义并不一样：

- Horizon 扩的是 `资产边界`
- V4 扩的是 `架构边界`
- Aave App 与 MetaMask/Kraken 扩的是 `分发边界`
- Aavenomics 扩的是 `持币价值边界`

## 2. 最近 X 上的讨论

由于本次没有逐条抓到完整 X 原帖流，这一节主要基于 Aave 官方博客、治理论坛、以及可索引的社区讨论做归纳，属于 `二手归纳，不是逐条推文复盘`。

近期围绕 Aave / AAVE 的讨论，主要集中在六条线：

- `多头主线一：AAVE 终于有真钱买回了。`
  过去几年 AAVE 最大痛点就是 token capture 太弱；现在 buyback 已经不是概念，而是链上持仓现实。
- `多头主线二：Aave 不再只是借贷协议，而是 stablecoin / fintech / wallet infra。`
  MetaMask、Kraken、Bitget Wallet、拉美 fintech 这类合作，被视为 Aave 进入外部流量的关键证明。
- `多头主线三：Horizon 和 V4 打开了下一阶段 TAM。`
  社区乐观者认为 RWA 与 unified liquidity 会把 Aave 带到新的规模层级。
- `空头主线一：buyback 回 reserve，不是 burn。`
  一部分投资者认为，AAVE 的 capture 仍然偏“资产负债表改善”，不是直接持有人分红。
- `空头主线二：服务商复杂度与流程风险上升。`
  `2026-03-11` 的 CAPO 事故强化了这点。
- `空头主线三：Anti-GHO 等后续 tokenomics 兑现速度不够快。`
  市场仍在等待更完整的 Part Two 路线。

我的理解是：

`市场今天对 Aave 的争议，已经不再是“协议强不强”，而是“AAVE 代币的价值回流，能不能继续从‘正在改善’走到‘已经足够强’”。`

## 3. 经济模型

AAVE 的经济模型，现在应该拆成五层来看。

### 3.1 供给层

- 总量上限 `16M`
- 流通约 `15.184M`
- 主要剩余库存集中在 reserve、migration、rewards 与 buyback 合约

它的核心特征是：

`供给已经很有限，真正的关键不再是解锁，而是库存调度和 buyback 累积。`

### 3.2 收入层

截至 `2026-03-19` 前后：

- 年化 fees 约 `5.79 亿美元`
- 年化 revenue 约 `7823 万美元`
- 年化 holders revenue 约 `7809 万美元`

这说明 Aave 协议已经是 DeFi 里极少数有真实、可持续收入规模的项目。

### 3.3 安全与流动性层：Umbrella / Safety Module

Umbrella 的意义，不只是“新版本保险池”，而是同时解决：

- 风险覆盖
- 流动性承诺
- 排放效率
- 长期 tokenomics 重构

`2025-09-10` 的官方治理提案显示：

- Umbrella 存款从 `248.9M` 增至 `357.0M`
- Safety Module 日排放从年初 `820 AAVE/day` 降到提案后的 `300 AAVE/day`
- stkAAVE 的 slashing 风险朝 `0%` 方向推进，cooldown 也缩短

这使 AAVE 的质押，不再只是“冒着高 slashing 风险换排放”，而是更接近 `低风险收益 + 协议对齐资产`。

### 3.4 回购层：buyback 已从实验走向制度

`2025-03-04` 的 Aavenomics Part One 明确：

- 先按 `100 万美元/周` 执行 6 个月
- 之后按季度 / 年度预算持续化

`2025-10-22` 的 buyback program update 又把目标升级为：

- `5000 万美元 / 年`
- 每周执行范围 `25 万 - 175 万美元`

截至 `2026-03-19`，CoinGecko 显示 buyback 合约里已经有 `191,565 AAVE`，按现价约 `2219 万美元`。

这意味着：

`AAVE 已经从“希望未来回购”进入“回购正在发生且规模在变大”的阶段。`

### 3.5 未完成层：Anti-GHO 与更强的持币收益

尽管 buyback 已落地，但 Aavenomics 并未完全收官。

- Anti-GHO 仍属于后续 tokenomics 升级的一部分
- buyback 目前主要回 reserve，而不是直接 burn
- AAVE 仍没有像股票分红一样的直接收益权

所以当前更准确的表述是：

`AAVE 的捕获路径已经变强，但还没有走到终局。`

## 4. 前景分析

### 4.1 协议前景：强

我对 Aave 协议本身的看法偏强，原因有五个：

- `规模和心智已经压制同类。`
- `收入真实且可持续。`
- `稳定币流动性深度形成了很强的正反馈。`
- `嵌入式分发让它进入更多非原生用户场景。`
- `V4 + Horizon 把未来天花板抬高。`

真正需要观察的，不是 Aave 有没有 PMF，而是它能否继续把优势扩展到：

- RWA
- 钱包与 fintech
- 移动端储蓄
- 非 EVM
- 更复杂的信用市场

### 4.2 AAVE 代币前景：中性偏强

我对 AAVE 比对协议本身更谨慎，但仍偏正面。

原因也很清楚：

- 正面：buyback、低排放、strong treasury、Umbrella 已让代币明显改善
- 保守：capture 仍不如协议层面直接，buyback ≠ burn ≠ 分红

因此，AAVE 当前更像：

`一家非常强的金融基础设施公司，已经开始回购并减少稀释，但回购带给股东的价值还不是完全即时与线性的。`

## 5. 捕获价值分析

这是 AAVE 最重要的一节。

### 5.1 过去的问题

过去几年，Aave 一直存在一个经典矛盾：

- 协议层面领先
- 代币层面捕获较弱

用户用 Aave、协议赚 revenue，不代表 AAVE 持有人马上得到很强的财务回报。

### 5.2 现在的变化

现在，AAVE 的捕获链条已经明显改善：

1. 协议产生 reserve factor 收入与 GHO 收入  
2. DAO 财政变强  
3. 排放被持续压低  
4. 多余收入开始用于买回 AAVE  
5. 买回的 AAVE 回到 reserve，提升 treasury 对 token 的对齐度  

这至少解决了一个老问题：

`Aave 不再是“协议赚钱但 token 一点都不回流”的项目。`

### 5.3 但为什么我仍然不把它当成最直接的现金流币

因为：

- buyback 主要回 reserve，不是 burn
- reserve 的最终用途仍由治理决定
- 持有人没有自动获得现金流分配

因此，AAVE 今天更像 `提升每币国库支持度与治理资产稀缺性`，而不是等价于拿到股息。

### 5.4 当前估值反映了什么

按当前数据粗看：

- 市值 / 年化 holders revenue `约 22.5x`
- 市值 / 年化 fees `约 3.0x`
- 市值 / TVL `约 0.07x`

这说明市场并不是按“高股息”在定价 AAVE，而是在定价：

- 协议龙头地位
- 稳定币与信用基础设施位置
- V4 / Horizon / App 的未来扩张
- tokenomics 持续改善的预期

### 5.5 真正的下一步

AAVE 要从“改善中的 capture”走向“强 capture”，最关键的三条线是：

- `长期 buyback 持续执行`
- `Anti-GHO / revenue redistribution 更完整落地`
- `V4 / Horizon / GHO 把收入池继续做大`

所以，我对 AAVE 的结论是：

`AAVE 的价值捕获已经不弱，但还没有强到市场可以完全忽略治理裁量和未来设计空间。`

## 6. 未来 12 个月将要发生的进展和重要事件

从 `2026-03-19` 往后看，我最关注以下时间窗：

- `2026`：Aave V4 主网上线是否按官方节奏兑现。
- `2026`：Aavenomics buyback program 是否继续按更长期预算执行，且 buyback 持仓继续增长。
- `2026`：Aavenomics Part Two / Anti-GHO 是否继续推进。
- `2026`：Horizon 是否引入更多 RWA 抵押品和机构合作方。
- `2026`：Aave App 是否扩大地域覆盖与真实用户数。
- `2026`：MetaMask、Kraken、fintech 与钱包分发是否继续带来可观净存款。
- `2026`：wstETH CAPO 事故后的流程改进与服务商责任机制是否建立得更清晰。
- `2026`：GHO 供应与 sGHO 使用率是否继续抬升。

未来一年最关键的验证点，其实可以压缩成四条：

- `V4 会不会顺利主网`
- `buyback 会不会持续累积`
- `Horizon 会不会继续放量`
- `Aave 的外部分发会不会让它真正走向百万级用户`

## 7. 未来 12 个月价格走势预测

这一节是情景分析，不是确定性预测。基准价格参考 `2026-03-19` 前后约 `115-117 美元`。

| 情景 | 价格区间 | 核心假设 | 证伪条件 |
| --- | --- | --- | --- |
| 熊市情景 | `70-95 美元` | Alt 流动性回落；借贷需求和 fees 收缩；buyback 放缓；V4 延期；竞争者继续蚕食新增市场；再出风控事故 | 若 buyback 保持强度、V4 顺利推进、Aave 继续领跑 stablecoin 流动性，该情景失效 |
| 基准情景 | `125-180 美元` | Aave 维持借贷龙头；buyback 持续；Horizon 和 App 温和放量；V4 进展稳定但尚未完全形成收入爆发 | 若 token capture 没有进一步改善，该情景上沿难到 |
| 牛市情景 | `220-320 美元` | V4 主网成功；Horizon 成为 RWA 借贷标准层；Aave App / MetaMask / Kraken 等分发显著放大存款；buyback 与 Anti-GHO 强化 AAVE 捕获 | 若协议增长继续强但持币价值仍偏间接，则牛市上沿难实现 |

为什么我不直接给更高牛市目标？因为 `AAVE 已经不是便宜废票`。它需要更强的 token capture 与新产品兑现，才能支撑更激进的倍数扩张。

## 8. 全方位多角度分析

这一节不只给“强 / 中性 / 弱”的标签，而是逐个维度回答：

`Aave 协议强在哪里，AAVE 代币还差哪一步，市场到底在给什么溢价。`

### 8.1 技术架构：`强`

- `现状`
  Aave V3 已经是多链主流借贷底座，V4 的 Hub-and-Spoke 架构进一步把“统一流动性 + 风险隔离”组合起来。
- `为什么重要`
  借贷协议越往后，决定胜负的不只是利率，而是能否在不碎片化流动性的前提下支持更多风险类型和资产。
- `谁受益，谁承担成本`
  机构、稳定币发行方和大额用户最受益；承担成本的是协议复杂度与治理协调成本上升。
- `未来验证点`
  `V4 主网上线后的真实资金迁移率` 和 `新市场启动效率` 才是关键。

### 8.2 产品与真实需求：`强`

- `现状`
  Aave 解决的是链上最硬的需求之一：`用已有资产获得信用与收益`。
- `为什么重要`
  这不是可有可无的工具，而是 DeFi 的核心金融原语。稳定币、RWA、fintech 接口越发展，信用层越关键。
- `结论`
  Aave 的需求不是叙事驱动，而是金融功能驱动，这让它的基本面质量高于多数协议。

### 8.3 用户与采用：`强`

- `现状`
  Aave 已不只是原生 DeFi 老用户在用它，钱包、交易所、fintech、机构和稳定币发行方都在接入。
- `为什么重要`
  这意味着 Aave 的新增流量来源，不再只依赖散户和 DeFi degens。
- `关键观察`
  未来更应盯 `净存款质量`、`机构资产`、`嵌入式渠道贡献`，而不是单纯地址数。

### 8.4 稳定币基础设施属性：`非常强`

- `现状`
  官方数据显示 Aave 有 `200 亿美元` 稳定币存款，占借贷协议稳定币流动性的 `70-90%`。
- `为什么重要`
  这让 Aave 更像链上美元市场，而不只是多资产借贷平台。
- `二阶影响`
  一旦新的稳定币发行，最容易做大的路径之一就是上 Aave。这会形成强网络效应。

### 8.5 经济模型与供需：`中性偏强`

- `现状`
  16M 上限、94.9% 流通、低解锁风险、排放持续下降、buyback 持续累积。
- `为什么重要`
  这使 AAVE 的供需环境比 2023 年前健康得多。
- `限制`
  供给更友好不代表 token 一定爆发，需求与捕获强度仍是主变量。

### 8.6 价值捕获：`中性偏强，但尚未到终局`

- `现状`
  buyback 已落地，排放下降，holders revenue 进入可建模区间。
- `为什么重要`
  这让 AAVE 终于摆脱“协议强、token 弱”的旧标签。
- `尚未完成的地方`
  buyback 回 reserve、Anti-GHO 未完全落地，说明它还不是最直接的现金流 token。

### 8.7 竞争格局：`中性偏强`

- `现状`
  Aave 仍然是绝对龙头，但 Morpho、Spark、Sky、Euler 在不同子领域都具备威胁。
- `为什么重要`
  借贷市场不是赢家通吃，尤其是定制化、隔离市场和稳定币财政市场上。
- `结论`
  Aave 在“默认、通用、深流动性”上最强；对手在“更激进、更模块化、更垂直”上更灵活。

### 8.8 治理与服务商体系：`中性`

- `现状`
  Aave 的治理很成熟，但也越来越依赖多服务商、风险提供方和专业委员会。
- `为什么重要`
  复杂治理提升了机构化能力，也提高了流程失误的可能性。
- `最近的提醒`
  CAPO 事故说明现在的主要风险之一是“配置与流程错误”，而不是代码没审计。

### 8.9 安全与系统风险：`中性偏强`

- `现状`
  Aave 过往在大规模清算中表现极强，`2025` 年处理了 `11 亿美元+` 清算而无系统性问题。
- `为什么重要`
  对信用基础设施来说，真正的品牌是“在压力下还能稳”。
- `风险边界`
  最近事故说明系统强不等于完全没有 operational risk，尤其在复杂 risk modules 下。

### 8.10 流动性与市场结构：`中性偏强`

- `现状`
  AAVE 交易流动性好、衍生品覆盖广、DEX/CEX 深度都在。
- `为什么重要`
  这使 AAVE 能承接大资金，但也让它更容易被当成 DeFi beta 龙头来交易。
- `结论`
  AAVE 兼具基本面和高 beta 属性，牛市里弹性高，熊市里也不会绝对防御。

### 8.11 宏观与监管敏感度：`中性`

- `现状`
  Aave 同时受 crypto 风险偏好、稳定币监管、利率环境与 tokenized assets 政策影响。
- `为什么重要`
  它不像 meme 币那样只靠情绪，也不像股票那样有稳定估值框架，而是两者之间的混合体。
- `关键判断`
  当稳定币扩张、风险偏好改善、tokenized treasuries 发展时，Aave 通常是最先受益的协议之一。

### 8.12 AI 相关性：`中性偏低`

- `现状`
  Aave 不是 AI 原生协议，但很适合作为 AI 代理的信用层和资金管理层。
- `为什么重要`
  如果未来 AI agents 需要自动管理稳定币、借贷和收益，Aave 很自然会成为底层之一。
- `结论`
  AI 不是当前主要定价锚，但可能是长期二阶催化。

把上面 12 个角度压缩成一句话，就是：

`Aave 已经在“信用基础设施、稳定币流动性、外部分发、收入质量”四个维度证明了自己；AAVE 还要继续证明的，是这种协议优势能否更直接、更持续地回流给持币者。`

## 9. 与 AI 相关的重点分析

Aave 与 AI 的关系，我的判断是：`相关，但不是核心驱动。`

最适合 Aave 的 AI 结合方向有三类：

- `AI Agent Treasury Management`
- `自动化稳定币现金管理`
- `基于策略的借贷与杠杆调度`

为什么 Aave 合适？

- 深流动性
- 标准化接口
- 多链部署
- 稳定币市场成熟

AI 对 Aave 的第一层影响，不是买入 AAVE，而是：

- 增加存款与借款频次
- 提高 stablecoin cash management 需求
- 放大 Aave 作为 default yield layer 的地位

只有当这些新增需求继续转成 revenue 与 buyback，AI 才会成为 AAVE 的代币利好。

所以结论是：

`AI 对 Aave 是产品层加分项；对 AAVE 是潜在二阶利好，而不是当前估值主线。`

## 10. 最新路线图

从 `2025` 年末到 `2026` 的官方材料看，Aave 当前路线图可归纳为五条：

### 已经落地的部分

- Horizon 上线
- Aave App 推出
- V4 测试网和代码公开
- Umbrella 升级
- Aavenomics buyback program 启动
- V3 on Aptos

### 仍待兑现的部分

- `V4 mainnet`
- `Anti-GHO / Aavenomics Part Two`
- 更广泛的嵌入式金融分发
- Horizon 的更多资产和机构接入
- App 的更广泛地区开放与用户增长

如果把路线图翻译成一句更直白的话，就是：

`Aave 想从 DeFi 里最大的借贷协议，变成链上世界默认的信用操作系统。`

## 11. 宏观经济对此标的的影响

Aave 对宏观的敏感度，和 BTC、纯 meme 币、L1 都不完全一样。

它更像：

`风险偏好 + 稳定币需求 + 利率环境 + 链上杠杆需求` 的混合资产。

最关键的传导路径有四条：

- `利率`
  TradFi 利率下降时，Aave 稳定币收益相对吸引力可能提升。
- `风险偏好`
  风险偏好改善时，借贷需求、杠杆需求和 token 估值一起上升。
- `稳定币扩张`
  稳定币供应增长通常直接利好 Aave。
- `波动率`
  适度波动提升借贷和清算活动，极端风险则压缩估值倍数。

所以 Aave 的宏观特征是：

`协议收入可能在波动中受益，但 token 估值倍数在 risk-off 环境中仍会被压缩。`

## 12. 经济政策的影响

政策对 Aave 的影响，比对多数 DeFi 项目更复杂，因为它横跨：

- 稳定币
- 借贷
- RWA
- 消费者储蓄 App
- 钱包与嵌入式金融

正面因素：

- MiCAR/CASP 之类框架为 Aave App 和合规入口打开空间
- 稳定币监管清晰化会利好 Aave 作为稳定币基础设施
- tokenized treasuries / RWA 合规框架成熟会直接利好 Horizon

负面与不确定因素：

- 消费者借贷、DeFi 前端、收益产品仍可能面临更严格限制
- RWA 产品的司法辖区差异会增加复杂度
- 前端与 App 层的牌照要求可能高于协议层

对 AAVE 来说，政策越清晰，Aave 越容易获得机构和 App 级流量；政策越模糊，AAVE 的估值折价越难消失。

## 13. 股市的影响

AAVE 不是股票，但它会受到美股尤其是金融科技与加密概念股风格影响。

最相关的股票或指数代理包括：

- `COIN`
- `HOOD`
- `NASDAQ 100`
- 部分 tokenization / fintech 概念股

传导路径有三条：

- `高 beta 风险偏好`
  科技股和加密股走强时，AAVE 这类 DeFi 蓝筹更容易获得溢价。
- `金融基础设施框架`
  市场如果开始更重视交易、结算、信用与 tokenized assets 基础设施，Aave 的类比框架会更好。
- `资金配置`
  宏观紧缩时，资金通常更先回到 BTC 与大型股票，而不是 DeFi token。

所以股市对 AAVE 的影响，短期偏情绪，中期偏估值框架。

## 14. 国际战争的影响

国际战争和地缘冲突对 AAVE 的影响，大多是间接的。

主要传导路径包括：

- 风险偏好下降，压制 DeFi 代币估值
- 稳定币与链上结算需求提升，间接利好 Aave 的稳定币流动性角色
- 网络安全与制裁风险上升，增加协议与前端层合规复杂度
- 能源与美元冲击改变风险资产估值

我的净判断是：

- `短期偏负面`
- `中长期偏中性`

因为地缘冲突首先打击的通常是高 beta 资产，但从更长周期看，跨境支付与链上美元体系的重要性上升，又可能利好 Aave 的基础设施属性。

## 15. 区块浏览器地址

建议重点看这几个入口：

- AAVE 代币（Ethereum）：[https://etherscan.io/token/0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9](https://etherscan.io/token/0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9)
- AAVE Buyback 合约： [https://etherscan.io/address/0x22740deBa78d5a0c24C58C740e3715ec29de1bFa](https://etherscan.io/address/0x22740deBa78d5a0c24C58C740e3715ec29de1bFa)
- Aave Web App： [https://app.aave.com/](https://app.aave.com/)

你可以在这些地址里查看：

- AAVE 的持币结构、转账、合约信息
- buyback 合约的持仓变化
- 各链市场的存款、借款、利率和抵押情况

## 16. 智能合约开发用什么语言

Aave 的核心协议栈主要是：

- `Solidity`
- `EVM`

补充两点：

- Aave V4 依然围绕 EVM 架构展开
- Aave V3 on Aptos 则采用 `Move` 语言

所以更准确地说：

`Aave 的主生态是 Solidity / EVM，但它已经开始探索多执行环境。`

## 关键风险

- `buyback 继续，但 token capture 仍偏间接`
- `V4 延期或落地效果不及预期`
- `Horizon / RWA 增长不及预期`
- `Morpho / Spark / Sky 等竞争加剧`
- `服务商流程或参数配置事故`
- `治理复杂度提升`
- `前端、App、收益产品监管趋严`

## 未证实但值得跟踪的问题

- `Aavenomics Part Two / Anti-GHO 何时真正落地？`
- `buyback 回 reserve 最终会不会演化成更直接的持币人收益机制？`
- `stkAAVE 未来是否会被更深地整合进借贷场景，例如作为更核心的抵押资产？`
- `Horizon 会不会成为真正的大规模机构信用市场，而不是样板间？`
- `Aave App 能否把 DeFi 从 native 用户扩展到更广泛的移动端储蓄用户？`

## 参考资料

- [Aavenomics implementation: Part one](https://governance.aave.com/t/arfc-aavenomics-implementation-part-one/21248)
- [Safety Module & Umbrella Emission Update](https://governance.aave.com/t/arfc-safety-module-umbrella-emission-update/23103)
- [AAVE Buybacks program: An update](https://governance.aave.com/t/arfc-aave-buybacks-program-an-update/23290)
- [wstETH CAPO Oracle Incident User Reimbursement](https://governance.aave.com/t/direct-to-aip-wsteth-capo-oracle-incident-user-reimbursement/24275)
- [AL Development Update | June 2025](https://governance.aave.com/t/al-development-update-june-2025/22492)
- [Aave 2025 Year in Review](https://aave.com/blog/aave-2025-recap)
- [Aave Horizon Launches](https://aave.com/blog/horizon-launch)
- [Aave Horizon Supports VanEck's Tokenized Treasury Fund VBILL](https://aave.com/blog/horizon-vaneck-vbill)
- [Aave is Infrastructure for Scaling Stablecoins](https://aave.com/blog/stablecoin-infrastructure)
- [Aave TVL, Fees, Revenue & Income Statement](https://defillama.com/protocol/aave)
- [Aave Price: AAVE Live Price Chart, Market Cap & News Today](https://www.coingecko.com/en/coins/aave)
- [Aave](https://www.aave.com/)
