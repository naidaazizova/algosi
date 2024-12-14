import time, tracemalloc
import os
import utils
import unittest
from lab2.task3.src.task3 import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_should_check_success_of_merge_sort_for_inversions(self):
        # given
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        input_file_path = os.path.join(project_root, 'lab2', 'task3', 'txtf', 'input.txt')
        data = utils.read_input(input_file_path)

        # when
        inversion_count = merge_sort(data[1], 0, len(data[1]) - 1, 0)
        tracemalloc.start()
        t_start = time.perf_counter()

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        output_file_path = os.path.join(project_root, 'lab2', 'task3', 'txtf', 'output.txt')
        utils.write_output(output_file_path, [str(inversion_count)])

        # then
        expected_inversion_count = 21
        self.assertEqual(inversion_count, expected_inversion_count)
        self.assertLess(time.perf_counter() - t_start, 5)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
    unittest.main()


