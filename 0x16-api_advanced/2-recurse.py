#!/usr/bin/python3
""" Module that returns a list containing the titles
    of all hot articles for a given subreddit """
import json
import requests


def recurse(subreddit, hot_list=[], after="null"):
    """ Function that queries the Reddit API and
        returns the titles of all hot articles
        """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": ""}
    params = {"limit": "100", "after": after}
    request = requests.get(url, allow_redirects=False,
                           headers=headers, params=params)

    if request.status_code != 200:
        return None

    children = request.json()["data"]["children"]
    after = request.json()["data"]["after"]

    if after is not None:
        hot_list.append(children[len(hot_list)]["data"]["title"])
        recurse(subreddit, hot_list, after)

    return hot_list
