#!/usr/bin/python3
# function that prints an integer with "{:d}".format()


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return(True)
    except (TypeError, ValueError):
        return(False)
