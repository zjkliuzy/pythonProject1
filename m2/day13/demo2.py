from multiprocessing import *
import time


def decorate(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("执行时间：", end_time - start_time)
        return res

    return wrapper


# @decorate
# def process_one():
#     primes = []
#     for i in range(1, 100001):
#         if isPrime(i):
#             primes.append(i)
#
#     print(sum(primes))
#
#
# if __name__ == '__main__':
#     process_one()
class PrimeSumProcess(Process):
    def __init__(self, begin, end):
        super().__init__()
        self.begin = begin
        self.end = end

    @staticmethod
    def isPrime(n):
        if n <= 1:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True

    def run(self) -> None:
        """
        begin---end之间的质数和
        :return:
        """
        primes = []
        for i in range(self.begin, self.end):
            if PrimeSumProcess.isPrime(i):
                primes.append(i)
        print(sum(primes))


@decorate
def process_four():
    jobs = []
    for i in range(1, 100001, 25000):
        p = PrimeSumProcess(i, i + 25000)
        jobs.append(p)
        p.start()
    [j.join() for j in jobs]


@decorate
def process_ten():
    jobs = []
    for i in range(1, 100001, 10):
        p = PrimeSumProcess(i, i + 10)
        jobs.append(p)
        p.start()
    [j.join() for j in jobs]


if __name__ == '__main__':
    process_ten()
