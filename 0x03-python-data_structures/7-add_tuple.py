#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    dup_tup_a = tuple_a + (0, 0)
    dup_tup_b = tuple_b + (0, 0)
    tuple_c = (dup_tup_a[0] + dup_tup_b[0], dup_tup_a[1] + dup_tup_b[1])
    return tuple_c
