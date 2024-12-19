import time, tracemalloc
import unittest
from lab6.task6.src.task6 import process_fibonacci

class TestFibonacci(unittest.TestCase):
    def test_should_check_success_of_fibonacci(self):
        # given
        data = [8, 1, 2, 3, 4, 5, 6, 7, 8]
        expected_data = ['Yes\n', 'Yes\n', 'Yes\n', 'No\n', 'Yes\n', 'No\n', 'No\n', 'Yes\n']

        # when
        t_start = time.perf_counter()
        tracemalloc.start()
        res = process_fibonacci(data[1:])
        tracemalloc.stop()

        # then
        self.assertEqual(res, expected_data)
        self.assertLess(time.perf_counter() - t_start, 6)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512)
if __name__ == '__main__':
    unittest.main()