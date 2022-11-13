#!/usr/bin/python3
# class 'Rectangle' that defines a rectangle by:
# (based on 8-rectangle.py)
"""
    define a class 'Rectangle'
"""


class Rectangle:
    """
        rectangle with private instance attributes: 'width' & 'height'
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Args:
                width (int): width of the new rectangle
                height (int): height of the new rectangle
        """
        Rectangle.number_of_instances += 1
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
                    area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
            Return:
                    perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
            Return:
                    printable representation of the rectangle(#)
        """
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height):
            string += str(self.print_symbol) * self.width
            if i < self.height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """
            Return:
                    representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
            prints message when a rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Return:
                    rectangle with largest area
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
            Return:
                    new rectangle instance that is a square
        """
        return cls(size, size)
