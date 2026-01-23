#!/usr/bin/python3
"""Unittests for max_integer([..]) function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Max at the end of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max somewhere in the middle of an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the beginning of the list."""
        self.assertEqual(max_integer([10, 9, 8, 7]), 10)

    def test_negative_numbers(self):
        """List containing only negative numbers."""
        self.assertEqual(max_integer([-5, -9, -3]), -3)

    def test_mixed_numbers(self):
        """List containing both positive and negative numbers."""
        self.assertEqual(max_integer([0, -5, 10, 7]), 10)

    def test_single_element(self):
        """List with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Empty list should return None."""
        self.assertIsNone(max_integer([]))

    def test_identical_values(self):
        """List where all values are the same."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        """List containing floats."""
        self.assertEqual(max_integer([1.5, 3.2, 2.0]), 3.2)

    def test_none_argument(self):
        """Passing None should raise a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()