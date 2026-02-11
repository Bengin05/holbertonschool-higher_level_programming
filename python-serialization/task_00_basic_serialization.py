#!/usr/bin/python3
"""Serialize a dict to JSON and load it back from a file."""
import json


def serialize_and_save_to_file(data, filename):
    """Save a Python dictionary to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and return its content as a Python dictionary."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
