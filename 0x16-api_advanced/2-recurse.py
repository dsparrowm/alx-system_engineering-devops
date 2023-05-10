#!/usr/bin/python3
"""queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.
"""
import requests
import sys


def recurse(subreddit, last_post=None, posts=None):
    """ Make a GET request to the subreddit's hot.json endpoint"""
    sub = sys.argv[1]
    api = "https://www.reddit.com/r/{}/hot.json".format(sub)
    response = requests.get(api,
                            headers={"User-agent": "Mozilla/5.0"},
                            params={"after": last_post})
    # Check if the request was successful
    if response.status_code != 200:
        # If the request was not successful, return None
        return None
    # If the request was successful, parse the JSON response
    data = response.json()
    # Initialize the list of posts if it's not already created
    if posts is None:
        posts = []
        # Extract the titles of the posts from the JSON data
        for post in data["data"]["children"]:
            posts.append(post["data"]["title"])
            # Check if there are more pages to load
            if data["data"]["after"] is not None:
                """ If there are more pages to load, recursively
                    call the function with the last post's name
                    as the "after" parameter
                """
                recurse(subreddit, last_post=data["data"]["after"],
                        posts=posts)
                # Return the list of posts
                return posts
