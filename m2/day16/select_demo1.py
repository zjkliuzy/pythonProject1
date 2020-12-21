"""
IO多路复用
"""
from select import select
from socket import socket, AF_INET, SOCK_DGRAM

file = open("log.txt")
udp_sock = socket(AF_INET, SOCK_DGRAM)

tcp_sock = socket()
tcp_sock.bind(("0.0.0.0", 8980))
tcp_sock.listen(5)

print("开始监控")
rs, ws, xs = select([], [udp_sock, file], [])
print("re:", rs)
print("ws:", ws)
print("xs:", xs)
