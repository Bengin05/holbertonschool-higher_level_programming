#!/usr/bin/python3
"""Module that defines BaseGeometry with area and int validation methods."""


class BaseGeometry:
    """Base class for geometry objects with validation helpers."""

    def area(self):
        """Raise an Exception if that the area method isnt implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
