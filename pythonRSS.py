# https://www.ansa.it/sito/static/ansa_rss.html
import feedparser
import re
import database
from textFormatter import convertText
import random

def feeds():
    url = ["https://www.ansa.it/sito/notizie/cronaca/cronaca_rss.xml",
           "https://rss.csmonitor.com/feeds/usa",
           "https://feeds.nbcnews.com/feeds/topstories",
           "https://feeds.nbcnews.com/feeds/worldnews",
           "https://www.newyorker.com/feed/news",
           "https://www.latimes.com/nation/rss2.0.xml",
           "https://feeds.washingtonpost.com/rss/rss_election-2012",
           "https://feeds.nbcnews.com/feeds/nbcpolitics",
           "https://feeds.feedburner.com/TechCrunch/Gaming",
           "http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml",
           "https://www.smh.com.au/rss/world.xml",
           "https://www.smh.com.au/rss/technology.xml"]
    return random.choice(url)

def getAnsaRecord(url):
    feeds = feedparser.parse(url)
    
    database.createTable()

    for feed in feeds.entries:
        if database.recordExist(feed.id) is None:
            title = convertText(feed.title, 1)
            summary = convertText(feed.summary, 2)
            link = feed.link
            
            text = f"{title}\n{summary}\n{link}"
            
            while len(title)+len(summary)+len(link) >= 220:
                if len(summary)>0:
                    summary = summary[:len(summary)-1]
                    text = f"{title}\n{(summary)}...\n{link}"
                else:
                    title = title[:len(title)-1]
                    text = f"{title}...\n{link}"
                print(summary)
            
            database.insertRecord(feed.id, feed.title, feed.published, feed.link)

    try:
        return text
    except:
        return None
print(getAnsaRecord(feeds()))
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