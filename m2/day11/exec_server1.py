import time
from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.bind(("0.0.0.0", 7878))
tcp_socket.listen(5)

print("等待连接。。。")
connfd, addr = tcp_socket.accept()
print("连上了:", addr)
filename = time.strftime("%Y-%m-%d", time.localtime())
file = open(filename + ".jpg", "wb")
while True:
    data = connfd.recv(1024)
    if not data:  # 收到空，因为客户端close了
        break
    file.write(data)
file.close()
connfd.close()
tcp_socket.close()
