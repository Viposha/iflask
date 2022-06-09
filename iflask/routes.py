from iflask import app
from flask import render_template, url_for
from iflask.forms import RegistrationForm, LoginForm


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)