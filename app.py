from flask_sqlalchemy import SQLAlchemy
from application import app, google_auth
#login dependencies
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

# Internal imports (needs to change to reflect our structure)
from db import init_db_command
from user import User

app.secret_key = 'secretkeygoogle'

app.register_blueprint(google_auth.app)

if __name__ == "__main__":
    app.run(debug=True)

db = SQLAlchemy(app)
