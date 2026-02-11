#!/usr/bin/python3
"""Convert CSV rows into JSON using the standard library."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and write it to data.json."""
    json_file = "data.json"

    try:
        with open(csv_filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = []
            for row in reader:
                rows.append(row)

        with open(json_file, "w", encoding="utf-8") as j_file:
            json.dump(rows, j_file, indent=4, ensure_ascii=False)

        return True

    except (FileNotFoundError, OSError):
        return False
