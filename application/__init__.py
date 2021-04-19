from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from application import routes

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost/digitalhealth/"

#Linking app to the persistance layer
db = SQLAlchemy(app)

