from flask import Flask

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from os import getenv
from application import routes

username = 'newuser'
password = 'password'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server = '127.0.0.1'
dbname = '/db'

# put them all together as a string that shows SQLAlchemy where the database is
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://newuser:password@localhost/db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = getenv('FLASK_SECRETKEY')

# Linking app to the persistence layer
db = SQLAlchemy(app)

# uncomment and run below code to check connection
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
