import time, tracemalloc
import os
import utils
import unittest
from lab2.task4.src.task4 import find_index

class TestBinarySearch(unittest.TestCase):

    def test_should_check_success_of_binary_search(self):
        # given
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        input_file_path = os.path.join(project_root, 'lab2', 'task4', 'txtf', 'input.txt')
        data = utils.read_input(input_file_path)

        # when
        tracemalloc.start()
        t_start = time.perf_counter()
        indexx = find_index(data[1], data[3], data[0])

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        output_file_path = os.path.join(project_root, 'lab2', 'task4', 'txtf', 'output.txt')
        utils.write_output(output_file_path, [indexx])

        # then
        expected_indexes = [2, 0, -1, 0, -1]
        self.assertEqual(indexx, expected_indexes)
        self.assertLess(time.perf_counter() - t_start, 5)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
    unittest.main()




