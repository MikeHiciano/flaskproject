#! usr/bin/env python
# -*- encoding:'utf-8' -*-

''' programa utilizando flask y html para controlar salidas del rpi'''

#adaptar para la raspberry pi
#modificar archivos de templates para que seas mas 'client friendy'
#aprender javascript y jquery para poder continuar con el proyecto
#baraje con su vida , y siga mañana caballero
#commit @10:16 pm 

from flask import Flask , render_template
import time

app = Flask(__name__)

@app.route('/')
def inicio():
	return render_template('index.html')

@app.route('/<name>')
def index(name):
	return render_template('notaindex.html', name = name)

@app.route('/led1on')
def red_led_on():
	
	#crear archivo html para esto
	return render_template('redledon.html')


@app.route('/led2on')
def green_led_on():
	
	#crear archivo html para esto
	return render_template('greenledon.html')

if __name__ == '__main__':
	app.run(debug = True,host = '0.0.0.0')