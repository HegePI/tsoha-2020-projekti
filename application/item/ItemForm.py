from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class ItemForm(FlaskForm):
    
    item_name = StringField("Esineen nimi")
    item_description = TextAreaField("Esineen kuvaus")
 
    class Meta:
        csrf = False