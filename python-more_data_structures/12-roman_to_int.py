#!/usr/bin/python3
# function def roman_to_int(roman_string):
# that converts a Roman numeral to an integer.


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    int_sum = 0
    converter = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    for current, next in zip(roman_string, roman_string[1:]):
        if converter[current] >= converter[next]:
            int_sum += converter[current]
        else:
            int_sum -= converter[current]
    int_sum += converter[roman_string[-1]]
    return int_sum
