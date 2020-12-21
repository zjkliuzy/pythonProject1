"""
client
"""
import sys
from socket import *
from multiprocessing import *

# 服务器地址
ADDR = ("127.0.0.1", 9733)


def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(data.decode())


def send_msg(sock, name):
    while True:
        try:
            msg_input = input("聊天内容")
        except KeyboardInterrupt:
            msg_input = "##"
        if msg_input == "##":  # 退出
            msg = "EXIT %s" % name
            sock.sendto(msg.encode(), ADDR)
            sys.exit()
        msg = "CHAT %s %s" % (name, msg_input)
        sock.sendto(msg.encode(), ADDR)


def do_login(sock):
    while True:
        name = input("输入姓名")
        msg = "LOGIN " + name
        sock.sendto(msg.encode(), ADDR)
        data, addr = sock.recvfrom(1024)
        if data == b"OK":
            print("登录成功")
            return name
        else:
            print("失败，重新登录")


def do_chat(sock, name):
    p = Process(target=recv_msg, args=(sock,), daemon=True)
    p.start()
    send_msg(sock, name)


def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(("0.0.0.0", 56778))
    name = do_login(sock)
    # 聊天
    do_chat(sock, name)


if __name__ == '__main__':
    main()
