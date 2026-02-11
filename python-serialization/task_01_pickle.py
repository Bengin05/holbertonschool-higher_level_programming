#!/usr/bin/python3
"""Pickle serialization helpers for a custom Python object."""
import pickle


class CustomObject:
    """Represent a simple object that can be serialized with pickle."""

    def __init__(self, name, age, is_student):
        """Initialize name, age and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object attributes using the required output format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize this instance to a pickle file or return None on error."""
        try:
            with open(filename, "wb") as file_obj:
                pickle.dump(self, file_obj)
        except (OSError, pickle.PicklingError):
            return None
        return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a pickle file into an instance or return None."""
        try:
            with open(filename, "rb") as file_obj:
                obj = pickle.load(file_obj)
        except (FileNotFoundError, OSError, pickle.UnpicklingError, EOFError):
            return None
        if not isinstance(obj, cls):
            return None
        return obj
