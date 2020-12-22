import pymysql

"""

"""


class DataDao:
    args = {"host": "192.168.92.129",
            "port": 3306,
            "user": "root",
            "password": "ieig",
            "database": "stu",
            "charset": "utf8"}

    def __init__(self):
        self.db = pymysql.connect(**DataDao.args)

    def courcs(self):
        self.cur = self.db.cursor()

    def courcs_close(self):
        self.cur.close()

    def close(self):
        self.db.close()

    def check_occupy(self, uname):
        sql = "select name from user where name = %s"
        self.cur.execute(sql, [uname])
        one = self.cur.fetchone()
        if not one:
            return False  # 没有占用
        else:
            return True

    def query_id_by_name(self, uname):
        sql = "select id from user where name = %s"
        self.cur.execute(sql, [uname])
        one = self.cur.fetchone()
        if not one:
            return None  # 没有找到
        else:
            return one[0]

    def insert_user(self, uname, upass):
        sql = "insert into user(name,passwd) values(%s,%s)"
        row = self.cur.execute(sql, [uname, upass])
        self.db.commit()
        return row

    def check_user(self, uname, upass):
        sql = "select name from user where name = %s and passwd = %s"
        self.cur.execute(sql, [uname, upass])
        one = self.cur.fetchone()
        if not one:
            return False  # 没找到，用户名密码错误
        else:
            return True

    def query_by_word(self, word):
        sql = "select means from words where word = %s"
        self.cur.execute(sql, [word])
        one = self.cur.fetchone()
        if not one:
            return None
        else:
            result = one[0]
            return result

    def insert_log(self, id, word):
        sql = "insert into history(user_id, word) VALUES (%s,%s)"
        row = self.cur.execute(sql, [id, word])
        self.db.commit()
        return row

    def query_history(self, uid):
        sql = "select u.name,h.word,h.time from history as h left join user as u on h.user_id= u.id where" \
              " u.name = %s order by h.time desc limit 10"
        self.cur.execute(sql, [uid])
        result = self.cur.fetchall()
        if not result:
            return None
        else:
            return result
