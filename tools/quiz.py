#!/usr/bin/env python3
"""
🧠 AI × Web3 概念闪卡测验
========================
一个帮助学习 AI 和 Web3 基础概念的交互式测验工具。

用法：python3 quiz.py
"""

import random
import sys

# ============================================
# 概念知识库（基于 Week 1 学习内容整理）
# ============================================

CONCEPTS = {
    # AI 概念
    "LLM": {
        "category": "AI",
        "question": "LLM（大语言模型）是什么？它能做什么，不能做什么？",
        "hint": "想想一个读过很多书但从没实践过的人",
        "answer": "LLM 是读过海量文本的'超级接话王'——它不真正理解你说的话，但能根据训练数据猜出最合理的回答。",
        "example": "问 Claude '什么是比特币？'，它基于训练时读过的无数文章拼出回答，就像一个从没炒过股但读了一万本财经书的人。",
        "misconception": "误区：LLM 会'一本正经地胡说八道'（hallucination）。答案是'统计上最可能的'，不是'事实正确的'。",
        "key_point": "LLM 是模式匹配，不是真正理解"
    },
    "Prompt": {
        "category": "AI",
        "question": "什么是 Prompt？为什么它很重要？",
        "hint": "想想去餐厅点菜",
        "answer": "Prompt 是给 AI 下的'指令'——说得越清楚，回答越好。",
        "example": "去餐厅点菜：说'来点吃的'→ 随便上；说'不辣的番茄鸡蛋盖饭，米饭少一点'→ 精准。",
        "misconception": "误区：Prompt 不只是'问问题'，可以设定角色、限定格式、给出示例、要求分步骤思考。",
        "key_point": "好的 Prompt = 好的结果"
    },
    "Context Window": {
        "category": "AI",
        "question": "Context Window 是什么？它有什么限制？",
        "hint": "想想微信聊天记录",
        "answer": "Context Window 是 AI 的'短期记忆容量'——一次能记住多少内容有上限。",
        "example": "跟朋友聊微信，1000 条消息他不可能全记住。Context Window 就是'最近能记住的范围'。",
        "misconception": "误区：AI 不能记住所有对话。Claude 约 200K token，超出就'忘'了。",
        "key_point": "AI 的记忆是有限的"
    },
    "Agent": {
        "category": "AI",
        "question": "Agent（智能体）和普通 AI 有什么区别？",
        "hint": "想想私人助理 vs 客服",
        "answer": "Agent 是能自己决定'下一步做什么'的 AI——不只是回答问题，还能主动规划和执行。",
        "example": "普通 AI 像客服（问一句答一句）；Agent 像私人助理（说'订明天去上海的高铁'，它自己查车次、比较、选座）。",
        "misconception": "误区：Agent 能力取决于工具和指令。没有好的 Prompt 和 Tool，Agent 像没有手机的助理。",
        "key_point": "Agent = 自主决策 + 工具调用"
    },
    "Tool Use": {
        "category": "AI",
        "question": "Tool Use（工具调用）是什么？为什么 AI 需要工具？",
        "hint": "想想军师有了手和脚",
        "answer": "Tool Use 让 AI 能'动手做事'——不只是说话，还能执行操作。",
        "example": "AI 本身只能生成文字。加上 Tool Use，能搜索网页、读写文件、调用 API、发送消息。",
        "misconception": "误区：AI 调用工具是靠提前'教'的。工具描述写得不好，AI 就会用错或不用。",
        "key_point": "AI + 工具 = 真正的执行力"
    },
    "Workflow": {
        "category": "AI",
        "question": "Workflow（工作流）是什么？为什么要把任务拆成多个步骤？",
        "hint": "想想银行贷款审批流程",
        "answer": "Workflow 把复杂任务拆成多个步骤，按顺序或条件自动执行。",
        "example": "银行贷款审批：提交申请 → 系统初审 → 人工复核 → 批准/拒绝 → 通知客户。",
        "misconception": "误区：不是让 AI 一口气干完所有事。好的 Workflow 每一步可检查、可修改。",
        "key_point": "拆分任务 = 可控 + 可检查"
    },
    "Human-in-the-Loop": {
        "category": "AI",
        "question": "Human-in-the-Loop（人机协作）是什么？为什么需要人工确认？",
        "hint": "想想自动驾驶的关键时刻接管",
        "answer": "在 AI 工作流程中设置'人工检查点'——关键决策由人做，AI 负责执行和建议。",
        "example": "自动驾驶汽车——大部分时候自己开，复杂路况提醒驾驶员接管。",
        "misconception": "误区：加了人工审核不等于万无一失。人也会偷懒、也会信任 AI 而不仔细看。",
        "key_point": "人机协作的关键是人真的会看"
    },
    
    # Web3 概念
    "Account": {
        "category": "Web3",
        "question": "Web3 的 Account（账户）和 Web2 的账户有什么区别？",
        "hint": "想想银行账户 vs 微信账户",
        "answer": "Web3 账户是'链上身份'——没有客服、没有找回密码、没有'忘记密码'按钮。",
        "example": "Web2：平台给你的账户，平台能冻结、能找回密码。Web3：你自己生成的账户，你是唯一的负责人。",
        "misconception": "误区：Web3 账户没有'找回密码'功能。丢了私钥 = 永远失去账户。",
        "key_point": "你的账户，你的责任"
    },
    "Address": {
        "category": "Web3",
        "question": "Address（地址）是什么？它可以公开吗？",
        "hint": "想想银行账号",
        "answer": "地址是账户的'银行账号'——别人给你转账需要知道你的地址。",
        "example": "0x7F1a8ddbdECCA0945c392297e97CFe4694A524DB 是一个地址，42 位十六进制字符。",
        "misconception": "误区：地址可以公开分享，但地址 ≠ 控制权。知道地址不能动钱。",
        "key_point": "地址可以公开，私钥不能"
    },
    "Wallet": {
        "category": "Web3",
        "question": "Wallet（钱包）里真的装着钱吗？",
        "hint": "想想密码管理器",
        "answer": "钱包不是'装钱的容器'，而是'管理私钥的工具'——币在链上，钱包只是保管钥匙。",
        "example": "MetaMask 帮我管理私钥、签名交易、连接 DApp。就像密码管理器——钱在银行里。",
        "misconception": "误区：删了钱包但有助记词，重新导入就能恢复所有资产——资产从来不'在'钱包里。",
        "key_point": "钱包 = 私钥管理器"
    },
    "Seed Phrase": {
        "category": "Web3",
        "question": "Seed Phrase（助记词）是什么？为什么它这么重要？",
        "hint": "想想终极备份",
        "answer": "助记词是 12 或 24 个英文单词，是账户的'终极备份'——谁拥有它，谁就拥有所有资产。",
        "example": "创建 MetaMask 时给的 12 个单词，能推导出所有私钥和地址。",
        "misconception": "误区：永远不要截图、存手机、发给任何人。任何让你'输入助记词验证'的网站都是诈骗。",
        "key_point": "助记词 = 所有资产的控制权"
    },
    "Private Key": {
        "category": "Web3",
        "question": "Private Key（私钥）是什么？为什么不能泄露？",
        "hint": "想想支票签字",
        "answer": "私钥是账户的'密码'——用它签名就能动用资产，丢了或泄露就完了。",
        "example": "MetaMask 点'确认交易'就是用私钥签名，就像在支票上签字。",
        "misconception": "误区：不要存在联网设备上，不要在任何网站输入。有人问你要私钥 = 100% 骗子。",
        "key_point": "私钥泄露 = 资产归零"
    },
    "Signature": {
        "category": "Web3",
        "question": "Signature（签名）是什么？为什么签名前要仔细看？",
        "hint": "想想签合同",
        "answer": "签名是用私钥对交易'盖章'——证明操作是你发起的，内容没有被篡改。",
        "example": "Sepolia 转账时点'确认'就是签名，像签了字的合同，不可否认或修改。",
        "misconception": "误区：签名不可逆，签前一定要看清内容。恶意 DApp 可能让你签名'授权'来转走资产。",
        "key_point": "签名 = 授权，不可逆"
    },
    "Transaction": {
        "category": "Web3",
        "question": "Transaction（交易）一定是转账吗？",
        "hint": "想想所有链上操作",
        "answer": "交易是区块链上的一次'操作记录'——转账、调用合约、部署合约，都是一笔交易。",
        "example": "Sepolia 上转 0.01 ETH 是交易，调用合约的 set() 函数也是交易。",
        "misconception": "误区：查看链上数据不需要交易——那是免费的'读'操作。",
        "key_point": "写入 = 交易，读取 = 免费"
    },
    "Gas": {
        "category": "Web3",
        "question": "Gas（燃料费）是什么？为什么要收费？",
        "hint": "想想寄快递的邮费",
        "answer": "Gas 是在区块链上执行操作的'手续费'——就像寄快递要付邮费。",
        "example": "Sepolia 转账 Gas 费几乎为零（测试网）。主网简单转账可能几美元。",
        "misconception": "误区：测试网 ETH 没有价值，不要花钱买。",
        "key_point": "Gas = 验证者的报酬 + 防滥用"
    },
    "Smart Contract": {
        "category": "Web3",
        "question": "Smart Contract（智能合约）是什么？它和普通程序有什么区别？",
        "hint": "想想自动售货机",
        "answer": "智能合约是部署在区块链上的'自动执行程序'——满足条件就执行，没有中间人，无法篡改。",
        "example": "自动售货机：投币（满足条件），自动出饮料（执行结果）。Uniswap 合约：存入 Token A，自动给 Token B。",
        "misconception": "误区：合约一旦部署通常无法修改。调用前要确认是可信的。",
        "key_point": "代码即法律"
    },
    "Testnet": {
        "category": "Web3",
        "question": "Testnet（测试网）是什么？为什么要用测试网？",
        "hint": "想想飞行模拟器",
        "answer": "测试网是区块链的'沙盒环境'——用没有价值的测试币模拟真实操作。",
        "example": "Sepolia 是以太坊测试网，操作流程和主网完全一样，但用免费测试 ETH，没有财务风险。",
        "misconception": "误区：测试网 ETH 没有价值，不能卖钱，不能转到主网。",
        "key_point": "测试网 = 安全的练习场"
    },
    "Block Explorer": {
        "category": "Web3",
        "question": "Block Explorer（区块浏览器）是什么？它能做什么？",
        "hint": "想想区块链的搜索引擎",
        "answer": "区块浏览器是区块链的'搜索引擎+账本查询'——查任何地址余额、任何交易详情、任何合约代码。",
        "example": "Etherscan 可以查交易哈希、发送方、接收方、金额、Gas 费、区块号。",
        "misconception": "误区：所有信息都是公开的，任何人都能查。",
        "key_point": "透明账本，人人可查"
    },
    "Write vs Read": {
        "category": "Web3",
        "question": "智能合约的'写入'和'读取'有什么区别？",
        "hint": "想想在黑板上写字 vs 看黑板",
        "answer": "写入 = 改变链上状态 = 需要签名 + Gas；读取 = 查看链上状态 = 免费。",
        "example": "set(42) 是写入，需要 MetaMask 签名 + Gas 费；get() 是读取，免费，不需要签名。",
        "misconception": "误区：读取不需要交易，不会记录在链上。",
        "key_point": "写入有成本，读取免费"
    }
}

