#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class body. """

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle props in contructor.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns an informal string representation
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        record_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                record_str += '#'
            record_str += '\n'
        return record_str[:-1]

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        """
        if not isinstance(value, int):

