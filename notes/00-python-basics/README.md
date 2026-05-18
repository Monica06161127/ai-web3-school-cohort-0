# 📓 Phase 0: 热身期 — Python 基础

> 学习目标：能用 Python 写出简单程序，理解编程是什么

## 学习路线

1. **Day 1-3**: 变量、数据类型、基本运算
2. **Day 4-7**: 条件判断 (if/else)、循环 (for/while)
3. **Day 8-10**: 函数、模块
4. **Day 11-14**: 文件操作、错误处理、小项目

## 核心概念

### 变量 = 带标签的盒子
```python
# 就像你在盒子上贴标签
name = "Luvia"          # 字符串盒子
age = 19                # 数字盒子
balance = 1000.50       # 浮点数盒子（金融！）
is_student = True       # 布尔盒子
```

### 条件判断 = 做选择
```python
# 就像你每天做的决定
if balance > 500:
    print("可以吃大餐 🍜")
else:
    print("还是吃食堂吧 🍚")
```

### 循环 = 重复做事情
```python
# 就像每天打卡
for day in range(1, 31):
    print(f"Day {day}: 今天也要好好学习！")
```

### 函数 = 食谱
```python
# 就像把做菜步骤写成食谱，以后随时用
def calculate_interest(principal, rate, years):
    """计算复利 — 金融专业的基本功！"""
    total = principal * (1 + rate) ** years
    return total

# 用这个"食谱"
result = calculate_interest(1000, 0.05, 10)
print(f"10年后你的钱变成了: {result:.2f}")
```

## 练习清单

- [ ] 写一个"自我介绍"程序
- [ ] 写一个汇率计算器
- [ ] 写一个复利计算器
- [ ] 写一个简单的猜数字游戏

---

*进度: 进行中 🔄*
