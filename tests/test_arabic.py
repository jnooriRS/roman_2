import pytest

from to_roman_numeral_converter import to_arabic_number


def test_to_arabic_number_1_rta():
    """simple to_arabic_number (I) == 1"""
    assert to_arabic_number("I") == 1


def test_to_arabic_number_2008_rta():
    """multi to_arabic_number (MMVIII) == 2008"""
    assert to_arabic_number("MMVIII") == 2008


def test_to_arabic_number_4_rta():
    """simple subtraction to_arabic_number (IV) == 4"""
    assert to_arabic_number("IV") == 4


def test_to_arabic_number_90_rta():
    """subtraction to_arabic_number (XC) == 90"""
    assert to_arabic_number("XC") == 90


def test_to_arabic_number_3999_rta():
    """big to_arabic_number (MMMCMXCIX) == 3999"""
    assert to_arabic_number("MMMCMXCIX") == 3999


if __name__ == "__main__":
    pytest.main()
