from dotenv import load_dotenv

import os

from twitter import Twitter
from twitter.oauth import OAuth
from twitter.stream import TwitterStream
from twitter.util import printNicely

load_dotenv('.env')

keyword = 'Florida'

auth=OAuth(
    os.environ['TOKEN'],
    os.environ['TOKEN_SECRET'],
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET']
)

stream = TwitterStream(auth=auth)

iterator = stream.statuses.filter(track=keyword)

for tweet in iterator:
    if tweet.get('text'):
        printNicely(tweet['text'])
    else:
        printNicely('-- DATA: ' + str(tweet))
