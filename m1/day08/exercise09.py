# 练习2：画出下列代码内存图，并写出打印结果。
def func01(p1, p2): 
    p1 = [100, 200]  
    p2[:] = [300, 400]
 
python = [10, 20]
b = [30, 40]
func01(python, b)
print(python)  # ?
print(b)  # ?
