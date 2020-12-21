from socket import socket

s = socket()
s.bind(("0.0.0.0", 9999))
s.listen(5)

conn, addr = s.accept()
data = conn.recv(1024)

# print(data.decode())
file = open("address.png", "rb")
cont = file.read()  # 图片内容
resp = "HTTP/1.1 200 OK\r\n" + "Content-Type:image/jpeg\r\n\r\n"

resp1 = resp.encode() + cont  # 把请求头和请求体合在一起

file.close()
conn.send(resp1)
conn.close()
