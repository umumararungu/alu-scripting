#!/usr/bin/python3
"""
uses reddit's APIs
to get the number of total number of subscribers
of a subrredit
"""


import json
import requests
import sys


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers of a given subrredit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'cynt user agent 1.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
if __name__ == "__main__":
    pass
