import tweepy
import json
from tweepy.auth import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = "FTdfjeihzxaUVKxGZvILikLs0"
consumer_secret = "c7D1pHZd77q2bV0L61M729WyM58d34xi3wF1cKOvUemnhNQ2pl"
access_token =	"347981696-6scrrVQWcTDaVZLlq6uTpBaRa4RiVSe6UNl4IJeD"
access_secret = "eW89ZrfLCKweiLuXmTNbljjaCRMcUxkYUEcWn756Ztpuj"


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#Prints 10 homepage tweets
def process_tweet(tweet):
	json.dumps(tweet)

processed_tweets = []
for tweet in tweepy.Cursor(api.home_timeline).items(10):
    processed_tweets.append(process_tweet(tweet._json))

print(processed_tweets)

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])
