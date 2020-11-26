list01 = [62, 3, 9, 33, 56, 12, 332, 395]


def condition01(number):
    return number > 10


def condition02(number):
    return number % 3 == 0


def find(func):
    for num in list01:
        if func(num):
            yield num


find(condition01)
