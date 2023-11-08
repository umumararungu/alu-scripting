#!/usr/bin/python3

import json
import requests


def number_of_subscribers(subreddit):

    """
    A function that queries the Reddit API for a given subreddit
    and returns the total number of subscribers. 
    Returns 0 if the subreddit is invalid
    """
    
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'cynt user agent 1.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
