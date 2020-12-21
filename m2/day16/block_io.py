from socket import *
from time import ctime, sleep

sockfd = socket()
sockfd.bind(("0.0.0.0", 7979))
sockfd.listen(5)
# 设置为非阻塞
# sockfd.setblocking(False)
sockfd.settimeout(1)
file = open("log.txt", "w")
while True:
    print("等待连接")
    try:
        connf, addr = sockfd.accept()
        print("连上了")
    except BlockingIOError as e:
        sleep(2)
        msg = "%s: %s\n" % (ctime(), e)
        file.write(msg)
        file.flush()
    except timeout as t:
        msg = "%s: %s\n" % (ctime(), t)
        file.write(msg)
        file.flush()
    else:
        data = connf.recv(1024)
        print(data.decode())
