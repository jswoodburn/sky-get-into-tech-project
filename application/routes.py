from flask import render_template, request, url_for
from flask_login import current_user
from werkzeug.utils import redirect
from application import app, db
from application.forms.journalform import JournalForm
from application.models import User, Journal
from datetime import datetime

#homepage needs to be edited so it redirects
@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        user_id = current_user.id
        user = db.session.query(User).get(user_id)
        first_name = user.first_name
        return render_template('homepage.html', title='Home', is_logged_in=True, name=first_name)
    else:
        return render_template('homepage.html', title='Home', is_logged_in=False)

@app.route('/login')
def login():
    return render_template('login.html', title='Home')

@app.route('/login/callback')
def login():
    return render_template('login.html', title='Home')


@app.route('/journal', methods=['GET', 'POST'])
def create_journal():
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
                                         entry=entry, title=title, deleted=False)
            db.session.add(journal_submission)
            db.session.commit()
            journal_id = journal_submission.journal_id
            return redirect(url_for('specific_journal_page', user_id=author, journal_id=journal_id))

    return render_template('create_journal_entry.html', form=form, message=error)
    # return render_template('journalv2.html', form=form, message=error)


@app.route('/journal/<user_id>')
# need to add filter_by(deleted==False) or something so that don't get stuff that's been deleted
def user_journal_list(user_id):
    author_entries = db.session.query(Journal.journal_id).filter_by(author_id=1).order_by(Journal.date).order_by(Journal.time)
    titles_and_ids = []
    for id in author_entries:
        journal_id = id[0]
        entry = db.session.query(Journal).get(journal_id)
        url = url_for('specific_journal_page', user_id=user_id, journal_id=journal_id)
        titles_and_ids.append([entry.title, url])
    return render_template('user_journals_list.html', title="Your Journal Entries", title_list=titles_and_ids)


@app.route('/journal/<user_id>/<journal_id>')
def specific_journal_page(user_id, journal_id):
    journal = db.session.query(Journal).get(journal_id)
    author = db.session.query(User).get(journal.author_id)
    time = str(journal.time)[:5]
    if journal.deleted:
        return render_template('deleted_journal_entry.html', title="Entry not found")
    else:
        return render_template('journal_entry.html', title=journal.title, entry=journal.entry, date=journal.date,
                           time=time, author=f"{author.first_name} {author.last_name}")


@app.route('/journal/<user_id>/<journal_id>/edit', methods=["GET", "POST"])
def edit_journal(user_id, journal_id):

    # only people who's user ID matches the user_id should be able to access edit page
    # put in an if loop for this later when have user sessions
    # also add in a delete button that fills out deleted column

    error = ""

    journal_to_edit = db.session.query(Journal).get(journal_id)
    author = db.session.query(User).get(journal_to_edit.author_id)
    form = JournalForm()

    if request.method == "POST":
        title = form.title.data
        entry = form.entry.data

        if len(title) == 0 or len(entry) == 0:
            error = "Please supply a title and entry"
        else:
            journal_to_edit.title = title
            journal_to_edit.entry = entry
            db.session.add(journal_to_edit)
            db.session.commit()
            journal_id = journal_to_edit.journal_id
            author_id = journal_to_edit.author_id
            return redirect(url_for('specific_journal_page', user_id=author_id, journal_id=journal_id))

    form.title.data = journal_to_edit.title
    form.entry.data = journal_to_edit.entry
    return render_template('create_journal_entry.html', form=form, message=error)
    # return render_template('journalv2.html', form=form, message=error)


# ------- FOR REFERENCE - DELETE ON MERGE ------- SQL ALCHEMY QUERIES AND UPDATES -------- #
# journal_1 = db.session.query(Journal).get(1)
# journal_1.date = '2000-02-01'
# author_1_entries = db.session.query(Journal.title).filter_by(author_id=1).order_by(Journal.date).order_by(Journal.time)
# print(author_1_entries[:])
# db.session.add(journal_1)
# db.session.commit()