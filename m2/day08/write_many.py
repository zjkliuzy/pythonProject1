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
list_stu = [("James", 20, "w", 98),
            ("Jackson", 23, "w", 97),
            ("Robert", 31, "w", 89)]

try:
    # 写操作
    sql = "insert into class_1(name,age,sex,score)values (%s,%s,%s,%s)"
    cur.executemany(sql, list_stu)
    # 使用pymysql，会自动开启事务，如果引擎不支持事务，execute后直接生效。如果引擎支持事务，commit后才提交
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭数据库连接
cur.close()
db.close()
