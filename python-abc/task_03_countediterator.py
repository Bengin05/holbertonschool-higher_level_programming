#!/usr/bin/python3
"""Provide a counted iterator that tracks items returned by next()."""


class CountedIterator:
    """Iterator wrapper that counts how many items were produced."""

    def __init__(self, iterable):
        self.it = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items successfully iterated."""
        return self.count

    def __next__(self):
        """Return the next item and increment the counter."""
        value = next(self.it)
        self.count += 1
        return value

    def __iter__(self):
        """Return self to make this object an iterator."""
        return self
