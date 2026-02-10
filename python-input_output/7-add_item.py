#!/usr/bin/python3
"""Script that stores args in a JSON list (add_item.json)."""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Load list, append CLI args, and save back to add_item.json."""
    filename = "add_item.json"
    args = sys.argv[1:]

    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(args)
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
