from application import db
from sqlalchemy.orm import relationship

class User(db.Model):

    __tablename__ = "accounts"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    character = relationship("Character", cascade="all, delete", backref="User")
    adventure = relationship("Adventure", cascade="all, delete", backref="User")

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def get_role(self):
        return self.role