# Hyperliquid (HYPE) 深度分析报告

- 报告日期：2026-03-19
- 分析标的：Hyperliquid（HYPE）
- 文件标识：hype
- 报告类型：首次覆盖
- 上一版报告：无

## 与上次相比的关键变化

- 首次覆盖。当前最值得盯的变量有五条：`HYPE` 的强价值捕获模型能否继续成立、`HyperEVM` 能否从 alpha 阶段走向更完整应用层、`2026-04-06` 起核心贡献者月度解锁会否压制斜率、去中心化永续市场份额会否被新对手侵蚀、以及美国对链上永续的监管框架会否开始成形。
- 官方文档近一个月的更新重点很清晰：`HyperEVM` 仍处于 `alpha` 阶段，写系统合约和更高吞吐还未上主网；与此同时，权限开放型 `spot quote assets`、`aligned stablecoins`、`HIP-3` 部署型永续与验证者文档持续完善。这说明 Hyperliquid 的主线已经从“单一 perp DEX”推进到“交易链 + 应用链 + 金融基础设施”。
- `2026-02-18`，`Hyperliquid Policy Center` 在美国华盛顿启动，`Hyper Foundation` 承诺 `1,000,000 HYPE` 作为启动资金。这个动作会显著提高项目与美国监管体系的耦合度，也会让市场对政策路径更敏感。
- `USDH` 文档在最近一周显示，这个原生美元稳定币给 Hyperliquid 带来的承诺很具体：`1M HYPE` 锁仓、`50%` 储备收益贡献给 `Assistance Fund`、并支持 `HyperCore / HyperEVM` 双侧使用。对 `HYPE` 来说，这类 aligned stable 可能成为新的价值放大器。

## 关键指标快照

- 价格：约 `$41.99`（CoinGecko 抓取于 `2026-03-19`）
- 市值：约 `$10.02B`
- FDV：约 `$40.46B`
- 流通量：约 `238.39M HYPE`
- 总供应：约 `962.27M HYPE`
- 理论最大供应：`1,000,000,000 HYPE`
- TVL：`$4.69B`（DeFiLlama）到 `$5.13B`（CoinGecko 引用 DeFiLlama 口径）之间
- 30 日永续成交量：约 `$182.48B`
- 24 小时永续成交量：约 `$6.76B`
- 当前未平仓合约：约 `$6.96B`
- 年化协议费用：约 `$769.27M`
- 年化持币者收入：约 `$681.46M`
- 年化协议 earnings：约 `$553.99M`
- 24 小时现货 + 二级交易量：约 `$444.98M`
- Assistance Fund 已移除供应：约 `37.56M HYPE`
- 当前活跃验证者集合：`24`

几个更有决策价值的观察：

- 按 CoinGecko 口径，`市值 / 持币者年化收入` 大约在 `14-15x` 区间；放在加密资产里并不便宜，但放在高增长交易基础设施里也并非夸张。
- `市值 / TVL` 约 `1.95x`，这对一个以高周转交易为核心的协议来说仍可接受。
- `流通 / FDV` 差距很大，说明二级市场当前交易的是一个高质量现金流资产，也同时在交易一条漫长的释放曲线。
- Assistance Fund 把手续费自动转成 `HYPE` 并移出流通，这一点让 Hyperliquid 在 DeFi 里拥有极少见的强价值捕获属性。

## 解锁与供给压力快照

- 公开分配结构来自 CoinGecko / Tokenomist 联合展示与 Tokenomist 页面：
  - `Future Emissions & Community Rewards`：`38.888%`
  - `Genesis Distribution`：`31.0%`
  - `Core Contributors`：`23.8%`
  - `Hyper Foundation Budget`：`6.0%`
  - `Community Grants`：`0.3%`
  - `HIP-2: Hyperliquidity`：约 `0.012%`
- 已解锁流通：约 `238.39M HYPE`，占理论最大供应约 `23.84%`
- 下一次已知解锁：`2026-04-06`
- 下一次解锁规模：约 `9.92M HYPE`
- 下一次解锁接收方：`Core Contributors`
- 完整解锁周期：公开仪表板显示将延续到 `2027`

