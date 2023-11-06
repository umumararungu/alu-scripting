#!/usr/bin/python3
"""
1-main
"""
import requests
import sys


def top_ten(subreddit):
    """
    1-main
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'cynt user agent 1.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    posts = response.json().get('data').get('children')
    for post in posts[:10]:
        print(post.get('data').get('title'))
