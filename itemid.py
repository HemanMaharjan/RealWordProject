import firebase
import feedparser
#firebase = firebase.FirebaseApplication('https://rssfeeddata.firebaseio.com/')

newsfeed = feedparser.parse('http://www.theverge.com/google/rss/index.xml',)
    
print newsfeed['entries'][0]['published'] ['guid']
#num = 0
#for item in feeds:
#    num+=1
#
#    title = item.title
#    desc = item.description.encode('utf-8')
#    data = item.title, item.description.encode('utf-8')
#    firebase.put('/articles/article'+str(num),'title',title )
#    firebase.put('/articles/article'+str(num),'body',desc )
    
    






