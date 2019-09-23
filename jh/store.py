import Adafruit_DHT
import time
import datetime
import MySQLdb



sensor = Adafruit_DHT.DHT11

pin = 24 #GPIO







# type = float




while True:    

    wtime = datetime.datetime.now()

    #t_date = wtime.strftime('%Y-%B-%d %A')

    t_year = wtime.strftime('%Y')

    t_month = wtime.strftime('%m')

    t_day = wtime.strftime('%d')

    #t_time = wtime.strftime('%H:%M')

    t_time = wtime.strftime('%H')




    t_humidity, t_temperature = Adafruit_DHT.read_retry(sensor, pin)

    sql = "insert into temperature values('%s','%s','%s','%s','%s','%s')" %(t_year,t_month,t_day,t_time,t_humidity,t_temperature)

    db = MySQLdb.connect("localhost","root","1234","SCOTT")

    cur = db.cursor()




    try:

        cur.execute(sql)

        db.commit()

    except KeyboardInterrupt:

        cur.close()

        db.close()

        print("stop")

    time.sleep(3600)




