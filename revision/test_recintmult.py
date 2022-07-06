import unittest
from recintmult import check_numbers, recursive_multiplication

class TestCheckNumbers(unittest.TestCase):
    def test_numbers_have_equal_length(self):
        with self.assertRaises(AssertionError):
            check_numbers(1234, 123)
    
    def test_lengths_are_powers_of_two(self):
        with self.assertRaises(AssertionError):
            check_numbers(12345, 67890)


class TestRecursiveMultiplication(unittest.TestCase):
    def test_recursive_multiplication(self):
        self.assertEqual(recursive_multiplication(1234, 5678), 7006652)
        self.assertEqual(recursive_multiplication(
            12344321, 56788765), 701018744353565)
