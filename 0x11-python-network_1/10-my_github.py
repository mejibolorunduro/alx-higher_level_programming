#!/usr/bin/python3

"""
Takes your GitHub credentials (username and password) and uses the GitHub API
to display your id
"""

if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
    else:
        print(f"Error: Unable to retrieve user data. Status code: {response.status_code}")
