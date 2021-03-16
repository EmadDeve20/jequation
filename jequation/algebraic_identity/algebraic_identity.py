#!/bin/env python3

"""
I used the Persian names of alliances for all functions
"""

import re

def is_binomial(phrase: str) -> bool:
    """this function for check your phrase is binomial or not"""
    if len(phrase) == 10:
        check = re.match(r"\(.+.\)\(.+.\)", phrase)
        if check.end() == len(phrase):
            return True
        check = re.match(r"\(.-.\)\(.-.\)", phrase)
        if check.end() == len(phrase):
            return True
    #TODO; if len(pharse) > 10
    return False

def is_married(phrase: str) -> bool:
    """this function for check your phrase is married or not"""
    check = re.match(r"\(.-.\)\(.+.\)", phrase)
    if check.end() == len(phrase):
        return True
    check = re.match(r"\(.+.\)\(.-.\)", phrase)
    if check.end() == len(phrase):
        return True
    return False
