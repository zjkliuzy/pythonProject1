# 进程执行函数
import multiprocessing
from time import sleep

python = 1


def fun():
    print("开始运行")
    sleep(3)
    # print(a)
    global python
    python = 100000
    print("执行完成")


if __name__ == '__main__':
    p = multiprocessing.Process(target=fun)
    # 启动进程
    p.start()

    print("执行2")
    sleep(2)
    print("完成2")

    # 阻塞等待回收进程
    p.join()
    print(python)
