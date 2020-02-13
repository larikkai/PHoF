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
db.session.commit()

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
                                error = "invalid username")
    
    user = User.query.filter_by(username=form.username.data).first()

    if user:
        return render_template("auth/signupform.html", form = SignUpForm(), 
                                error = user.username + " already taken")

    u = User(form.firstName.data+' '+form.lastName.data)
    #ADD DEFAULT ROLE
    u.roles = [user_role,]
    #u.roles = [admin_role,]
    
    u.username = form.username.data
    u.password = form.password.data
    db.session().add(u)
    db.session().commit()
    return redirect(url_for("auth_login"))
    