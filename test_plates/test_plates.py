import unittest
from plates import is_valid


class TestPlateValidation(unittest.TestCase):
    def test_min_max_characters(self):
        self.assertTrue(is_valid('AB'))
        self.assertTrue(is_valid('ABCDEF'))
        self.assertFalse(is_valid('A'))
        self.assertFalse(is_valid('ABCDEFGH'))

    def test_starting_with_two_letters(self):
        self.assertTrue(is_valid('AA'))
        self.assertFalse(is_valid('A2'))
        self.assertFalse(is_valid('22'))

    def test_numbers_in_middle(self):
        self.assertTrue(is_valid("AAA222"))
        self.assertFalse(is_valid("AAA22A"))

    def test_first_number_zero(self):
        self.assertFalse(is_valid("CS05"))
        self.assertTrue(is_valid("CS50"))
        self.assertFalse(is_valid("CS50P"))

    def test_other_characters(self):
        self.assertFalse(is_valid("PI3.14"))
        self.assertFalse(is_valid("CS 50"))
        self.assertFalse(is_valid("Hello!"))


if __name__ == '__main__':
    unittest.main()
