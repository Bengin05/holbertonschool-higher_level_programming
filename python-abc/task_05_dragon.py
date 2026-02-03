#!/usr/bin/python3
"""Provide mixins for swim/fly behaviors and a Dragon using them."""


class SwimMixin:
    """Mixin that adds swimming behavior."""

    def swim(self):
        """Print a swim message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""

    def fly(self):
        """Print a fly message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon that can swim and fly via mixins."""

    def roar(self):
        """Print a roar message."""
        print("The dragon roars!")
