#!/usr/bin/python3
"""Define an abstract Animal and concrete Dog/Cat implementations."""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals with a required sound method."""

    @abstractmethod
    def sound(self):
        """Return the animal sound as a string."""
        pass


class Dog(Animal):
    """Concrete Animal that barks."""
    def sound(self):
        """Return the dog sound."""
        return "Bark"


class Cat(Animal):
    """Concrete Animal that meows."""
    def sound(self):
        """Return the cat sound."""
        return "Meow"
