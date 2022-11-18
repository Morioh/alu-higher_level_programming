#!/usr/bin/python3
# function that returns 'True' if the object is an instance,
# of a class that inherited (directly or indirectly) from,
# the specified class ; otherwise 'False'
"""
    define a function 'inherits_from'
"""


def inherits_from(obj, a_class):
    """
        checks if an object is an inherited instance of a class
        Return: - True
                - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
