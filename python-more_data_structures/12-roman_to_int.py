#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None or type(roman_string) is not str:
        return 0

    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(roman_string)):
        value = rom_val[roman_string[i]]

        if i < len(roman_string) - 1 and value < rom_val[roman_string[i + 1]]:
            total -= value
        else:
            total += value

    return total
