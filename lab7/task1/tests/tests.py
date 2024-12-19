import time, tracemalloc
import unittest
from lab7.task1.src.task1 import min_coins

class TestMinCoins(unittest.TestCase):
    def test_should_check_success_of_min_coins(self):
        # given
        data = [[34, 3], [1, 3, 4]]
        expected_data = 9

        # when
        t_start = time.perf_counter()
        tracemalloc.start()
        res = min_coins(data[0][0], data[1])
        tracemalloc.stop()

        # then
        self.assertEqual(res, expected_data)
        self.assertLess(time.perf_counter() - t_start, 6)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512)

if __name__ == '__main__':
    unittest.main()