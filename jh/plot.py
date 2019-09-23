import MySQLdb
import datetime
import matplotlib.pyplot as plt
import sys



## xpoint, ypoint (x = time, y = temperature)



sql = "select ctime,cpercent from detectdata_detect where cname='%s'"

db = MySQLdb.connect("70.12.111.178","tester","1234","mysample")

cur = db.cursor()
cur.execute(sql%(sys.argv[1]))
row = cur.fetchall()

x=[]
y=[]
y1=[]




for i in row:
   # x.append(i[0])
    x.append(i[0])
    y.append(i[1])
    y1.append(10)
    print(i[0],i[1])


plt.title('face_recog')
plt.xlabel('time')
plt.ylabel('percent')
#plt.xlim([0,24])
plt.plot(x,y)
#plt.savefig("detect.png", dpi=350)
plt.show()
cur.close()
db.close()


