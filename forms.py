from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField, FileField


class AddFileForm(FlaskForm):
    file_field = FileField(label='Select file:')
    submit = SubmitField(label='Process file')
