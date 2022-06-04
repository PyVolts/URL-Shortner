# TODO create form to gather new shorten; toggle custom;
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from shorten.models import urls


class shortURL(FlaskForm):
    original_url = StringField('Original URL', validators=[DataRequired()])
    custom_url = StringField('Custom Short URL')
    submit = SubmitField('Submit')

        
