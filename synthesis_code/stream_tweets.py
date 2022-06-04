import config
import os
import tweepy as tw
import pandas as pd
import json
import logging
import requests
from requests_oauthlib import OAuth1
import urllib3
import tweepy
from tweepy.errors import TweepyException
from tweepy.models import Status

tweet_limit = 1000000

class Stream: 
    """ Filter Tweet Stream

    Params
    -------
    api_key: str
        Twitter API key 
    api_secret: str
        Twitter API secret
    acess_token: str
        Twitter API access token
    access_token_secret : str
        Twitter API access token secret
    verify : bool
        Verify server's TLS cert

    Attributes
    -----------
    running : bool
        Is Stream Currently Running
    user_agent : str
        Agent connected to Stream
    """

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, verify = True):
        self.consumer_key = config.consumer_key
        self.consumer_secret = config.consumer_secret
        self.access_token = config.access_token
        self.access_token_secret = config.access_token_secret

        self.running = False
        self.user_agent = (
            f"Python/{python_version()} "
            f"Requests/{requests.__version__} "
            f"Tweepy/{tweepy.__version__}")

        def _connect(self, method):
            self.running = True

            error_count = 0
            # https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/connecting
            stall_timeout = 90
            network_error_wait = network_error_wait_step = 0.25
            network_error_wait_max = 16
            http_error_wait = http_error_wait_start = 5
            http_error_wait_max = 320
            http_420_error_wait_start = 60

            auth = OAuth1(self.consumer_key, self.consumer_secret,
                      self.access_token, self.access_token_secret)

            if self.session is None:
                self.session = requests.Session()
                self.session.headers["User-Agent"] = self.user_agent

            url = f"https://stream.twitter.com/1.1/{endpoint}.json"

            try:
                while self.running and error_count <= self.max_retries:
                    try:
                        with self.session.request(
                            method, url, params=params, headers=headers, data=body,
                            timeout=stall_timeout, stream=True, auth=auth,
                            verify=self.verify, proxies=self.proxies
                        ) as resp:
                            if resp.status_code == 200:
                                error_count = 0
                                http_error_wait = http_error_wait_start
                                network_error_wait = network_error_wait_step

                                self.on_connect()
                                if not self.running:
                                    break

                                for line in resp.iter_lines(
                                    chunk_size=self.chunk_size
                                ):
                                    if line:
                                        self.on_data(line)
                                    else:
                                        self.on_keep_alive()
                                    if not self.running:
                                        break

                                if resp.raw.closed:
                                    self.on_closed(resp)
                            else:
                                self.on_request_error(resp.status_code)
                                if not self.running:
                                    break

                                error_count += 1

                                if resp.status_code == 420:
                                    if http_error_wait < http_420_error_wait_start:
                                        http_error_wait = http_420_error_wait_start

                                sleep(http_error_wait)

                                http_error_wait *= 2
                                if http_error_wait > http_error_wait_max:
                                    http_error_wait = http_error_wait_max
                    except (requests.ConnectionError, requests.Timeout,
                            requests.exceptions.ChunkedEncodingError,
                            ssl.SSLError, urllib3.exceptions.ReadTimeoutError,
                            urllib3.exceptions.ProtocolError) as exc:
                    # This is still necessary, as a SSLError can actually be
                    # thrown when using Requests
                    # If it's not time out treat it like any other exception
                        if isinstance(exc, ssl.SSLError):
                            if not (exc.args and "timed out" in str(exc.args[0])):
                                raise

                        self.on_connection_error()
                        if not self.running:
                            break

                        sleep(network_error_wait)

                        network_error_wait += network_error_wait_step
                        if network_error_wait > network_error_wait_max:
                            network_error_wait = network_error_wait_max
            except Exception as exc:
                self.on_exception(exc)
            finally:
                self.session.close()
                self.running = False
                self.on_disconnect()

class StreamListener(tweepy.Stream):

    def __init__(self, api=None):
        super(StreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("Impeach_tweets_noon.txt", "w")
        
    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        

        if self.num_tweets <= tweet_limit:
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


stream_listener = tweepy.Stream()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=['#BLM', '#BlackGirlMagic', '#InsecureHBO', '#OscarsSoWhite', '#BlackLivesMatter', '#BlackTwitter'])
