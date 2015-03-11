
import feedparser

newsfeed = feedparser.parse('http://feeds.bbci.co.uk/news/business/rss.xml',)

feeds = newsfeed['entries']


num = 0

for item in ('http://feeds.bbci.co.uk/news/business/rss.xml')
    num+=1

    title = item.title
    desc = item.description.encode('utf-8')
    data = item.title, item.description.encode('utf-8')
    ID =item.guid
    Tags = tags.category
    print title
    print ID
    print Tags
    
   
