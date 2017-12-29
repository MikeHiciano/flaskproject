import RPi.GPIO as GPIO
from flask import Flask , render_template
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def inicio():
	return render_template('index.html')

@app.route('/<name>')
def index(name):
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	return render_template('notaindex.html', name = name)

@app.route('/led1on')
def red_led_on():
	
	#crear archivo html para esto
	GPIO.output(17,GPIO.HIGH)
	return render_template('redledon.html')


@app.route('/led2on')
def green_led_on():
	
	#crear archivo html para esto
	GPIO.output(27,GPIO.HIGH)
	return render_template('greenledon.html')

if __name__ == '__main__':
	app.run(debug = True,host = '0.0.0.0')