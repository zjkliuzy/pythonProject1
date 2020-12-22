import sys
from socket import socket


class ClientView:
    def __init__(self):
        self.client = Client("127.0.0.1", 7890)
        self.level = 1  # 标识现在是第几层目录

    def display_menu_1(self):
        print("****一级******")
        print("1)注     册")
        print("2)登     录")
        print("3)退     出")
        print()

    def display_menu_2(self):
        print("****二级******")
        print("1)查   单   词")
        print("2)查询历史记录")
        print("3)注       销")
        print()

    def __manu_select1(self):
        select = input("选择>>")
        if select == "1":  # 注册
            uname = input("输入用户名:")
            upass = input("输入密码")
            result = self.client.register(uname, upass)
            if result == "OK":
                self.level = 2
                print("创建成功")
            else:
                print("用户名已被占用，请重新注册")
                pass
        elif select == "2":  # 登录
            uname = input("输入用户名:")
            upass = input("输入密码")
            result = self.client.login(uname, upass)
            if result == "OK":
                self.level = 2
                print("登录成功")
            else:
                print("用户名或密码输入错误，请重新登录")

        elif select == "3":  # 退出
            self.client.close()
            sys.exit("退出")
        else:
            print("重新选择")

    def __manu_select2(self):
        select = input("选择>>")
        if select == "1":  # 查单词
            while True:  # 循环
                word = input("输入单词(输入’##‘退出)：")
                if word == "##":
                    break
                value = self.client.query_word(word)
                print(value)
        elif select == "2":  # 查询历史记录
            value = self.client.query_history()
            print(value)

        elif select == "3":  # 注销
            self.level = 1
        else:
            print("重新选择")

    def main(self):
        while True:
            if self.level == 1:  # 一级
                self.display_menu_1()
                self.__manu_select1()
            elif self.level == 2:  # 二级
                self.display_menu_2()
                self.__manu_select2()


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.addr = (host, port)
        self.sock = self.connect_server()
        self.name = ""

    def close(self):
        self.sock.close()

    def connect_server(self):
        tcp_sock = socket()
        tcp_sock.connect(self.addr)
        return tcp_sock

    def register(self, uname, upass):
        str1 = "REG %s %s" % (uname, upass)
        self.sock.send(str1.encode())
        data = self.sock.recv(1024)
        result = data.decode()
        self.name = uname  # 登录或者注册要记住名字
        return result

    def login(self, uname, upass):
        str1 = "LOGIN %s %s" % (uname, upass)
        self.sock.send(str1.encode())
        data = self.sock.recv(1024)
        result = data.decode()
        self.name = uname  # 登录或者注册要记住名字
        return result

    def query_word(self, word):  # 查单词
        str1 = "QUERY %s %s" % (word, self.name)
        self.sock.send(str1.encode())
        data = self.sock.recv(1024)
        result = data.decode()
        if result == "OK":
            means = self.sock.recv(1024).decode()
            return means
        else:
            return "没查询到这个单词的解释"

    def query_history(self):  # 查历史记录
        str1 = "HIST %s" % self.name
        self.sock.send(str1.encode())
        data = self.sock.recv(1024)
        result = data.decode()
        if result == "OK":
            means = self.sock.recv(1024).decode()
            return means
        else:
            return "该用户没有查询记录"


if __name__ == '__main__':
    view = ClientView()
    view.main()
