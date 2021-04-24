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

# input sample data here
test_journal_1 = Journal(date=datetime.now().date(), time=datetime.now().time(), author_id=1, entry="This is a test "
                                                                                                    "entry.",
                         title="Test Entry", deleted=False)
test_journal_2 = Journal(date=datetime.now().date(), time=datetime.now().time(), author_id=1, entry="This is a test "
                                                                                                    "entry. It should "
                                                                                                    "register as "
                                                                                                    "deleted",
                         title="Test Entry 2 - deleted", deleted=True)
themes = JournalTheme(theme=['Reflection', 'Gratitude', 'Awareness of surroundings'])

# add and commit sample data to db here
db.session.add(themes)
db.session.add(test_journal_1)
db.session.add(test_journal_2)
db.session.commit()
