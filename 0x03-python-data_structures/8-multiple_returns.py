#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuple_a = (len(sentence), sentence[0])
        return tuple_a
    else:
        tuple_none = (0, None)
        return tuple_none
