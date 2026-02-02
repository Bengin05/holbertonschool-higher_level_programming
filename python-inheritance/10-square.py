#!/usr/bin/python3
"""Module that defines a Rectangle class that inherits from BaseGeometry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square is a rectangle with equal sides."""

    def __init__(self, size):
        """Initialize a Square after validating size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
