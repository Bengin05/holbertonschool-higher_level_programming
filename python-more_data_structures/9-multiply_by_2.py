#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    new_value = 0

    for key in a_dictionary:
        value = a_dictionary[key]
        new_value = value * 2
        new_dict[key] = new_value

    return new_dict
