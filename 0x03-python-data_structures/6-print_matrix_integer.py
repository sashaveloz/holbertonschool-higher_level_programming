#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range(len(row)):
            if col < 2:
                print("{:d}".format(row[col]), end=' ')
            else:
                print("{:d}".format(row[col]), end='')
        print()
