#!/usr/bin/python3
"""This module defines an abstract Shape interface and concrete shapes."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """This class defines the common interface that all shapes must provide."""

    @abstractmethod
    def area(self):
        """This method returns the area of the current shape instance."""
        pass

    @abstractmethod
    def perimeter(self):
        """This method returns the perimeter of the current shape instance."""
        pass


class Circle(Shape):
    """This class represents a circle and stores its radius."""

    def __init__(self, radius):
        """This method initializes a circle using the given radius value."""
        self.radius = radius

    def area(self):
        """This method returns the area computed from the circle radius."""
        return pi * self.radius * self.radius

    def perimeter(self):
        """This method return the perimeter computed from the circle radius."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """This class represents a rectangle using width and height values."""

    def __init__(self, width, height):
        """This method initialize a rectangle using width and height values."""
        self.width = width
        self.height = height

    def area(self):
        """This method returns the area computed from width and height."""
        return self.width * self.height

    def perimeter(self):
        """This method returns the perimeter computed from width and height."""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Print area and perimeter for a shape-like object."""
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
