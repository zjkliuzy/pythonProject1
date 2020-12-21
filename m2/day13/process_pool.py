from multiprocessing.pool import Pool
from time import ctime, sleep
import random


def worker(mag, sec):
    sleep(sec)
    print(ctime(), "---", mag)


if __name__ == '__main__':
    pool = Pool()
    for i in range(40):
        msg = "订单-%d" % i
        pool.apply_async(worker, args=(msg, random.random() * 8))
    pool.close()
    pool.join()
