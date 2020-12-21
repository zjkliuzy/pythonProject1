from select import *
from socket import *

ADDR = ("0.0.0.0", 7878)
tcp_sock = socket()
tcp_sock.bind(ADDR)
tcp_sock.listen(5)
# 查找字典 {fileno:IO对象}
map1 = {tcp_sock.fileno(): tcp_sock}

p = epoll()
p.register(tcp_sock, EPOLLIN)
print("开始监控")
events = p.poll()  # 负责监控
while True:
    # [(fileno,event)]
    # 文件描述符： 系统分配给每一个IO的整数编号
    for fileno, event in events:
        r = map1.get(fileno)
        if r is tcp_sock:
            connfd, addr = r.accept()  # ￣へ￣
            print("连上：", addr)
            connfd.setblocking(False)
            map1[connfd.fileno()] = connfd
            p.register(connfd, EPOLLIN)
        else:
            da = r.recv(1024)
            if not da:
                p.unregister(fileno)
                r.close()
                map1.pop(r.fileno())
                continue
            print(da.decode())
