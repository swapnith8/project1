
import os


from flask import Flask, session,request,render_template,redirect
from flask_session import Session
from sqlalchemy import create_engine,desc
from sqlalchemy.orm import scoped_session, sessionmaker
import logging
logging.basicConfig(level=logging.DEBUG)

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

@app.route('/admin')
def admin():
    allusersdata = userschema.query.order_by(desc(userschema.time_stamp)).all()
    return render_template("adminer.html",admin = allusersdata)

@app.route('/auth', methods=['POST'])
def login():
    user_data = userschema.query.filter_by(username = request.form['username']).first()
    if user_data is not None:
        if request.form['pwd'] == user_data.pwd:
            return redirect('/home')
        else:
            var1 = "wrong Credentials"
            return render_template('Registration.html', message = var1)
    else:
        var1 = "Error: You are not a registered. Please first register to login"
        return render_template("Registration.html", message = var1)

@app.route('/home')
def homePage():
        return render_template("login.html")
    


@app.route('/logout')
def logout():
        var1= "Logged-Out"
        return render_template("Registration.html",message=var1)
    
