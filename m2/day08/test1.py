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
name = input("姓名")
try:
    # 写操作
    sql = "update class_1 set score=100 where name ='Bob';"
    cur.execute(sql)
    # 使用pymysql，会自动开启事务，如果引擎不支持事务，execute后直接生效。如果引擎支持事务，commit后才提交
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭数据库连接
cur.close()
db.close()
