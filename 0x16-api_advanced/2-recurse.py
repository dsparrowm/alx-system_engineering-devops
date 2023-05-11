#!/usr/bin/python3
"""queries the Reddit API and returns a list containing the titles
   of all hot articles for a given subreddit.
   If no results are found for the given subreddit,
   the function should return None.
"""
import requests


def recurse(subreddit, next_page='', count=0, hot_list=[]):
    """ Make a GET request to the subreddit's hot.json endpoint"""
    req_params = {
            'after': next_page,
            'count': count,
            'limit': 100
            }
    url = "{}/{}/hot.json".format(API, subreddit)

    resp = requests.get(url, params=req_params,
                        headers={"User-agent": "Mozilla/5.0"},
                        allow_redirects=False)

    # Check if request was successfull
    if resp.status_code != requests.codes.ok:
        return (None)

    # Parse res to JSON and return list of all titles
    listing = resp.json().get('data')
    next_page = listing.get('after')  # Get the next page to fetch
    count += len(listing.get('children'))

    # Append all page titles to hot_list
    for child in listing.get('children'):
        hot_list.append(child.get('data').get('title'))

    # Return hot list if no next page
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, count)
    return hot_list
