import time, tracemalloc
import unittest
from lab5.task1.src.task1 import is_heap

class TestIsHeap(unittest.TestCase):
    def test_should_check_success_of_is_heap(self):
        # given
        data = [5, [1, 3, 2, 5, 4]]
        expected_data = "Yes"

        # when
        t_start = time.perf_counter()
        tracemalloc.start()
        res = is_heap(data[0], data[1])
        tracemalloc.stop()

        # then
        self.assertEqual(res, expected_data)
        self.assertLess(time.perf_counter() - t_start, 2)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
    unittest.main()