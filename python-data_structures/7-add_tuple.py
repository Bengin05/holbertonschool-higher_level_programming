#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 0:
        a = 0
        a1 = 0

    elif len(tuple_a) == 1:
        a0 = tuple_a[0]
        a1 = 0

    else:
        a0 = tuple_a[0]
        a1 = tuple_a[1]

    if len(tuple_b) == 0:
        b = 0
        b1 = 0

    elif len(tuple_b) == 1:
        b0 = tuple_b[0]
        b1 = 0

    else:
        b0 = tuple_b[0]
        b1 = tuple_b[1]

    result0 = a0 + b0
    result1 = a1 + b1
    return (result0, result1)
