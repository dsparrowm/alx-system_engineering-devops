#!/usr/bin/python3
"""print the top 10 posts from the Api endpoint"""
import requests
import sys


def top_ten(subreddit):
    """ Make a GET request to the subreddit's hot.json endpoint"""
    sub = sys.argv[1]
    base_url = "https://www.reddit.com/r/{}/hot.json".format(sub)
    response = requests.get(base_url,
                            headers={"User-agent": "Mozilla/5.0"},
                            params={"limit": 10})
    # Check if the request was successful
    if response.status_code != 200:
        # If the request was not successful, print None
        print(None)
        return
    # If the request was successful, parse the JSON response
    data = response.json()
    # Extract the titles of the first 10 posts from the JSON data
    for post in data["data"]["children"]:
        print(post["data"]["title"])
