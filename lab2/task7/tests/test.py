import time, tracemalloc
import random
import utils
import os
import unittest
from lab2.task7.src.task7 import max_subarray

class TestMaxSubarray(unittest.TestCase):

    def test_should_check_success_of_max_subarray_example(self):
        # given
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        input_file_path = os.path.join(project_root, 'lab2', 'task7', 'txtf', 'input.txt')
        data = utils.read_input(input_file_path)

        # when
        tracemalloc.start()
        tt_start = time.perf_counter()
        result = max_subarray(data[1])

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        output_file_path = os.path.join(project_root, 'lab2', 'task7', 'txtf', 'output.txt')
        utils.write_output(output_file_path, [result])

        # then
        self.assertLess(time.perf_counter() - tt_start, 5)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

        tracemalloc.stop()

    def test_should_check_max_subarray_for_different_cases(self):
        # given
        array_worst = sorted([random.randint(-1000, 1000) for _ in range(10000)], reverse=True)
        array_middle = [random.randint(-1000, 1000) for _ in range(10000)]
        array_best = sorted([random.randint(-1000, 1000) for _ in range(10000)])
        arrays = [array_worst, array_middle, array_best]
        arr_names = ['худший случай', "средний случай", 'лучший случай']

        # when
        for i, arr in enumerate(arrays):
            with self.subTest(case=arr_names[i]):
                tt_start = time.perf_counter()
                tracemalloc.start()

                result = max_subarray(arr)

                # then
                self.assertLess(time.perf_counter() - tt_start, 5)
                self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)
                tracemalloc.stop()
if __name__ == '__main__':
    unittest.main()




