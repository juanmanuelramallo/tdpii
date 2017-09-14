from flask import Flask, render_template, request, flash, redirect, url_for, session, logging, jsonify
from flaskext.mysql import MySQL

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
	cursor = mysql.connect().cursor()
	cursor.execute(" SELECT valor FROM periodos ORDER BY id DESC LIMIT 1")
	periodo = cursor.fetchone();
	cursor.execute(" SELECT AVG(temperatura) FROM datos ORDER BY id DESC LIMIT 10")
	promediotemp = cursor.fetchone()
	cursor.execute(" SELECT AVG(humedad) FROM datos ORDER BY id DESC LIMIT 10")
	promediohum = cursor.fetchone()
	cursor.execute(" SELECT AVG(presion) FROM datos ORDER BY id DESC LIMIT 10")
	promediopresion = cursor.fetchone()
	cursor.execute(" SELECT AVG(velocidad_viento) FROM datos ORDER BY id DESC LIMIT 10")
	promediovel = cursor.fetchone()
	cursor.execute(" SELECT temperatura FROM datos ORDER BY id DESC LIMIT 1")
	ultimatemperatura = cursor.fetchone()
	cursor.execute(" SELECT humedad FROM datos ORDER BY id DESC LIMIT 1")
	ultimahum = cursor.fetchone()
	cursor.execute(" SELECT presion FROM datos ORDER BY id DESC LIMIT 1")
	ultimapresion = cursor.fetchone()
	cursor.execute(" SELECT velocidad_viento FROM datos ORDER BY id DESC LIMIT 1")
	ultimavelocidad = cursor.fetchone()
	cursor.close()
	return render_template('response.html', periodo = periodo, promediotemp = promediotemp, promediohum = promediohum, promediopresion = promediopresion, promediovel = promediovel, ultimatemperatura = ultimatemperatura, ultimapresion = ultimapresion, ultimavelocidad = ultimavelocidad, ultimahum = ultimahum)

@app.route('/datos')
def sensor():
	cursor = mysql.connect().cursor()
	cursor.execute(" SELECT valor FROM periodos ORDER BY id DESC LIMIT 1")
	periodo = cursor.fetchone();
	cursor.execute(" SELECT AVG(temperatura) FROM datos ORDER BY id DESC LIMIT 10")
	promediotemp = cursor.fetchone()
	cursor.execute(" SELECT AVG(humedad) FROM datos ORDER BY id DESC LIMIT 10")
	promediohum = cursor.fetchone()
	cursor.execute(" SELECT AVG(presion) FROM datos ORDER BY id DESC LIMIT 10")
	promediopresion = cursor.fetchone()
	cursor.execute(" SELECT AVG(velocidad_viento) FROM datos ORDER BY id DESC LIMIT 10")
	promediovel = cursor.fetchone()
	cursor.execute(" SELECT temperatura FROM datos ORDER BY id DESC LIMIT 1")
	ultimatemperatura = cursor.fetchone()
	cursor.execute(" SELECT humedad FROM datos ORDER BY id DESC LIMIT 1")
	ultimahum = cursor.fetchone()
	cursor.execute(" SELECT presion FROM datos ORDER BY id DESC LIMIT 1")
	ultimapresion = cursor.fetchone()
	cursor.execute(" SELECT velocidad_viento FROM datos ORDER BY id DESC LIMIT 1")
	ultimavelocidad = cursor.fetchone()
	cursor.close()
	return jsonify(periodo = periodo, promedio_temperatura = promediotemp, promedio_humedad = promediohum, promedio_presion = promediopresion, promedio_velocidad = promediovel, ultima_temperatura = ultimatemperatura, ultima_presion = ultimapresion, ultima_velocidad = ultimavelocidad, ultima_humedad = ultimahum)

@app.route('/configurar', methods=['POST'])
def configurar():
  periodo = request.form['periodo']
  query = " INSERT INTO periodos(valor) VALUES(%s)"
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute(query, (periodo))
  conn.commit()
  cursor.close()
  return jsonify(periodo)

if __name__ == '__main__':
	app.run(host='localhost', port=80)
else:
	print('FALLO la aplicacion')
