import MySQLdb

from flask import Flask

from flask import render_template




app = Flask(__name__)


@app.route("/")

def hello():

    db = MySQLdb.connect("localhost", "root", "1234","nodejs")

    cur = db.cursor()

    cur.execute("select * from todos")




    while True:

        emp = cur.fetchone()

        if not emp: break

        templateData = {

            'empno' : emp[0],

            'ename' : emp[1]

        }

        return render_template('test.html', **templateData)

    cur.close()

    db.close()







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)



