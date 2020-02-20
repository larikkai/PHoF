from application import db
from application.models import Base

from sqlalchemy.sql import text

class New(Base):
    title = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(300), nullable=False)
    author = db.Column(db.String(144), nullable=False)
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, title):
        self.title = title
