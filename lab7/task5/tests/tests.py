import time, tracemalloc
import unittest
from lab7.task5.src.task5 import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):
    def test_should_check_success_of_longest_common_subsequence(self):
        # given
        data = [5, [8, 3, 2, 1, 7], 7, [8, 2, 1, 3, 8, 10, 7], 6, [6, 8, 3, 1, 4, 7]]
        expected_data = 3

        # when
        t_start = time.perf_counter()
        tracemalloc.start()
        res = longest_common_subsequence(data[1], data[3], data[5])
        tracemalloc.stop()

        # then
        self.assertEqual(res, expected_data)
        self.assertLess(time.perf_counter() - t_start, 6)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512)

if __name__ == '__main__':
    unittest.main()