#!/usr/bin/python3
"""Module defining a Student class with JSON-like serialization."""


class Student:
    """Represent a student with basic identifying information."""
    def __init__(self, first_name, last_name, age):
        """Initialize a Student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the student."""
        return self.__dict__
