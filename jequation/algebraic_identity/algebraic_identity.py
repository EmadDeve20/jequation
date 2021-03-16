#!/bin/env python3

"""
I used the Persian names of alliances for all functions
"""

import re

def Twosentence_square(phrase: str) -> bool:
    """this function for check your phrase is binomial or not"""
    if len(phrase) == 10:
        check = re.match(r"\(.+.\)\(.+.\)", phrase)
        if check.end() == len(phrase):
            return True
        check = re.match(r"\(.-.\)\(.-.\)", phrase)
        if check.end() == len(phrase):
            return True
    return False

def is_married(phrase: str) -> bool:
    """this function for check your phrase is married or not"""
    if len(phrase) == 10:
        check = re.match(r"\(.-.\)\(.+.\)", phrase)
        if check.end() == len(phrase):
            return True
        check = re.match(r"\(.+.\)\(.-.\)", phrase)
        if check.end() == len(phrase):
            return True
    return False

def is_Threesentence_square(phrase: str) -> bool:
    pass

def is_Twosentence_cube(phrase: str) -> bool:
    pass

def is_fat_and_thin(phrase: str) ->bool:
    pass

def is_Common_sentence(phrase: str) -> bool:
    pass

def is_Newtons_binomial_expansion_sentence(phrase: str) -> bool:
    pass

def is_lagrange_alliance(phrase: str) -> bool:
    pass

def is_euler_alliance(phrase: str) -> bool:
    pass
