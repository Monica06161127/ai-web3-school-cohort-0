# Sprint Plan — Week 4（6/8–6/13）

> Week 3 任务：Week 4 Sprint Plan
> 项目：EIV (Execution-Integrity Validator)
> 截止：2026-06-13 12:00（UTC+8）提交 · 6/14 Demo Day

## 团队分工

- **John** = 技术 lead，做**全部技术**（validator 核心 + 检查逻辑 + chain adapter + ERC-8004 整合 + attest + MCP + 最小 dashboard + 玩具 agent + 部署）
- **Luvia** = 运营，扛**全部非程式**（pitch + 3–5 分钟影片 + README 打磨 + 提交 + 发推文 + 协调）

**1-dev 现实的范围取舍**：只有 John 一个开发者，dashboard 砍到最小（简单表格 / 静态页 / CLI viewer 即可呈现 diff，不做打磨的 web app）；玩具 agent 走最小脚本。

## 前置（已完成，Week 4 不重做）

- 接口 schema 冻结 + 假数据 walking skeleton（`predicates.py` 已测；selftest 23/23）
- DESIGN.md v2 为权威设计

## 6/8（一）— 开核心工

- **John**：起 `RpcChainAdapter` 骨架（链已定 Sepolia，直接接 Sepolia RPC）；确认 AIP `hashIntent` 可接；由 ERC-8004 ABI 写 Solidity interface
- **Luvia**：盘 pitch 大纲与影片脚本骨架；备 README 打磨清单；确认提交流程与素材需求
- 真实现：chain adapter 骨架 + ERC-8004 interface
- Mock/fallback：dashboard 暂不动

## 6/9（二）— Chain adapter 真解 tx + 玩具 agent 最小脚本

- **John**：RpcChainAdapter 真解一笔 Sepolia tx → ExecutionTrace；写最小脚本让玩具 agent 在 Sepolia 发"干净 swap"交易
- **Luvia**：依目前 demo 流程草拟 pitch 叙事（对齐"FAIL 可重跑 / 约束力来自 reputation"）；收集既有 walking-skeleton 截图素材
- 真实现：1 条真链 trace 解出 + 1 笔真干净 tx
- Mock/fallback：其余场景仍 fixture

## 6/10（三）— 自部署 Validation Registry + ERC-8004 真写 attestation + EIP-712 真验章

- **John**：在 Sepolia 部署最小兼容 Validation Registry；OnChainAttestationSink 真送 validationResponse；EIP712Verifier 换真验章 + ecrecover；补"残留 allowance""未授权 target"两场景的最小发 tx 脚本
- **Luvia**：README 打磨（problem / track / MVP flow / risks）；整理提交所需字段清单
- 真实现：Validation Registry 部署 + attest 上链 + 真验章

## 6/11（四）— End-to-end 串接 + GLM-5.1 调查外圈 + 最小 dashboard

- **John**：把 source→adapter→validate→attest 串成真链端到端（至少干净场景全真）；接 GLM-5.1 调查回圈 + grounding guard；接最小 dashboard / CLI viewer
- **Luvia**：依端到端结果定稿 pitch；开始录影分镜；持续 README 打磨
- 真实现：≥1 场景真链端到端 + attestation + 最小 diff 视图
- Mock/fallback：GLM 外圈可先半自动；dashboard 维持最小

## 6/12（五）— 2–3 场景 + 边界硬化 + 录影

- **John**：跑齐 2–3 场景（干净 PASS / 残留 FAIL / 未授权 FAIL）；边界硬化（错签→401、未知 tx→404 等）
- **Luvia**：录 3–5 分钟影片；README/proposal 定稿；备妥提交内容
- 真实现：demo 场景齐
- Mock/fallback：诚实标明哪些场景的链上部分仍 mock

## 6/13（六）— 提交（12:00 截止）

- 上午 **John**：最终端到端彩排、截图、诚实限制声明就位
- 上午 **Luvia**：README 最终检查、**执行提交**、**手动发布赛道推文**（tweet-draft.md，John 确认后）
- **12:00 前提交**
- 缓冲：任何未完成项一律走当天 fallback，不临时扩范围

## 6/14（日）— Demo Day

- Luvia 主讲 pitch + 影片；John 答技术质疑

## 「真实现 vs mock」一览

| 能力 | 目标状态 | Fallback |
|------|----------|----------|
| Chain adapter 解 tx | 真（≥1 场景，Sepolia） | 其余 fixture |
| ERC-8004 attest | 真上链（自部署 Validation Registry） | 本即自部署 |
| EIP-712 验章 | 真 ecrecover | —（优先做完） |
| GLM-5.1 调查外圈 | 真回圈 + grounding guard | 半自动 |
| Dashboard / diff 视图 | **最小**（表格 / 静态页 / CLI viewer） | 纯 CLI/log 输出 |
| Reputation consumer | mock consumer | 本就是 demo 演法 |
| 多场景 | 2–3 场景齐 | 部分链上 mock，诚实标 |
