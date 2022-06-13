from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e993ef007102772e684ad667a53c839d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iflask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

# from .models import User, Post
# db.create_all()

from iflask import routes
