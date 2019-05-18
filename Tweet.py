from __future__ import print_function
import tweepy, sys, time
import time
import requests
import json
import pyjokes
from apscheduler.schedulers.background import BackgroundScheduler
from resteasy import RESTEasy
import urllib.request
import threading
from threading import Timer
import time
import threading

consumer_key = 'xxx'
consumer_secret = 'xxx'
access_key = 'xxx'
access_key_secret = 'xxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_key_secret)

api = tweepy.API(auth)
user = api.me()

def tweetToTwitter():
    responeData = requests.get("http://api.icndb.com/jokes/random/?escape=javascript")
    mystatustext = str(responeData.json()['value']['joke'])
    api.update_status(status=mystatustext)

def printit():
  threading.Timer(21600.0, printit).start()
  tweetToTwitter()
  print("Tweet printed! - https://twitter.com/DailyJo46516382 ")
  print("Username >> " + user.name)
  tweets = api.user_timeline()
  for tweet in tweets:
      print(tweet.text)


printit()

