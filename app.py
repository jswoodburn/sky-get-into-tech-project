from application import app
from flask import Flask
app.config['SECRET_KEY'] = 'skygit'
if __name__ == "__main__":
    app.run(debug=True)