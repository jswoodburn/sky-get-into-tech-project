from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TextField
from wtforms.validators import DataRequired, length
# from flask_bootstrap import Bootstrap

class JournalForm(FlaskForm):
    title = StringField('Title')
    entry = TextAreaField('Journal Entry (3000 characters)')
    submit = SubmitField("Post entry")


# class JournalForm(FlaskForm):
#     title = StringField('Title')
#     entry = StringField('Journal Entry')
#     submit = SubmitField("Post entry")