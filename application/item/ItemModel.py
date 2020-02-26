from application import db
from sqlalchemy.sql import text

class Item(db.Model):

    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(120), nullable=False)
    item_description = db.Column(db.String(240), nullable=False)

    def __init__(self, name, description):
        self.item_name = name
        self.item_description = description