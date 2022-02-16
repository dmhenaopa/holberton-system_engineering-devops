#!/usr/bin/python3
""" Module to obtain the total number of subscribers """
import json
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API and
       returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": ""}
    request = requests.get(url, allow_redirects=False, headers=headers)

    if request.status_code >= 400:
        return 0

    subscribers = request.json()["data"]["subscribers"]
    return subscribers
