from flask_wtf import  FlaskForm
from wtforms.fields.simple import SubmitField, FileField


class AddFileForm(FlaskForm):

    file = FileField(label='Upload image')
    submit = SubmitField(label='Process image')