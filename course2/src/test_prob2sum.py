import unittest
import programming_assignment_4 as pa4


class TestProb2Sum(unittest.TestCase):
    def test_naive_counter(self):
        values = [-3, -1, 1, 2, 9, 11, 7, 6, 2]
        values = sorted(list(set(values)))
        targets = range(3, 11)
        self.assertEqual(pa4.naive_counter(values, targets), 8)

    def test_iterative_counter(self):
        values = [-3, -1, 1, 2, 9, 11, 7, 6, 2]
        values = sorted(list(set(values)))
        targets = range(3, 11)
        self.assertEqual(pa4.iterative_counter(values, targets), 8)
