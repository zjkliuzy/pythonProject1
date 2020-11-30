class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


list_name = ["jack", "bob", "james"]
list_age = [22, 33, 44]
list_sex = ["男", "男", "男"]

list_student = [Student(*i) for i in zip(list_name, list_age, list_sex)]

for item in list_student:
    print(item)

a = 0
b = 1
for i in range(1, 12):
    a, b = b, a + b
    print(b)
