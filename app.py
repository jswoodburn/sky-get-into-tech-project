from application import app
from flask import Flask

app.config['SECRET_KEY'] = 'skygit'
if __name__ == "__main__":
    app.run(debug=True)

#add Db
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:testpass@localhost/digitalhealth’

#Initialise db
db = SQLAlchemy(app)

