#!/usr/bin/python3
def uniq_add(my_list=[]):

    unique_value = set(my_list)
    total = 0
    for number in unique_value:
        total += number

    return total
