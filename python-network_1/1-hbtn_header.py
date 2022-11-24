#!/usr/bin/python3
# python script that takes in a URL, sends a request to the URL,
# and displays the value of the 'X-Request-Id',
# variable found in the header of the response.
"""
   send request to a URL, & displays value of the 'X-Request-Id'
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
