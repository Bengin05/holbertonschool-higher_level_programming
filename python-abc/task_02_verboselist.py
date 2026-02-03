#!/usr/bin/python3
"""Verbose list that prints messages on add/remove operations."""


from abc import ABC, abstractmethod


class VerboseList(list):
    """List subclass that prints notifications on mutations."""

    def append(self, item):
        """Append an item and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extend the list and print how many items were added."""
        super().extend(x)
        print("Extended the list with [{}] items.".format(len(x)))

    def remove(self, item):
        """Remove an item and print a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, item=None):
        """Pop an item by index and print a notification."""
        if item is None:
            removed = super().pop()
        else:
            removed = super().pop(item)

        print("Popped [{}] from the list.".format(removed))
        return removed
