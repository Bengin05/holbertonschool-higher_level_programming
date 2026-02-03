#!/usr/bin/python3
"""Define Fish, Bird and FlyingFish to demonstrate multiple inheritance."""


class Fish:
    """Fish with swimming behavior and a water habitat."""

    def swim(self):
        """Print a swimming message for a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat message for a fish."""
        print("The fish lives in water")


class Bird:
    """Bird with flying behavior and a sky habitat."""

    def fly(self):
        """Bird with flying behavior and a sky habitat."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat message for a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Flying fish combining Fish and Bird behaviors."""

    def fly(self):
        """Print a flying message for a flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a swimming message for a flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the habitat message for a flying fish."""
        print("The flying fish lives both in water and the sky!")
