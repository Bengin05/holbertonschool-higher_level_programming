#!/usr/bin/python3
def multiple_returns(sentence):
    first = ""

    if sentence == "":
        first = None
    else:
        first = sentence[0]

    lenght = len(sentence)
    return (lenght, first)
