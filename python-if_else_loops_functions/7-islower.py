#!/usr/bin/python3
def islower(c):
    char = ord(c)
    if char >= ord('a') and char <= ord('z'):
        return True
    else:
        return False
