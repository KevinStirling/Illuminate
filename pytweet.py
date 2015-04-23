
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import ColorLibrary

import time
from neopixel import *


#secret stuff
consumer_key = 'AstAYAqNU3xi0UeXX0B744XwT'
consumer_secret = 'vF94dDxrxL9YWPxfqCvSMUWZQVIKhTfdJOnRxO5vah7RQbk4SQ'
access_token_key = '1054441159-CAkOIIEBCi8cDGm9fe8e4WeEqqT1u9YP0ba0m8Z'
access_token_secret = 'yuJ96C22YxU1Ks8cFv6oRSWcTOAiSFYzO6nzrZfI4U9eY'

tweetColor=""

# LED strip configuration:
LED_COUNT      = 180     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


		
class listener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to console.
    """
			
    def on_data(self, data):
        try:
			#print data; this gives us all data as a JSON object, then we scrape relevant data
			#scrapes relevant data. actual tweet and time of tweet
			tweet = data.split(',"text":"')[1].split('","source')[0] 
			tweetColor  = tweet.split(" ")[1]
			
			#prints tweet to console			
			print tweetColor

			#create instance of Colors class to get rgb values
			instance = ColorLibrary.Colors()
			RGBString = instance.returnRGBVal(tweetColor)
			print RGBString

			red = instance.returnRed(RGBString)
			green = instance.returnGreen(RGBString)
			blue = instance.returnBlue(RGBString)
			
			#pass these variables to light up variable
			red = instance.returnRed(RGBString)
			green =  instance.returnGreen(RGBString)
			blue =  instance.returnBlue(RGBString)

			# Create NeoPixel object with appropriate configuration.
			strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
			# Intialize the library (must be called once before other functions).
			strip.begin()
			for i in range(180):
				strip.setPixelColorRGB(i, red,green,blue)
			strip.show()
			'''			
			#saves tweet and stores it in  a txt file :: is a separator, separates time and tweet.
			#format time better
			saveThis= str(time.time())+'::' + tweet 
			saveFile = open('tweets.txt','a') #'a' means append
			saveFile.write(saveThis)
			saveFile.write('\n')
			saveFile.close()
			'''
			return True
			
        except BaseException, e:
            print 'failed ondata,', str(e)
            time.sleep(5)
    def on_error(self, status):
        print status
	
			
#Oauth stuff			
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

#call streaming class
twitter_stream = Stream(auth,listener())

#.filter user ID so we can get this users tweets. Google twitter ID to find user ID
twitter_stream.filter(['2841969057'])

