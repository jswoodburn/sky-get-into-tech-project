from flask import render_template, request
from application import app
from application.forms.journalform import JournalForm


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

        if len(title) == 0 or len(entry) == 0:
            error = "Please supply a title and entry"
        else:
            #take user to personal journal page with all their published journal sorted by date posted
            return "Thank you"

    return render_template('journal.html', form=form, message=error)


@app.route('/favourites')
def favourites():
    faves = ['books', 'food', 'puppies']
    return render_template('favourites.html', title='Journal', list=faves)

# @app.route('/mindfulness'):
# def mindful():
#     return render_template(mindful.html, title='Mindfulness')
