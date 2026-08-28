#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList that inherits from list.
"""


class MyList(list):
    """
    A subclass of list with custom methods.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        without modifying the original list.
        """
        print(sorted(self))
