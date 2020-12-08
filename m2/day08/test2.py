import re

import pymysql


def get_data():
    """
    取得txt文件数据
    :return: 元组列表
    """
    dict1 = []
    with open("dict.txt") as file:
        dataline = file.readlines()
        for line in dataline:
            # split_text = line.split(" ", 1)
            # word = split_text[0]
            # expl = split_text[1].strip()
            # dict1.append((word, expl))
            word = re.findall(r"(\w+)\s+(.*)", line)
            dict1.append(word[0])
            print(word)

    return dict1


args = {"host": "192.168.92.129",
        "port": 3306,
        "user": "root",
        "password": "ieig",
        "database": "stu",
        "charset": "utf8"}


def insert_data(data):
    # 生成数据库对象

    db = pymysql.connect(**args)
    # 创建游标
    cur = db.cursor()
    try:
        sql = "insert into words(word,means) values (%s,%s)"
        cur.executemany(sql, data)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        cur.close()
        db.close()


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
    data = get_data()
    insert_data(data)
    # print(find_means("outwards"))
