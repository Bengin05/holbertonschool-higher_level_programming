#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        total = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        total = None
    finally:
        print("Inside result: {}".format(total))
        return total
