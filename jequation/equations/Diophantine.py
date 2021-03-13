#!/bin/env python3

"""
This is a Demo module for solving Diophantine equations
"""

def linear_with_one_unknown\
    (number_a: int, number_b: int, number_c: int = 0, target: str = "") -> int:
    """this function for linear

        |ax+by=c|
        get number of a and number of b and return answer
        return x,y
    """

    answer = 0
    if target in ('', 'x,y', 'X,y', 'X,Y', 'x,Y'):
        if number_c == 0:
            answer = -number_b/number_a, -number_a/number_b
        else:
            answer = (number_c - number_b) / number_a, (-number_c + number_b) / -number_a
    elif target in ("X", "x"):
        if number_c == 0:
            answer = -number_b/number_a
        else:
            answer = (number_c - number_b) / number_a
    elif target in ("Y", "y"):
        if number_c == 0:
            answer = -number_a/number_b
        else:
            answer = (-number_c + number_b) / -number_a

    return answer


def linear_with_tow_unknown\
        (number_of_x_one: int, number_one: int, number_of_x_two: int, number_two: int):
    """This function can solve a linear equation with two expressions(unknown)

       -----------------
       |ax1+b1 = ax2+b2|
       -----------------"""
    result = (number_of_x_one - number_of_x_two) / (number_one - number_two)
    return result

if __name__ == "__main__":
    from doctest import testmod
    testmod(name="linear_with_one_unknown", verbose=True)
    testmod(name="linear_with_tow_unknown", verbose=True)
