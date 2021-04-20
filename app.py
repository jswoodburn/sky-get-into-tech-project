from flask_sqlalchemy import SQLAlchemy
from application import app, google_auth
import os
import functools
import json
import os

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

app.secret_key = 'secretkeygoogle'

app.register_blueprint(google_auth.app)

if __name__ == "__main__":
    app.run(debug=True)

db = SQLAlchemy(app)
