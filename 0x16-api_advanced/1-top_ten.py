#!/usr/bin/python3
""" Module that function that queries the Reddit API and
    prints the titles of the first 10 hot posts listed for
    a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
        Queries the Reddit API and returns the top 10 hot posts
        of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {
        "User-Agent": (
            "Python:subreddit.subscriber.counter:v1.0 (by /u/shifty_shadows)"
        )
    }
    sub_info = requests.get(url, headers=header, allow_redirects=False)
    if sub_info.status_code >= 300:
        print('None')
    try:
        data = sub_info.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    except ValueError:
            print("Error: Response is not in JSON format")
#        for child in sub_info.json().get("data").get("children"):
#            print(child.get("data").get("title"))
