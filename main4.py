from common.iterable_tools import IterableHelper

list01 = [62, 3, 9, 33, 56, 12, 332, 395]


def find01():
    for item in list01:
        print(item % 2)


# find01()


def find02():
    for item in list01:
        if item % 3 == 0 or item % 5 == 0:
            yield item


def cond01(num):
    return num % 2 != 0


def cond02(num):
    return num % 3 == 0 or num % 5 == 0


def find_all(func):
    for item in list01:
        if func(item):
            yield item


for i in find_all(lambda a: a % 2 != 0):
    print(i)

for i in find_all(lambda num: num % 3 == 0 or num % 5 == 0):
    print(i)

IterableHelper.find_all(list01, lambda a: a % 2 != 0)
