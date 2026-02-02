#!/usr/bin/python3
"""Module that provides a function to list an object's available attributes"""


def lookup(obj):
    """Return a list of available attributes and methods of an object"""
    return dir(obj)
