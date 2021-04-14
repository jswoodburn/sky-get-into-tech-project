from datetime import datetime

class JournalEntry:

    # need to add some kind of verification of content -- should be a string or HTML content?

    def __init__(self, author, title, content):
        now = datetime.now()
        self.date_created = now.strftime("%d/%m/%Y")
        self.time_created = now.strftime("%H:%M")
        self.author = author
        self.title = title
        self.content = content

    # IMPORTANT - this method only works if content is string, not if it is HTML.
    def get_wordcount(self):
        return len(self.content.split())

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self,new_title):
        self.title = new_title

    @property
    def content(self):
        return self.content

    @content.setter
    def content(self, new_content):
        self.content = new_content

    # if someone just wants to edit one word of a blog, need to return their old content to them, and then have it be
    # returned as new content -- use properties.

    # @property
    # def view_count(self):
    #     return self.page_views
    #
    # @view_count.setter
    # def view_count(self):
    #     self.page_views += 1
