from flask_wtf import FlaskForm
from wtforms import StringField

class UserForm(FlaskForm):
    name = StringField("Username")
    password = StringField("Password")
 
    class Meta:
        csrf = False
