#!/usr/bin/python3
""" This module queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. Returns 0 if the subreddit is invalid.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: Number of subscribers or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 404:
            return 0

        result = response.json().get("data")
        return result.get("subscribers")
    except requests.RequestException:
        return 0
