from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager

UPLOAD_FOLDER = 'static/images/'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e993ef007102772e684ad667a53c839d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


from .models import User, Post
db.create_all()

from iflask import routes
