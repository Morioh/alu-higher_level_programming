#!/usr/bin/python3
# class 'Square' that defines a square by:
# (based on 3-square.py)
"""
    define a class 'Square'
"""


class Square:
    """
        square with private instance attribute: 'size'
    """

    def __init__(self, size=0):
        """
            Args:
                size (int): size of the new square
        """
        self.size = size

    @property
    def size(self):
        """
            gets current size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
            validates size is an integer that is greater than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
            Return: area of the square
        """
        return (self.__size * self.__size)
