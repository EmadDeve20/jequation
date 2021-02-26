#!/bin/env python3

"""
This is Demo module for solving Diophantine equations
"""


def linear(number_a: int, number_b: int, number_c: int = 0, target: str = "") -> int:
    """this function for linear

        |ax+by=c|
        get number of a and number of b and return anwser
        return x,y
    """

    awnser = 0
    if target in ('', 'x,y', 'X,y', 'X,Y', 'x,Y'):
        if number_c == 0:
            awnser = -number_b/number_a, -number_a/number_b
        else:
            awnser = (number_c - number_b) / number_a, (-number_c + number_b) / -number_a
    elif target in ("X", "x"):
        if number_c == 0:
            awnser = -number_b/number_a
        else:
            awnser = (number_c - number_b) / number_a
    elif target in ("Y", "y"):
        if number_c == 0:
            awnser = -number_a/number_b
        else:
            awnser = (-number_c + number_b) / -number_a

    return awnser


def linear_with_tow(number_of_x_one: int, number_one: int, number_of_x_two: int, number_two: int):
    """this function can solve linear equation with tow X"""
    result = (number_of_x_one - number_of_x_two) / (number_one - number_two)
    return result
