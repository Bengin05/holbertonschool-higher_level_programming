#!/usr/bin/python3
"""Define an abstract Shape and concrete Circle/Rectangle classes."""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes with area and perimeter."""

    @abstractmethod
    def area(self):
        """Return the shape area as a float."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the shape perimeter as a float."""
        pass


class Circle(Shape):
    """Circle shape defined by its radius."""

    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the circle area."""
        return pi * self.radius * self.radius

    def perimeter(self):
        """Return the circle perimeter."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle shape defined by width and height."""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter."""
        return (self.width * self.height) * 2


def shape_info(object):
    """Print area and perimeter for a shape-like object."""
    print("Area:", object.area())
    print("Perimeter:", object.perimeter())
