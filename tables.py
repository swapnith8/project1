from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class userschema(db.Model):
    __tablename__="userschema"
    username = db.Column(db.String,primary_key=True)
    email = db.Column(db.String, primary_key=True)
    city = db.Column(db.String, nullable=False)
    pwd = db.Column(db.String, nullable=False)
    creationtimestamp = db.Column(db.DateTime(timezone=True),nullable=False)

    def __init__(self,username,email,city,pwd):
        self.username=username
        self.email=email
        self.city=city
        self.pwd=pwd
        self.creationtimestamp=datetime.now()
