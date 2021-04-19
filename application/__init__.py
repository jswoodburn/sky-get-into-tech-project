from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from application import routes


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost/digital_health"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://127.0.0.1:3306/?user=root"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


# Linking app to the persistence layer
db = SQLAlchemy(app)


