
import firebase
import hashlib
import feedparser
firebase = firebase.FirebaseApplication('https://rssfeeddata.firebaseio.com/', None)

newsfeed = feedparser.parse('http://www.theverge.com/google/rss/index.xml',)
    

feeds = newsfeed['entries']
#key = hashlib.md5(newsfeed.entries[0].link + newsfeed.entries[0].title.encode('utf-8')).hexdigest()
#firebase.put('ID',':', key,)
#
#num = 0
#for item in feeds:
#    num+=1
#
#    title = item.title
#    desc = item.description.encode('utf-8')
#    data = item.title, item.description.encode('utf-8')
#    firebase.put('/articles/article'+str(num),'title',title )
#    firebase.put('/articles/article'+str(num),'body',desc )

if __name__ == '__main__':
    UpdateChecker = feedparser.parse('http://www.theverge.com/google/rss/index.xml',)
    NewUpdate = hashlib.md5(newsfeed.entries[0].link + newsfeed.entries[0].title.encode('utf-8')).hexdigest()
    lastUpdate=firebase.get('/ID',':')

    
    if lastUpdate == NewUpdate:
        print "It's Up-to-date"
    else:
        print "It's not up-to-date"
        num = 0
        for item in UpdateChecker.entries:
            num+=1
            if lastUpdate != NewUpdate:
                title = item.title
                desc = item.description.encode('utf-8')
                firebase.put('/articles/article'+str(num),'title',title )
                firebase.put('/articles/article'+str(num),'body',desc )
                firebase.put('ID',':',NewUpdate)
            else:
                print "It's uptodate "
        
        
        
    
    
    
    






