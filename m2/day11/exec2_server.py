from socket import *


# 回复函数
def response(connf):
    q = connf.recv(1024).decode()
    # 遍历字典关键词是否在问题中
    for key in dict_answer:
        if key in q:
            connf.send(dict_answer[key].encode())
            break
    else:
        connf.send("听不懂".encode())


dict_answer = {"你好": "你好",
               "多大": "我两岁了",
               "天气": "晴天"
               }
if __name__ == '__main__':

    tcp_socket = socket()
    # 绑定地址
    tcp_socket.bind(("0.0.0.0", 8888))

    # 设置监听
    tcp_socket.listen(5)

    while True:
        connf, addr = tcp_socket.accept()
        response(connf)
        connf.close()
