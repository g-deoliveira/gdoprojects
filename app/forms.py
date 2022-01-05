from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UrlForm(FlaskForm):
    url = StringField('url', validators=[DataRequired()])
    submit = SubmitField('Submit')
