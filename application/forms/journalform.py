from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# from flask_wtf import FlaskForm, form
# from wtforms import StringField, SubmitField, TextAreaField, TextField
# from wtforms.validators import DataRequired, length
# from flask_bootstrap import Bootstrap



# class JournalForm(FlaskForm):
#     title = StringField('Title')
#     entry = TextAreaField(('Journal Entry (2047 characters)'), validators=[Required(),Length(max=2047)] )
#     submit = SubmitField("Post entry")

class JournalForm(FlaskForm):
    title = StringField('Title')
    entry = StringField('Journal Entry')
    submit = SubmitField("Post entry")



# original
# class JournalForm(FlaskForm):
#     title = StringField('Title')
#     entry = StringField('Journal Entry')
#     submit = SubmitField("Post entry")
