# https://www.ansa.it/sito/static/ansa_rss.html
import feedparser
import re

url = "https://www.ansa.it/sito/notizie/cronaca/cronaca_rss.xml"
feeds = feedparser.parse(url)

for feed in feeds.entries:
    if re.search('.*().*', feed.id, re.IGNORECASE):
        print("id: "+feed.id)
        print("title: "+feed.title)
        print("summary: "+feed.summary)
        print("published: "+feed.published)
        print("link: "+feed.link)

'''
print("id: "+feeds.entries[1].id)
print("link: "+feeds.entries[1].link)
print("published: "+feeds.entries[1].published)
print("summary: "+feeds.entries[1].summary)
print("title: "+feeds.entries[1].title)
'''