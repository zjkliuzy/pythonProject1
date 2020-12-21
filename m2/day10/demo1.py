import socket

# 创建udp套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 本地 127.0.0.1 另外一个程序必须在同一台计算机上

udp_socket.bind(("0.0.0.0", 9799))

data, addr = udp_socket.recvfrom(1024)

udp_socket.close()
