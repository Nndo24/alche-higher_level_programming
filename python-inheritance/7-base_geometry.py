#!/usr/bin/python3
"""
Module 7-base_geometry
Contains class BaseGeometry
"""


class BaseGeometry:
    """
    A class representing BaseGeometry with area and validation methods.
    """

    def area(self):
        """
        Raises an Exception indicating area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as an integer greater than 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
