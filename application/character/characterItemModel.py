from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class characterItem(db.Model):

    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    character = relationship("Character", back_populates="items")
    item = relationship("Item", back_populates="characters")