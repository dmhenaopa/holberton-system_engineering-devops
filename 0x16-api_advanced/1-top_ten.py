#!/usr/bin/python3
""" Module that prints the titles of the first 10 hot posts """
import requests


def top_ten(subreddit):
    """ Function that queries the Reddit API and
        prints the titles of the first 10 hot
        posts listed """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": ""}
    request = requests.get(url, allow_redirects=False, headers=headers)

    if request.status_code >= 400:
        print(None)

    else:
        for post in request.json()["data"]["children"]:
            print(post["data"]["title"])
