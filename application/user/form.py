from flask_wtf import FlaskForm
from wtforms import StringField

class UserForm(FlaskForm):
    username = StringField("Username")
    password = StringField("Password")
 
    class Meta:
        csrf = False