按当前节奏做保守推演：

- 未来 `30` 天：已知解锁约 `9.92M HYPE`，约占理论最大供应 `1.0%`
- 未来 `90` 天：若近期月度节奏延续，粗算约 `29.76M HYPE`
- 未来 `365` 天：若当前月度释放节奏延续，粗算约 `119M HYPE`

需要注意两点：

- 第一，Hyperliquid 的二级价格并未因过去几轮贡献者释放而立刻失稳，这说明需求侧承接非常强。
- 第二，未来若行情转弱，`9.92M` 这种单月解锁体量会迅速变成压制因子，尤其是在高位震荡阶段。

我的判断：

- `HYPE` 的解锁压力属于“可被买盘吸收，但不能忽视”的类型。
- 单靠“强基本面”不足以让市场完全无视解锁。
- 真正决定价格斜率的，是 `Assistance Fund` 烧币速度、永续市场份额、以及新增生态需求能否持续快于新增流通。

## 节点与验证者概况

- Hyperliquid 链级验证采用 `HyperBFT`，官方 `Running a validator` 文档写明：
  - 运行验证节点与非验证节点都属于 permissionless
  - 活跃验证者集合由按 stake 排名前 `24` 的地址透明决定
- 官方 `Staking` 文档进一步补充：
  - 验证者想变为 active，至少需要 `10k HYPE` 自委托
  - 每笔委托有 `1 天` 锁定期
  - 从 staking 账户提回 spot 账户需要 `7 天` 队列
  - 当前没有自动 slashing，但存在 `jailing` 机制与未来对双签等恶意行为的 slashing 预留
- 官方 `Delegation Program` 文档显示：
  - Foundation 会主动把委托分散给可靠节点，以提升验证网络多样性
  - 申请者需运行至少两个 `non-validator` 节点，且要求 `95%` 以上 uptime
- 官方 `Foundation non-validating node` 文档显示：
  - Foundation 公开提供一个非验证节点做低延迟数据接入
  - 该节点部署在 AWS `apne1-az1`

这部分对投资判断的意义：

- `24` 个活跃验证者集合很小，带来的是低延迟和高性能，也带来更高的验证者集中度风险。
- Hyperliquid 的去中心化质量，高于前端托管式交易平台，低于大规模通用公链。
- 只要它坚持追求极致交易性能，这种“小验证者集合”的设计大概率会长期存在，市场也会持续给一部分去中心化折价。

## 股票信息与核心指标

不适用。

## 赛道定位

- 主赛道：`DeFi / 去中心化永续交易`
- 次赛道：`高性能 L1 / 金融基础设施`

这个框架最适合 `HYPE`，因为它已经同时具备三层属性：

- 一条专为交易和流动性优化的高性能链
- 一个在链上永续市场拥有强产品市场契合度的交易协议
- 一个依靠 gas、staking、上币抵押、手续费回购销毁来捕获价值的基础设施资产

## 核心投资逻辑

- `HYPE` 的核心多头逻辑，在于它把“交易链”“永续交易所”“回购销毁型代币”三件事装进了同一个系统。
- 协议的成交量、手续费、持币者收入和 `Assistance Fund` 烧币形成了非常直接的价值闭环。
- `HyperEVM`、`HIP-3`、permissionless quote assets、aligned stables 让这条链的价值来源从单一永续交易继续外扩。
- 如果 Hyperliquid 能维持链上永续龙头地位，同时把 HyperEVM 生态做深，`HYPE` 估值中枢仍有抬升空间。

## 反方观点与证伪条件

- 反方观点一：Hyperliquid 当前高度依赖永续交易主业务，一旦市场份额被新对手分走，整个价值闭环会同步变弱。
- 反方观点二：紧急干预历史会长期困扰估值。`2025-03` 的 JELLY 事件和更早的 HLP 压力事件，让市场意识到这套系统在极端行情下仍带有强治理与强应急色彩。
- 反方观点三：`HyperEVM` 还在 alpha 阶段。生态想象空间很大，但真正能否跑出应用层收入，目前仍待验证。
- 反方观点四：链级验证集合只有 `24` 个 active validators。对强调高性能的市场来说这可接受，对强调极限去中心化的资金来说这会一直是减分项。

