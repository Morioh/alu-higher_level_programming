#!/usr/bin/python3
# function that reads a text file (UTF8),
# and prints it to stdout
"""
    define a function 'read_file'
"""


def read_file(filename=""):
    """
        reads a text file & prints it to stdout
    """

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
