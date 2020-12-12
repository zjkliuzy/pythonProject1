from socket import *

##
#
##
udp_socket = socket(AF_INET, SOCK_DGRAM)

ADDR = ("127.0.0.1", 8789)

msg = input(">>")
n = udp_socket.sendto(msg.encode(), ADDR)

data, addr1 = udp_socket.recvfrom(1024)
print("收到回复：", data.decode())
