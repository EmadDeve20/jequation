#!/bin/env python3



class Diophantine:
    """This class for solving Diophantine equation"""
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
                
        
