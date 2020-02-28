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

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "main_menu"
login_manager.login_message = "Please login to use this functionality."

from functools import wraps

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):

            if not (current_user and current_user.is_authenticated):
               return login_manager.unauthorized()

            # acceptable_roles = set(("ANY", *current_user.get_role()))
            users_role = current_user.get_role()

            if users_role != role and role != "ANY":
                return login_manager.unauthorized()
            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

from application import views
 
from application.user import NewUserView, EditUserInfoView, LoginView
from application.character import NewCharacterView, AllCharacterView, AddItemView
from application.adventure import NewAdventureView, AdventureListView, MenuView
from application.item import NewItemView, AllItemsView, EditItemView, DeleteItemView

from application.user import UserModel
from application.character import CharacterModel
from application.character import characterItemModel
from application.adventure import AdventureModel
from application.item import ItemModel

from application.user.UserModel import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db.create_all()
