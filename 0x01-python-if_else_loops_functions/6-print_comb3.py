#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(num1, 10):
        if num1 == 9 and num2 == 9:
            print('{}{}'.format(num1, num2))
        else:
            print('{}{}'.format(num1, num2), end=', ')
