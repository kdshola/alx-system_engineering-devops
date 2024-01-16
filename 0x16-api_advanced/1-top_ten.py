#!/usr/bin/python3
""" Function that queries API """

import requests


def top_ten(subreddit):
    """ Afunction that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 404:
        print('None')
        return None
    data = response.json()
    results = data.get('data', {})
    [print(child.get('data').get('title'))
        for child in results.get('children')]
