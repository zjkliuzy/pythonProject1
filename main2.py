list01 = [22, "hh", 334, "gdgd", 42, 66, 12, "hhh"]
result1 = (item for item in list01 if type(item) == str)
for item in result1:
    print(item)
result2 = (item * item for item in list01 if type(item) == int)
for item in result2:
    print(item)
