from application import app
# import mysql.connector as mysql

if __name__ == "__main__":
    app.run(ssl_context="adhoc", debug=True)
