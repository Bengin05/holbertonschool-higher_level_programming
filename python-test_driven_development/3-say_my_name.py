#!/usr/bin/python3
"""Module for say_my_name.

This module defines the function say_my_name(first_name, last_name="")
that prints the string "My name is <first name> <last name>".
Both arguments must be strings, otherwise a TypeError is raised.
"""


def say_my_name(first_name, last_name=""):
    """Print "My name is <first name> <last name>".

    Args:
        first_name: first name, must be a string.
        last_name: last name, must be a string (can be empty).
    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