# ============================================
# 测验功能
# ============================================

def print_header():
    """打印欢迎信息"""
    print("\n" + "=" * 60)
    print("🧠 AI × Web3 概念闪卡测验")
    print("=" * 60)
    print("\n这个工具帮你巩固 Week 1 学习的 AI 和 Web3 基础概念。")
    print("每个概念包含：问题、提示、答案、例子和常见误区。")
    print("\n输入 'quit' 退出，输入 'all' 查看所有概念。")

def print_concept(concept_name, concept_data):
    """打印一个概念的完整信息"""
    print(f"\n{'─' * 60}")
    print(f"📚 {concept_name} [{concept_data['category']}]")
    print(f"{'─' * 60}")
    print(f"\n❓ 问题：{concept_data['question']}")
    print(f"\n💡 提示：{concept_data['hint']}")
    
    # 等待用户按回车显示答案
    input("\n按回车查看答案...")
    
    print(f"\n✅ 答案：{concept_data['answer']}")
    print(f"\n📝 例子：{concept_data['example']}")
    print(f"\n⚠️ 误区：{concept_data['misconception']}")
    print(f"\n🎯 关键点：{concept_data['key_point']}")

def run_quiz(mode="random"):
    """运行测验"""
    concepts_list = list(CONCEPTS.keys())
    
    if mode == "random":
        random.shuffle(concepts_list)
    
    score = 0
    total = 0
    
    for concept_name in concepts_list:
        concept_data = CONCEPTS[concept_name]
        
        print(f"\n{'─' * 60}")
        print(f"📚 概念：{concept_name} [{concept_data['category']}]")
        print(f"{'─' * 60}")
        print(f"\n❓ {concept_data['question']}")
        print(f"\n💡 提示：{concept_data['hint']}")
        
        user_input = input("\n你的理解（按回车查看答案，输入 'skip' 跳过）：").strip()
        
        if user_input.lower() == 'skip':
            continue
        if user_input.lower() == 'quit':
            break
        
        print(f"\n✅ 答案：{concept_data['answer']}")
        print(f"\n📝 例子：{concept_data['example']}")
        print(f"\n⚠️ 误区：{concept_data['misconception']}")
        print(f"\n🎯 关键点：{concept_data['key_point']}")
        
        # 询问用户是否理解
        feedback = input("\n你理解了吗？(y/n): ").strip().lower()
        total += 1
        if feedback == 'y':
            score += 1
        
        continue_quiz = input("\n继续下一个概念？(y/n): ").strip().lower()
        if continue_quiz != 'y':
            break
    
    if total > 0:
        print(f"\n{'=' * 60}")
        print(f"📊 测验结果：{score}/{total} 个概念理解正确")
        print(f"{'=' * 60}")

