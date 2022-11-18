#!/usr/bin/python3
# function that returns the list of available,
# attributes and methods of an object
"""
    define a function 'lookup'
"""


def lookup(obj):
    """
        Return:list object
    """
    return (dir(obj))
