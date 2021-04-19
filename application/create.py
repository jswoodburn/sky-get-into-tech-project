# EVERYONE RUN THIS TO GET DBS SYNCED UP

from application import db
from application.models import Journal, User

db.drop_all()
db.create_all()

# input sample data here
test_user_1 = User(email='jackie.woodburn@gmail.com', password='password1', phone_number='07512656497',
                   first_name='Jackie', last_name='Woodburn')
test_journal = Journal(journal_id=234324)


# add and commit sample data to db here
db.session.add(test_user_1)
db.session.commit()