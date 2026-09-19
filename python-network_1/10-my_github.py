#!/usr/bin/python3
"""Uses the GitHub API to display the user ID using Basic Authentication."""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, password))
    print(r.json().get('id'))
