#!/usr/bin/python3
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    req = requests.get(url, headers={'User-Agent': 'h'})
    if (req.status_code == requests.codes.ok):
        big_json = req.json()
        for i in range(len(big_json['data']['children'])):
            print(big_json['data']['children'][i]['data']['title'])
    else:
        print(None)
