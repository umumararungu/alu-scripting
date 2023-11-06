#!/usr/bin/python3

"""
module
"""
import requests


def number_of_subscribers(subreddit):
    """
    module
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {'User-Agent': 'Ayo User Agent 1.0'}
    respnse = requests.get(url, headers=head, allow_redirects=False)

    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
