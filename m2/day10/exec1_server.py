from socket import *

##
#
##
udp_socket = socket(AF_INET, SOCK_DGRAM)

udp_socket.bind(("0.0.0.0", 8789))


while True:
    data, addr = udp_socket.recvfrom(1024)

    print("收到:", data.decode(), "地址：", addr)

    n = udp_socket.sendto("你好".encode(), addr)

udp_socket.close()
