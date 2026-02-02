#!/usr/bin/python3
"""Module that defines MyList, a list subclass with a sorted print method."""


class MyList(list):
    """MyList is a list subclass can print elements in sorted order."""

    def print_sorted(self):
        """Print list in ascending order without modifying the original list"""
        print(sorted(self))
