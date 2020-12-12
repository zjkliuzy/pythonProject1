from multiprocessing import Process
from time import sleep


# 有参数的进程函数
def fun(sec, name):
    for i in range(3):
        sleep(sec)
        print("我是{}".format(name))
        print("执行中")


if __name__ == '__main__':
    p = Process(target=fun, kwargs={"sec": 2, "name": "Bob"})
    # 启动进程
    p.start()

    # 阻塞等待回收进程
    p.join()
