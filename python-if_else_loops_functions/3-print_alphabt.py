#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
    if letter != ord('e') and letter != ord('q'):
        print("{:c}".format(letter), end="")
