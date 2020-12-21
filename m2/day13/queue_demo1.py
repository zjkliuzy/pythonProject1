from multiprocessing import *

q = Queue(12)


def handle():
    while True:
        res = q.get()
        print("res:", res)
        try:
            eval(res)
        except:
            print("错误")


if __name__ == '__main__':
    p = Process(target=handle, daemon=True)

    p.start()
    while True:
        value = input("输入")
        if value == "exit":
            break
        q.put(value)