几个明确的证伪条件：

- 未来 `6-12` 个月，永续成交量和未平仓合约持续下滑，且新业务无法补上收入。
- `HyperEVM` 依旧停留在“开发者叙事 + 目录页”，没有显著应用落地和可见 gas 消耗。
- `Assistance Fund` 烧币速度明显放缓，同时核心贡献者解锁继续按月推进，供需平衡转弱。
- 美国对链上永续的监管框架朝强限制方向发展，Hyperliquid 的政策弹性不及市场预期。

## 市场可能忽略的变量

- 市场低估的变量一：`HYPE` 的价值捕获并不只来自“手续费折扣”，更核心的是手续费回流、买回、销毁与供应收缩。
- 市场低估的变量二：`200k HYPE` 的 quote asset 抵押、`500k HYPE` 的 HIP-3 部署抵押，会让生态扩张和代币需求之间出现更直接的连接。
- 市场低估的变量三：aligned stable 模式如果跑通，会把稳定币收益、交易费优惠和 HYPE 锁仓三件事绑定在一起，进一步增强系统黏性。
- 市场高估的变量一：HyperEVM 只要上线，应用生态就会自然繁荣。现实里，HyperEVM 当前仍处 alpha 阶段，距离成熟开发者飞轮还有距离。
- 市场高估的变量二：去中心化交易量持续增长就一定转化为 `HYPE` 价格上涨。解锁节奏、风险事件、竞争强度与监管路径都能改变这个斜率。

## 对标项目比较

- 对标对象：`dYdX`、`GMX`、`Jupiter`
- 为什么选它们：
  - `dYdX` 是最接近的链上订单簿永续协议基准
  - `GMX` 是价值捕获很强的老牌链上永续协议
  - `Jupiter` 代表强分发、强零售和多产品 DeFi 平台路线

### 对比结论

- `HYPE vs dYdX`
  - 两者都走“交易基础设施 + 自有链 / 自有执行层”路线。
  - Hyperliquid 的优势在于产品体验、市场份额、交易深度和收入规模明显更强。
  - dYdX 的优势在于更早的治理传统和更成熟的开放市场认知，但近期市场注意力明显落后。

- `HYPE vs GMX`
  - GMX 的强项是简洁的价值捕获和社区心智。
  - Hyperliquid 的强项是量级、订单簿、速度和更宽的应用外延。
  - 对投资者而言，GMX 更像高现金流协议，HYPE 更像“高现金流协议 + 高成长交易链”。

- `HYPE vs Jupiter`
  - Jupiter 的优势在于 Solana 分发和零售触达。
  - Hyperliquid 的优势在于永续交易主场、统一执行环境、以及更强的交易基础设施属性。
  - 若市场偏好“交易和衍生品基础设施”，HYPE 更占优；若市场偏好“流量入口和多产品钱包 / 路由平台”，JUP 更容易被理解。

### 估值判断

- `HYPE` 相对 `dYdX / GMX / JUP` 理应享有溢价。
- 这层溢价来自市场份额、手续费闭环、生态扩张方式以及供给收缩设计。
- 这层溢价成立的前提，是 Hyperliquid 继续维持链上永续龙头，并把 `HyperEVM` 与 builder 生态做成第二增长曲线。

## 执行摘要

Hyperliquid 当前最强的地方，在于它把链、交易所和代币经济整合成了一个高闭环系统。`HYPE` 的价值捕获链条相当直接：交易活跃带来手续费，手续费流向 `Assistance Fund`，`Assistance Fund` 自动换成 `HYPE` 并移出流通，同时 `HYPE` 还承担 gas、staking、交易费折扣、quote asset 抵押和 `HIP-3` 部署抵押等功能。官方文档近一个月的更新显示，项目的重点已经扩展到 `HyperEVM`、permissionless quote assets、aligned stablecoins 和政策基础设施。当前最大的分歧也很清晰：多头押注它成为链上金融基础设施主入口，空头担心它仍过度依赖永续交易、去中心化质量有限、加上月度解锁会压制估值。我的总体判断是：`HYPE` 仍是当前 DeFi 里最强的一类价值捕获资产，但它已经进入“看持续执行、看供给承接、看政策路径”的阶段，后续上涨更依赖基本面兑现，而非单纯叙事扩张。

