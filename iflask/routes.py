from iflask import app
from flask import render_template, url_for


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html', title='About')


@app.route('/register')
def register():
	return render_template('register.html', title='Register')


@app.route('/login')
def login():
	return render_template('login.html', title='Login')