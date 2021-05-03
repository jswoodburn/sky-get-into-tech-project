from application import db
from datetime import datetime
from flask_login import LoginManager, UserMixin

login_manager = LoginManager()


class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    google_id = db.Column('google_id', db.String(50), unique=True, nullable=False)
    email = db.Column('email', db.String(100), nullable=False, unique=True)
    first_name = db.Column('first_name', db.String(50), nullable=False)
    last_name = db.Column('last_name', db.String(50), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.first_name


# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    user = db.session.query(User).get(user_id)
    return user


class Journal(db.Model):
    __table_args__ = {'extend_existing': True}
    journal_id = db.Column('journal_id', db.Integer, primary_key=True, nullable=False)
    date_created = db.Column('date_created', db.Date, nullable=False)
    time_created = db.Column('time_created', db.Time, nullable=False)
    author_id = db.Column('author_id', db.Integer, db.ForeignKey(User.id), nullable=False)
    entry = db.Column('journal_entry', db.String(3000), nullable=False)
    title = db.Column('journal_title', db.String(200), nullable=False)
    deleted = db.Column('deleted', db.Boolean, nullable=False, default=False)


class JournalTheme(db.Model):
    __table_args__ = {'extend_existing': True}
    theme_id = db.Column('theme_id', db.Integer, primary_key=True, nullable=False)
    theme = db.Column('theme', db.String(3000), nullable=False)

# create a string to return model
# def __repr__(self):
#     return '<Title %r>' % self.title
