from socket import *

ADDR = ("127.0.0.1", 7878)

tcp_socket = socket()

tcp_socket.connect(ADDR)

file = open("databases.jpg", "rb")

while True:
    data = file.read(1024)
    if not data:
        break
    tcp_socket.send(data)
file.close()
tcp_socket.close()
