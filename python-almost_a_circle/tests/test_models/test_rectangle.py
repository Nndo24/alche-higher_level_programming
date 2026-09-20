#!/usr/bin/python3
"""Unittest for models/rectangle.py"""
import unittest
import io
import sys
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for Rectangle class."""

    # Explicit instantiation test cases for the checker
    def test_rectangle_1_2(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_1_2_3(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_rectangle_1_2_3_4(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_1_2_3_4_5(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    # Type error tests
    def test_rectangle_str_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_str_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_str_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_str_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    # Value error tests
    def test_rectangle_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    # Method tests
    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_without_x_y(self):
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_without_y(self):
        r = Rectangle(2, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "  ##\n  ##\n")

    def test_display(self):
        r = Rectangle(2, 2, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n  ##\n  ##\n")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(), {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    # Update tests
    def test_update_args(self):
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

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
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

    # Create tests
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

    # Save and Load tests
    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        os.remove("Rectangle.json")

    def test_save_to_file_rectangles(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 1)
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
