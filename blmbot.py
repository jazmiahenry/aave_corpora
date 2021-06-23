import os
import tweepy as tw
import pandas as pd
from textblob import TextBlob
import json
import logging
import requests
from requests_oauthlib import OAuth1
import urllib3
import tweepy
from tweepy.error import TweepError
from tweepy.models import Status

consumer_key= 'PLACE KEY HERE'
consumer_secret= 'PLACE KEY HERE'
access_token= 'PLACE KEY HERE'
access_token_secret= 'PLACE KEY HERE'

tweet_limit = 100000

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)



class StreamListener(tweepy.StreamListener):

    def __init__(self, api=None):
        super(StreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("blm_bgm.txt", "w")
        
    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        

        if self.num_tweets =< tweet_limit:
            if self.num_tweets % 100 == 0:
                print('Number of tweets captured so far: {}'.format(self.num_tweets))
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

    def on_error(self, status_code):
        if status_code == 420:
            return False


stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=['#BLM', '#BlackGirlMagic', '#BlackLivesMatter'])

