#!/usr/bin/python3
# class Rectangle that defines a rectangle by:
# (based on 3-rectangle.py)
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
        self.__width = width
        self.__height = height

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
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
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
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
            Return:
                    area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
            Return:
                    perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
            Return:
                    string version of rectangle
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += "#" * self.width
            if i < self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """
            Return:
                    string representation of the rectangle(#)
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
