#!/usr/bin/python3
def best_score(a_dictionary):
    best_value = 0
    best_key = None

    if not a_dictionary:
        return None

    for key in a_dictionary:
        value = a_dictionary[key]

        if best_value is None or value > best_value:
            best_value = value
            best_key = key
    return best_key
