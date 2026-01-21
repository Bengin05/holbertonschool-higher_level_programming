#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_after = len(my_list) - 1
    for i in range(list_after, -1, -1):
        print("{:d}".format(my_list[i]))
