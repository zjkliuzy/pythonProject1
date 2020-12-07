import re

# s = "Alex:1994,Bob:1999"
# res = re.finditer(r"\w+", s)
# for item in res:
#     # match对象
#     print("内容", item.group())
#     print("位置", item.span())
#
# res2 = re.match(r"\d+", s)
# print(res2)
#
# res = re.search(r"(\w+):(?P<aaa>\d+)", s)
# print(res.group(1))
# print(res.groupdict())
s = """Hello
北京
"""
result = re.findall(r"^\w+", s, re.M | re.A)
print(result)
