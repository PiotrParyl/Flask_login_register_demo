
from . import db
from flask import Blueprint, render_template,request,flash,redirect, url_for
#from flask_login import login_user, login_required, logout_user, current_user
from .models import User

auth = Blueprint('auth', __name__)

mycursor = db.cursor()


@auth.route('/login',  methods= ['GET','POST'] )
def login():
    return render_template("login.html")


@auth.route('/register',  methods= ['GET','POST'] )
def register():

    if request.method == 'POST':
        email = request.form.get('useremail')
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')


        new_user = User(email=email,username=username,password=password)

        
        mycursor.execute (f"INSERT INTO Users (email,username,password) VALUES ('{new_user.email}','{new_user.username}','{new_user.password}')")
        db.commit()
        flash ("Dodano")
    

        return render_template("login.html")
    else:
        return render_template("signin.html")
