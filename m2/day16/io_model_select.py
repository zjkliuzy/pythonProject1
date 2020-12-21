from select import select
from socket import *

ADDR = ("0.0.0.0", 7878)
tcp_sock = socket()
tcp_sock.bind(ADDR)
tcp_sock.listen(5)
tcp_sock.setblocking(False)

rlist = [tcp_sock]
wlist = []
xlist = []

while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        if r is tcp_sock:
            connfd, addr = r.accept()
            print("连上：", addr)
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            da = r.recv(1024)
            if not da:
                rlist.remove(r)
                r.close()
                continue
            print(da.decode())
            wlist.append(r)
    for w in ws:  #
        w.send(b"ok")
        wlist.remove(w)
