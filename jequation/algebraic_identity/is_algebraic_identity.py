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
        phrase = phrase.replace("(", "", 1)
        # phrase = "a+b)(a+b)"
        phrase = phrase.replace(")", " ", 1)
        # phrase = "a+b (a+b)"
        phrase = phrase.replace("(", "")
        # phrase = "a+b a+b)"
        phrase = phrase.replace(")", "")

        # phrase = "a+b a+b"
        if phrase.find("+") != -1:
            phrase = phrase.replace("+", " ")
        elif phrase.find("-") != -1:
            phrase = phrase.replace("-", " ")
        # phrase = "a b a b"
        phrase = phrase.split(" ")
        # phrase = "['a', 'b', 'a', 'b']"

        for j in range(2):
            for i in range(2,4):
                if (len(phrase[j]) == len(phrase[i]) and phrase[i][0] in phrase[j]) and\
                   (not phrase[j].isdigit() and not "." in phrase[j]):
                    number_of_match = 0
                    for p in phrase[i]:
                        if p in phrase[j]:
                            number_of_match += 1
                    if number_of_match == len(phrase[j]):
                        phrase[i] = phrase[j]
        ok_style = (phrase.count(phrase[0]) == 2 and phrase.count(phrase[1]) == 2) or\
            phrase.count(phrase[0]) == 4
        if ok_style:
            return True
        return False

    check = re.match(r"\(.+(\+|-).+\)\(.+(\+|-).+\)", phrase)
    
    if (check and check.group(1) == check.group(2)) and a_and_b(check.string):
        return True

    check = re.match(r"\(.+(\+|-).+\)\^2", phrase)
    if check and check.end() == len(phrase):
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
        phrase = phrase.replace("(", "", 1)
        # phrase = "a+b)(a-b)"
        phrase = phrase.replace(")", " ", 1)
        # phrase = "a+b (a-b)"
        phrase = phrase.replace("(", "")
        # phrase = "a+b a-b)"
        phrase = phrase.replace(")", "")

        # phrase = "a+b a-b"
        phrase = phrase.replace("+", " ")
        # phrase = "a b a-b"
        phrase = phrase.replace("-", " ")
        # phrase = "a b a b"
        phrase = phrase.split(" ")
        # phrase = "['a', 'b', 'a', 'b']"

        for j in range(2):
            for i in range(2,4):
                if (len(phrase[j]) == len(phrase[i]) and phrase[i][0] in phrase[j]) and\
                   (not phrase[j].isdigit() and not "." in phrase[j]):
                    number_of_match = 0
                    for p in phrase[i]:
                        if p in phrase[j]:
                            number_of_match += 1
                    if number_of_match == len(phrase[j]):
                        phrase[i] = phrase[j]
        ok_style = (phrase.count(phrase[0]) == 2 and phrase.count(phrase[1]) == 2) or\
            phrase.count(phrase[0]) == 4
        if ok_style:
            return True
        return False

    check = re.match(r"\(.+(-|\+).+\)\(.+(\+|-).+\)", phrase)
    if (check and check.group(1) != check.group(2)) and a_and_b(check.string):
        return True
    return False

#def is_threesentence_square(phrase: str) -> bool:

def is_two_cube(phrase: str) -> bool:
    """this is a function for check your phrase is two-sentence cube or not
    >>> import is_two_cube
    >>> is_two_cube("(a+b)^3")
    True
    >>> is_two_cube("(a+b)^4")
    False
    >>> is_two_cube("(a+b)(a+b)(a+b)")
    True
    """
    def a_and_b(phrase: str) -> bool:
        # phrase = "(a+b)(a+b)(a+b)"
        phrase = phrase.replace("(", "", 2)
        # phrase = "a+b)a+b)(a+b)"
        phrase = phrase.replace(")", " ", 2)
        # phrase = "a+b a+b (a+b)"
        phrase = phrase.replace("(", "")
        # phrase = "a+b a+b a+b)"
        phrase = phrase.replace(")", "")

        # phrase = "a+b a+b a+b"
        if phrase.find("+") != -1:
            phrase = phrase.replace("+", " ")
        elif phrase.find("-") != -1:
            phrase = phrase.replace("-", " ")
        # phrase = "a b a b a b"
        phrase = phrase.split(" ")
        # phrase = "['a', 'b', 'a', 'b', 'a', 'b']"

        for j in range(2):
            for i in range(2,6):
                if (len(phrase[j]) == len(phrase[i]) and phrase[i][0] in phrase[j]) and\
                   (not phrase[j].isdigit() and not "." in phrase[j]):
                    number_of_match = 0
                    for p in phrase[i]:
                        if p in phrase[j]:
                            number_of_match += 1
                    if number_of_match == len(phrase[j]):
                        phrase[i] = phrase[j]

        ok_style = (phrase.count(phrase[0]) == 3 and phrase.count(phrase[1]) == 3) or\
            phrase.count(phrase[0]) == 6
        if ok_style:
            return True
        return False

    check = re.match(r"\(.+(\+|-).+\)\(.+(\+|-).+\)\(.+(\+|-).+\)", phrase)
    if (check and check.group(1) == check.group(2) == check.group(3)) and a_and_b(check.string):
        return True
    check = re.match(r"\(.+\+.+\)\^3", phrase)
    if (not check is None) and check.end() == len(phrase):
        return True
    check = re.match(r"\(.+-.+\)\^3", phrase)
    if (not check is None) and check.end() == len(phrase):
        return True
    return False

