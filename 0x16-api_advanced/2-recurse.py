#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for the given subreddit.

    If no results are found for the given subreddit, the function
    returns None.
    """
    if hot_list is None:
        hot_list = []

    # Set a custom User-Agent to avoid rate limiting
    headers = {'User-Agent': 'MyRedditApp/1.0'}

    # Construct the API endpoint URL
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'

    try:
        # Send a GET request to the API endpoint
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the post titles from the JSON response
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])

            # Check if there are more pages of results
            after = data['data']['after']
            if after:
                # Recursively call the function with the next page of results
                return recurse(subreddit, hot_list, after)
            else:
                # No more pages, return the hot_list
                return hot_list
        else:
            # If the subreddit is not valid, return None
            return None
    except (requests.exceptions.RequestException, KeyError):
        # If an error occurs, return None
        return None
