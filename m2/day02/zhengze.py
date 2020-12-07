import re

print(re.findall("[A-Z][a-z]*", "How are you,Jame"))

print(re.findall("[0-9]+", "小明身高:175cm,体重 70kg"))

print(re.findall("-?[0-9]+", "小明身高:175cm,体重 -70kg"))

print(re.findall("1[3578][0-9]{9}", "15730303030"))

print(re.findall(r"\d{4}-\d{1,2}-\d{1,2}", "2020-1-1"))

re.findall('[1-9][0-9]{5,10}', "Baron:1259296994")
print(re.findall(r"\b[A-Z]+[a-z]*", "Hello,A boy iPython NBA"))
print(re.findall(r"\$\d+", "日❤：$120"))
print("❀")
# ❤❤❤❤❤❤❀❀❀❀❀❀❀❀❀
print(re.findall(r"《.+?》", "《你好@@@》,《我们~~~~》,《嘿嘿嘿###》"))

print((re.search(r"(\d{1,3}\.){3}\d{1,3}", "11.0.0.245").group()))
print("o(*￣︶￣*)o")
print(re.findall(r"(\w+):(\d+)", "Alex:1994,Bob:1999"))
print(re.split(r"\d+", "Alex:1994,Bob:1999"))
print(re.sub(r"\W+", "##", "Alex:1994,Bob:1999"))
