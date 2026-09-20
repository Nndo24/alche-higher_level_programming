#!/usr/bin/python3
"""Unittest for models/rectangle.py"""
import unittest
import io
import sys
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for Rectangle class."""

    def test_instantiation(self):
        r1 = Rectangle(1, 2)
        self.assertIsNotNone(r1)
        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.x, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.y, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)

    def test_type_and_value_errors(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        r1 = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

        r2 = Rectangle(2, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "  ##\n  ##\n")

        r3 = Rectangle(2, 2, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n  ##\n  ##\n")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(), {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_update(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 1)
        self.assertEqual(r.width, 1)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create(self):
        r1 = Rectangle.create(**{'id': 89})
        self.assertEqual(r1.id, 89)
        r2 = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r2.width, 1)
        r3 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r3.height, 2)
        r4 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r4.x, 3)
        r5 = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r5.y, 4)

    def test_save_and_load_file(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 1)
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
