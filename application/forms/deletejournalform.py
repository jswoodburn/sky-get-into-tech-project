from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField


class DeleteJournalForm(FlaskForm):
    submit = SubmitField("Delete")
