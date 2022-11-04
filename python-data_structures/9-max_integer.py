#!/usr/bin/python3
# Function that finds the biggest integer of a list


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    biggest = my_list[0]
    for integer in range(len(my_list)):
        if my_list[integer] > biggest:
            biggest = my_list[integer]

    return (biggest)