## 1. 最近生态进展

- `2026-02-18`：`Hyperliquid Policy Center` 在美国正式启动，`Hyper Foundation` 提供 `1,000,000 HYPE` 作为启动资金。对项目而言，这代表它开始主动参与去中心化永续和链上金融基础设施的政策叙事。
- `2026-02` 到 `2026-03`：`HyperEVM` 文档保持高频更新，官方明确写出当前仍处于 `alpha` 阶段，且更高吞吐和 write system contracts 还未在主网上线。
- 最近一个月：`Aligned quote assets` 和 `permissionless spot quote assets` 文档更新后，稳定币和 quote asset 的抵押门槛、validator 投票、slashing 逻辑都更明确。
- 最近一周：`USDH` 文档显示其作为原生稳定币已承诺 `1M HYPE` 锁仓，并把 `50%` 储备收益贡献给 `Assistance Fund`。
- `2026-02-25`：BitMEX 在 X 上宣布已支持 `Hyperliquid L1` 的原生 `HYPE` 集成和 HYPE 现货交易，这有助于提升外部交易通道与资金可达性。
- `2026-02-09`：生态项目 `tread.fi` 在 X 上披露 Hyperliquid builder revenue 累计突破 `$1M`，说明 builder 生态开始出现更可见的收入信号。

为什么重要：

- Hyperliquid 的增长已经从更大的 perp 盘口，延伸到更完整的稳定币、builder、政策和 EVM 生态。
- 这些扩张线条只要有一两条兑现，`HYPE` 的估值中枢就有继续上抬的条件。

## 2. 最近 X 上的讨论

直接抓取官方 X 原帖受到访问限制，这一节主要结合可索引 X 结果、官方文档和二级研究交叉归纳。

近期 X 上最集中讨论的主题有五个：

- `政策中心`：多头认为这代表 Hyperliquid 开始正面参与美国对链上永续的制度设计；空头担心它会让项目与监管博弈更深度绑定。
- `Builder 收入与生态扩张`：围绕 `tread.fi` 的累计 builder revenue、`USDH` 的 aligned stable 方案、以及 HyperEVM 生态目录，市场在重新评估 Hyperliquid 是否能从“单应用”扩展到“平台型协议”。
- `HYPE 供给与烧币`：市场非常关注 `Assistance Fund` 移出流通、`Core Contributors` 月度解锁、以及市场 cap / FDV / outstanding value 三组口径的差异。
- `BNB 类比`：多头经常把 HYPE 视作“链上交易所 + 销毁 + 应用生态”的高质量标的，试图用 `BNB` 的历史路径做映射。
- `风险事件记忆`：`2025-03` JELLY 事件和极端行情下的 ADL 机制依然被频繁提及，许多人会把它当作 Hyperliquid 在压力测试下的核心弱点。

我的归纳：

- 多头看的是“交易王者 + 价值闭环 + 平台化扩张”。
- 空头盯的是“紧急干预能力 + 解锁节奏 + 竞争分流 + 监管路径”。
- 这类分歧让 `HYPE` 具备很强趋势弹性，也让它在风险事件出现时回撤会更陡。

## 3. 经济模型

`HYPE` 的经济模型非常完整，且比大多数 DeFi 代币更直接。

### 第一层：基础供应

- 理论最大供应：`1,000,000,000 HYPE`
- 当前 CoinGecko 估算总供应：`962.27M HYPE`
- 差值主要来自 `Assistance Fund` 已移出的销毁量

### 第二层：协议手续费闭环

- 官方 `Fees` 文档写明，手续费归属社区侧，核心包括 `HLP`、`Assistance Fund` 和 deployers。
- `Assistance Fund` 会把交易手续费自动转换为 `HYPE`
- 文档明确写出，进入 `Assistance Fund` 的 `HYPE` 会永久移出流通与总供应

### 第三层：代币用途

