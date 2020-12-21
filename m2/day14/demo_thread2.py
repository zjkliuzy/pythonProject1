from threading import Thread
from time import sleep


def func1(msg, sec):
    print("有参数")
    sleep(sec)
    print("{}执行完成".format(msg))


jobs = []
for i in range(5):
    t1 = Thread(target=func1, args=("哈哈%d" % i, 3))
    t1.start()
    jobs.append(t1)

[i.join() for i in jobs]
