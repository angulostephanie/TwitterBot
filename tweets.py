import tweepy, time, sys
import keys

CONSUMER_KEY = keys.consumer_key
CONSUMER_SECRET = keys.consumer_secret
ACCESS_KEY = keys.access_token
ACCESS_SECRET = keys.access_token_secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def retweet(id):
    # example - 990335296129527808 (need to parse the link and get the number)
    tweet = api.get_status(id)
    tweet.retweet()


api.update_status("This is a test!")
