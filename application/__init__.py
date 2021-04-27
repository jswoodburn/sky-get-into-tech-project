from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from application import routes

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost/flask_test"

#Linking app to the persistance layer
db = SQLAlchemy(app)

# Python standard libraries
import json
import os


# Third party libraries
from flask import Flask, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
username = 'newuser'
password = 'password'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server = '127.0.0.1'
dbname = '/db'

# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://newuser:password@localhost/db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False