def show_all_concepts():
    """显示所有概念概览"""
    print(f"\n{'=' * 60}")
    print("📚 所有概念概览")
    print(f"{'=' * 60}")
    
    ai_concepts = [k for k, v in CONCEPTS.items() if v['category'] == 'AI']
    web3_concepts = [k for k, v in CONCEPTS.items() if v['category'] == 'Web3']
    
    print(f"\n🤖 AI 概念 ({len(ai_concepts)} 个):")
    for i, concept in enumerate(ai_concepts, 1):
        print(f"  {i}. {concept}")
    
    print(f"\n🔗 Web3 概念 ({len(web3_concepts)} 个):")
    for i, concept in enumerate(web3_concepts, 1):
        print(f"  {i}. {concept}")

def browse_by_category():
    """按类别浏览"""
    print(f"\n{'=' * 60}")
    print("📂 按类别浏览")
    print(f"{'=' * 60}")
    print("\n1. AI 概念")
    print("2. Web3 概念")
    print("3. 返回主菜单")
    
    choice = input("\n请选择 (1-3): ").strip()
    
    if choice == '1':
        concepts = [k for k, v in CONCEPTS.items() if v['category'] == 'AI']
    elif choice == '2':
        concepts = [k for k, v in CONCEPTS.items() if v['category'] == 'Web3']
    else:
        return
    
    print(f"\n{'─' * 60}")
    for i, concept in enumerate(concepts, 1):
        print(f"{i}. {concept}")
    print(f"{'─' * 60}")
    
    while True:
        idx = input("\n输入序号查看概念（输入 'back' 返回）：").strip()
        if idx.lower() == 'back':
            break
        try:
            idx = int(idx) - 1
            if 0 <= idx < len(concepts):
                concept_name = concepts[idx]
                print_concept(concept_name, CONCEPTS[concept_name])
            else:
                print("❌ 无效序号")
        except ValueError:
            print("❌ 请输入数字")

