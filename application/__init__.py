from flask import Flask
from models import User
from flask_sqlalchemy import SQLAlchemy
from os import getenv
# Python standard libraries
import json
import os
import sqlite3

# Third-party libraries
from flask import Flask, redirect, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests

# Internal imports
from db import init_db_command
from user import User

# instantiate Flask object (app)
app = Flask(__name__)
app.secret_key = 'skyGIT'

# make sure the username, password and database name are correct

username = 'newuser'
password = 'password'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server = '127.0.0.1'
dbname = '/db'

# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://newuser:password@localhost/db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = getenv('FLASK_SECRETKEY')

# Linking app to the persistence layer
db = SQLAlchemy(app)

from application import routes

app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)


# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    user = db.session.query(User).get(user_id)
    return user


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()
