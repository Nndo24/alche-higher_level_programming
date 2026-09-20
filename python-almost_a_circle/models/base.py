#!/usr/bin/python3
"""
This module defines the Base class.
"""


class Base:
    """
    Base class to manage the id attribute across models.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int, optional): ID value for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
