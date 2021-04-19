from application import app
import json
import os
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

# Google Config
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration")


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


app.config['SECRET_KEY'] = 'skygit'

if __name__ == "__main__":
    app.run(debug=True)

# add Db
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:testpass@localhost/digitalhealth/'

# Initialise db
db = SQLAlchemy(app)
