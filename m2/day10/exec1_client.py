from socket import *

##
#
##
udp_socket = socket(AF_INET, SOCK_DGRAM)

ADDR = ("172.40.54.108", 8789)
while True:
    msg = input(">>")
    if not msg:
        break
    n = udp_socket.sendto(msg.encode(), ADDR)
    # if msg == "##":
    #     break
    data, addr1 = udp_socket.recvfrom(1024)
    print("收到回复：", data.decode())
udp_socket.close()
