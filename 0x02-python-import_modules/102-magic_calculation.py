#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for q in range(4, 6):
            c = add(c, q)
            return (c)
        else:
            return sub(a, b)
