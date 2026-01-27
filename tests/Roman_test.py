import unittest

import pytest


class RomanCalcTester(unittest.TestCase):
    @pytest.mark.parametrize("input,expected", [
        ("II", 2),
        ("IV", 4),
        ("MDCCCLXVII", 1867),
        ("XCIV", 94),
        ("MMMCMXCIX", 3999),

        ("XXXX", None),
        ("VV", None),
        ("LM", None),
        ("MMMCMXCXX", None),
    ])
    def test_something(self):
        self.assertEqual(roman_translation(input), expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()
