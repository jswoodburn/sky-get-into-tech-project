from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class JournalForm(FlaskForm):
    title = StringField('Title')
    entry = StringField('Journal Entry')
    submit = SubmitField("Post entry")
