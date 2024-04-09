#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, word_counts=None, after=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of the given keywords.

    If no posts match or the subreddit is invalid, it prints nothing.
    """
    if word_counts is None:
        word_counts = {}

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
                title = post['data']['title'].lower()
                for word in word_list:
                    count = title.count(word.lower())
                    if count > 0:
                        word_counts[word] = word_counts.get(word, 0) + count

            # Check if there are more pages of results
            after = data['data']['after']
            if after:
                # Recursively call the function with the next page of results
                return count_words(subreddit, word_list, word_counts, after)
            else:
                # No more pages, print the sorted word counts
                sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word} {count}")
    except (requests.exceptions.RequestException, KeyError):
        # If an error occurs, do nothing
        pass
