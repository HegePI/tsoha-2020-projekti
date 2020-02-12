from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///register.db"    
    app.config["SQLALCHEMY_ECHO"] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import views

from application.login import LoginView
from application.menu import MenuView
from application.user import NewUserView
from application.user import EditUserInfoView
from application.character import NewCharacterView
from application.adventure import NewAdventureView
from application.character import AllCharacterView

from application.user import UserModel
from application.character import CharacterModel
from application.adventure import AdventureModel

from application.user.UserModel import User

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login_form"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):

            if not current_user.is_authenticated():
               return current_app.login_manager.unauthorized()
            user_role = current_app.login_manager.reload_user().get_role()
            if (user_role != role) and (role != "ANY"):
                return current_app.login_manager.unauthorized()      
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


db.create_all()
