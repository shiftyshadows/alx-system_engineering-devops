#!/usr/bin/python3
""" This module queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit."""
import requests

def number_of_subscribers(subreddit):
    """ This function queries the Reddit API and returns the number of
        subscribers(not active users, total subscribers) for a given subreddit
    """
    # Define a custom User-Agent
    headers = {'User-Agent': 'Python:subscribers-script:v1.0 (by /u/yourusername)'}

    # URL for Reddit's API to fetch subreddit data
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        # Make the request to the Reddit API without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If the status code is 200 (OK), parse the data
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the subreddit is not valid or does not exist
            return 0
    except requests.RequestException:
        # Handle any potential exceptions during the request
        return 0
