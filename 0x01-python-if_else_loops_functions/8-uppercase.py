#!/usr/bin/python3
def uppercase(str):
    for index in str:
        letter = ord(index)
        if (letter > 96 and letter < 123):
            print('{:c}'.format(letter), end='')
