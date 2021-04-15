from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class JournalForm(FlaskForm):
    title = StringField('Title')
    entry = StringField('Journal Entry')
    submit = SubmitField("Post entry")
