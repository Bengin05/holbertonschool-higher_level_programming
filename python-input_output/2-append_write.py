#!/usr/bin/python3
"""Module for appending text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 file and return char count."""
    with open(filename, 'a', encoding="utf-8") as file:
        append_data = file.write(text)
        return (append_data)
