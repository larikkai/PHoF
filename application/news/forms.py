from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewsForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=5, max=50)])
    content = StringField("Content", [validators.Length(min=50, max=300)])
 
    class Meta:
        csrf = False