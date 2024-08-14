#!/usr/bin/python3

"""
This module contains a function to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API and returns the number of subscribers 
    (not active users, total subscribers) for a given subreddit. If an invalid 
    subreddit is given, the function should return 0.

    Parameters:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers for the given subreddit.
    """
    
    # Set a custom User-Agent to avoid getting errors related to Too Many Requests
    headers = {'User-Agent': 'My User Agent 1.0'}
    
    # Construct the API URL for the given subreddit
    url = f'https://oauth.reddit.com/r/{subreddit}/about'
    
    # Send a GET request to the API
    response = requests.get(url, headers=headers)
    
    # If the request is successful, the status code will be 200
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Return the number of subscribers
        return data['data']['subscribers']
    else:
        # If the request is not successful, return 0
        return 0
