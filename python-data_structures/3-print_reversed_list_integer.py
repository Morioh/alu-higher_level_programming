#!/usr/bin/python3
# function that prints all integers of a list, in reverse order


def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
