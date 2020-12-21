from select import select
from socket import socket


class Handle:

    def __init__(self, connfd):
        self.connfd = connfd

    def request(self):
        data = self.connfd.recv(1024).decode()


class WebServer:
    def __init__(self, host, port, html):
        self.host = host
        self.port = port
        self.html = html
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.sock = self.create_sock()

    def create_sock(self):
        tcp_sock = socket()
        self.adderss = (self.host, self.port)
        tcp_sock.bind(self.adderss)
        tcp_sock.setblocking(False)
        return tcp_sock

    def connect(self):
        connfd, addr = self.sock.accept()
        connfd.setblocking(False)
        self.rlist.append(connfd)

    def start(self):
        self.sock.listen(5)
        self.rlist.append(self.sock)
        # io多路复用
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sock:
                    self.connect()
                else:
                    self.handle(r)
                    r.close()
                    self.rlist.remove(r)

    def handle(self, connfd):
        try:
            result = connfd.recv(1024 * 1024)
            print(result.decode())
            header = result.decode().split("\r\n")[0]
            cont = header.split(" ")[1]
            print("请求内容", cont)
            self.send_response(cont, connfd)
        except:
            pass

    def send_response(self, cont, connfd):
        try:
            if cont == "/":
                with open("static/index.html", "rb") as file:
                    resp = " HTTP/1.1 200 OK\r\n" + "Content-Type: text/html\r\n\r\n"
                    response = resp.encode() + file.read()
                connfd.send(response)
            else:

                with open("static" + cont, "rb") as file:
                    resp = " HTTP/1.1 200 OK\r\n" + "Content-Type: text/html\r\n\r\n"
                    response = resp.encode() + file.read()
                connfd.send(response)
        except Exception as e:
            response = "HTTP/1.1 404 Not Found\r\n"
            connfd.send(response.encode())
            print(e)


if __name__ == '__main__':
    httpd = WebServer(host="0.0.0.0", port=80, html="")
    httpd.start()
