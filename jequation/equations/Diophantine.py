#!/bin/env python3



def linear(number_a: int, number_b: int, number_c: int = 0,target: str = "") -> int:
    """this function for linear

        |ax+by=c|
        get number of a and number of b and return anwser
        return x,y
    """

    if target == "":
        if number_c == 0:
            return -number_b/number_a, -number_a/number_b
        else:
            return (number_c - number_b) / number_a,(-number_c + number_b) / -number_a
    elif target == "X" or target == "x":
        if number_c == 0:
            return -number_b/number_a
        else:
            return (number_c - number_b) / number_a
    elif target == "Y" or target == "y":
        if number_c == 0:
            -number_a/number_b
        else:
            (-number_c + number_b) / -number_a

def linear_with_tow(number_of_x_one: int, number_one: int, number_of_x_two: int, number_two: int):
    """this function can solve linear equation with tow X"""
    result = (number_of_x_one - number_of_x_two) / (number_one - number_two)
    return result

