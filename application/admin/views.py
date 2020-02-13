from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db, adminlogin_required
from application.auth.models import User
from application.auth.models import Role
from application.auth.models import UserRoles

@app.route("/admin/", methods = ["GET"])
@login_required
@adminlogin_required(role='Admin')
def admin_index():
    return render_template("admin.html", users = User.query.all())
