#!/usr/bin/python3
# class Rectangle that defines a rectangle by:
# (based on 0-rectangle.py)
"""
    define a class 'Rectangle'
"""


class Rectangle:
    """
        rectangle with private instance attributes: 'width' & 'height'
    """

    def __init__(self, width=0, height=0):
        """
            Args:
                width (int): width of the new rectangle
                height (int): height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            get the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            validates width as a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            get the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            validates height as a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
