"""
    行
"""
# 3个物理行3个逻辑行(建议)
python = 5
b = 2
c = python + b

# 1个物理行3个逻辑行(不建议)
python = 5;b = 2;c = python + b

# 3个物理行1个逻辑行(不建议)
# 折行符
data = 1 + 2 + 3 \
       + 4 + 5 + \
       6 + 7 + 8 + 9

# 括号是天然的换行符
data = (1 + 2 + 3
       + 4 + 5 +
       6 + 7 + 8 + 9)


print(
    int(input("请输入年龄:")) > 25 and
    int(input("请输入身高:")) < 170
)
