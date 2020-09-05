#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    for idx in argv[1:]:
        add += int(idx)
    print(add)
