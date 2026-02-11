#!/usr/bin/python3
"""Serialize and deserialize dictionaries using XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Write a dictionary to an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Read an XML file and return a dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
    except (FileNotFoundError, OSError):
        return None

    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
