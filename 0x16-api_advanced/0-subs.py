#!/usr/bin/python3
""" Function that queries Reddit API """

import requests


def number_of_subscribers(subreddit):
    """ A function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should returns 0.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        return response_data.get('data', {}).get('subscribers', 0)
    return 0
