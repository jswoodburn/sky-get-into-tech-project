from application import db
from models import User, Journal
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

# input sample data here
test_journal_1 = Journal(date=datetime.now().date(), time=datetime.now().time(), author_id=1, entry="This is a test "
                                                                                                    "entry.",
                         title="Entry")

# add and commit sample data to db here
db.session.add(test_journal_1)
db.session.commit()