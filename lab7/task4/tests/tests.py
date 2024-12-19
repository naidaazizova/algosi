import time, tracemalloc
import unittest
from lab7.task4.src.task4 import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):
    def test_should_check_success_of_longest_common_subsequence(self):
        # given
        data = [4, [2, 7, 8, 3], 4, [5, 2, 8, 7]]
        expected_data = 2

        # when
        t_start = time.perf_counter()
        tracemalloc.start()
        res = longest_common_subsequence(data[1], data[3])
        tracemalloc.stop()

        # then
        self.assertEqual(res, expected_data)
        self.assertLess(time.perf_counter() - t_start, 6)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512)

if __name__ == '__main__':
    unittest.main()