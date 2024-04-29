#!/usr/bin/python3
"""Square class defination"""


class Square:
    """Square class body"""

    def __init__(self, size=0, position=(0, 0)):
        """Square constructor .
        Args:
            size (int): The size of the new square.
            square position (int, int): of Tupple.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Setter and getter of a  square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter and Setter for position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or

