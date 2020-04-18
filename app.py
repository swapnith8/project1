
import os


from flask import Flask, session,request,render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from tables import *

app = Flask(__name__)
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)
# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
Session = scoped_session(sessionmaker(bind=engine))
session = Session()

# db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
    return render_template("Registration.html")
@app.route("/register",methods=["POST","GET"])
def cont():
    db.create_all()
    if request.method=="GET":
        return ("Registration.html")
    else:
        userdata=userschema(request.form["username"],request.form["email"],request.form["city"],request.form["pwd"])
        u=userschema.query.filter_by(username=request.form['username']).first()
        if u is not None:
            variable="Username Already in Exists"
            return render_template("Registration.html",message=variable)
        else:
            db.session.add(userdata)
            db.session.commit()
            variable1="Registered successfully!!"
            return render_template("Registration.html",message1=variable1)
        # return render_template("Details.html",username=username,Email=Email,city=city)
       
