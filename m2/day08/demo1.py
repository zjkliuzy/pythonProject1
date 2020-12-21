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

# 操作数据

# 关闭数据库连接
cur.close()
db.close()
