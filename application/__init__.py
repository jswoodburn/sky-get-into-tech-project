from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

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


