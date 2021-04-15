from flask import render_template

from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html', title='Home')


@app.route('/journal')
def journal():
    return render_template('journal.html', title='Journal')

# @app.route('/mindfulness'):
# def mindful():
#     return render_template(mindful.html, title='Mindfulness')
