#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is not valid, returns 0.
    """
    # Set a custom User-Agent to avoid rate limiting
    headers = {'User-Agent': 'MyRedditApp/1.0'}

    # Construct the API endpoint URL
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        # Send a GET request to the API endpoint
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the subscriber count from the JSON response
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the subreddit is not valid, return 0
            return 0
    except (requests.exceptions.RequestException, KeyError):
        # If an error occurs, return 0
        return 0
