from flask import render_template
from application import app

from application.auth.models import User
from application.news.models import New

@app.route('/')
def index():
    return render_template("index.html", news=New.query.all())