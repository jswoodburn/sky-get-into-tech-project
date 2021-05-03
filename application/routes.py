from flask import render_template, request, url_for, make_response
from flask_login import current_user
from google.auth.transport import requests
from application.__init__ import get_google_provider_cfg, client, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, login_manager
import json
from datetime import datetime

import requests
from flask import render_template, request, url_for
from flask_login import current_user, login_required, logout_user, login_user, login_manager, user_logged_in
# from google.auth.transport import requests
import requests
from sqlalchemy import exists, desc
from sqlalchemy.sql.expression import func, select
from werkzeug.utils import redirect

from application import app, db
from application.__init__ import get_google_provider_cfg, client, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
from application.forms.journalform import JournalForm
from application.forms.deletejournalform import DeleteJournalForm
from application.models import User, Journal, JournalTheme
from datetime import datetime
import tweepy
from feedgen.feed import FeedGenerator
import feedparser

from application.exceptions.PageNotFound import PageNotFoundError
from application.exceptions.RequiresLogin import PageRequiresLoginError
from application.exceptions.PageDeletedError import PageDeletedError
from application.exceptions.UserPermissionsDenied import PermissionsDeniedError

@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        first_name = db.session.query(User).get(id)
        return render_template('homepage.html', title='Home', is_logged_in=True,
                               first_name=f"{current_user.first_name}")

    else:
        return render_template('homepage.html', title='Home', is_logged_in=False)


