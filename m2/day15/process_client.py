from socket import *

ADDR = ("127.0.0.1", 7878)

tcp_socket = socket()

tcp_socket.connect(ADDR)

while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())

    # data = tcp_socket.recv(1024)
    # print("收到服务器：", data.decode())

tcp_socket.close()
