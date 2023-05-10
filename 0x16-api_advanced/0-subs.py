#!/usr/bin/python3
"""Returns the number of subscribers from an Api endpoint"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ Make a GET request to the subreddit's
    about.json endpoint
    """
    sub = sys.argv[1]
    base_url = "https://www.reddit.com/r/{}/about.json".format(sub)
    response = requests.get(base_url, headers={"User-agent": "Mozilla/5.0"})
    # Check if the request was successful
    if response.status_code != 200:
        # If the request was not successful, return 0
        return 0
    # If the request was successful, parse the JSON response
    data = response.json()
    # Extract the number of subscribers from the JSON data
    subscribers = data["data"]["subscribers"]
    # Return the number of subscribers
    return subscribers
