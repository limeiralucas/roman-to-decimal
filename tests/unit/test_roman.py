from roman import RomanNumber


def test_roman_equality():
    assert RomanNumber("X") == RomanNumber("X")
    assert RomanNumber("II") == RomanNumber("II")

def test_roman_to_decimal_single_symbol():
    assert RomanNumber("I").to_decimal() == 1
    assert RomanNumber("V").to_decimal() == 5
    assert RomanNumber("X").to_decimal() == 10
    assert RomanNumber("L").to_decimal() == 50
    assert RomanNumber("C").to_decimal() == 100
    assert RomanNumber("D").to_decimal() == 500
    assert RomanNumber("M").to_decimal() == 1000
    

def test_roman_to_decimal_greater_multiple_symbols():
    assert RomanNumber("VI").to_decimal() == 6
    assert RomanNumber("IX").to_decimal() == 9
    assert RomanNumber("CXX").to_decimal() == 120
    assert RomanNumber("DLIV").to_decimal() == 554
