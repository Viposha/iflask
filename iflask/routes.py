from flask_login import current_user, login_user, logout_user, login_required
from iflask import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from iflask.forms import RegistrationForm, LoginForm
from iflask.models import User, Post


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
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'{form.username.data}, you are successfully register!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout_page():
	logout_user()
	return redirect(url_for('home'))


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
	return render_template('account.html', title='Account')


@app.route("/new_post", methods=['GET', 'POST'])
@login_required
def new_post():
	return render_template('new_post.html', title='Account')
