"""
多个
"""
from multiprocessing import Process

import os
import sys
from time import sleep


def func1():
    print("eat")
    sleep(2)
    print(os.getpid(), "----", os.getppid())
    sys.exit("哈哈")


def func2():
    sleep(2)
    print("sleep")
    print(os.getpid(), "----", os.getppid())
    sys.exit("呵呵")


def func3():
    sleep(2)
    print("walk")
    print(os.getpid(), "----", os.getppid())
    sys.exit("嘿嘿")


jobs = []
if __name__ == '__main__':
    for f in [func1, func2, func3]:
        p = Process(target=f)
        jobs.append(p)
        p.start()

[i.join() for i in jobs]
