import time, tracemalloc
import os
import utils
import unittest
from lab3.task1.src.task2 import randomized_quicksort

class Test1(unittest.TestCase):
    def test_should_check_success_of_randomized_quicksort(self):
        # given
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        input_file_path = os.path.join(project_root, 'lab3', 'task1', 'txtf', 'input.txt')
        data = utils.read_input(input_file_path)

        # when
        t_start = time.perf_counter()
        tracemalloc.start()

        res = randomized_quicksort(data[1], 0, data[0] - 1)

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        output_file_path = os.path.join(project_root, 'lab3', 'task1', 'txtf', 'output.txt')
        utils.write_output(output_file_path, [res])

        # then
        self.assertEqual(res, [-7, -4, -1, 2, 3, 5, 7] )
        self.assertLess(time.perf_counter() - t_start, 5)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
    unittest.main()