- `staking`：保护 `HyperBFT` 共识
- `gas`：`HYPE` 是 HyperEVM 的原生 gas token
- `fee discount`：根据 staking 数量提供 `5% - 40%` 交易费折扣
- `quote asset` 抵押：permissionless quote token 需质押 `200k HYPE`
- `aligned stable`：在 quote token 基础上还要额外锁定 `800k HYPE`
- `HIP-3` 部署永续：当前主网要求 `500k HYPE`

### 第四层：通胀与收益

- staking 收益来自 future emissions reserve
- 官方文档给出参考：若总质押约 `400M HYPE`，年化奖励约 `2.37%`

结论非常直接：

- `HYPE` 同时具备“交易收入回流”“供应收缩”“链级 gas”“生态抵押资产”四重需求来源。
- 在 DeFi 代币里，这种模型非常少见。

## 4. 前景分析

如果单看 Hyperliquid 这条链和这套系统会不会继续变强，我的答案偏积极。

看多前景的理由：

- 永续交易已经证明产品市场契合度，Hyperliquid 在链上永续里仍然占据领先位置。
- 统一状态机很关键。`HyperCore` 和 `HyperEVM` 同链共识，让“交易流动性 + 应用层”之间的组合性明显优于跨链拼装方案。
- 官方路线越来越清晰：一边继续守住永续主场，一边往 builder 生态、quote asset、stablecoin 和 EVM 应用层推进。
- 政策中心的成立，说明团队在尝试把链上永续从灰色地带往制度化讨论里推进。

制约前景的因素：

- 永续交易仍是主引擎，业务集中度高。
- HyperEVM 仍在 alpha 阶段，生态爆发并无确定性。
- 验证者集合较小，去中心化折价难以消除。
- 极端风险事件出现时，系统仍需依靠特殊流程和社会层共识来稳定局面。

我的判断：

- Hyperliquid 会继续变强的概率偏高。
- 真正决定上限的，不只是永续 volume，还包括它能否把“流动性层 + 应用层 + 稳定币层”做成复合飞轮。

## 5. 捕获价值分析

`HYPE` 是当前 DeFi 里少见的强价值捕获资产。

价值传导路径主要有六条：

- 手续费回流：交易手续费进入 `Assistance Fund`
- 自动换币：`Assistance Fund` 自动把费用转成 `HYPE`
- 供应收缩：这些 `HYPE` 从 circulating 和 total supply 中移除
- staking：质押保护共识并获得 future emissions reserve 奖励
- 交易折扣：持有和质押 HYPE 可以显著降低交易成本
- 生态抵押：quote token、aligned stable、HIP-3 永续部署都要求锁定大量 HYPE

这套设计的难得之处，在于“协议活跃”和“代币需求”之间的连接非常直接。

也要看清潜在断点：

- 如果交易量下降，买回与销毁也会同步下降。
- 如果 HyperEVM 生态迟迟做不起来，`HYPE` 的长期成长逻辑就会继续依赖永续主业务。
- 如果市场开始怀疑紧急干预机制的边界，哪怕现金流模型依旧强，估值倍数也会下修。

我的结论：

- Hyperliquid 的协议前景和 `HYPE` 的代币捕获，大体上是同向的。
- 这在加密资产里属于质量很高的一类结构。

## 6. 未来 12 个月将要发生的进展和重要事件

- `2026-04-06`：下一次已知 `Core Contributors` 解锁，约 `9.92M HYPE`
- `2026` 全年：若当前节奏延续，核心贡献者月度解锁会继续成为价格层的重要变量
- `HyperEVM`：更高吞吐和 write system contracts 何时上线主网，是应用层成长的关键催化剂
- `Aligned stablecoins`：若 `USDH` 跑通，后续可能吸引更多发行方采用 Hyperliquid 的对齐模式
- `HIP-3`：主网 `500k HYPE` 抵押要求未来预计会下调，这会影响 permissionless perps 的上新速度
- 政策路径：Hyperliquid Policy Center 如何推动链上永续与美国监管框架对话，会显著影响估值溢价
- 更多外部交易与托管支持：类似 BitMEX 这样的原生接入若继续增加，会改善外部流动性和资金可达性

## 7. 未来 12 个月价格走势预测

以下内容仅作情景分析，不构成确定性判断。

