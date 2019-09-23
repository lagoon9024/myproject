import MySQLdb

db = MySQLdb.connect(host="70.12.111.178", user="tester", passwd="1234",charset="utf8",db="mysample")
cur = db.cursor()

sql="insert into sample values(112,'jjh','2019-11-25','F',10)"

try:
    cur.execute(sql)
    db.commit()
except:
    db.rollback()


rs = cur.fetchall()

for i in rs:
    print i

cur.close()
db.close()



