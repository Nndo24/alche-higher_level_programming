#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestCase class to test max_integer function.
    """

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max value at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_floats_and_ints(self):
        """Test with a list containing integers and floats."""
        self.assertEqual(max_integer([1.5, 2.8, 0.5, 2]), 2.8)

    def test_negative_numbers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_sign_numbers(self):
        """Test with positive and negative integers."""
        self.assertEqual(max_integer([-10, 5, 0, -2]), 5)

    def test_one_negative_number(self):
        """Test with a single negative number in list."""
        self.assertEqual(max_integer([-5]), -5)

    def test_string(self):
        """Test with a string input."""
        self.assertEqual(max_integer("Python"), 'y')


if __name__ == '__main__':
    unittest.main()
