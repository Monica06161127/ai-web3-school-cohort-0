# Risk / Assumption Memo

> Week 3 任务：Risk / Assumption Memo
> 项目：EIV (Execution-Integrity Validator)

## 前提假设

1. **ERC-8004 生态会持续发展**：我们押注 ERC-8004 作为 attestation + reputation 的链上标准。如果这个标准被弃用或大幅改动，需要重新适配。
2. **Sepolia 有足够真实的 DeFi 活动**：我们的验证需要真实交易可验。如果 Sepolia 上 DeFi 活动太少，可能需要切到其他 testnet 或 mainnet fork。
3. **GLM-5.1 能胜任多步调查任务**：作为赛道指定的 demo backend，我们需要它能诠释松散 intent、编排多步调查、抓未列举偏离。
4. **FAIL reputation 有约束力**：我们的核心假设是"agent 的 FAIL reputation 能被其他协议/用户读取并作为拒绝依据"。这在 production 中尚无大量先例。

## 最可能失败点（Pre-Mortem）

### 1. 单一开发者人力瓶颈
- **风险**：John 一人扛全部技术（validator + chain adapter + ERC-8004 + dashboard + agent + 部署），6 天内可能完不成
- **对策**：dashboard 砍到最小、玩具 agent 走脚本、核心 timebox；我扛所有非程式产出让 John 专注核心

### 2. ERC-8004 Validation Registry in-flux
- **风险**：Validation Registry 没有 canonical 已部署地址，仍在讨论中，接口可能变
- **对策**：自部署最小兼容版（DESIGN.md 既有备案）；pin master commit 控变动

### 3. 最后一天整合接不起来
- **风险**：各模块独立开发，最后串接时可能出问题
- **对策**：Day-1 已冻结接口 + 假数据 walking skeleton 先行；23/23 selftest 已覆盖接口正确性

### 4. "薄包装"质疑
- **风险**：评委可能质疑我们只是把 LLM 包了一层，不是真长程 agent
- **对策**：刻意建多步调查回圈，log/demo 显式秀长程（解析 → 捞链 → 比对 → 起 PoC → 校验 → attest）

## Week 4 Fallback

| 场景 | Fallback |
|------|----------|
| Validation Registry 无法按时部署 | 走自部署最小兼容版，不依赖上游可用性 |
| GLM-5.1 调查回圈不稳定 | 先半自动（人 + LLM 协作），保证核心流程跑通 |
| 真链 tx 解码出问题 | 先用结构正确的 fixture 跑通管线，再切真 Sepolia RPC |
| Dashboard 做不出来 | 纯 CLI / log 输出 diff，demo 够用 |
| 2–3 场景跑不齐 | 至少 1 个场景全真链端到端，其余诚实标明 mock |

## 核心信任主张一致性

- **FAIL 可重跑**（trustless 一半）：任何人拿到相同 intent + txRef，可以重跑验证看结果是否一致
- **PASS 有界**：没验出问题不等于没问题，依赖覆盖率与诚实
- **非即时防护**：这是究责/信任层，不阻止单笔交易
- **Production 补丁**：staking / zkML / TEE 是 future，不在 MVP 范围
