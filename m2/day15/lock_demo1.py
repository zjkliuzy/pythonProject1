"""
线程锁
join
"""
from threading import Thread, Lock

a = b = 1
lo = Lock()  # 创建锁


def func():
    while True:
        lo.acquire()  # 上锁，阻塞
        if a != b:
            print("a={},b={}¤℗◎卐©".format(a, b))
        lo.release()


t = Thread(target=func)
t.start()
while True:
    with lo:  # 上锁，阻塞¤℗◎卐©
        a += 1
        b += 1

# t.join()
