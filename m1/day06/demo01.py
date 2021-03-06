"""
    笔试题:
        请叙述元组与列表的区别.
        答:内存存储机制不同.
           元组采用按需分配的存储机制,节省内存.
           列表   预留空间  +  自动扩容,操作灵活

    面试题:
        为什么要有元组(为什么要有不可变).
        答:任何数据本质都可以理解为不可变,元组就是不可变数据.(计算机世界)
        但是在实际应用中,需要不断存储新数据,所以Python提供了列表.

        Python语言有哪些数据类型
        答:只可变与不可变2种类型
            常用的可变数据:列表...
                不可变  :str,元组,数值(int,float),bool...
"""
# 创建
# 语法1: 元组名 = (数据1,数据2,数据3)
tuple01 = ("曹伟伟", "杨德义", "王杰")
# 语法2:元组名 = tuple(可迭代对象)
list01 = [10, 20, 30]  # 用于存储计算过程中的数据
tuple02 = tuple(list01)  # 用于存储最后结果
print(tuple02)

# 定位(读取)
print(tuple01[-1])
# 通过切片读取数据,会创建新容器
print(tuple01[:2])

# 遍历
for item in tuple01:
    print(item)

for i in range(len(tuple01) - 1, -1, -1):
    print(tuple01[i])

# 特殊1:如果元组中只有一个元素,必须加逗号
tuple03 = (10,)
print(type(tuple03))

# 特殊2:创建元组的括号,在没有歧义的情况下可以省略.
tuple04 = 10, 20, 30
print(tuple04)

# 特殊3:拆包
python, b, c = tuple04
python, b, c = [10, 20, 30]
python, b, c = "孙悟空"
print(python)
print(b)
print(c)
