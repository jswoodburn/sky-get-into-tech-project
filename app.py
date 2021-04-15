from application import app
from flask import Flask
app.config['SECRET_KEY'] = 'Flask.secret_key'
if __name__ == "__main__":
    app.run(debug=True)