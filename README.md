# AI × Web3 School Cohort 0 — Luvia's Learning Repository

> 记录我在 AI × Web3 School 共学营的完整学习历程

## 关于 AI × Web3 School

[AI × Web3 School](https://aiweb3.school) 是一个为期 4 周的高强度共学营（2026-05-18 ~ 2026-06-14），由 LXDAO 与 ETHPanda 联合发起，Z.AI 领衔赞助，Cobo 联合赞助。

- **官网**: https://aiweb3.school
- **Handbook**: https://aiweb3.school/zh/handbook/
- **共学营打卡页面**: https://intensivecolearn.ing/programs/AI-Web3-School
- **Learning Agent Prompt**: https://aiweb3.school/learning-agent.zh.txt

## 关于我

**Luvia** — 金融专业大一学生，零编程基础，正在学习 AI × Web3。

详见 [profile.md](./profile.md)

## Week 1 学习目标（5/18-5/23）

本周是共学营第一周，目标是**建立 AI 和 Web3 的共同语言**，完成两侧的基础实践。

### 模块 A：AI 基础 — 从 LLM 到 Agent Workflow
- 理解 LLM 工作原理（上下文概率生成 token）
- 掌握四大控制层：上下文窗口、系统指令、Prompt、工具调用
- 区分 Prompt / Workflow / Agent 的边界
- 了解 Agent 核心组件：MCP、Skills、Tool Calling、Guardrails
- 认识 AI 输出必须验证的原因

### 模块 B：Web3 基础 — 账户、钱包、签名与链上执行
- 理解账户、地址、钱包的关系
- 掌握 Gas、签名、交易的基本概念
- 区分主网与测试网
- 了解智能合约与普通后端逻辑的区别

### 模块 C：最小交叉实验
- 体验完整流程：AI 输出 → 人工审查 → 钱包确认 → 链上执行 → 验证记录

### 本周任务
- [x] 参加开幕式（5/17）
- [x] 创建课程 GitHub Repo
- [ ] 搭建个人学习 Agent（Claude Code / Codex / Hermes 三选一）
- [ ] 创建测试钱包，完成测试网转账
- [ ] 部署最小智能合约
- [ ] 用 Agent 生成可交互的学习产物
- [ ] 在 X/Twitter 上发布 AI × Web3 School 起点帖
- [ ] 建立 AI × Web3 行业关注清单

## 记录结构

本仓库按以下结构组织学习记录：

```
ai-web3-school-cohort-0/
├── README.md                  ← 你正在看的这个文件
├── profile.md                 ← 个人简介 & 目标
├── learning-plan.md           ← 4 周共学营完整学习计划
├── daily-checkin/             ← 每日学习打卡
│   ├── template.md            ← 打卡模板
│   └── 2026-05-*.md           ← 每日打卡记录
├── notes/                     ← 学习笔记（按主题分类）
│   ├── 00-python-basics/      ← Python 基础
│   ├── 01-ai-basics/          ← AI / LLM 基础
│   ├── 02-web3-basics/        ← Web3 / 区块链基础
│   ├── 03-ai-web3-crossover/  ← AI × Web3 交叉方向
│   └── 04-capstone/           ← 毕业项目
├── tasks/                     ← 课程任务记录
├── experiments/               ← 实验代码 & 探索
├── handbook-feedback/         ← Handbook 改进建议
├── hackathon/                 ← Hackathon 准备 & 项目
├── submissions/               ← 提交的作业/项目
├── templates/                 ← 笔记模板
└── resources/                 ← 学习资源收藏
```

**每日记录方式**：
- `daily-checkin/` — 每日打卡（今天学了什么、核心收获、还没搞懂的）
- `notes/` — 按主题整理的深度笔记（从 daily-checkin 中提炼）
- `experiments/` — 代码实验和动手练习
- `handbook-feedback/` — 对课程 Handbook 的改进建议

## 学习进度

### 共学营 4 周（5/18-6/14）

| Week | 日期 | 主题 | 核心内容 | 状态 |
|------|------|------|----------|------|
| Week 1 | 5/18-5/23 | AI 与 Web3 基础知识 | LLM/Agent/钱包/签名/智能合约/测试网 | 进行中 |
| Week 2 | 5/24-5/31 | AI × Web3 交叉方向 | Agentic Commerce/Dev Tooling/AI Security/Governance | |
| Week 3 | 6/1-6/7 | 实践深化与 Hackathon 启动 | 小型实战练习 + 确定 Hackathon 项目 | |
| Week 4 | 6/8-6/14 | Hackathon 集中开发与 Demo | 核心功能开发 + Demo 展示 | |

### 预习冲刺（5/10-5/15，已完成）

| Day | 主题 | 收获 |
|-----|------|------|
| Day 1 | Web3 基础 | 区块链、以太坊、智能合约 |
| Day 2 | AI 基础 | LLM、神经网络、梯度下降 |
| Day 3 | Web3 实操 | MetaMask 转账、DeFi、比特币 |
| Day 4 | AI Agent | Agent vs Chatbot、AutoGen |
| Day 5 | AI×Web3 交叉 | Vibe Coding、Agentic Commerce、DePIN |
| Day 6 | 整合复习 | 笔记整理 + 问题清单 |

## Learning Agent 使用说明

本仓库在初始化和日常学习中使用了 **Claude Code**（Anthropic 的 CLI Agent）作为学习助手。

**Agent 做了什么**：
- 根据共学营官网课程结构，生成了 4 周学习计划框架
- 根据官网推荐材料，整理了资源链接列表
- 辅助编写每日打卡笔记的结构模板
- 帮助解释课程中的技术概念（如 MCP、ACP、Function Call）

**我人工确认了什么**：
- 所有学习计划内容均与官网（web3career.build）对照确认
- 每日笔记中的技术理解由我本人根据课程直播内容填写
- Agent 生成的解释经我核对后才写入笔记
- 仓库结构、文件命名、提交内容均由我审核

> Agent 是辅助工具，不是替代学习的捷径。所有核心理解必须自己消化。

## 隐私提醒

本仓库为 **public**，所有内容公开可见。请注意：
- 不要在笔记中提交私钥、助记词、API Key 等敏感信息
- 不要在代码中硬编码 Token 或密码
- 学习笔记中的错误是成长的一部分，不需要隐藏

## 相关链接

- [AI × Web3 School 官网](https://aiweb3.school)
- [Handbook](https://aiweb3.school/zh/handbook/)
- [残酷共学打卡页面](https://intensivecolearn.ing/programs/AI-Web3-School)
- [GitHub 学习仓库](https://github.com/Monica06161127/ai-web3-school-cohort-0)

---

*"最好的学习方式是边做边学。" — AI × Web3 School*
