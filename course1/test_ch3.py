import unittest

from ch3 import brute_force_inversions
from ch3 import sort_and_count_inv


class TestBruteForceInversions(unittest.TestCase):
    def test_brute_force_inversions(self):
        self.assertEqual(brute_force_inversions([1, 3, 5, 2, 4, 6]), 3)

    def test_brute_inversions2(self):
        self.assertEqual(brute_force_inversions([5, 4, 3, 2, 1]), 10)

    def test_brute_inversions3(self):
        x = list(range(1000))
        y = list(reversed(x))
        n_invs = 1000*999//2
        self.assertEqual(brute_force_inversions(y), n_invs)


class TestSortCountInv(unittest.TestCase):
    def test_sort_and_count_inv(self):
        self.assertEqual(sort_and_count_inv([1, 3, 5, 2, 4, 6]),
                         ([1, 2, 3, 4, 5, 6], 3))

    def test_sort_and_count_inv2(self):
        self.assertEqual(sort_and_count_inv([5, 4, 3, 2, 1]),
                         ([1, 2, 3, 4, 5], 10))

    def test_sort_and_count_inv3(self):
        x = list(range(1000))
        y = list(reversed(x))
        n_invs = 1000*999//2
        self.assertEqual(sort_and_count_inv(y), (x, n_invs))
