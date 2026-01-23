#!/usr/bin/python3
"""Module for add_integer.
Defines one function add_integer(a, b=98).
Adds two integers or floats, casting floats to ints.
Raises a TypeError if either argument is not
an integer or a float.
"""


def add_integer(a, b=98):
    """Add two integers or floats.

    Floats are cast to ints before addition.
    Raise TypeError if a or b is not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
