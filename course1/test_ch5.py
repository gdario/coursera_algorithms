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

    def test_choose_pivot_even2(self):
        qs = QuickSort('quicksort_dummy_input.txt')
        qs.data = [2, 8, 6, 5, 1, 9, 4, 3, 7, 10]
        self.assertEqual(qs.choose_median_of_three_pivot(3, 8), 8)
        self.assertEqual(qs.choose_median_of_three_pivot(3, 9), 3)
