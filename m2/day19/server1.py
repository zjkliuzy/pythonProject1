from socket import socket
from threading import Thread
from time import sleep

from m2.day19.database1 import DataDao


class Handle:
    def __init__(self, connfd):
        self.connfd = connfd
        self.db = DataDao()
        self.db.courcs()

    def exit(self):
        self.connfd.close()
        self.db.courcs_close()
        self.db.close()

    def register(self, data):
        temp = data.split(" ")
        uname = temp[0]
        upass = temp[1]
        result = self.db.check_occupy(uname)
        if not result:  # 没查到，没有被占用
            row = self.db.insert_user(uname, upass)
            if row:
                self.connfd.send(b"OK")
            else:
                self.connfd.send(b"FAIL")
        else:
            self.connfd.send(b"FAIL")

    def login(self, data):
        temp = data.split(" ")
        uname = temp[0]
        upass = temp[1]
        result = self.db.check_user(uname, upass)
        if result:
            self.connfd.send(b"OK")
        else:
            self.connfd.send(b"FAIL")

    def query_word(self, data):
        temp = data.split(" ")
        result = self.db.query_by_word(temp[0])
        id = self.db.query_id_by_name(temp[1])
        self.db.insert_log(id, temp[0])
        if not result:
            self.connfd.send(b"FAIL")
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
            self.connfd.send(result.encode())

    def query_history(self, name):
        result = self.db.query_history(name)
        if not result:
            self.connfd.send(b"FAIL")
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
            value = ""
            for name, word, time in result:
                value += "%s %s %s\n" % (name, word, str(time))
            self.connfd.send(value.encode())

    def request(self, data):
        temp = data.split(" ", 1)
        if temp[0] == "REG":
            self.register(temp[1])
        elif temp[0] == "LOGIN":
            self.login(temp[1])
        elif temp[0] == "QUERY":
            self.query_word(temp[1])
        elif temp[0] == "EXIT":
            self.exit()
        elif temp[0] == "HIST":
            self.query_history(temp[1])


class ClientProcess(Thread):
    def __init__(self, connfd):
        super().__init__(daemon=True)
        self.connfd = connfd
        self.handle = Handle(connfd)

    def run(self) -> None:
        while True:
            data = self.connfd.recv(1024)
            if not data:
                break
            self.handle.request(data.decode())


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
            try:
                connfd, addr = self.sock.accept()
            except:
                self.sock.close()
                break
            t = ClientProcess(connfd)
            t.start()


if __name__ == '__main__':
    server = ConcurrentServer(host="0.0.0.0", port=7890)
    server.serve()
