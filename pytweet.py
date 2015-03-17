'''
test python twitter api get input streaming for your tweets
Should work as long as you have connection
cd C:\Projects\pytweet\testenv
.\Scripts\activate
cd src
python pytweet.py
'''
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

consumer_key = 'AstAYAqNU3xi0UeXX0B744XwT'
consumer_secret = 'vF94dDxrxL9YWPxfqCvSMUWZQVIKhTfdJOnRxO5vah7RQbk4SQ'
access_token_key = '1054441159-CAkOIIEBCi8cDGm9fe8e4WeEqqT1u9YP0ba0m8Z'
access_token_secret = 'yuJ96C22YxU1Ks8cFv6oRSWcTOAiSFYzO6nzrZfI4U9eY'

tweetColor=""

		
class listener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to console.
    """
	
    def printRGBVal(self, color):
		if color == 'yellow':
			print "225,225,0"
		elif color == 'red':
			print "225,0,0"
		elif color == 'lime':
			print "0,225,0"
		elif color == 'blue':
			print "0,0,225"
		elif color == 'green':
			print "0,128,0"
		elif color == 'purple':
			print "128,0,128"
		elif color == 'navy':
			print "0,0,128"
		else:
			print 'test'
			
    def on_data(self, data):
        try:
			#print data; this gives us all data as a JSON object, then we scrape relevant data
			#scrapes relevant data. actual tweet and time of tweet
			tweet = data.split(',"text":"')[1].split('","source')[0] 
			tweetColor  = tweet.split(" ")[1]
			
			#prints tweet to console			
			print tweetColor
			self.printRGBVal(tweetColor)
			#saves tweet and stores it in  a txt file :: is a separator, separates time and tweet.
			#format time better
			saveThis= str(time.time())+'::' + tweet 
			saveFile = open('tweets.txt','a') #'a' means append
			saveFile.write(saveThis)
			saveFile.write('\n')
			saveFile.close()
			return True
			
        except BaseException, e:
            print 'failed ondata,', str(e)
            time.sleep(5)
    def on_error(self, status):
        print status
	
			
			
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

twitter_stream = Stream(auth,listener())

#.filter user ID so we can get this users tweets. Google twitter ID to find user ID
twitter_stream.filter(['2841969057'])

