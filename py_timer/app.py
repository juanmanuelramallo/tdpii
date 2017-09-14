from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from flaskext.mysql import MySQL
import time
from random import randint
import threading
import datetime

app = Flask(__name__)

# Config MySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jmra1234'
app.config['MYSQL_DATABASE_DB'] = 'tpii'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


#Define la ruta con la que se ingresa desde browser
@app.route('/')
def index():
  print "Empieza"
  periodo = 1.0
  conn = mysql.connect()
  cursor = conn.cursor()
  while 1:
    print "Start : %s" % time.ctime()
    time.sleep( periodo )
    print "End : %s" % time.ctime()
    cursor.execute(" SELECT valor FROM periodos ORDER BY id DESC LIMIT 1")
    periodo = cursor.fetchone()[0]
    print("periodo %s " % periodo)
    randomtemp = randint(0,100)
    randomhum = randint(0,100)
    randompresion = randint(0,10)
    randomvel = randint(0,200)
    print randomtemp
    print randomhum
    print randompresion
    print randomvel
    query = "INSERT INTO datos(temperatura, humedad, presion, velocidad_viento) VALUES (%s,%s,%s,%s)"
    cursor.execute(query,(randomtemp, randomhum, randompresion, randomvel))
    conn.commit()
  cursor.close()
  return render_template('index.html', frecuencia_muestreo = frecuencia_muestreo)

if __name__ == '__main__':
	app.run(host='localhost', port=5000)
else:
	print('FALLO la aplicacion')
