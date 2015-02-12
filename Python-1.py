
import firebase
import feedparser
firebase = firebase.FirebaseApplication('https://rssfeeddata.firebaseio.com/')



feedURLS =['http://feeds2.feedburner.com/techradar/allnews','http://feeds.bbci.co.uk/news/business/rss.xml']
feedList= []


for i in feedURLS:
  
    feedList.append(feedparser.parse(i))
    
count = 0
if __name__ == '__main__':
    
    for feed in feedList:
        for item in feed.entries:
            title = item.title
            description =item.description
            link =item.link
            firebase.put('/articles/article'+str(count),'title',title )
            firebase.put('/articles/article'+str(count),'body',description )
            firebase.put('/articles/article'+str(count),'link',link )
            count+=1

#newsfeed = feedparser.parse('http://www.theverge.com/google/rss/index.xml',)
#newsfeed.etag
#newsfeed2 = feedparser.parse('http://www.theverge.com/google/rss/index.xml', etag=newsfeed.etag)
#
#print newsfeed2.status
#print newsfeed2.entries
#
#
#feeds = newsfeed['entries']
#feeds2 = newsfeed2['entries']
#
#num = 0
#
#for item in feeds:
#    num+=1
#
#    title = item.title
#    desc = item.description.encode('utf-8')
#    data = item.title, item.description.encode('utf-8')
#    firebase.put('/articles/article'+str(num),'title',title )
#    firebase.put('/articles/article'+str(num),'body',desc )
#
#num2 = 0
#
#for item in feeds2:
#    num2+=1
#
#    title = item.title
#    desc = item.description.encode('utf-8')
#    data = item.title, item.description.encode('utf-8')
#    firebase.put('/articles/article'+str(num2),'title',title )
#    firebase.put('/articles/article'+str(num2),'body',desc )