from application import app
import json
import os
# Third-party libraries
from flask import Flask, redirect, request, url_for
import functools
import json
import os

import flask

# from authlib.client import OAuth2Session
# import google.oauth2.credentials
# import googleapiclient.discovery

# from application.login import google_auth

app = flask.Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)

# app.register_blueprint(google_auth.app)


@app.route('/')
def index():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info,
                                                                                                            indent=4) + "</pre>"

    return 'You are not currently logged in.'


app.config['SECRET_KEY'] = 'skygit'
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

db = SQLAlchemy(app)
