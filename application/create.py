from application import db
from models import User, Journal, JournalTheme
from sqlalchemy.sql import exists
from  sqlalchemy.sql.expression import func, select
from datetime import datetime

# EVERYONE RUN THIS TO GET DBS SYNCED UP
db.drop_all()
db.create_all()

# input sample data here

test_user_1 = User(google_id='101399590782175635333', email='random@gmail.com',
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
# theme1 = JournalTheme(theme='What things make me feel alive and fulfilled?')
# theme2 = JournalTheme(theme='What things in my life can I be grateful for today?')
# db.session.add(theme1, theme2)
# theme3 = JournalTheme(theme='What things in my life can I be grateful for today?')
# theme4 = JournalTheme(theme='Inner Strength')
# db.session.add(theme3, theme4)
# theme5 = JournalTheme(theme='Self Care')
# theme6 = JournalTheme(theme='Checking in with yourself')
# db.session.add(theme5, theme6)
# theme7 = JournalTheme(theme='What might challenge me today?')
# theme8 = JournalTheme(theme='What are my most important values?')
# db.session.add(theme7, theme8)
# theme9 = JournalTheme(theme='How am I impacting other people around me daily?')
# theme10 = JournalTheme(theme='Connection')
# db.session.add(theme9, theme10)


themes = {JournalTheme(theme='What things make me feel alive and fulfilled?'),
          JournalTheme(theme='What things in my life can I be grateful for today?'),
          JournalTheme(theme='Inner Strength'),
          JournalTheme(theme='Self Care'),
          JournalTheme(theme='Checking in with yourself'),
          JournalTheme(theme='What might challenge me today?'),
          JournalTheme(theme='What are my most important values?'),
          JournalTheme(theme='How am I impacting other people around me daily?'),
          JournalTheme(theme='Connection')}
db.session.add_all(themes)
# add and commit sample data to db here


db.session.add(test_journal_1)
db.session.add(test_journal_2)
db.session.commit()

# =======
# print(db.session.query(exists().where(User.google_id == '101399575635333')).scalar())
# # input sample data here
# test_journal_1 = Journal(date=datetime.now().date(), time=datetime.now().time(), author_id=1, entry="This is a test "
#                                                                                                     "entry.",
#                          title="Test Entry", deleted=False)
# test_journal_2 = Journal(date=datetime.now().date(), time=datetime.now().time(), author_id=1, entry="This is a test "
#                                                                                                     "entry. It should "
#                                                                                                     "register as "
#                                                                                                     "deleted",
#                          title="Test Entry 2 - deleted", deleted=True)
# #themes = JournalTheme(theme=['Reflection', 'Gratitude', 'Awareness of surroundings'])
#
# # add and commit sample data to db here
# #db.session.add(themes)
# db.session.add(test_journal_1)
# db.session.add(test_journal_2)
# db.session.commit()
