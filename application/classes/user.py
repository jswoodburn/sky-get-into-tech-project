from flask_login import UserMixin
class User:

    # all this info needs to be saved off to SQL

    numCreated = 0


    from db import get_db

    class User(UserMixin):
        def __init__(self, id_, name, email, profile_pic):
            self.id = id_
            self.name = name
            self.email = email
            self.profile_pic = profile_pic
            self.mindful_minutes = 0
            self.journal_words = 0

        @staticmethod
        #This needs to change to match our db structure
        def get(user_id):
            db = get_db()
            user = db.execute(
                "SELECT * FROM user WHERE id = ?", (user_id,)
            ).fetchone()
            if not user:
                return None

            user = User(
                id_=user[0], name=user[1], email=user[2], profile_pic=user[3]
            )
            return user

        @staticmethod
        def create(id_, name, email, profile_pic):
            db = get_db()
            db.execute(
                "INSERT INTO user (id, name, email, profile_pic) "
                "VALUES (?, ?, ?, ?)",
                (id_, name, email, profile_pic),
            )
            db.commit()

    @property
    def forename(self):
        return self._first_name

    @forename.setter
    def forename(self, first_name):
        self._first_name = first_name.capitalize()

    @property
    def surname(self):
        return self._last_name

    @surname.setter
    def surname(self, last_name):
        self._last_name = last_name.capitalize()

    def __str__(self):
        return [self.user_id, f"{self._first_name} {self._last_name}"]


    @property
    def mindfulness(self):
        return self.mindful_minutes

    @mindfulness.setter
    def mindfulness(self, minutes):
        self.mindful_minutes += minutes

    @property
    def journal(self):
        return self.journal_words

    @journal.setter
    def journal(self, words):
        self.journal_words += words
