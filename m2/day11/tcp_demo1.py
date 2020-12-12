from socket import *
from time import sleep

tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.bind(("0.0.0.0", 7878))
tcp_socket.listen(5)

while True:
    print("等待连接。。。")
    connfd, addr = tcp_socket.accept()
    print("连上了:", addr)
    while True:
        data = connfd.recv(5)
        # if data.decode() == "##":
        #     connfd.close()
        #     break
        if not data:  # 收到特定字节串，表示客户端以及断开
            break
        print("收到:", data.decode())
        connfd.send("Hello".encode())
        sleep(0.1)
    connfd.close()

tcp_socket.close()

