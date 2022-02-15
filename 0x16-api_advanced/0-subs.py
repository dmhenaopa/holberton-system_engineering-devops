#!/usr/bin/python3
""" Module to obtain the total number of subscribers """
import json
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API and
       returns the number of subscribers """
    import requests
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    subscribers = requests.get(url).data.subscribers
