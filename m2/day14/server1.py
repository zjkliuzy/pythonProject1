"""
server
"""
from socket import *
from multiprocessing import *

# 地址
ADDR = ("127.0.0.1", 9733)

# 用户信息
user = {}


def do_login(name, addr, sock):
    if name in user or "管理" in name:
        sock.sendto(b"FAIL", addr)
    else:
        print("收到姓名", name)
        msg = name + "进入聊天室"
        for key, value in user.items():
            sock.sendto(msg.encode(), value)
        user[name] = addr
        sock.sendto(b"OK", addr)


def do_chat(cont, sock):
    name = cont.split(" ", 1)[0]
    for key in user:
        msg = name + ":" + cont.split(" ", 1)[1]
        if key != name:
            sock.sendto(msg.encode(), user[key])


def do_ext(sock, name):
    del user[name]
    msg = name + "退出聊天室"
    for key, value in user.items():
        sock.sendto(msg.encode(), value)


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)

    p = Process(target=recv_method, args=(sock,), daemon=True)
    p.start()

    while True:
        cont = input("管理员消息")
        if cont == "##":
            break
        msg = "CHAT 管理员消息 " + cont
        sock.sendto(msg.encode(), ADDR)


def recv_method(sock):
    # 循环接收请求
    while True:
        data, addr = sock.recvfrom(1024)
        spr = data.decode().split(" ", 1)[0]
        cont = data.decode().split(" ", 1)[1]
        if spr == "LOGIN":
            do_login(cont, addr, sock)
        elif spr == "CHAT":
            do_chat(cont, sock)
        elif spr == "EXIT":
            do_ext(sock, cont)


if __name__ == '__main__':
    main()
