#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    narg = len(argv) - 1
    args = "argument" if narg == 1 else "arguments"
    if narg == 0:
        print('{} {}.'.format(narg, args))
    else:
        print('{} {}:'.format(narg, args))
    for idx, arg in enumerate(argv):
        if idx != 0:
            print('{}: {}'.format(idx, arg))
