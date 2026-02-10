#!/usr/bin/python3
"""Module for converting an object to a JSON-serializable dict."""


def class_to_json(obj):
    """Return a JSON-serializable dict description of an object."""
    return obj.__dict__
