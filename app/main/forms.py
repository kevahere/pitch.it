from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField
from ..models import Pitch
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    title = StringField('Pitch Category Title', validators=[DataRequired()])
    body = TextAreaField('Enter your Pitch here', validators=[DataRequired()])
    submit = SubmitField('Submit')
