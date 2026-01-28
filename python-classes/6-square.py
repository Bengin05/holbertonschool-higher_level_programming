#!/usr/bin/python3
"""This module defines the Square class for printing squares."""


class Square:
    """Represents a square with a validated private size attribute."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with an optional size.
        Args:
            size (int): The size of the square. Must be an integer >= 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with type/value validation."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' characters and space."""
        if self.size == 0:
            print()
        else:
            lign = " " * self.__position[0] + "#" * self.__size
            for number in range(self.__position[1]):
                print()
            for row in range(self.__size):
                print(lign)
