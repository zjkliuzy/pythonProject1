from socket import socket


class FtpView:
    def __init__(self):
        self.ftp_client = FtpClient("127.0.0.1", 7878)

    def __display_menu(self):
        print("1)查看文件")
        print("2)下载文件")
        print("3)上传文件")
        print("4)退出")
        print()

    def __manu_select(self):
        select = input("选择>>")
        if select == "1":
            self.ftp_client.check_file()
        elif select == "2":
            pass
        elif select == "3":
            pass
        elif select == "4":
            pass
        else:
            print("重新选择")

    def main(self):
        while True:
            self.__display_menu()
            self.__manu_select()


class FtpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.addr = (host, port)
        self.sock = self.connect_server()

    def connect_server(self):
        tcp_sock = socket()
        tcp_sock.connect(self.addr)
        return tcp_sock

    def check_file(self):
        self.sock.send(b"LIST")
        data = self.sock.recv(1024)
        result = data.decode()



if __name__ == '__main__':
    ftpView = FtpView()
    ftpView.main()
