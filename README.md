# Currency Research Report

一个面向 `Codex / AI 研究工作流` 的研究仓库，包含两部分内容：

- `reports/`：已经生成好的币种、链、股票深度研究报告
- `skills/coin-report-writer/`：用于自动生成研究报告的 Codex skill

这套 skill 默认输出中文报告，强调 `全面`、`深刻`、`可追踪更新`，适合做加密资产、链、项目、股票的研究归档。

## 仓库结构

```text
Currency-Research-Report/
├── README.md
├── reports/
└── skills/
    └── coin-report-writer/
        ├── SKILL.md
        ├── agents/
        ├── assets/
        ├── references/
        └── scripts/
```

## 报告特点

- 默认 `一个币种 / 链 / 股票 = 一个单独文档`
- 默认输出 `简体中文`
- 同一标的再次生成时，会优先写 `新发生的事情`
- 支持 `加密资产`、`链`、`股票`
- 强制加入 `对标项目比较`
- 强制加入 `解锁信息`、`节点/验证者信息`
- 强制加入 `宏观经济`、`经济政策`、`股市影响`、`国际战争影响`
- 强制加入 `历史大事件与影响意义`
- 支持 `未来 12 个月价格走势预测`
- 支持 `链与 AI 最佳结合方式` 分析

## 报告固定覆盖维度

每份报告默认会覆盖以下核心部分：

1. 与上次相比的关键变化
2. 关键指标快照
3. 解锁与供给压力快照
4. 节点与验证者概况
5. 股票信息与核心指标
6. 赛道定位
7. 核心投资逻辑
8. 反方观点与证伪条件
9. 市场可能忽略的变量
10. 对标项目比较
11. 执行摘要
12. 历史大事件与影响意义
13. 最近生态进展
14. 最近 X 上的讨论
15. 经济模型
16. 前景分析
17. 捕获价值分析
18. 未来 12 个月重要事件
19. 未来 12 个月价格走势预测
20. 全方位多角度分析
21. 与 AI 相关的重点分析
22. 最新路线图
23. 宏观经济对此标的的影响
24. 经济政策的影响
25. 股市的影响
26. 国际战争的影响
27. 区块浏览器地址
28. 智能合约开发语言
29. 关键风险
30. 未证实但值得跟踪的问题
31. 参考资料

## 如何安装 Skill

把 skill 复制到本机 `Codex` 的 skills 目录：

```bash
cp -R skills/coin-report-writer ~/.codex/skills/
```

安装后，新会话里直接输入币种、链名或股票代码即可触发。

## 如何使用

你可以直接输入：

```text
BTC
ETH
SOL
ICP
NVDA
分析此链未来的发展前景
分析此链与 AI 最好的结合方式
预测一年内价格走势
```

也可以一次输入多个标的：

```text
BTC ETH SOL
```

系统会分别生成多份独立文档，而不是合并成一份。

## 文档输出位置

默认输出到工作区的：

```text
reports/
```

文件名格式类似：

```text
2026-03-19-btc-analysis.md
2026-03-19-solana-analysis.md
2026-03-19-nvda-analysis.md
```

## 适用场景

- 币种深度研究
- 公链前景研究
- 代币经济模型分析
- 解锁抛压分析
- 节点与去中心化分析
- AI 结合路径分析
- 股票与加密映射研究
- 更新版跟踪报告

## Skill 关键文件

- `skills/coin-report-writer/SKILL.md`
- `skills/coin-report-writer/scripts/init_coin_report.py`
- `skills/coin-report-writer/assets/report-template.md`
- `skills/coin-report-writer/references/report-rubric.md`
- `skills/coin-report-writer/references/report-quality.md`

## 说明

这个仓库当前既保存 `研究报告结果`，也保存 `生成这些报告的 skill 源码`，便于后续继续扩展、复用和提交更新。
