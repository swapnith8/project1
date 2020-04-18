from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class userschema(db.Model):
    __tablename__="userschema"
    username = db.Column(db.String,primary_key=True)
    email = db.Column(db.String, primary_key=True)
    city = db.Column(db.String, nullable=False)
    pwd = db.Column(db.String, nullable=False)

    def __init__(self,username,email,city,pwd):
        self.username=username
        self.email=email
        self.city=city
        self.pwd=pwd