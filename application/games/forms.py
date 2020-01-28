from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class GameForm(FlaskForm):
    name = StringField("Game name", [validators.Length(min=2)])
    done = BooleanField("Done")
 
    class Meta:
        csrf = False