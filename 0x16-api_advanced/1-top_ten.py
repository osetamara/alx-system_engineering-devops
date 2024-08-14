#!/usr/bin/python3

"""
This module contains a function to query the Reddit API and print the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    This function queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
    If an invalid subreddit is given, it prints None.

    Parameters:
    subreddit (str): The name of the subreddit.
    """
    
    # Set a custom User-Agent to avoid getting errors related to Too Many Requests
    headers = {'User-Agent': 'My User Agent 1.0'}
    
    # Construct the API URL for the given subreddit
    url = f'https://oauth.reddit.com/r/{subreddit}/hot'
    
    # Send a GET request to the API
    response = requests.get(url, headers=headers)
    
    # If the request is successful, the status code will be 200
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Get the list of posts
        posts = data['data']['children']
        
        # Print the titles of the first 10 hot posts
        for post in posts[:10]:
            print(post['data']['title'])
    else:
        # If the request is not successful, print None
        print(None)
