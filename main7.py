class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


# def get_count01():
#     for i in list_employees:
#         if i.money > 20000:
#             yield i

def sort_by01():
    for i in range(len(list_employees)):
        for j in range(0, len(list_employees) - i - 1):
            if list_employees[j] > list_employees[j + 1]:
                list_employees[j], list_employees[j + 1] = list_employees[j + 1], list_employees[j]


def sort_by(iterable, func):
    for i in range(len(iterable)):
        for j in range(0, len(iterable) - i - 1):
            if func(iterable[j]) > func(iterable[j + 1]):
                iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]


sort_by(list_employees, lambda emp: emp.money)
for l in list_employees:
    print(l.__dict__)


def get_count(func, iterable, money):
    for item in iterable:
        if func(item) > money:
            yield item

# for aaa in get_count(lambda emp: emp.money, list_employees, 20000):
#     print(aaa.__dict__)
