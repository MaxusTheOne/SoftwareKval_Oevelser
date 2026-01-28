import unittest

import pytest

from src.RomanTranslator import translate_roman_to_integer


@pytest.mark.parametrize("roman,expected", [
    ("II", 2),
    ("IV", 4),
    ("MDCCCLXVII", 1867),
    ("XCIV", 94),
    ("MMMCMXCIX", 3999),


])
def test_roman_calc(roman, expected):
    assert translate_roman_to_integer(roman) == expected

@pytest.mark.parametrize("roman, error_type", [
    ("XXXX", ValueError),
    ("VV", ValueError),
    ("LM", ValueError),
    ("MMMCMXCXX", ValueError),
])
def test_invalid_input(roman, error_type):
    with pytest.raises(error_type):
        translate_roman_to_integer(roman)


if __name__ == '__main__':
    unittest.main()
