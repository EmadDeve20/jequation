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
            phrase = phrase.replace("+", " ")
        # phrase = "a b a b"
        phrase = phrase.split(" ")
        # phrase = "['a', 'b', 'a', 'b']"

        ok_style = phrase.count(phrase[0]) == 2 and phrase.count(phrase[1]) == 2
        if phrase[0] != phrase[1] and ok_style:
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

        ok_style = phrase.count(phrase[0]) == 2 and phrase.count(phrase[1]) == 2
        if phrase[0] != phrase[1] and ok_style:
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

        ok_style = phrase.count(phrase[0]) == 3 and phrase.count(phrase[1]) == 3
        if phrase[0] != phrase[1] and ok_style:
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

def is_fat_and_thin(phrase: str) -> bool:

    # this (2+4)(4-8+16) or this (2-4)(4-8+16) is True 
    check = re.match(r"\((\d+)(\+|-)(\d+)\)\((\d+)(-|\+)(\d+)\+(\d+)\)", phrase)
    if not check is None:
        if (int(check.group(1)) ** 2) == int(check.group(4)) and\
        (int(check.group(3)) ** 2) == int(check.group(7)) and\
        int(check.group(6)) == int(check.group(1)) * int(check.group(3)) and\
        check.group(2) != check.group(5):
            return True
        
    # this (2-4)(4-8+16) or this (2+4)(4-8+16) is True
    check = re.match(r"\((\d+)(-|\+)(\d+)\+(\d+)\)\((\d+)(\+|-)(\d+)\)", phrase)
    if not check is None:
        if int(check.group(1)) == (int(check.group(5)) ** 2) and\
        int(check.group(3)) == (int(check.group(5)) * int(check.group(7))) and\
        int(check.group(4)) == (int(check.group(7)) ** 2) and\
        check.group(2) != check.group(6):
            return True

    # this (a+b)(a^2-ab+b^2) or (a-b)(a^2+ab+b^2) is True
    check = re.match(r"\((.+)(\+|-)(.+)\)\(.+\^2(-|\+)(.+)\+.+\^2\)", phrase)
    if not check is None:
        ok_style = check.group(2) != check.group(4)
        if check.group(5).isdecimal():
            nums_group = float(check.group(1)) * float(check.group(3))
            if float(check.group(2)) == nums_group and ok_style:
                return True
        else:
            if (check.group(1)+check.group(3)) == check.group(5) and ok_style:
                return True
    
    
    # this (a^2-ab+b^2)(a+b) or (a^2+ab+b^2)(a-b) is True
    check = re.match(r"\(.+\^2(\+|-)(.+)\+.+\^2\)\((.+)(-|\+)(.+)\)", phrase)
    if not check is None:
        ok_style = check.group(1) != check.group(4)
        if check.group(2).isdecimal():
            nums_group = float(check.group(3)) * float(check.group(5))
            if float(check.group(2)) == nums_group and ok_style:
                return True
        elif ok_style and (check.group(3) + check.group(5)) == check.group(2):
            return True
    
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
        phrase = phrase.replace("(", "")
        # phrase = "x+a)x+b)"
        phrase = phrase.replace(")", "")
        # phrase = "x+ax+b"
        counter = 0
        last_char = ""
        for i in phrase:
            if i in ("+", "-"):
                continue
            if phrase.count(i) == 2 and not i in last_char:
                counter += 1
                last_char += i

        if counter == 1:
            return True
        return False

    check = re.match(r"\(.+\+.+\)\(.+\+.+\)", phrase)
    if not check is None and check.end() == len(phrase) and one_subscribe(phrase):
        return True
    check = re.match(r"\(.+-.+\)\(.+-.+\)", phrase)
    if not check is None and check.end() == len(phrase) and one_subscribe(phrase):
        return True

    check = re.match(r"\(.+\+.+\)\^2", phrase)
    if not check is None and check.end() == len(phrase):
        return True
    check = re.match(r"\(.+-.+\)\^2", phrase)
    if not check is None and check.end == len(phrase):
        return True
    return False
#def is_newtons_binomial_expansion_sentence(phrase: str) -> bool:
#def is_lagrange_alliance(phrase: str) -> bool:
#def is_euler_alliance(phrase: str) -> bool:
