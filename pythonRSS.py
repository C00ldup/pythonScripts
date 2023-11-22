# https://www.ansa.it/sito/static/ansa_rss.html
import feedparser
import re
import database

def getAnsaRecord():
    url = "https://www.ansa.it/sito/notizie/cronaca/cronaca_rss.xml"
    feeds = feedparser.parse(url)

    database.createTable()

    for feed in feeds.entries:
        if database.recordExist(feed.id) is None:
            text = f"Title: {feed.title}\nSummary: {feed.summary}\nLink: {feed.link}"
            '''
            print("id: "+feed.id)
            print("title: "+feed.title)
            print("summary: "+feed.summary)
            print("published: "+feed.published)
            print("link: "+feed.link)
            '''
            database.insertRecord(feed.id, feed.title, feed.published, feed.link)

    try:
        return text
    except:
        return None
'''
# example
giovanni=getAnsaRecord()
if giovanni != None:
    print(giovanni)
'''
#database.selectAll()
'''
print("id: "+feeds.entries[1].id)
print("link: "+feeds.entries[1].link)
print("published: "+feeds.entries[1].published)
print("summary: "+feeds.entries[1].summary)
print("title: "+feeds.entries[1].title)
'''