#!/usr/bin/python3
"""Module for print_square.
This module defines the function print_square(size)
that prints a square made of '#' characters.
"""


def print_square(size):
    """Print a square with the character '#'.
    Args:
        size: the size of the square (number of rows and columns).
    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
    """
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
