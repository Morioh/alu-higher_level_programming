#!/usr/bin/python3
# function that appends a string at the end of a text file (UTF8),
# and returns the number of characters added
"""
    define a function 'append_write'
"""


def append_write(filename="", text=""):
    """
        appends a string to end of text file,
        and return num of characters written
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
