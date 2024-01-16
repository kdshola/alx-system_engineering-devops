#!/usr/bin/python3
""" Function that queries API """

import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """ A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function returns None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after, 'count': count}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    data = response.json().get('data')
    count += data.get('dist')
    after = data.get('after')
    children = data.get('children')
    [hot_list.append(child.get('data').get('title')) for child in children]
    if after is not None:
        recurse(subreddit, hot_list, after=after, count=count)
    return hot_list
