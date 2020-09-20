#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for col in range(len(row)):
                if col < 2:
                    print(row[col], end=' ')
                else:
                    print(row[col], end='')
            print()