def is_fat_thin(phrase: str) -> bool:
    """
    this is a function to check your phrase is fat and thin or not
    >>> import is_fat_thin
    >>> is_fat_thin("(2+4)(4-8+16)")
    True
    >>> is_fat_thin("(a+b)(a^2-ab+b^2)")
    True
    >>> is_fat_thin("(a-b)(a^2+ab-b^2)")
    False
    """

    # this (2+4)(4-8+16) or this (2-4)(4-8+16) is True
    check = re.match(r"\((.+)(\+|-)(.+)\)\((.+)(-|\+)(.+)\+(.+)\)", phrase)
    if check:
        print(check.string)
        return True

    # this (2-4)(4-8+16) or this (2+4)(4-8+16) is True
    check = re.match(r"\((.+)(-|\+)(.+)\+(.+)\)\((.+)(\+|-)(.+)\)", phrase)
    if check:
        print(check.string)
        return True

    print("Hi")
    return False

def is_common_sentence(phrase: str) -> bool:
    """This fucntion for checking your phrase is common sentence or not
        >>> import is_common_sentence
        >>> is_common_sentence("(x+a)(x+b)")
        True
        >>> is_common_sentence("(x+a)(x+a)")
    """
    # this Function for checking you phrase has one subscriber or no
    def one_subscribe(phrase: str):
        # phrase = "(x+a)(x+b)"
        phrase = phrase.replace("(", "", 1)
        # phrase = "x+a)(x+b)"
        phrase = phrase.replace(")", " ", 1)
        # phrase = "x+a (x+b)"
        phrase = phrase.replace("(", "")
        # phrase = "x+a x+b)"
        phrase = phrase.replace(")", "")

        # phrase = "x+a x+b"
        if phrase.find("+") != -1:
            phrase = phrase.replace("+", " ")
        elif phrase.find("-") != -1:
            phrase = phrase.replace("-", " ")
        # phrase = "a b a b"
        phrase = phrase.split(" ")
        # phrase = "['a', 'b', 'a', 'b']"

        for j in range(2):
            for i in range(2,4):
                if (len(phrase[j]) == len(phrase[i]) and phrase[i][0] in phrase[j]) and\
                   (not phrase[j].isdigit() and not "." in phrase[j]):
                    number_of_match = 0
                    for p in phrase[i]:
                        if p in phrase[j]:
                            number_of_match += 1
                    if number_of_match == len(phrase[j]):
                        phrase[i] = phrase[j]
        ok_style = phrase.count(phrase[0]) == 2 or phrase.count(phrase[1]) == 2 
        if ok_style:
            return True
        return False

    check = re.match(r"\(.+(\+|-).+\)\(.+(\+|-).+\)", phrase)
    if (check and check.group(1) == check.group(2)) and one_subscribe(check.string):
        return True
    return False


def is_newtons_binomial_expansion_sentence(phrase: str) -> bool:
    def ok_style(phrase: str):
        if phrase.count("+") != 0 and phrase.count("-") != 0 \
            or (phrase.count("(") != phrase.count("-") and phrase.count("(") != phrase.count("+")):
            return False
        phrase = phrase.replace("(", "")
        phrase = phrase.replace(")", " ", phrase.count(")")-1)
        phrase = phrase.replace(")", "")
        phrase = phrase.replace("+", " ")
        phrase = phrase.split(" ")
        for j in range(2):
            for i in range(2,len(phrase)):
                if (len(phrase[j]) == len(phrase[i]) and phrase[i][0] in phrase[j]) and\
                   (not phrase[j].isdigit() and not "." in phrase[j]):
                    number_of_match = 0
                    for p in phrase[i]:
                        if p in phrase[j]:
                            number_of_match += 1
                    if number_of_match == len(phrase[j]):
                        phrase[i] = phrase[j]
        ok_style = phrase.count(phrase[0]) == len(phrase)/2 and phrase.count(phrase[1]) == len(phrase)/2 
        if ok_style:
            return True
        return False

    check = re.match(r"\(.+(\+|-).+\)\^.+", phrase)
    if not check is None and check.end() == len(phrase):
        return True

    check = re.match(r"\(.+(\+|-).+\)", phrase)
    if check.end() == len(phrase):
        if ok_style(check.string):
            return True

    return False

def is_lagrange_alliance(phrase: str) -> bool:
    check = re.match(r"\((.+)(\^.+)\+(.+)(\^.+)\)\((.+)(\^.+)\+(.+)(\^.+)\)", phrase)
    ok_style = not check is None and\
            (check.group(1) != check.group(3) and check.group(5) != check.group(8))
    if ok_style:
        return True
    return False
#def is_euler_alliance(phrase: str) -> bool: