import os
import secrets
from PIL import Image

from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.utils import secure_filename

from iflask import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request, current_app
from iflask.forms import RegistrationForm, LoginForm, CreatePostForm
from iflask.models import User, Post


@app.route('/')
@app.route('/home')
def home():
	posts = Post.query.order_by(Post.date_posted.desc())
	return render_template('home.html', posts=posts)


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

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/images', picture_fn)

    output_size = (500, 600)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/new_post", methods=['GET', 'POST'])
@login_required
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        if form.picture.data:
            filename = save_picture(form.picture.data)
        post = Post(title=form.title.data, description=form.description.data, author=current_user,
                    picture=filename)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('new_post.html', title='New Post', form=form, legend='New Post')


@app.route("/user/<string:username>")
def user_posts(username):
    user = User.query.filter_by(username=username).first()
    posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc())
    return render_template('user_posts.html', posts=posts, user=user)
