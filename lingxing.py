# a = int(input("请输入菱形每条边星星的个数："))
# b = a
# c = a
# print(" " * (a - 1), "*")
# for i in range(2, a + 1):  # 先打印正三角，由空格和*根据规律组成
#     print(" " * (b - 1) + "*" + " " * (2 * i - 3) + "*")
#     b -= 1
#     if i == a:  # 临界点，当打印到此，开始打印倒三角
#         for y in range(2, a):
#             print(" " * y + "*" + " " * (2 * c - 5) + "*")
#             c -= 1
#         print(" " * a + "*")

a = 5
b = a
c = a
for i in range(1, a + 1):
    print(" " * (b - 1), "*" * (i * 2 - 1))
    b -= 1
    if i == a:
        for j in range(0, a):
            print(" " * j, "*" * (2 * c - 1))
            c -= 1
