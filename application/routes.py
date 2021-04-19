from flask import render_template, request
from application import app, db
from application.forms.journalform import JournalForm
from application.models import Journal
from datetime import datetime

from login import google_auth


@app.route('/')
def index():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info,
                                                                                                            indent=4) + "</pre>"

    return 'You are not currently logged in.'


@app.route('/home')
def home():
    return render_template('homepage.html', title='Home')


@app.route('/journal', methods=['GET', 'POST'])
def journal():
    error = ""
    form = JournalForm()

    if request.method == 'POST':
        title = form.title.data
        entry = form.entry.data
        author = 1  # ---------------- PLACEHOLDER ----> REPLACE THIS WITH USER ID --------------------------

        if len(title) == 0 or len(entry) == 0:
            error = "Please supply a title and entry"
        else:
            journal_submission = Journal(date=datetime.now().date(), time=datetime.now().time(), author_id=author,
                                         entry=entry, title=title)
            db.session.add(journal_submission)
            db.session.commit()
            return "Thank you"

    return render_template('journal.html', form=form, message=error)

# @app.route('/favourites')
# def favourites():
#     faves = ['books', 'food', 'puppies']
#     return render_template('favourites.html', title='Journal', list=faves)

# @app.route('/mindfulness'):
# def mindful():
#     return render_template(mindful.html, title='Mindfulness')
