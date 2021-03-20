#!/bin/env python3

"""
I used the Persian names of alliances for all functions
"""

import re


def is_two_square(phrase: str) -> bool:
    """this function for check your phrase is is two-sentence square or not
        >>> import is_two_square
        >>> is_two_square("(a+b)(a+b)")
        True
        >>> is_two_square("(a+b)(a+c)")
        False
    """
    # (a -|+ b)(b -|+ a) and and any more like this is True for this function
    def a_and_b(phrase: str) -> bool:
        # phrase = "(a+b)(a+b)"
        phrase = phrase.replace("(", "")
        # pharse = "a+b)a+b)"
        phrase = phrase.replace(")", "")
        # pharse = "a+ba+b"

        ok_style = phrase.count(phrase[0]) == 2 and phrase.count(phrase[2]) == 2
        if ok_style and phrase[0] != phrase[2]:
            return True
        return False

    check = re.match(r"\(.+\+.+\)\(.+\+.+\)", phrase)
    if not check is None and check.end() == len(phrase) and a_and_b(phrase):
        return True
    check = re.match(r"\(.+-.+\)\(.+-.+\)", phrase)
    if not check is None and check.end() == len(phrase) and a_and_b(phrase):
        return True

    check = re.match(r"\(.+\+.+\)\^2", phrase)
    if not check is None and check.end() == len(phrase):
        return True
    check = re.match(r"\(.+-.+\)\^2", phrase)
    if not check is None and check.end == len(phrase):
        return True
    return False

def is_married(phrase: str) -> bool:
    """this function for check your phrase is married or not
        >>> import is_married
        >>> is_married('(a+b)(a-b)')
        True
        >>> is_married('(a+b)(a+b)')
        False
        >>> is_married('(a-b)(b+a)')
        True
    """
    # (a + b)(b - a) and and any more like this is True for this function
    def a_and_b(phrase: str) -> bool:
        # phrase = "(a+b)(a-b)"
        phrase = phrase.replace("(", "")
        # pharse = "a+b)a-b)"
        phrase = phrase.replace(")", "")
        # pharse = "a+ba-b"

        ok_style = phrase.count(phrase[0]) == 2 and phrase.count(phrase[2]) == 2
        if ok_style and phrase[0] != phrase[2]:
            return True
        return False

    check = re.match(r"\(.+-.+\)\(.+\+.+\)", phrase)
    if (not check is None and check.end()) == len(phrase) and a_and_b(phrase):
        return True
    check = re.match(r"\(.+\+.+\)\(.+-.+\)", phrase)
    if (not check is None and check.end()) == len(phrase) and a_and_b(phrase):
        return True
    return False

#def is_threesentence_square(phrase: str) -> bool:

def is_twosentence_cube(phrase: str) -> bool:
    """demo"""
    def a_and_b(phrase: str) -> bool:
        # phrase = "(a+b)(a+b)"
        phrase = phrase.replace("(", "")
        # pharse = "a+b)a+b)"
        phrase = phrase.replace(")", "")
        # pharse = "a+ba+b"

        ok_style = phrase.count(phrase[0]) == 3 and phrase.count(phrase[2]) == 3
        if ok_style and phrase[0] != phrase[2]:
            return True
        return False
    check = re.match(r"\(.+\+.+\)\(.+\+.+\)\(.+\+.+\)", phrase)
    if (not check is None and check.end() == len(phrase)) and a_and_b(phrase):
        return True
    check = re.match(r"\(.+-.+\)\(.+-.+\)\(.+-.+\)", phrase)
    if (not check is None and check.end() == len(phrase)) and a_and_b(phrase):
        return True
    check = re.match(r"\(.+\+.+\)\^3", phrase)
    if (not check is None) and check.end() == len(phrase):
        return True
    check = re.match(r"\(.+-.+\)\^3", phrase)
    if (not check is None) and check.end() == len(phrase):
        return True
    return False

#def is_fat_and_thin(phrase: str) ->bool:
#def is_common_sentence(phrase: str) -> bool:
#def is_newtons_binomial_expansion_sentence(phrase: str) -> bool:
#def is_lagrange_alliance(phrase: str) -> bool:
#def is_euler_alliance(phrase: str) -> bool:
