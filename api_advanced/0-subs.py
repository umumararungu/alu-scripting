#!/usr/bin/python3

"""
module
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    module
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    respnse = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