- 熊市场景：`$24 - $35`
  - 假设：永续市场份额回落，HyperEVM 进展偏慢，月度解锁压制上涨，监管预期转紧。
  - 证伪条件：成交量与 OI 持续下降，Assistance Fund 烧币速度明显走弱。

- 基准场景：`$45 - $75`
  - 假设：Hyperliquid 维持龙头地位，`HyperEVM` 有阶段性应用落地，aligned stable 与 builder 生态继续扩张，解锁被需求吸收。
  - 这一情景对应的是“高质量交易基础设施资产”被市场持续给出溢价。

- 牛市场景：`$85 - $130`
  - 假设：链上永续继续吃份额，HyperEVM 出现强应用，政策路径边际改善，稳定币与新资产发行层共同放大 `HYPE` 需求。
  - 这一情景本质上依赖市场把 `HYPE` 视作链上金融基础设施的核心资产，而非单一交易币。

## 8. 全方位多角度分析

- 技术架构：`HyperCore + HyperEVM + HyperBFT` 的统一状态设计，是 Hyperliquid 最独特的护城河。
- 产品与需求：永续交易的真实需求已经被证明，应用层需求仍在孵化。
- 用户与采用：高成交量、高 OI、高 fee capture 显示用户黏性很强。
- 经济模型与供需：强烧币闭环对冲部分解锁压力，但解锁仍会影响价格斜率。
- 价值捕获：在 DeFi 里属于极强梯队。
- 竞争格局：`dYdX / GMX / Jupiter / 新一代 perp DEX` 都在抢交易份额，竞争并不轻松。
- 治理与团队：团队执行力强，且自筹资金、无外部资本压力；市场也会持续检验其在极端事件下的边界。
- 安全与风险：ADL、jailing、未来 slashing 预留构成风险控制层，但系统在极端行情下仍有治理依赖。
- 流动性与市场结构：链上与中心化平台双边交易量都在扩大，HYPE 现货深度已明显好于多数 DeFi 代币。
- 社区与叙事：交易王者、BNB 类比、链上金融基础设施，这三条叙事都很强。
- 宏观敏感度：高 beta，受整体 risk appetite 和交易活跃度影响很大。
- 监管与政策：链上永续的合法性框架是估值上限的重要外生变量。
- AI 相关性：存在辅助价值，核心仍在交易与市场基础设施。
- 地域与生态依赖：美国政策路径、全球稳定币扩张、以及跨交易所流动性都很关键。
- 地缘政治与战争敏感度：波动上升时业务数据可能受益，代币价格则取决于市场如何平衡 risk-off 与 volume uplift。

## 9. 与 AI 相关的重点分析

Hyperliquid 与 AI 的关系属于“基础设施可受益”，主业务仍是交易与金融基础设施。

### 最佳结合方向

- AI agent 交易执行与自动化策略网络

### 为什么最适合这条路径

- Hyperliquid 的低延迟订单簿、统一执行环境和原生流动性，非常适合 agent 做高频执行、跨市场风控、自动清算和策略协同。
- `HyperCore` 的深流动性与 `HyperEVM` 的应用层，让 agent 能把“决策”和“执行”放在同一系统里完成。

### 次优方向

- AI 驱动的 vault / copy trading / 风险管理层
- AI 做市与流动性管理工具
- AI 研究与链上交易数据产品

### 相对偏弱的路径

- 大模型训练网络
- 分布式 GPU / 纯算力租赁
- 数据标注市场

这些方向与 Hyperliquid 的原生护城河连接较弱。

### 落地路径

- 先让 agent 用 Hyperliquid 做低摩擦执行
- 再在 HyperEVM 上沉淀可组合的风控、清算、信用与自动化策略应用
- 最后通过 gas、builder 生态与交易收入把这部分需求回流到 `HYPE`

### 价值捕获

- AI 带来的最大增量，会体现在交易量、活跃度、应用层 gas 和新型金融工具上
- `HYPE` 是否受益，仍取决于这些活动能否转成真实费用、真实锁仓和真实烧币

## 10. 最新路线图

Hyperliquid 没有一个传统意义上的单页路线图，当前更像通过文档更新和 HIP 机制来持续披露方向。

