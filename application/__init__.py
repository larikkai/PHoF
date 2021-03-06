from flask import Flask
from flask_bcrypt import Bcrypt
from flask_bcrypt import generate_password_hash

app = Flask(__name__)
bcrypt = Bcrypt(app)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///games.db"
    app.config["SQLALCHEMY_ECHO"] = True

  
db = SQLAlchemy(app)

# login functionality
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# roles in login_required
from functools import wraps
def adminlogin_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            if role not in current_user.get_roles(current_user.id):
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

# load application content
from application import views

from application.games import models
from application.games import views

from application.auth import models
from application.auth import views

from application.tournaments import models
from application.tournaments import views

from application.admin import views

from application.accounts import views

from application.news import models
from application.news import views

# login functionality2
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


try: 
    db.create_all()

    """#Create default roles
    from application.auth.models import Role

    admin_role = Role(name='Admin')
    user_role = Role(name='User')
    db.session().add(admin_role)
    db.session().add(user_role)
    db.session().commit()

    user_role = Role.query.filter_by(name='User').first()
    admin_role = Role.query.filter_by(name='Admin').first()

    if os.environ.get("HEROKU"):
        #Create default users
        user1 = User('User user')
        user1.username = 'test_user1'
        pw_hash = bcrypt.generate_password_hash('test123').decode('utf-8')
        user1.password = pw_hash
        user1.roles.append(user_role)
        db.session().add(user1)

        user2 = User('Admin user')
        user2.username = 'admin'
        pw_hash = bcrypt.generate_password_hash('test123').decode('utf-8')
        user2.password = pw_hash
        user2.roles.append(admin_role)
        db.session().add(user2)
        db.session().commit()"""
except:
    pass