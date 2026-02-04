#!/usr/bin/python3
"""This module defines MyList, a list subclass with a sorted display method."""


class MyList(list):
    """This class extends list and can print its elements in sorted order."""

    def print_sorted(self):
        """This method prints list in ascending order without changing it."""
        print(sorted(self))
