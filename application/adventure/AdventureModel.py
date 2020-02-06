from application import db

class Adventure(db.Model):

    __tablename__ = "adventure"
    
    id = db.Column(db.Integer, primary_key=True)
    adventure_name = db.Column(db.String(120), nullable=False)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    dungeon_master = db.Column(db.Integer, db.ForeignKey('accounts.id'),nullable=False)
    

    def __init__(self, name, dm):
        self.adventure_name = name
        self.dungeon_master = dm