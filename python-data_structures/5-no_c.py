#!/usr/bin/python3
# Function that removes all characters 'c' and 'C' from a string


def no_c(my_string):
    copy = [letter for letter in my_string if letter != 'c' and letter != 'C']
    return ("".join(copy))
