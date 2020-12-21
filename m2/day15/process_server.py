"""
网络并发模型
"""
import sys
from socket import *
from multiprocessing import *

HOST = "0.0.0.0"
PORT = 7878
ADDR = (HOST, PORT)


# 处理的入口
def handle(coonfd):
    while True:
        data = coonfd.recv(1024)
        if not data:
            break
        print(data.decode())
    coonfd.close()


def main():
    tcp_socket = socket()
    tcp_socket.bind(ADDR)
    tcp_socket.listen(5)

    while True:
        try:
            connfd, addr = tcp_socket.accept()
        except KeyboardInterrupt:
            tcp_socket.close()
            sys.exit("退出")
        p = Process(target=handle, args=(connfd,), daemon=True)
        p.start()


if __name__ == '__main__':
    main()
