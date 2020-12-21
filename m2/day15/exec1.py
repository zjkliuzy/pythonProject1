"""
使用两个线程，一个打印1->52
一个打印A->Z
要求顺序为
12A34B --> 5152Z
"""
from threading import Thread, Lock

l1 = Lock()
l2 = Lock()


def print_number():
    for i in range(1, 53, 2):
        l1.acquire()
        print(i)
        print(i + 1)
        l2.release()  # 分别解开另一个锁


def print_word():
    for i in range(65, 91):
        l2.acquire()
        print(chr(i))
        l1.release()


t1 = Thread(target=print_word)
t2 = Thread(target=print_number)

l2.acquire()  # 先把2号锁上，一个开头

t1.start()
t2.start()

t1.join()
t2.join()
