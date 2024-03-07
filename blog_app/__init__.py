from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from  flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '69de6319736a3b8bdf8f0098059a7dd9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from blog_app import routes
