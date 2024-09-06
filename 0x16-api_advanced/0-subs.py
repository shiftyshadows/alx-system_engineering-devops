#!/usr/bin/python3
""" This module queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """ This function queries the Reddit API and returns the number of
        subscribers(not active users, total subscribers) for a given subreddit
    """
    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
