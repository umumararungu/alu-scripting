#!/usr/bin/python3

"""
module
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    module
    """
    subs_number =requests.get("https://www.reddit.com/api/subscribe"
                              .format(argv[1]))
    subs_number = subs_number.json()

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(subs_number(sys.argv[1])))
