#!/usr/bin/python3
"""This module defines the Square class for basic OOP practice."""
class Square:
    """Represents a square with a private size attribute."""
    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square (no type/value check here).
        """
        self.__size = size
