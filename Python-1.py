import hashlib
import firebase
import feedparser
firebase = firebase.FirebaseApplication('https://multiplerssfeed.firebaseio.com/')


#feedURLS =['http://feeds2.feedburner.com/techradar/allnews','http://feeds.bbci.co.uk/news/business/rss.xml']
#feedList= []
##key = hashlib.md5(newsfeed.entries[0].link + newsfeed.entries[0].title.encode('utf-8')).hexdigest()
#for i in feedURLS:
#    feedList.append(feedparser.parse(i))
#count = 0
#counter = 0
#
#if __name__ == '__main__':
#    
#    for feed in feedList:
#      key = hashlib.md5(feed.entries[0].link).hexdigest()
#      firebase.put('ID',':'+str(counter),key)
#      counter+=1
#      
#
#            
#      for item in feed.entries:
#         
#            title = item.title
#            description =item.description
#            link =item.link
#            firebase.put('/articles/article'+str(count),'title',title )
#            firebase.put('/articles/article'+str(count),'body',description )
#            firebase.put('/articles/article'+str(count),'link',link )
#            count+=1
#            
            
UpdateChecker =['http://feeds2.feedburner.com/techradar/allnews','http://feeds.bbci.co.uk/news/business/rss.xml']
feedList= []
for i in UpdateChecker:
    feedList.append(feedparser.parse(i))
counter = 0

for feed in feedList:
      key = hashlib.md5(feed.entries[0].link).hexdigest()
      firebase.put('NEWID',':'+str(counter),key)
      counter+=1
      
LastUpdate =firebase.get('/ID',None)
print LastUpdate
NewUpdate = firebase.get('/NEWID', None)
print NewUpdate


if NewUpdate == LastUpdate:
   print "It's up-to-date"
else:
   print "I'ts not up-to-date"