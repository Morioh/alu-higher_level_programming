#!/usr/bin/python3
# Function that prints all integers of a list

def print_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        print("{:d}".format(my_list[i]))
