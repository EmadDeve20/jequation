#!/bin/env python3

"""
I used the Persian names of alliances for all functions
"""

import re


def is_twosentence_square(phrase: str) -> bool:
    """this function for check your phrase is binomial or not"""
    # (a -|+ b)(b -|+ a) and and any more like this is True for this function
    def a_and_b(phrase: str) -> bool:
        # phrase = "(a+b)(a+b)"
        phrase = phrase.replace("(", "")
        # pharse = "a+b)a+b)"
        phrase = phrase.replace(")", "")
        # pharse = "a+ba+b"
        if phrase.find("+") != -1:
            phrase = phrase.split("+")
        elif phrase.find("-") != -1:
            phrase = phrase.split("-")
        # pharse = "[a, ba, b]"

        if (phrase[0] != phrase[2]) and phrase[1] == phrase[2] + phrase[0]:
            return True
        if (phrase[0] == phrase[2]) and \
            (phrase[1][0:int(len(phrase[1])/2)] == \
                phrase[1][int(len(phrase[1])/2):len(phrase[1])]):
            return True
        return False

    check = re.match(r"\(.+\+.+\)\(.+\+.+\)", phrase)
    if check != None and check.end() == len(phrase) and a_and_b(phrase):
        return True
    check = re.match(r"\(.+-.+\)\(.+-.+\)", phrase)
    if check != None and check.end() == len(phrase) and a_and_b(phrase):
        return True

    check = re.match(r"\(.+\+.+\)\^2", phrase)
    if check != None and check.end() == len(phrase):
        return True
    check = re.match(r"\(.+-.+\)\^2", phrase)
    if check != None and check.end == len(phrase):
        return True
    return False

def is_married(phrase: str) -> bool:
    """this function for check your phrase is married or not"""
    # (a + b)(b - a) and and any more like this is True for this function
    def a_and_b(phrase: str) -> bool:
        # phrase = "(a+b)(a-b)"
        phrase = phrase.replace("(", "")
        # pharse = "a+b)a-b)"
        phrase = phrase.replace(")", "")
        # pharse = "a+ba-b"
        phrase = phrase.replace("+", " ")
        # pharse = "a ba-b"
        phrase = phrase.replace("-", " ")
        # pharse = "a ba b"
        phrase = phrase.split(" ")
        # pharse = "[a, ba, b]"

        if (phrase[0] != phrase[2]) and phrase[1] == phrase[2] + phrase[0]:
            return True
        if (phrase[0] == phrase[2]) and \
            (phrase[1][0:int(len(phrase[1])/2)] == \
                phrase[1][int(len(phrase[1])/2):len(phrase[1])]):
            return True
        return False

    check = re.match(r"\(.+-.+\)\(.+\+.+\)", phrase)
    if check != None and check.end() == len(phrase) and a_and_b(phrase):
        return True
    check = re.match(r"\(.+\+.+\)\(.+-.+\)", phrase)
    if check != None and  check.end() == len(phrase) and a_and_b(phrase):
        return True
    return False

def is_threesentence_square(phrase: str) -> bool:
    pass

def is_twosentence_cube(phrase: str) -> bool:
    pass

def is_fat_and_thin(phrase: str) ->bool:
    pass

def is_common_sentence(phrase: str) -> bool:
    pass

def is_newtons_binomial_expansion_sentence(phrase: str) -> bool:
    pass

def is_lagrange_alliance(phrase: str) -> bool:
    pass

def is_euler_alliance(phrase: str) -> bool:
    pass
