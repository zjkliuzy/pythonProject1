import sys
from socket import socket
from threading import Thread


class Handle:
    def request(self, data):
        print(data)


class ClientThread(Thread):
    def __init__(self, connfd):
        super().__init__(daemon=True)
        self.connfd = connfd
        self.handle = Handle()

    def run(self) -> None:
        while True:
            data = self.connfd.recv(1024)
            if not data:
                break
            self.handle.request(data.decode())


# 并发服务类
class ConcurrentServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.addr = (host, port)
        self.sock = self.__create_connection()

    def __create_connection(self):
        tcp_socket = socket()
        tcp_socket.bind(self.addr)
        return tcp_socket

    def serve(self):
        self.sock.listen(5)
        while True:
            connfd, addr = self.sock.accept()
            t = ClientThread(connfd)
            t.start()


if __name__ == '__main__':
    con = ConcurrentServer("0.0.0.0", 7878)
    con.serve()
