#!/usr/bin/python3
def multiple_returns(sentence):

    first = ""

    if sentence == "":
        sentence = None
    else:
        first = sentence[0]

    length = len(sentence)
    return (sentence, first)
