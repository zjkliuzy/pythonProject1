a = 4
b = a
print("*" + " " * (2 * a - 3) + "*")
for i in range(1, a):
    if i != a - 1:
        print(" " * i + "*" + " " * (2 * b - 5) + "*")
        b -= 1
    else:
        print(" " * i + "*")
