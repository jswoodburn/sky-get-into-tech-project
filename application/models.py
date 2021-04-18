from application import db
from datetime import datetime


class User(db.Model):
    user_id = db.Column('user_id', db.Integer, primary_key=True, nullable=False)
    _email = db.Column('email', db.String(100), nullable=False)
    _password = db.Column('password', db.String(50), nullable=False)
    phone_number = db.Column('phone_number', db.String(11))
    _first_name = db.Column('first_name', db.String(50), nullable=False)
    _last_name = db.Column('last_name', db.String(50), nullable=False)

    # Do we not need an __init__ here? Is it okay to add other methods to a class that is using SQL Alchemy?
    # def __init__(self):
    #     self.user_id = db.Column('user_id', db.Integer, primary_key=True, nullable=False)
    #     self._email = db.Column('email', db.String(100), nullable=False)
    #     self._password = db.Column('password', db.String(50), nullable=False)
    #     self.phone_number = db.Column('phone_number', db.String(11))
    #     self._first_name = db.Column('first_name', db.String(50), nullable=False)
    #     self._last_name = db.Column('last_name', db.String(50), nullable=False)


class Journal(db.Model):
    journal_id = db.Column('journal_id', db.Integer, primary_key=True, nullable=False)
    date = db.Column('date_created', db.Date, nullable=False)
    time = db.Column('time_created', db.Time, nullable=False)
    author_id = db.Column('author_id', db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    entry = db.Column('journal_entry', db.String(3000), nullable=False)
    title = db.Column('journal_title', db.String(200), nullable=False)
    archived = db.Column('is_journal_archived', db.Boolean)
