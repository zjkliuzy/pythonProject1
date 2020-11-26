class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]
t1 = ([1, 1], [2, 2, 2], [3, 3, 3, 3])
m2 = max(t1, key=lambda x: len(x))
print("最大值", m2)

list111 = map(lambda x: (x.name, x.price), list_commodity_infos)
print(list(list111))
