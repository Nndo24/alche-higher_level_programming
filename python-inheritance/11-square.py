#!/usr/bin/python3
"""Module for Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class representation with custom str output."""

    def __init__(self, size):
        """Initializes square size using Rectangle constructor."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
