#!/usr/bin/python3
"""Module that defines an BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry is a base class for geometry-related objects."""

    def area(self):
        """Raise an Exception if that the area method isnt implemented."""
        raise Exception("area() is not implemented")
