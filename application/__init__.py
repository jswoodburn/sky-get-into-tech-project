# Python standard libraries
import json
import os
import sqlite3

# Third party libraries
from flask import Flask, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests

# instantiate Flask object (app)

app = Flask(__name__)
# app.secret_key = 'skyGIT'
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

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

# ----------- GOOGLE AUTH ---------------

GOOGLE_CLIENT_ID = "1078137073918-2ur6jb9jsihmd95uohhp2hq6qkegnmoa.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "yEGN03m9WSjLAGkK2azEvqof"
GOOGLE_DISCOVERY_URL = "http://127.0.0.1:5000/login/auth"

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

from application.models import User


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()
