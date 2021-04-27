from application import db
from models import User, Journal, JournalTheme
from datetime import datetime

# EVERYONE RUN THIS TO GET DBS SYNCED UP
db.drop_all()
db.create_all()

# input sample data here

test_user_1 = User(email='jackie.woodburn@gmail.com',
                   first_name='Jackie', last_name='Woodburn')

# add and commit sample data to db here
db.session.add(test_user_1)
db.session.commit()
# [19:18]
# email=akdhsfkashdf number= ajsdflkajsfd
# [19:22]
# instantiate Flask object (app)
app = Flask(name)
app.secret_key = 'skyGIT'