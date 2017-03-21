from flask import Flask, render_template
import json
#import MySQLdb
import string
from flaskext.mysql import MySQL 
#from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'flasktest'
app.config['MYSQL_DATABASE_PASSWORD'] = 'flaskpass'
app.config['MYSQL_DATABASE_DB'] = 'flasktest_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    #user = { 'nickname': 'Miguel' } 
    #return render_template("page1.html",
        #title = 'Home',
        #user = user)
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT *  FROM extens")
    data = cursor.fetchall()
    return json.dumps(data)
	
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5010,debug=True)
