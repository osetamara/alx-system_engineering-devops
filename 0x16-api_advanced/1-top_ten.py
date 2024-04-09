#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is not valid, prints None.
    """
    # Set a custom User-Agent to avoid rate limiting
    headers = {'User-Agent': 'MyRedditApp/1.0'}

    # Construct the API endpoint URL
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        # Send a GET request to the API endpoint
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the post titles from the JSON response
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            # If the subreddit is not valid, print None
            print(None)
    except (requests.exceptions.RequestException, KeyError):
        # If an error occurs, print None
        print(None)
