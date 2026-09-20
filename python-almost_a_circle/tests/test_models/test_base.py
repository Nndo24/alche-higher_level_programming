#!/usr/bin/python3
"""Unittest for models/base.py"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test suite for Base class."""

    def test_id_auto_assignment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_id_custom_assignment(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        s = Base.to_json_string([{'id': 12}])
        self.assertEqual(s, '[{"id": 12}]')
        self.assertIsInstance(s, str)

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        res = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(res, [{'id': 89}])
        self.assertIsInstance(res, list)

    def test_create(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_save_and_load_file(self):
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        list_rects = Rectangle.load_from_file()
        self.assertEqual(len(list_rects), 1)
        self.assertEqual(list_rects[0].id, 1)
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
