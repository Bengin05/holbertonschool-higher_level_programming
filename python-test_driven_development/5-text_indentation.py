#!/usr/bin/python3
"""Module for text_indentation.
Defines the function text_indentation(text) that prints a text
with two new lines after each '.', '?' or ':' character, without
leading or trailing spaces on each printed line.
"""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'.
    Args:
        text (str): The text to process.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    at_line_start = True

    for ch in text:
        if at_line_start and ch == " ":
            continue

        line += ch
        at_line_start = False

        if ch in ".?:":
            print(line.rstrip(" "))
            print()
            line = ""
            at_line_start = True

    line = line.strip(" ")
    if line != "":
        print(line, end="")
