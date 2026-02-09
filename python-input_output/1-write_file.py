#!/usr/bin/python3
"""Module for writing and overriting a UTF-8 text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 file and return char count."""
    with open(filename, 'w', encoding="utf-8") as file:
        write_data = file.write(text)
        return write_data
