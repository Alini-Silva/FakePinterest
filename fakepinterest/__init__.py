from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///comunidade.db"
app.config['SECRET_KEY']  = "908415b6496579bb5412881f6b70df90"
app.config['UPLOAD_FOLDER'] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.logim_view = "homepage"

from fakepinterest.models import Usuario, Foto

from fakepinterest import routes