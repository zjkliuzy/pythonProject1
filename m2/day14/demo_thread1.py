import os
from threading import Thread
from time import sleep

a = 1


def func1():
    global a  # 一个进程中的所有线程共享这个进程的资源
    print("a=", a)
    a = 100000
    for i in range(3):
        sleep(3)
        print(os.getppid(), "你好你好")


t = Thread(target=func1)
t.start()
for i in range(4):
    sleep(2)
    print(os.getppid(), "你是谁你是谁")
t.join()
print(a)
