import unittest
from lab2.task1.src.task1 import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_should_sort_positive_num(self):
        data = [4, 8, 2, 1, 5]
        result = merge_sort(data)
        self.assertEqual(result, [1, 2, 4, 5, 8])

    def test_should_sort_negative_num(self):
        data = [-4, -8, -2, -1, -5]
        result = merge_sort(data)
        self.assertEqual(result, [-8, -5, -4, -2, -1])

    def test_should_sort_single_elem(self):
        data = [2]
        result = merge_sort(data)
        self.assertEqual(result, [2])

    def test_should_sort_mixed_num(self):
        data = [4, -8, 2, -1, 5]
        result = merge_sort(data)
        self.assertEqual(result, [-8, -1, 2, 4, 5])

    def test_should_sort_dublicates(self):
        data = [4, 8, 8, 1, 5]
        result = merge_sort(data)
        self.assertEqual(result, [1, 4, 5, 8, 8])

if __name__ == '__main__':
    unittest.main()
