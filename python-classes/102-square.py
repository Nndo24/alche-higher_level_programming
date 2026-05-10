#!/usr/bin/python3
"""Module for a Square class with comparison capabilities."""


class Square:
    """Defines a square and allows comparison by area."""

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (number): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation for numbers."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if areas are equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if areas are not equal."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if area is less than other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if area is less than or equal to other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if area is greater than other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if area is greater than or equal to other."""
        return self.area() >= other.area()
