from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from application import app
import os



# from authlib.client import OAuth2Session
# import google.oauth2.credentials
# import googleapiclient.discovery

# from application.login import google_auth

app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)

# app.register_blueprint(google_auth.app)


app.config['SECRET_KEY'] = 'skygit'


if __name__ == "__main__":
    app.run(debug=True)

db = SQLAlchemy(app)