已明确成型的方向：

- `HyperCore` 继续巩固链上永续和现货订单簿优势
- `HyperEVM` 作为同链应用层继续推进
- `HIP-3` 让永续部署更 permissionless
- `Permissionless quote assets` 和 `Aligned quote assets` 扩大资产发行与稳定币层
- `Referrals`、builder revenue、部署型 fee share 继续激励外部生态扩张

当前仍待兑现的重点：

- `HyperEVM` 更高吞吐
- write system contracts 上主网
- 更成熟的应用层生态飞轮
- 更多 aligned stable / quote asset 成熟案例
- 更强的验证者与节点多样性

## 11. 宏观经济对此标的的影响

- `HYPE` 对整体 risk appetite 很敏感。
- 牛市里，交易量、未平仓合约、用户活跃度和手续费往往同步上升，`HYPE` 会同时受益于“高 beta”与“高现金流”双重驱动。
- 熊市里，成交和 OI 下滑会直接削弱烧币速度与持币者收入预期。
- 与多数 L1 相比，Hyperliquid 对“市场波动率”更敏感。强波动不一定利空业务，很多时候反而会推高 volume 和 fee。

## 12. 经济政策的影响

- 链上永续属于 `HYPE` 最大的政策变量。
- `Hyperliquid Policy Center` 的成立，说明项目正在尝试把“去中心化永续”带入更正式的政策讨论框架。
- 同时，官方验证者委托项目和 Foundation 非验证节点接入都明确排除了美国、Ontario 以及部分受限制地区，这说明现实中的合规边界已经在影响生态结构。
- 如果美国对链上永续采取更清晰且可操作的路径，`HYPE` 会显著受益。
- 如果政策继续趋严，Hyperliquid 的分发、接入和机构扩张都可能承压。

## 13. 股市的影响

- `HYPE` 的股市映射更接近“高增长交易基础设施股”，和传统 L1 的定价逻辑存在明显差异。
- 最相关的股票与板块代理包括：
  - `COIN`
  - `HOOD`
  - `CME`
  - 高波动高周转的金融科技与交易平台板块

传导路径主要有三条：

- 当市场偏好高增长交易平台时，`HYPE` 的估值溢价往往更容易抬升。
- 当美股交易平台股走强，市场会更愿意给 Hyperliquid 这类“链上交易所 + 链”组合更高想象空间。
- 当金融科技和交易平台股被压估值时，`HYPE` 往往也会遭遇估值回撤。

这类影响短期偏情绪，中期会转化成一定的估值锚。

## 14. 国际战争的影响

Hyperliquid 受国际战争影响的路径，比普通公链更复杂，结论偏“业务面可能受益，币价面未必同步”。

### 关键传导路径

- 地缘冲突抬升油价、黄金、BTC、ETH 等大类资产波动，永续交易需求往往同步升温
- 波动率上升带来更高交易量、更高未平仓、更高协议手续费
- severe risk-off 又会让高 beta 资产估值承压

### 相关案例

- DefiLlama 在 `2026-03-12` 和 `2026-03-16` 链接的 DL News 报道里，已经把 Hyperliquid 与伊朗局势升级下的油价交易热度直接联系起来

### 结论

- 短期地缘冲突对 Hyperliquid 的业务量往往偏正面
- 对 `HYPE` 价格的影响更取决于市场是在交易“volume uplift”还是在交易“全面 risk-off”

## 15. 区块浏览器地址

