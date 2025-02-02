from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from at.programs import *
app = Flask(__name__)
app.config["SECRET_KEY"]="pdsdjfxkcnvmxbvieihpaskklcm,mvvkjdnvc"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)
migrate = Migrate(app,db)
app.app_context().push()
class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(200),nullable = False,unique = True,index = True)
    password = db.Column(db.String(300),nullable = False)
    full_name = db.Column(db.String(500),nullable = True)
    email = db.Column(db.String(200),nullable = True,unique = True,index = True)
    roll_num = db.Column(db.Integer,nullable = True)
    status = db.Column(db.String(100),nullable = False, default = "pending")
    role = db.Column(db.String(200),nullable = False)
@app.route("/")
def index():

    return render_template("index.html")
@app.route("/registration",methods = ["GET","POST"]) #'name', 'Umma Iman Monea'), ('email', 'iman241-15-540@diu.edu.bd'), ('password', 'muniamunia'), ('role', 'student')
def registration():
    if request.method == "POST":
        data = request.form
        full_name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')
        username = usrname_generator(full_name)
        newUser = User(
            username = username,
            full_name = full_name,
            password = password,
            email = email,
            role = role,
        )
        try:
            db.session.add(newUser)
            db.session.commit()
            flash("registration successful","success") 
        except Exception as error:
            print(error)
            flash("registration unsuccessful due to error","error") 
        return redirect(url_for('registration'))
    return render_template("registration.html")
@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        userData = User.query.filter_by(email = email).first()
        if password == userData.password:
            flash("login successful","success") 
        flash("login unsuccessful","error") 
        return redirect(url_for('login'))
    return render_template("login.html")
# @app.route("/logout")
# def logout():
    
#         return redirect(url_for('logout'))
#     return render_template("logout.html")

if __name__=="__main__":
    app.run(debug=True,port=8989,host="localhost")
