
import firebase
import feedparser
firebase = firebase.FirebaseApplication('https://multiplerssfeed.firebaseio.com/')



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
            
