#!/usr/bin/python3
import requests


def recurse(subreddit, host_list=[], next_str="0"):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if not host_list:
        req = requests.get(url, headers={'User-Agent': 'h_reddit'})
        if (req.status_code != requests.codes.ok):
            return (None)
    else:
        if next_str is not None:
            more = {'after': next_str}
            req = requests.get(url, headers={'User-Agent': 'L'}, params=more)
        else:
            return (host_list)
    big_json = req.json()
    for i in range(len(big_json['data']['children'])):
        host_list.append(big_json['data']['children'][i]['data']['title'])
    return recurse(subreddit, host_list, big_json['data']['after'])
