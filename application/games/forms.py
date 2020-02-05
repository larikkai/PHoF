from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators, ValidationError

class GameForm(FlaskForm):
    def customValidation(self,field):
        if (field.data)%2 != 0:
            raise ValidationError('Number must be even')

    name = StringField("Game name", [validators.Length(min=5)])
    playerCount = IntegerField("Player count", [validators.NumberRange(min=2, max=8), customValidation])
    done = BooleanField("Done")
 
    class Meta:
        csrf = False