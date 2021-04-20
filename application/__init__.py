from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv

app = Flask(__name__)

# make sure the username, password and database name are correct
username = 'newuser'
password = 'password'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
# keep this as is for a hosted website
server = '127.0.0.1'
# change to YOUR database name, with a slash added as shown
dbname  = '/db'
# no socket


# change NOTHING below

# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://newuser:password@localhost/db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = getenv('FLASK_SECRETKEY')

# Linking app to the persistance layer

db = SQLAlchemy(app)

# @app.route('/')
# def testdb():
#     try:
#         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # see Terminal for description of the error
#         print("\nThe error:\n" + str(e) + "\n")
#         return '<h1>Something is broken.</h1>'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

