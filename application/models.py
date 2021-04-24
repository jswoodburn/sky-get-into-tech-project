from application import db
from datetime import datetime
from flask_login import LoginManager

login_manager = LoginManager()

class User(db.Model):
    __table_args__ = {'extend_existing': True}
    user_id = db.Column('user_id', db.Integer, primary_key=True, nullable=False)
    email = db.Column('email', db.String(100), nullable=False, unique=True)
    first_name = db.Column('first_name', db.String(50), nullable=False)
    last_name = db.Column('last_name', db.String(50), nullable=False)

    # Flask-Login helper to retrieve a user from our db
    @login_manager.user_loader
    def load_user(user_id):
        user = db.session.query(User).get(user_id)
        return user

# Do we not need an __init__ here? Is it okay to add other methods to a class that is using SQL Alchemy?
    # def __init__(self):
    #     self.user_id = db.Column('user_id', db.Integer, primary_key=True, nullable=False)
    #     self._email = db.Column('email', db.String(100), nullable=False)
    #     self._password = db.Column('password', db.String(50), nullable=False)
    #     self.phone_number = db.Column('phone_number', db.String(11))
    #     self._first_name = db.Column('first_name', db.String(50), nullable=False)
    #     self._last_name = db.Column('last_name', db.String(50), nullable=False)


class Journal(db.Model):
    __table_args__ = {'extend_existing': True}
    journal_id = db.Column('journal_id', db.Integer, primary_key=True, nullable=False)
    date = db.Column('date_created', db.Date, nullable=False, default=datetime.utcnow())
    time = db.Column('time_created', db.Time, nullable=False, default=datetime.utcnow())
    author_id = db.Column('author_id', db.Integer, db.ForeignKey(User.user_id), nullable=False)
    entry = db.Column('journal_entry', db.String(3000), nullable=False)
    title = db.Column('journal_title', db.String(200), nullable=False)
    deleted = db.Column('deleted', db.Boolean, nullable=False)


class JournalTheme(db.Model):
    __table_args__ = {'extend_existing': True}
    theme_id = db.Column('theme_id', db.Integer, primary_key=True, nullable=False)
    theme = db.Column('theme', db.String(3000), nullable=False)


#create a string to return model
    # def __repr__(self):
    #     return '<Title %r>' % self.title
