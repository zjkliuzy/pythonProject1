"""
    练习2:
    在终端中输入性别
    打印"您好先生"  "您好女士"  "未知"
"""
sex = input("请输入性别:")
if sex == "男":
    print("您好先生")
elif sex == "女":
    print("您好女士")
else:
    print("未知")
# 练习3：
#     在终端中输入课程阶段数,显示课程名称
#     1 显示 Python语言核心编程
#     2 显示 Python高级软件技术
#     3 显示 Web 全栈
#     4 显示 网络爬虫
#     5 显示 数据分析、人工智能