def search_concept():
    """搜索概念"""
    keyword = input("\n输入关键词搜索概念：").strip().lower()
    
    results = []
    for name, data in CONCEPTS.items():
        if (keyword in name.lower() or 
            keyword in data['question'].lower() or 
            keyword in data['answer'].lower()):
            results.append(name)
    
    if results:
        print(f"\n找到 {len(results)} 个相关概念：")
        for i, name in enumerate(results, 1):
            print(f"  {i}. {name} [{CONCEPTS[name]['category']}]")
        
        choice = input("\n输入序号查看（输入 'back' 返回）：").strip()
        if choice.lower() != 'back':
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(results):
                    print_concept(results[idx], CONCEPTS[results[idx]])
            except ValueError:
                pass
    else:
        print("❌ 没有找到相关概念")

# ============================================
# 主程序
# ============================================

def main():
    """主程序入口"""
    print_header()
    
    while True:
        print(f"\n{'─' * 60}")
        print("📋 主菜单")
        print(f"{'─' * 60}")
        print("1. 随机测验（推荐）")
        print("2. 按类别浏览")
        print("3. 搜索概念")
        print("4. 查看所有概念")
        print("5. 退出")
        
        choice = input("\n请选择 (1-5): ").strip()
        
        if choice == '1':
            run_quiz("random")
        elif choice == '2':
            browse_by_category()
        elif choice == '3':
            search_concept()
        elif choice == '4':
            show_all_concepts()
        elif choice == '5' or choice.lower() == 'quit':
            print("\n👋 再见！继续学习 AI × Web3！")
            break
        else:
            print("❌ 无效选择，请重试")

if __name__ == "__main__":
    main()
