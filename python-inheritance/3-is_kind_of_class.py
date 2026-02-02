#!/usr/bin/python3
"""Module that provides a function to check class membership and inheritance"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of class or a subclass, else False"""
    return isinstance(obj, a_class)
