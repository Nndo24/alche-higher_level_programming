#!/usr/bin/python3
"""
This module defines the Base class for the project.
"""
import json
import os


class Base:
    """
    Base class for manage id attribute in all future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializer for Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON string representation of list_objs to a file.
        """
        filename = f"{cls.__name__}.json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from JSON file.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            json_str = f.read()
        dicts = cls.from_json_string(json_str)
        return [cls.create(**d) for d in dicts]
