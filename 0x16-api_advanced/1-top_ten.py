#!/usr/bin/python3
""" Module that function that queries the Reddit API and
    prints the titles of the first 10 hot posts listed for
    a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit. If the subreddit is invalid, prints None.

    Args:
        subreddit (str): The name of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": (
            "Python:subreddit.hot.posts.v1.0 (by /u/shifty_shadows)"
        )
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])
            for post in data:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
