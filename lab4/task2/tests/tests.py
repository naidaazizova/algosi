import time, tracemalloc
import utils
import os
import unittest
from lab4.task2.src.task2 import queue_func

class TestTask2(unittest.TestCase):
    def test_should_check_success_of_queue_func(self):
        # given
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        input_file_path = os.path.join(project_root, 'lab4', 'task2', 'txtf', 'input.txt')
        data = utils.read_input(input_file_path)

        # when
        tt_start = time.perf_counter()
        tracemalloc.start()

        res = queue_func(data[1:])

        tracemalloc.stop()

        # then
        self.assertEqual(res, ['1\n', '10\n'])
        self.assertLess(time.perf_counter() - tt_start, 2)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
    unittest.main()

