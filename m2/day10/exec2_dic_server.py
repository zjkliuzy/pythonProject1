from socket import *

import pymysql

args = {"host": "192.168.92.129",
        "port": 3306,
        "user": "root",
        "password": "ieig",
        "database": "stu",
        "charset": "utf8"}


def find_means(word):
    # 生成数据库对象
    db = pymysql.connect(**args)
    # 创建游标
    cur = db.cursor()
    try:
        sql = "select means from words where word=%s"
        cur.execute(sql, [word])
        value = cur.fetchone()
        return value[0]
    except Exception as e:
        print(e)
    finally:
        cur.close()
        db.close()


if __name__ == '__main__':
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    udp_socket.bind(("0.0.0.0", 8789))

    while True:
        data, addr = udp_socket.recvfrom(1024)
        try:
            mean = find_means(data.decode())
            n = udp_socket.sendto(mean.encode(), addr)
        except:
            n = udp_socket.sendto("单词输入错误".encode(), addr)
            continue
