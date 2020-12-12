import multiprocessing
from time import sleep


def fun():
    print("开始运行")
    sleep(3)
    print("执行完成")


if __name__ == '__main__':
    p = multiprocessing.Process(target=fun, name="AID", daemon=True)
    # 启动进程
    p.start()
    print(p.pid)
    print(p.is_alive())
    # 阻塞等待回收进程
    # p.join()
