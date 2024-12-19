import time, tracemalloc
import unittest
from lab6.task1.src.task1 import operations_process

class TestOperations(unittest.TestCase):
    def test_should_check_success_of_operations(self):
        # given
        data = [8, ['A', '2'], ['A', '5'], ['A', '3'], ['?', '2'], ['?', '4'], ['A', '2'], ['D', '2'], ['?', '2']]
        expected_data = ['Y\n', 'N\n', 'N\n']

        # when
        t_start = time.perf_counter()
        tracemalloc.start()
        res = operations_process(data[0], data[1:])
        tracemalloc.stop()

        # then
        self.assertEqual(res, expected_data)
        self.assertLess(time.perf_counter() - t_start, 6)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512)

if __name__ == '__main__':
    unittest.main()






