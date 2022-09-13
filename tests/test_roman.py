import pytest

from to_roman_numeral_converter import to_roman_numeral


def test_to_roman_numeral_1_atn():
    """simple to_roman_numeral (1) == I"""
    assert to_roman_numeral(1) == "I"


def test_to_roman_numeral_2008_atn():
    """multi to_roman_numeral (2008) == MMVIII"""
    assert to_roman_numeral(2008) == "MMVIII"


def test_to_roman_numeral_4_atn():
    """simple subtraction to_roman_numeral (4) == IV"""
    assert to_roman_numeral(4) == "IV"


def test_to_roman_numeral_90_atn():
    """subtraction to_roman_numeral (90) == XC"""
    assert to_roman_numeral(90) == "XC"


def test_to_roman_numeral_3999_atn():
    """big to_roman_numeral (3999) == MMMCMXCIX"""
    assert to_roman_numeral(3999) == "MMMCMXCIX"


if __name__ == "__main__":
    pytest.main()
