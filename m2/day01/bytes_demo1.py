"""
字节串变量
"""
b = b"hello world"  # 定义字节串 ascii字符
print(type(b))
# 非ascii字符的字节串
bc = "你好".encode()
print(bc)
s1 = b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode()
print(s1)
