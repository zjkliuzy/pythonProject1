from common.iterable_tools import IterableHelper


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


# def find02():
#     for emp in list_employees:
#         yield emp.eid, emp.money
#
#
# def find01():
#     for emp in list_employees:
#         yield emp.name

def cond1(emp):
    return emp.eid, emp.money


def cond2(emp):
    return emp.name


list0 = IterableHelper.select(list_employees, lambda emp: (emp.eid, emp.money))

list0000 = map(lambda x: x.name, list_employees)
print(list(list0000))
list111 = map(lambda x: (x.eid, x.money), list_employees)
print(list(list111))


def get_max(func, iterable):
    max_value = iterable[0]
    for item in range(1, len(iterable)):
        if func(max_value) < func(item):
            max_value = item
    return max_value
