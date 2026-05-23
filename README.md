# 🎯 Week 1 Proof-of-Work Pack

> AI × Web3 School Cohort 0 · Luvia · 学员 #3312
> 2026-05-18 ~ 2026-05-23

---

## 📋 本周总览

| 维度 | 完成内容 | 状态 |
|------|---------|------|
| **AI 基础** | 7 个核心概念（LLM、Prompt、Context Window、Agent、Tool Use、Workflow、Human-in-the-Loop） | ✅ |
| **Web3 基础** | 11 个核心概念（Account、Address、Wallet、Seed Phrase、Private Key、Signature、Transaction、Gas、Smart Contract、Testnet、Block Explorer） | ✅ |
| **AI 工具实践** | Hermes Agent（Learning Agent）+ Claude Code | ✅ |
| **Web3 实践** | Sepolia 测试网 ETH 转账 + 智能合约部署 | ✅ |
| **AI × Web3 交叉** | 受限 Web3 助手 Workflow + 交叉流程图 | ✅ |
| **学习产物** | 概念闪卡测验工具（Python CLI） | ✅ |

---

## 🤖 一、AI 学习记录

### 概念卡片（7 个）

| 概念 | 一句话理解 | 关键点 |
|------|-----------|--------|
| **LLM** | 读过海量文本的"超级接话王"，不真正理解但能猜出最合理的回答 | 模式匹配，不是真正理解 |
| **Prompt** | 给 AI 下的"指令"，说得越清楚回答越好 | 好的 Prompt = 好的结果 |
| **Context Window** | AI 的"短期记忆容量"，一次能记住多少有上限 | AI 的记忆是有限的 |
| **Agent** | 能自己决定"下一步做什么"的 AI，不只是回答问题 | 自主决策 + 工具调用 |
| **Tool Use** | 让 AI 能"动手做事"，不只是说话 | AI + 工具 = 真正的执行力 |
| **Workflow** | 把复杂任务拆成多个步骤，按顺序自动执行 | 拆分任务 = 可控 + 可检查 |
| **Human-in-the-Loop** | 在 AI 工作流程中设置"人工检查点" | 关键是人真的会看 |

**详细笔记**：[AI 基础概念卡片](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tasks/ai-concepts.md)

---

## 🔗 二、Web3 学习记录

### 概念卡片（11 个）

| 概念 | 一句话理解 | 安全提醒 |
|------|-----------|---------|
| **Account** | Web3 的"链上身份"，没有客服没有找回密码 | 你是唯一的负责人 |
| **Address** | 账户的"银行账号"，可以公开分享 | 地址 ≠ 控制权 |
| **Wallet** | "管理私钥的工具"，币在链上不在钱包里 | 钱包 = 私钥管理器 |
| **Seed Phrase** | 12/24 个单词的"终极备份" | 泄露 = 资产归零 |
| **Private Key** | 账户的"密码"，用它签名就能动用资产 | 泄露 = 资产归零 |
| **Signature** | 用私钥对交易"盖章"，不可逆 | 签名前看清内容 |
| **Transaction** | 链上的一次"操作记录" | 写入 = 交易，读取 = 免费 |
| **Gas** | 链上操作的"手续费" | 测试网 ETH 没有价值 |
| **Smart Contract** | 部署在链上的"自动执行程序" | 代码即法律 |
| **Testnet** | 区块链的"沙盒环境" | 安全的练习场 |
| **Block Explorer** | 区块链的"搜索引擎" | 透明账本，人人可查 |

**详细笔记**：[Web3 基础概念卡片](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tasks/web3-concepts.md)

---

## 🛠️ 三、Learning Agent / AI 工具实践

### 使用的 AI 工具

| 工具 | 版本 | 用途 |
|------|------|------|
| **Hermes Agent** | v0.14.0 | 主力 Learning Agent：每日提醒、任务管理、笔记生成、WCB 提交 |
| **Claude Code** | v2.1.146 | 代码辅助：写脚本、调试、理解技术文档 |

### Learning Agent 配置

- ✅ GitHub CLI 已认证（Monica06161127）
- ✅ 学习仓库已创建（ai-web3-school-cohort-0）
- ✅ Obsidian 知识库已组织（~/AI-Web3-Notes/）
- ✅ WCB API 已配置
- ✅ 每日提醒 Cron 已设置（9:00 + 21:00）

**详细记录**：[工具准备记录](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tasks/tool-preparation.md)

---

## 💰 四、链上验证记录

### 1. 测试网 ETH 转账

