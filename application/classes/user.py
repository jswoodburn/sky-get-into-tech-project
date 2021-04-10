class User:

    # all this info needs to be saved off to SQL

    numCreated = 0
    mindful_minutes = 0
    journal_words = 0

    def __init__(self, email, password):
        self._email = email  # add a try/except for valid email (or have this in JS)
        self._password = password  # maybe add password rules (try/except or JS)
        User.numCreated += 1
        self.user_id = User.numCreated

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
    def email_address(self):
        return self._email

    @email_address.setter
    def email(self, address):
        self._email = address

    def change_password(self, new_password):
        self._password = new_password

    @property
    def mindfulness(self):
        return self.mindful_minutes

    @mindfulness.setter
    def mindfulness(self,minutes):
        self.mindful_minutes += minutes

    @property
    def journal(self):
        return self.journal_words

    @journal.setter
    def journal(self, words):
        self.journal_words += words
