#!/usr/bin/python3
""" Module that function that queries the Reddit API and
    prints the titles of the first 10 hot posts listed for
    a given subreddit.
"""


def top_ten(subreddit):
    """
        Queries the Reddit API and returns the top 10 hot posts
        of the subreddit.
    """
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in sub_info.json().get("data").get("children")]
