import feedparser
feed = feedparser.parse("https://www.goodnewsnetwork.org/category/news/feed/")
entry = feed.entries[0]
# title = entry.title
# published = entry.published
# summary = entry.summary
# link = entry.link
image = entry.media_content[0]['url']
print(str(image))