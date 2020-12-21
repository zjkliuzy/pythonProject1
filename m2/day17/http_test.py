from socket import socket

s = socket()
s.bind(("0.0.0.0", 9999))
s.listen(5)

conn, addr = s.accept()
data = conn.recv(1024)

print(data.decode())
resp = """ HTTP/1.1 200 OK

<a href='www.baidu.com'>家</a>
"""

conn.send(resp.encode())
conn.close()
