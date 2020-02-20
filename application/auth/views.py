from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.models import Role
from application.auth.models import UserRoles
from application.auth.forms import LoginForm
from application.auth.forms import SignUpForm

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
                                error = "Invalid information")
    
    user = User.query.filter_by(username=form.username.data).first()

    if user:
        return render_template("auth/signupform.html", form = SignUpForm(), 
                                error = user.username + " already taken")

    user = User(form.firstName.data+' '+form.lastName.data)

    user_role = Role.query.filter_by(name='User').first()
    
    user.username = form.username.data
    user.password = form.password.data
    user.roles.append(user_role)
    db.session().add(user)
    db.session().commit()
    return redirect(url_for("auth_login"))