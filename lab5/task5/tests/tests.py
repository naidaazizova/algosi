import time, tracemalloc
import unittest
from lab5.task5.src.task5 import task_manager

class TestTaskManager(unittest.TestCase):
    def test_should_check_success_of_task_manager(self):
        # given
        data = [[2, 5], [1, 2, 3, 4, 5]]
        expected_data = ['0 0\n', '1 0\n', '0 1\n', '1 2\n', '0 4\n']

        # when
        t_start = time.perf_counter()
        tracemalloc.start()
        res = task_manager(data[0][0], data[0][1], data[1])
        tracemalloc.stop()

        # then
        self.assertEqual(res, expected_data)
        self.assertLess(time.perf_counter() - t_start, 2)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
    unittest.main()