#!/usr/bin/python3
# function that returns 'True' if the object is exactly,
# an instance of the specified class ; otherwise 'False'
"""
    define a class 'is_same_class
"""


def is_same_class(obj, a_class):
    """
        check if an object is an exact instance
        Return: - True
                - False
    """
    if type(obj) == a_class:
        return True
    return False
