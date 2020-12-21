import os
from socket import socket
from threading import Thread


class Handle:
    def __init__(self, connfd):
        self.connfd = connfd

    def check_files(self):  # 查看文件家里面的文件
        file_list = os.listdir("dir")
        if file_list:
            pass
        else:
            self.connfd.send(b"FAIL")
        files = ""
        for file in file_list:
            files += file + "\n"
        self.connfd.send(files.encode())

    def request(self, data):  # 分情况
        temp = data.split(" ")
        if temp[0] == "LIST":
            self.check_files()


class ClientThread(Thread):
    def __init__(self, connfd):
        super().__init__(daemon=True)
        self.connfd = connfd
        self.handle = Handle(connfd)

    def run(self) -> None:
        while True:
            data = self.connfd.recv(1024).decode()
            if not data:
                break
            self.handle.request(data)
        self.connfd.close()


class FtpServer:
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
    ftp = FtpServer("0.0.0.0", 7878)
    ftp.serve()
