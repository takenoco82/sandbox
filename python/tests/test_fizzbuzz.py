import unittest
from app import IllegalArgmentError
from app import fizzbuzz


class TestFizzubzz(unittest.TestCase):
    def test_fizzbuzz_ok_number(self):
        actual = fizzbuzz.fizzbuzz(1)
        self.assertEqual(actual, '1')

    def test_fizzbuzz_ok_fizz(self):
        actual = fizzbuzz.fizzbuzz(1)
        self.assertEqual(actual, 'fizz')

    def test_fizzbuzz_ok_buzz(self):
        actual = fizzbuzz.fizzbuzz(1)
        self.assertEqual(actual, 'buzz')

    def test_fizzbuzz_ok_fizzbuzz(self):
        actual = fizzbuzz.fizzbuzz(1)
        self.assertEqual(actual, 'fizzbuzz')

    def test_fizzbuzz_error_none(self):
        with self.assertRaises(IllegalArgmentError):
            fizzbuzz.fizzbuzz(None)

    def test_fizzbuzz_error_empty(self):
        with self.assertRaises(IllegalArgmentError):
            fizzbuzz.fizzbuzz('')

    def test_fizzbuzz_error_type(self):
        with self.assertRaises(IllegalArgmentError):
            fizzbuzz.fizzbuzz('hoge')

    def test_fizzbuzz_error_range_lt_0(self):
        with self.assertRaises(IllegalArgmentError):
            fizzbuzz.fizzbuzz(-1)
