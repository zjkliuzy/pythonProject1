# file = open(r"D:\p1\aa.txt", "r")
# cont = file.read()
# print(cont)
# #print(file)
# file.close()
with open(r"D:\p1\aa.txt", "w", buffering=1) as file:
    # res = ""
    # while True:
    #     line = file.read(5)
    #     if not line:
    #         break
    #     print(line, end="")  # 每次打印不换行

    # res = file.readlines(8)
    # print(res)
    while True:
        input_text = input(">>")
        file.write(input_text)
        file.flush()
