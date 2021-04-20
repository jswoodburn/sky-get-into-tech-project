from flask import render_template, request, url_for
from werkzeug.utils import redirect
from application import app, db
from application.forms.journalform import JournalForm
from application.models import User, Journal
from datetime import datetime


@app.route('/')
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
            journal_id = journal_submission.journal_id
            print(journal_id)
            return redirect(url_for('specific_journal_page', user_id=author, journal_id=journal_id))

    return render_template('create_journal_entry.html', form=form, message=error)

@app.route('/journal/<user_id>/<journal_id>')
def specific_journal_page(user_id, journal_id):
    journal = db.session.query(Journal).get(journal_id)
    author = db.session.query(User).get(journal.author_id)
    time = str(journal.time)[:5]
    return render_template('journal_entry.html', title=journal.title, entry=journal.entry, date=journal.date,
                           time=time, author=f"{author.first_name} {author.last_name}")

# @app.route('/journal/<user_id>')
# def user_journal_list(user_id):
#     user_journal_titles = db.select([Journal.title]).where(Journal.author_id == 1).order_by(db.desc(Journal.date)).\
#         order_by(db.desc(Journal.time))
#     return render_template('user_journals_list.html', title="Your Journal Entries", title_list = user_journal_titles)


# journal_1 = db.session.query(Journal).get(1)
# journal_1.date = '2000-02-01'
# author_1_entries = db.session.query(Journal.title).filter_by(author_id=1).order_by(Journal.date).order_by(Journal.time)
# print(author_1_entries[:])
# db.session.add(journal_1)
# db.session.commit()