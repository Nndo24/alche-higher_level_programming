#!/usr/bin/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    """Returns True if obj inherited (subclass) from a_class; otherwise False."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
