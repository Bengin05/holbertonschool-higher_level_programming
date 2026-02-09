#!/usr/bin/python3
"""Module for reading and printing a UTF-8 text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout."""
    read_data = ""
    with open(filename, 'r', encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end='')
