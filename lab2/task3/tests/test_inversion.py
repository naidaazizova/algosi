import unittest
from lab2.task3.src.task3 import count_inversions

class TestInversion(unittest.TestCase):

    def test_count_inversions_timeout(self):
        large_array = list(range(100000, 0, -1))
        n = len(large_array)
        time_limit = 0.0001
        expected = "Время выполнения превышено"
        result = count_inversions(large_array, n, time_limit)
        self.assertEqual(result, expected)

    def test_count_inversions_without_inversions(self):
        array = [1, 2, 3, 4, 5]
        n = len(array)
        expected_inversions = 0
        result = count_inversions(array, n)
        self.assertEqual(result, expected_inversions)

    def test_count_inversions_with_all_inversions(self):
        array = [5, 4, 3, 2, 1]
        n = len(array)
        expected_inversions = 10
        result = count_inversions(array, n)
        self.assertEqual(result, expected_inversions)

    def test_count_inversions_baza(self):
        array = [1, 20, 6, 4, 5]
        n = len(array)
        expected_inversions = 5
        result = count_inversions(array, n)
        self.assertEqual(result, expected_inversions)

if __name__ == '__main__':
    unittest.main()