@app.route('/login')
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/callback", methods=["POST", "GET"])
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens. let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        google_uid = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # print(db.session.query(User.id).filter_by(google_id=google_uid))
    user = User(
        google_id=google_uid, first_name=users_name, email=users_email
    )

    # If user does not exist in db, create and add them to it
    # if not db.session.query(User.id).filter_by(google_id=google_uid):
    if not db.session.query(exists().where(User.google_id == google_uid)).scalar():
        db.session.add(user)
        db.session.commit()
    else:
        user = db.session.query(User).filter_by(google_id=google_uid).first()

    # Begin user session by logging the user in

    login_user(user)

    # Send user back to homepage
    return redirect(url_for("home"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/mindfulness')
def mindfulness():
    if current_user.is_authenticated:
        return render_template('mindfulness.html', title='Mindfulness', is_logged_in=True,
                               first_name=f"{current_user.first_name}")
    else:
        return render_template('mindfulness.html', title='Mindfulness', is_logged_in=False)


rss_url = 'https://www.goodnewsnetwork.org/category/news/feed/'


@app.route('/impactfulmedia')
def impactful_media():
    auth = tweepy.OAuthHandler("VXNAakrOK2uorxArIJGWWLYlC", "ND4xneY9OboE4kQJe2IhhUwZdHb1qh366HiWVcGkCAAs9UghLv")
    auth.set_access_token("1355474665972621316-dWfZkdGO6xLSpSDIn2khGc4V2l5j0Y",
                          "sSnf7RrNQDVY2SBE5H5sO4qN0LJ7wscwGdmF6SizpG2XW")
    api = tweepy.API(auth)

    search = request.args.get('q')

    public_tweets = api.user_timeline(search)
    # Define the search term and the date_since date as variables
    search_words = "#positivity"
    date_since = "2021-03-03"
    tweets = tweepy.Cursor(api.search,
                           q=search_words,
                           lang="en",
                           since=date_since).items(5)

    tweets = tweepy.Cursor(api.search,
                           q=search_words,
                           lang="en",
                           since=date_since).items(20)

    feed = feedparser.parse("https://www.goodnewsnetwork.org/category/news/feed/")
    entry = feed.entries
    # title = entry.title
    # published = entry.published
    # summary = entry.summary
    # link = entry.link
    # image = entry.media_content[0]['url']

    if current_user.is_authenticated:
        return render_template('impactfulmedia.html', title='Mindfulness', is_logged_in=True, feed=feed,
                               first_name=f"{current_user.first_name}", tweets=tweets,
                               entry=entry)
    else:
        return render_template('impactfulmedia.html', title='Mindfulness', is_logged_in=False, feed=feed,
                               entry=entry, tweets=tweets)


@app.route('/journal', methods=['GET', 'POST'])
def create_journal():
    error = ""
    form = JournalForm()
    if request.method == 'POST':
        title = form.title.data
        entry = form.entry.data
        author_id = current_user.id
        author = current_user.first_name

        if len(title) == 0 or len(entry) == 0:
            error = "Please supply a title and entry."
        else:
            journal_submission = Journal(date_created=datetime.now().date(), time_created=datetime.now().time(),
                                         author_id=author_id, entry=entry, title=title)
            db.session.add(journal_submission)
            db.session.commit()
            journal_id = journal_submission.journal_id
            return redirect(url_for('specific_journal_page', journal_id=journal_id, user_id=author_id))
    if current_user.is_authenticated:
        randomtheme = db.session.query(JournalTheme.theme).order_by(func.rand()).first()
        return render_template('create_journal_entry.html', form=form, message=error, is_logged_in=True,
                               randomtheme=randomtheme[0], is_edit=False, delete_form="")
    else:
        raise PageRequiresLoginError("User tried to access journal creation page without logging in.")


@app.route('/journal/<user_id>')
def user_journal_list(user_id):
    author_entries = db.session.query(Journal.journal_id).filter_by(author_id=user_id).filter_by(
        deleted=False).order_by(desc(Journal.date_created)).order_by(desc(Journal.time_created))
    author = db.session.query(User).get(user_id)
    author_name = author.first_name
    journal_data = []
    for journal_entry in author_entries:
        journal_id = journal_entry[0]
        entry = db.session.query(Journal).get(journal_id)
        url = url_for('specific_journal_page', user_id=user_id, journal_id=journal_id)
        if len(entry.entry) > 50:
            shortened_entry = entry.entry[:50] + "..."
        else:
            shortened_entry = entry.entry
        journal_data.append([entry.title, url, entry.date_created, shortened_entry])
    return render_template('user_journals_list.html', title=f"{author_name}'s Journals", title_list=journal_data,
                           is_logged_in=True)


@app.route('/journal/<user_id>-<journal_id>')
def specific_journal_page(user_id, journal_id):
    journal_entry = db.session.query(Journal).get(journal_id)
    user = db.session.query(User).get(user_id)
    if not journal_entry:
        raise PageNotFoundError(f"The user has tried to access journal ID {journal_id} which does not exist in the "
                                f"database.")
    elif int(journal_entry.author_id) != int(user_id):
        raise PageNotFoundError(f"The journal ID {journal_id} does not exist for the user ID {user_id}.")
    elif journal_entry.deleted:
        raise PageDeletedError(f"The journal ID {journal_id} was soft-deleted by the user and cannot be accessed by "
                               f"the public.")
    else:
        time = str(journal_entry.time_created)[:5]
        can_edit = False
        if current_user.is_authenticated:
            if int(current_user.id) == int(user_id):
                can_edit = True
        return render_template('journal_entry.html', title=journal_entry.title, entry=journal_entry.entry,
                               date=journal_entry.date_created, time=time, author=f"{user.first_name}",
                               index_url=f"/journal/{user_id}", is_logged_in=True, can_edit=can_edit,
                               edit_url=f"/journal/{user_id}-{journal_id}-edit")


@app.route('/journal/<user_id>-<journal_id>-edit', methods=["GET", "POST"])
def edit_journal(user_id, journal_id):

    error = ""

    journal_to_edit = db.session.query(Journal).get(journal_id)
    author = db.session.query(User).get(journal_to_edit.author_id)
    journal_form = JournalForm()
    delete_form = DeleteJournalForm()

    if request.method == "POST":
        title = journal_form.title.data
        entry = journal_form.entry.data

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
    if not journal_to_edit:
        raise PageNotFoundError(f"The user has tried to access journal ID {journal_id} which does not exist in the "
                                f"database.")
    elif int(journal_to_edit.author_id) != int(user_id):
        raise PageNotFoundError(f"The journal ID {journal_id} does not exist for the user ID {user_id}.")
    elif journal_to_edit.deleted:
        raise PageDeletedError(f"The journal ID {journal_id} was soft-deleted by the user and cannot be accessed by "
                               f"the public.")
    elif current_user.is_authenticated:
        if int(user_id) != int(current_user.id):
            raise PermissionsDeniedError(f"User with ID {current_user.id} tried to access edit page for entry "
                                         f"{journal_id} by user with ID {user_id}")
        else:
            journal_form.title.data = journal_to_edit.title
            journal_form.entry.data = journal_to_edit.entry
            return render_template('create_journal_entry.html', form=journal_form, message=error, is_logged_in=True,
                                   randomtheme="", is_edit=True, delete_form=delete_form,
                                   journal_id=journal_to_edit.journal_id, user_id=journal_to_edit.author_id)
    else:
        raise PageRequiresLoginError("User tried to access journal edit page without logging in.")


@app.route('/journal/<user_id>-<journal_id>-delete', methods=["POST"])
def delete_journal(user_id, journal_id):
    if current_user.is_authenticated:
        if int(user_id) != int(current_user.id):
            raise PermissionsDeniedError(f"User with ID {current_user.id} tried to delete entry "
                                         f"{journal_id} by user with ID {user_id}.")
        else:
            journal_to_delete = db.session.query(Journal).get(journal_id)
            journal_to_delete.deleted = True
            db.session.add(journal_to_delete)
            db.session.commit()
            return redirect(url_for('user_journal_list', user_id=user_id))
    else:
        raise PageRequiresLoginError("User tried to access journal deletion without logging in.")



@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if current_user.is_authenticated:
        journals_written = db.session.query(Journal).filter_by(author_id=current_user.id)
        words = 0
        for journal_entry in journals_written:
            entry_word_string = journal_entry.entry
            words += len(entry_word_string.split())
        return render_template('profile.html', first_name=f"{current_user.first_name}", is_logged_in=True,
                               words_journaled=words, journal_index_url=url_for("user_journal_list",
                                                                                user_id=current_user.id))
    else:
        raise PageRequiresLoginError("Anonymous user tried to access profile page.")



@app.route('/aboutus')
def aboutus():
    if current_user.is_authenticated:
        first_name = db.session.query(User).get(id)
        return render_template('aboutus.html', title='About Us', is_logged_in=True,
                               first_name=f"{current_user.first_name}")

    else:
        return render_template('aboutus.html', title='About Us', is_logged_in=False)


@app.route('/search/<search_input>')
def search_results(search_input):
        search_with_spaces = " ".join(search_input.split("-"))
        search_sql = f"%{search_with_spaces}%"
        posts = db.session.query(Journal).filter(Journal.title.like(search_sql)).filter_by(
            deleted=False).order_by(desc(Journal.date_created)).order_by(desc(Journal.time_created))

        search_result_list = []
        for post in posts:
            url = url_for('specific_journal_page', user_id=post.author_id, journal_id=post.journal_id)
            if len(post.entry) > 50:
                shortened_entry = post.entry[:50] + "..."
            else:
                shortened_entry = post.entry
            author = db.session.query(User).get(post.author_id)
            author_index_page = url_for('user_journal_list', user_id=post.author_id)
            search_result_list.append({"title": post.title,
                                   "journal_url": url,
                                   "date": post.date_created,
                                   "preview": shortened_entry,
                                   "name": author.first_name,
                                   "author_url": author_index_page})
        no_results = False
        if len(search_result_list) == 0:
            no_results = True
        if current_user.is_authenticated:
            return render_template('search_results.html', search_input=search_with_spaces,
                                   search_results=search_result_list, is_logged_in=True, no_results=no_results)
        else:
            return render_template('search_results.html', search_input=search_with_spaces,
                                   search_results=search_result_list, is_logged_in=False, no_results=no_results)


@app.errorhandler(404)
@app.errorhandler(PageNotFoundError)
def page_does_not_exist(err):
    app.logger.exception(err)
    return render_template('generic_exception_page.html', message="The page you are looking for does not exist.",
                           sub_message="Please check the URL and try again.", is_logged_in=False)



@app.errorhandler(401)  # unauthorised error - generated by @login_required
@app.errorhandler(PageRequiresLoginError)
def page_requires_login(err):
    app.logger.exception(err)
    return render_template('generic_exception_page.html', message="You must log in to access this page.",
                           sub_message="", is_logged_in=False)



@app.errorhandler(PageDeletedError)
def page_deleted(err):
    app.logger.exception(err)
    return render_template('generic_exception_page.html', message="Sorry, this journal entry has been deleted.",
                           sub_message="", is_logged_in=False)



@app.errorhandler(PermissionsDeniedError)
def page_deleted(err):
    app.logger.exception(err)
    return render_template('generic_exception_page.html', message="You do not have permission to access this page.",
    sub_message="You must be logged in as the owner of this page to access it.", is_logged_in=False)


@app.errorhandler(500) # server error
@app.errorhandler(Exception) # catch all for any other errors
def something_wrong(err):
    app.logger.exception(err)
    return render_template('generic_exception_page.html', message="Oops, something has gone wrong.",
                           sub_message="Please try refreshing the page or come back later. Our engineers are hard at work to fix the "
                                       "problem.", is_logged_in=False)
