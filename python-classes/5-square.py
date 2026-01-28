#!/usr/bin/python3
"""This module defines the Square class for printing squares."""


class Square:
    """Represents a square with a validated private size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square with an optional size.

        Args:
            size (int): The size of the square. Must be an integer >= 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type/value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' characters."""
        if self.size == 0:
            print()
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
