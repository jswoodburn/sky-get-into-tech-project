from app import db
from application.models import *
# EVERYONE RUN THIS TO GET DBS SYNCED UP
db.drop_all()
db.create_all()

# input sample data here
# test_user_1 = User(email='jackie.woodburn@gmail.com',
#                    first_name='Jackie', last_name='Woodburn')
themes = JournalTheme(theme=['Reflection', 'Gratitude', 'Awareness of surroundings'])

# add and commit sample data to db here
# db.session.add(test_user_1)
db.session.add(themes)
# db.session.commit()