| 项目 | 内容 |
|------|------|
| **网络** | Sepolia 测试网 |
| **发送方** | `0x7F1a8ddbdECCA0945c392297e97CFe4694A524DB` |
| **接收方** | `0x6fD78Be313597511Cb034100Db13499D6c41a968` |
| **金额** | 0.01 ETH |
| **交易哈希** | `0xf9294ae505992162fa29c10a8d92c8b3485bc7be290e03e1e3f4a3f80c1de8c5` |
| **Etherscan** | [查看交易](https://sepolia.etherscan.io/tx/0xf9294ae505992162fa29c10a8d92c8b3485bc7be290e03e1e3f4a3f80c1de8c5) |
| **状态** | ✅ Success |

### 2. 智能合约部署

| 项目 | 内容 |
|------|------|
| **合约名称** | SimpleStorage |
| **合约地址** | `0x265e61c8422D9dE1de2C45b3A659619E16C056eD` |
| **部署网络** | Sepolia 测试网 |
| **创建者** | `0x7F1a8ddbdECCA0945c392297e97CFe4694A524DB` |
| **Etherscan** | [查看合约](https://sepolia.etherscan.io/address/0x265e61c8422D9dE1de2C45b3A659619E16C056eD) |
| **功能** | `set(uint256)` 写入 + `get()` 读取 |
| **测试结果** | `set(42)` → `get()` 返回 `42` ✅ |

**详细记录**：
- [智能合约部署记录](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tasks/smart-contract-deployment.md)
- [合约代码](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/contracts/SimpleStorage.sol)

---

## 🔄 五、AI × Web3 交叉实验

### 1. 受限 Web3 助手 Workflow

设计了一个"受限"的 AI Web3 助手，明确 AI 能做什么、不能做什么：

**AI 可以做**：规划、解释、检查、生成草稿、查询结果、生成记录

**AI 不能做**：访问私钥、替用户签名、自动发起交易、修改授权额度

**必须人工确认**：审查摘要、MetaMask 签名、验证成功

**详细设计**：[受限 Web3 助手 Workflow](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tasks/constrained-web3-workflow.md)

### 2. AI × Web3 最小交叉流程图

基于真实经历（Sepolia 转账）画出的完整流程：

```
用户发起 → AI 规划 → 人工确认 → AI 指引 → 人工签名 → 链上执行 → AI 查询 → 人工验证
```

**核心原则**：AI 是参谋，不是司机

**详细流程图**：[AI × Web3 交叉流程图](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tasks/ai-web3-workflow.md)

---

## 🧰 六、学习产物

### 概念闪卡测验工具

一个帮助巩固 Week 1 概念的交互式 Python 工具：

- **包含概念**：17 个（7 个 AI + 10 个 Web3）
- **功能**：随机测验、按类别浏览、搜索概念
- **运行方式**：`python3 quiz.py`

**代码**：[tools/quiz.py](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tools/quiz.py)

---

## ⚠️ 七、遇到的问题和人工修正

### 问题 1：Web Scraping 产生不准确结果

**场景**：用自动化工具抓取 Etherscan 交易页面，显示的 from 地址和交易类型与实际不符。

**发现**：用户手动查看页面，发现实际是"简单 ETH 转账"，但抓取结果显示的是"Uniswap Swap"。

**修正**：以用户手动查看的结果为准，不信任自动化抓取。

**教训**：动态页面的自动化抓取可能不准确，用户提供的数据优先级更高。

### 问题 2：Remix IDE 部署环境选择

**场景**：第一次部署合约时，使用了 Remix VM（本地模拟环境），而不是 Sepolia 测试网。

**发现**：部署成功但没有真实的交易哈希和 Etherscan 记录。

**修正**：切换到 "Injected Provider - MetaMask"，重新部署到 Sepolia 测试网。

**教训**：本地 VM 和测试网的区别——VM 是模拟，测试网是真实的区块链。

### 问题 3：合约地址 vs 钱包地址混淆

**场景**：提交合约部署记录时，误将钱包地址当作合约地址。

**发现**：钱包地址（`0x7F1a...524DB`）和合约地址（`0x265e...056eD`）是不同的。

**修正**：明确区分两个地址，合约地址是部署后获得的唯一标识。

**教训**：钱包地址 = 你的账户；合约地址 = 你部署的程序。

---

## 📁 八、所有提交材料汇总

### 概念卡片
- [AI 基础概念卡片（7 个）](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tasks/ai-concepts.md)
- [Web3 基础概念卡片（11 个）](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tasks/web3-concepts.md)

### 工具和实践
- [工具准备记录](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tasks/tool-preparation.md)
- [智能合约部署记录](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tasks/smart-contract-deployment.md)
- [合约代码](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/contracts/SimpleStorage.sol)

### AI × Web3 交叉
- [受限 Web3 助手 Workflow](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tasks/constrained-web3-workflow.md)
- [AI × Web3 交叉流程图](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tasks/ai-web3-workflow.md)

### 学习产物
- [概念闪卡测验工具](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tools/quiz.py)
- [工具文档](https://github.com/Monica06161127/ai-web3-school-cohort-0/blob/master/tools/README.md)

### 链上验证
- **测试网转账**：[Etherscan 交易](https://sepolia.etherscan.io/tx/0xf9294ae505992162fa29c10a8d92c8b3485bc7be290e03e1e3f4a3f80c1de8c5)
- **智能合约**：[Etherscan 合约](https://sepolia.etherscan.io/address/0x265e61c8422D9dE1de2C45b3A659619E16C056eD)

---

## 🎯 九、本周核心收获

### 1. AI 的边界
- AI 能做：规划、解释、检查、生成、查询
- AI 不能做：签名、授权、接触私钥、自动执行链上操作
- **核心原则**：Human-in-the-Loop 不是形式，而是真的会看

### 2. Web3 的本质
- 写入 = 改变世界状态 = 需要共识 = 需要成本
- 读取 = 查看世界状态 = 免费
- **核心原则**：你的私钥，你的责任

### 3. AI × Web3 的正确姿势
- AI 是参谋，不是司机
- 私钥和助记词是不可触碰的红线
- **核心原则**：AI 帮你规划，你来决策和签名

---

## 📊 十、Week 1 进度统计

| 任务类型 | 完成数 | 总分 |
|----------|--------|------|
| 前置准备 | 7/7 | 65 分 |
| AI 向任务 | 2/3 | 40 分 |
| Web3 向任务 | 2/3 | 40 分 |
| AI × Web3 综合 | 3/4 | 100 分 |
| 线上活动 | 8/8 | 100 分 |
| **总计** | **22/25** | **345 分** |

---

*AI × Web3 School Week 1 · Luvia*
*最后更新：2026-05-23*
