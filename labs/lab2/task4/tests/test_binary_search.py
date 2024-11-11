import unittest
from labs.lab2.task4.src.task4 import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_should_find_first_elem(self):
        data = [1, 2, 3, 4, 5]
        target = 1
        expected_index = 0
        result = binary_search(data, target)
        self.assertEqual(result, expected_index)

    def test_should_return_minusone_for_missing_elem(self):
        data = [1, 2, 3, 4, 5]
        target = 6
        expected_index = -1
        result = binary_search(data, target)
        self.assertEqual(result, expected_index)

    def test_should_find_elem_in_list(self):
        data = [1, 2, 3, 4, 5]
        target = 5
        expected_index = 4
        result = binary_search(data, target)
        self.assertEqual(result, expected_index)

    def test_should_find_single_element(self):
        data = [9]
        target = 9
        expected_index = 0
        result = binary_search(data, target)
        self.assertEqual(result, expected_index)

if __name__ == '__main__':
    unittest.main()
