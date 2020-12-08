"""
读操作
"""
import pymysql

# 生成数据库对象
args = {"host": "192.168.92.129",
        "port": 3306,
        "user": "root",
        "password": "ieig",
        "database": "stu",
        "charset": "utf8"}
db = pymysql.connect(**args)
# 创建游标
cur = db.cursor()

sql = "select name,score from class_1 where score >%s"
cur.execute(sql, [50])

# 迭代法
# for row in cur:
#     print(row)

one = cur.fetchone()
print(one)

many = cur.fetchmany(3)
print(many)

all_1 = cur.fetchall()
print(all_1)

# 关闭数据库连接
cur.close()
db.close()