- 官方主入口：
  - [Hyperliquid App](https://app.hyperliquid.xyz)
- 社区主流浏览器：
  - [Hypurrscan](https://hypurrscan.io/)

可以查看的内容包括：

- 地址余额、spot / staking / vault 相关数据
- Assistance Fund、Foundation、生态项目地址
- 现货与永续市场信息
- 验证者、staking、解锁与供应相关地址
- HyperEVM 合约与原生 HYPE 转移

## 16. 智能合约开发用什么语言

- HyperEVM 应用层：`Solidity` 为主，可使用标准 EVM tooling
- 执行环境：`EVM / Cancun without blobs`
- 主网 Chain ID：`999`
- 官方 RPC：`https://rpc.hyperliquid.xyz/evm`
- 开发者工具链：官方文档列出 `Python SDK`、社区 `Rust SDK`、社区 `TypeScript SDK`

补充一点：

- `HyperCore` 本身并非一个通用智能合约环境，它更接近高性能原生金融状态机
- 真正面向通用合约开发的部分，是 `HyperEVM`

## 关键风险

- 永续业务集中度过高，收入结构仍偏单一
- 月度解锁会在高位阶段反复压制价格斜率
- 极端行情下的 ADL、jailing、应急干预边界仍会被放大审视
- 活跃验证者集合只有 `24`，去中心化折价很难完全消失
- `HyperEVM` alpha 阶段若推进偏慢，平台化增长会低于预期
- 美国对链上永续的监管路径仍存在明显不确定性
- 新一代 perp DEX 和其他高性能执行层正持续分流注意力

## 未证实但值得跟踪的问题

- `HyperEVM` 在未来 6-12 个月能否跑出真正具备收入与用户黏性的主流应用
- `USDH` 这类 aligned stable 是否会演化成一个可复制的稳定币增长模板
- `HIP-3` 永续部署抵押门槛下调后，优质 builder 会否明显增加
- 市场最终会如何处理 `circulating / outstanding / total supply` 三组口径带来的估值分歧
- 在美国政策语境下，Hyperliquid 能否推动链上永续形成更清晰的合规叙事

## 参考资料

- [Hyperliquid Docs: About Hyperliquid](https://hyperliquid.gitbook.io/hyperliquid-docs)
- [Hyperliquid Docs: HyperCore Overview](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/overview)
- [Hyperliquid Docs: Staking](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/staking)
- [Hyperliquid Docs: Running a Validator](https://hyperliquid.gitbook.io/hyperliquid-docs/validators/running-a-validator)
- [Hyperliquid Docs: Delegation Program](https://hyperliquid.gitbook.io/hyperliquid-docs/validators/delegation-program)
- [Hyperliquid Docs: Fees](https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees)
- [Hyperliquid Docs: HyperEVM](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/hyperevm)
- [Hyperliquid Docs: HyperEVM Alpha Overview](https://hyperliquid.gitbook.io/hyperliquid-docs/hyperevm)
- [Hyperliquid Docs: API](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api)
- [Hyperliquid Docs: Permissionless Spot Quote Assets](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/permissionless-spot-quote-assets)
- [Hyperliquid Docs: Aligned Quote Assets](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/aligned-quote-assets)
- [Hyperliquid Docs: HIP-3 Builder-deployed Perpetuals](https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals)
- [Hyperliquid Docs: Support Guide](https://hyperliquid.gitbook.io/hyperliquid-docs/support)
- [Hyperliquid Docs: Foundation Non-validating Node](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/nodes/foundation-non-validating-node)
- [Hyperliquid Policy Center Launch Press Release](https://hyperliquidpolicy.org/blog/launch-press-release)
- [USDH Docs](https://docs.usdh.com/)
- [CoinGecko: Hyperliquid](https://www.coingecko.com/en/coins/hyperliquid)
- [DefiLlama: Hyperliquid](https://defillama.com/protocol/hyperliquid)
- [Tokenomist: Hyperliquid](https://tokenomist.ai/hyperliquid)
- [Tokenomist: Hyperliquid Claim / Unlocks](https://tokenomist.ai/hyperliquid/claim)
- [DL News: Hyperliquid smashes $1bn oil volume with price near $100](https://dlnews.com/articles/markets/hyperliquid-smashes-1bn-oil-volume-with-price-near-100/)
- [DL News: How Hyperliquid became an Iran war winner](https://dlnews.com/articles/snapshot/how-hyperliquid-became-an-iran-war-winner/)
- [CoinDesk: HyperLiquid Delists JELLY After Vault Squeezed](https://www.coindesk.com/markets/2025/03/26/hyperliquid-delists-jellyjelly-after-vault-squeezed-in-usd13m-tussle)
- [BitMEX on X](https://x.com/BitMEX/status/2026871734134255618)
- [tread.fi on X](https://x.com/tread_fi/status/2021017110441492768)
