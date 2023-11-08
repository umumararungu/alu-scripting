#!/usr/bin/python3
"""
1-main
"""
import requests


def top_ten(subreddit):
    """
    1-main
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'cynt user agent 1.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get('data').get('children')
    for post in posts[:10]:
        print(post.get('data').get('title'))
