from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db, adminlogin_required
from application.news.forms import NewsForm
from application.auth.models import User
from application.news.models import New

@app.route("/news/", methods=["GET"])
def news_index():
    return render_template("news/list.html", news = New.query.all())

@app.route("/news/new/")
@login_required
@adminlogin_required(role='Admin')
def news_form():
    return render_template("news/new.html", form = NewsForm())

@app.route("/news/", methods=["POST"])
@login_required
@adminlogin_required(role='Admin')
def news_create():

    form = NewsForm(request.form)

    print(form.title.data)
    print(form.content.data)
  
    if not form.validate():
        print('FAIL TO POST NEWS')
        return render_template("news/new.html", form = form)
    
    user = User.query.get(current_user.id)

    new = New(form.title.data)
    new.content = form.content.data
    new.account_id = current_user.id
    new.author = user.name
  
    db.session().add(new)
    db.session().commit()
  
    return redirect(url_for("news_index"))

@app.route("/news/<new_id>/", methods=["GET", "POST"])
@login_required
@adminlogin_required(role='Admin')
def news_view_new(new_id):

    form = NewsForm()

    new = New.query.get(new_id)

    if new and request.method == "GET":
        return render_template("news/new.html", form = NewsForm(), new=new)

    form = NewsForm(request.form)
  
    if not form.validate():
        return render_template("news/<new_id>", form = form)

    new = New.query.get(new_id)
    new.title = form.title.data
    new.content = form.content.data

    db.session().commit()

    return render_template("news/list.html", new=New.querty.all())