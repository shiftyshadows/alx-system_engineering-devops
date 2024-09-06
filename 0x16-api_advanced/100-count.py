#!/usr/bin/python3
import requests
import re
from collections import Counter


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursively queries the Reddit API to count occurrences of keywords in hot
    article titles from a given subreddit and prints the sorted count of these
    keywords.

    Parameters:
    - subreddit (str): The name of the subreddit to fetch hot articles from.
    - word_list (list): A list of keywords to count occurrences of.
    - word_count (Counter, optional): A Counter object to accumulate keyword
      counts across recursive calls.
    - after (str, optional): The 'after' parameter used for pagination.

    Returns:
    - None: The function prints the sorted count of keywords and does not
      return any value.

    Notes:
    - Keywords are counted case-insensitively and are matched exactly.
    - The function prints results sorted by count in descending order and
      alphabetically for ties.
    - If no keywords match or the subreddit is invalid, it prints nothing.
    """

    if word_count is None:
        word_count = Counter()

    # Define a custom User-Agent to avoid blocking by Reddit's API
    headers = {'User-Agent': 'hot-articles-script:v1.0'}

    # Set up the URL for Reddit's hot articles with pagination handling
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after, 'limit': 100}  # Limit results to 100 per page

    try:
        # Make the request to the Reddit API without following redirects
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        # If the request fails (invalid subreddit, or status code is not OK),
        # print nothing
        if response.status_code != 200:
            return

        # Parse the JSON response
        data = response.json()

        # Retrieve the list of posts and 'after' value for pagination
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after', None)

        # Process each post title
        for post in posts:
            title = post['data']['title'].lower()  # Convert title to lowercase
            # Count occurrences of each keyword
            for word in word_list:
                word_pattern = r'\b' + re.escape(word.lower()) + r'\b'
                word_count[word] += len(re.findall(word_pattern, title,
                                        re.IGNORECASE))

        # If there are more pages, recurse
        if after:
            return count_words(subreddit, word_list, word_count, after)
        # Print sorted keyword counts
        for word, count in sorted(word_count.items(),
                                  key=lambda x: (-x[1], x[0])):
            if count > 0:
                print(f"{word}: {count}")

    except requests.RequestException:
        # Handle any potential request-related errors
        return
