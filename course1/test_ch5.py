import unittest

from ch5 import QuickSort


class TestQuickSort(unittest.TestCase):

    def test_quicksort_class(self):
        qs = QuickSort('quicksort_dummy_input.txt')
        qs.quicksort(0, qs.len_data-1)
        self.assertEqual(qs.data, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_sorted_array(self):
        qs = QuickSort('quicksort_dummy_input.txt')
        qs.data = sorted(qs.data)
        qs.quicksort(0, qs.len_data-1)
        self.assertEqual(qs.num_comparisons, 28)

    def test_choose_pivot_even(self):
        qs = QuickSort('quicksort_dummy_input.txt')
        qs.data = [1, 5, 3, 2]
        self.assertEqual(qs.choose_pivot(0, 3), 3)

    def test_choose_pivot_odd(self):
        qs = QuickSort('quicksort_dummy_input.txt')
        qs.data = [1, 5, 3, 2, 4]
        self.assertEqual(qs.choose_pivot(0, 4), 2)

    def test_choose_pivot_even2(self):
        qs = QuickSort('quicksort_dummy_input.txt')
        qs.data = [2, 8, 6, 5, 1, 4, 3, 7]
        self.assertEqual(qs.choose_pivot(0, 7), 3)
