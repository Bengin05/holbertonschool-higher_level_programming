#!/usr/bin/python3
"""
Task 0: Creating a Simple Templating Program
"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template with placeholders
    and a list of objects.
    
    Args:
        template: A string containing the invitation template with placeholders
        attendees: A list of dictionaries containing attendee information
    """
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template or template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Attendees must be a list of dictionaries.")
            return

    for index, attendee in enumerate(attendees, start=1):
        content = template

        import re
        placeholders = re.findall(r'\{(\w+)\}', template)

        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None or (isinstance(value, str) and value.strip() == ""):
                replacement = "N/A"
            else:
                replacement = str(value)
            content = content.replace("{" + placeholder + "}", replacement)
        
        filename = f"output_{index}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except IOError as e:
            print(f"Error: Could not write to file {filename}. {e}")
            continue
