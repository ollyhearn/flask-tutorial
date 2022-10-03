from app import app
from flask import render_template

@app.route('/')
def index():
	name = "Me"
	return render_template('index.html', n=name)

@app.route('/info')
def info():
	return render_template('info.html', n="INFO!")
