#!/usr/bin/python3
"""
    Module that recursively queries the Reddit API and returns
    a list of titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
       Recursively queries the Reddit API and returns a list
       of titles of all hot articles for a given subreddit.
       If no results are found or the subreddit is invalid,
       it returns None.

       Parameters:
       - subreddit (str): The name of the subreddit to fetch
         hot articles from.
       - hot_list (list, optional): Accumulates the titles
         of the hot articles across recursive calls. Default
         is an empty list.
       - after (str, optional): The 'after' parameter used for
         pagination to get the next page of results. Default
         is None.

       Returns:
       - list: A list containing the titles of all hot
         articles for the given subreddit.
       - None: If the subreddit is invalid or there are
         no hot articles found.

       Notes:
       - The Reddit API uses pagination for separating pages
         of responses. We handle this recursively by using
         the 'after' parameter.
       - Invalid subreddits may redirect to search results.
         This function does not follow redirects to ensure
         it returns None for invalid subreddits.
       - Each recursive call retrieves a maximum of 100
         hot articles (limit set in the API request).

       Example:
       - recurse('python') -> Returns a list of hot article
         titles from the 'python' subreddit
       - recurse('invalidsubreddit') -> Returns None
    """

    headers = {'User-Agent': 'hot-articles-script:v1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after', None)
        for post in posts:
            hot_list.append(post['data']['title'])
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list if hot_list else None

    except requests.RequestException:
        return None
