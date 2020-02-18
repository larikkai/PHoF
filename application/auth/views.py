from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.models import Role
from application.auth.models import UserRoles
from application.auth.forms import LoginForm
from application.auth.forms import SignUpForm

admin_role = Role(name='Admin')
user_role = Role(name='User')

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 

@app.route("/auth/signup", methods = ["GET", "POST"])
def auth_signup():
    if request.method == "GET":
        return render_template("auth/signupform.html", form = SignUpForm())

    form = SignUpForm(request.form)

    if not form.validate():
        return render_template("auth/signupform.html", form = SignUpForm(), 
                                error = "name+lastname min 6, max 25 char + unique, password lenght min 4, max 15")
    
    user = User.query.filter_by(username=form.username.data).first()

    if user:
        return render_template("auth/signupform.html", form = SignUpForm(), 
                                error = user.username + " already taken")

    user = User(form.firstName.data+' '+form.lastName.data)
    #ADD DEFAULT ROLE
    user.roles = [user_role,]
    #user.roles = [admin_role,]
    
    user.username = form.username.data
    user.password = form.password.data
    db.session().add(user)
    db.session().commit()
    return redirect(url_for("auth_login"))
    