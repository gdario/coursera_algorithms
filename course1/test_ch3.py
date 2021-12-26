import unittest

from ch3 import brute_force_inversions


class TestBruteForceInversions(unittest.TestCase):
    def test_brute_force_inversions(self):
        self.assertEqual(brute_force_inversions([1, 3, 5, 2, 4, 6]), 3)
