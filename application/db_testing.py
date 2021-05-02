from application import db
from application.models import User, Journal, JournalTheme
from sqlalchemy.sql import exists
from  sqlalchemy.sql.expression import func, select
from datetime import datetime

id = int(2)
journal_id = int(1)

journal = db.session.query(Journal).get(journal_id)
user = db.session.query(User).get(id)

print(journal)
print(user)
for journal in db.session.query(Journal).filter_by(journal_id=journal_id).filter_by(author_id=id):
    print(journal.title)