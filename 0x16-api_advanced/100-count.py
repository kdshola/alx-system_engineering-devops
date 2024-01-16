#!/usr/bin/python3
""" Function that queries API recursively"""

import requests


def count_words(subreddit, word_list):
    """ Arecursive function that queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count as
    javascript, but java should not).
    If no posts match or the subreddit is invalid, prints nothing.
    """
