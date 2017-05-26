#!/usr/bin/python3
"""
Subroutine that grabs the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Query API and return the number of subscribers if it exists
    Return 0 if API does not exist
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers={'User-Agent': 'lee'})
    if (req.status_code == requests.codes.ok):
        big_json = req.json()
        return(big_json['data']['subscribers'])
    return (0)
