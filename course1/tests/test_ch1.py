import unittest

from src.ch1 import align_numbers, karatsuba, mergesort


class TestAlignNumbers(unittest.TestCase):
    def test_align_left(self):
        self.assertEqual(align_numbers('123', '1234'), ('0123', '1234'))

    def test_align_right(self):
        self.assertEqual(align_numbers('1234', '567'), ('1234', '0567'))

    def test_align_both(self):
        self.assertEqual(align_numbers('123', '456'), ('0123', '0456'))

    def test_already_aligned(self):
        self.assertEqual(align_numbers('1234', '5678'), ('1234', '5678'))

    def test_equal_length(self):
        self.assertEqual('7006652', karatsuba('1234', '5678'))

    def test_different_lengths(self):
        self.assertEqual('9740830744704', karatsuba('123456', '78901234'))

    def test_different_and_large(self):
        self.assertEqual('38212069602071645984334',
                         karatsuba('1280984532098', '29830234983'))

    def test_mergesort_even(self):
        self.assertEqual(mergesort([3, 1, 4, 2]), [1, 2, 3, 4])

    def test_mergesort_odd(self):
        self.assertEqual(mergesort([1, 7, 3, 5, 2, 4, 6]),
                         [1, 2, 3, 4, 5, 6, 7])


if __name__ == '__main__':
    unittest.main()