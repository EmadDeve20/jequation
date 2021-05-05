#!/bin/env python3

"""
This is a Demo module for solving Diophantine equations
"""
import math

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

def taxicab_number(num: int) -> float:
    """The smallest nontrivial solution in positive integers is 123 + 13 = 93 + 103 = 1729.
    It was famously given as an evident property of 1729,
    a taxicab number (also named Hardy–Ramanujan number) by Ramanujan to Hardy while
    meeting in 1917
    There are infinitely many nontrivial solutions.
    https://en.wikipedia.org/wiki/Taxicab_number
    """
    #TODO: this code need good comments
    count, iter_num = 0, 1
    while count < num:
        iter_num += 1
        int_count = 0
        for num_one in range(1, math.ceil(pow(iter_num, 1.0 / 3)) + 1):
            for num_two in range(num_one+1, math.ceil(pow(iter_num, 1.0 / 3)) + 1):
                if num_one**3 + num_two**3 == iter_num:
                    int_count += 1
        if int_count == 2:
            count += 1
        

    return iter_num

def pythagorean_triple():
    """
    For n = 2 there are infinitely many solutions (x, y, z): the Pythagorean triples.
    For larger integer values of n, Fermat's Last Theorem
    (initially claimed in 1637 by Fermat and proved by Andrew Wiles in 1995)
    states there are no positive integer solutions (x, y, z).
    https://en.wikipedia.org/wiki/Pythagorean_triple
    """
    pass

if __name__ == "__main__":
    from doctest import testmod
    testmod(name="linear_with_one_unknown", verbose=True)
    testmod(name="linear_with_tow_unknown", verbose=True)
