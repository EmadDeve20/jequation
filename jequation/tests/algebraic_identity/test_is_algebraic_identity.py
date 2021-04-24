def is_two_square(phrase: str) -> bool:
    from jequation.algebraic_identity.is_algebraic_identity import is_two_square
    if is_two_square(phrase):
        return True
    return False
    
def is_two_cube(phrase: str) -> bool:
    from jequation.algebraic_identity.is_algebraic_identity import is_two_cube
    if is_two_cube(phrase):
        return True
    return False

def is_married(phrase: str) -> bool:
    from jequation.algebraic_identity.is_algebraic_identity import is_married
    if is_married(phrase):
        return True
    return False

def is_common_sentence(phrase: str) -> bool:
    from jequation.algebraic_identity.is_algebraic_identity import is_common_sentence
    if is_common_sentence(phrase):
        return True
    return False

def is_fat_thin(phrase: str) -> bool:
    from jequation.algebraic_identity.is_algebraic_identity import is_fat_thin
    if is_fat_thin(phrase):
        return True
    return False

def is_newtons_binomial_expansion_sentence(phrase: str) -> bool:
    from jequation.algebraic_identity.is_algebraic_identity import is_newtons_binomial_expansion_sentence
    if is_newtons_binomial_expansion_sentence(phrase):
        return True
    return False

def is_lagrange_alliance(phrase: str) -> bool:
    from jequation.algebraic_identity.is_algebraic_identity import is_lagrange_alliance
    if is_lagrange_alliance(phrase):
        return True
    return False

def tests():
    def for_two_square():
        assert is_two_square("(20+20)(20+20)") is True
        assert is_two_square("(20+10)(10-20)") is False
        assert is_two_square("(20+10)^3)") is False
        assert is_two_square("(20-10)(20-100)") is False
        assert is_two_square("(20+10)(10+20)") is True
        assert is_two_square("(AXB-ACV)(VCA-ABX)") is True
        assert is_two_square("(20+10)^2") is True
    def for_two_cube():
        assert is_two_square("(20+20)(20+20)(20+20)") is True
        assert is_two_cube("(1+2)(2+1)(1+2)") is True
        assert is_two_cube("(1+2)^3") is True
        assert is_two_cube("(dsa+x)(x+sda)(x+asd)") is True
        assert is_two_cube("(1+2)(3+4)(5+6)") is False
        assert is_two_cube("(1+2)^2") is False
        assert is_two_cube("(1+2)(2-1)") is False
    def for_married():
        assert is_married("(a+b)(b-a)") is True
        assert is_married("(a+b)(a+b)") is False
        assert is_married("(avc+x)(x-vca)") is True
    def for_common_sentence():
        assert is_common_sentence("(10-2)(2-11)") is True
        assert is_common_sentence("(xvc+a)(b+xcv)") is True
        assert is_common_sentence("(10+11)(11+10)") is True
    def for_fat_thin():
        assert is_fat_thin("(2+4)(4-8+16)") is True
        assert is_fat_thin("(a-b)(a^2+ab-b^2)") is False
        assert is_fat_thin("(a-b)(a^2+ab+b^2)") is True
        assert is_fat_thin("(acv+x)(vca^2-xcav+x^2)") is True
    def for_newtons():
        assert is_newtons_binomial_expansion_sentence("(a+b)(b+a)(a+b)") is True
        assert is_newtons_binomial_expansion_sentence("(a-b)^10") is True
        assert is_newtons_binomial_expansion_sentence("(a+b)(a-b)(a+b)") is False
        assert is_newtons_binomial_expansion_sentence("(a+b)^") is False
        assert is_newtons_binomial_expansion_sentence("(a+b)") is True
        assert is_newtons_binomial_expansion_sentence("(ab+cx)(xc+ba)(ab+cx)(ba+xc)") is True
    def for_lagrange_alliance():
        assert is_lagrange_alliance("(a^2+b^2)(c^2+d^2)") is True

    for_two_square()
    for_two_cube()
    for_married()
    for_common_sentence()
    for_fat_thin()
    for_newtons()
    for_lagrange_alliance()
