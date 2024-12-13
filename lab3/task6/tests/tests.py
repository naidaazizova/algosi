import time, tracemalloc
import utils
import os
import unittest
from lab3.task6.src.task6 import sum_of_tenth

class TestSumOfTenth(unittest.TestCase):
    def test_should_check_success_sum_of_tenth(self):
        # given
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        input_file_path = os.path.join(project_root, 'lab3', 'task6', 'txtf', 'input.txt')
        data = utils.read_input(input_file_path)

        # when
        tracemalloc.start()
        tt_start = time.perf_counter()

        res = sum_of_tenth(data[1], data[2])

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        output_file_path = os.path.join(project_root, 'lab3', 'task6', 'txtf', 'output.txt')
        utils.write_output(output_file_path, res)

        print('Пример для теста')
        utils.print_test(time.perf_counter() - tt_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
        tracemalloc.stop()

        # then
        self.assertEqual(res, 51)
        self.assertLess(time.perf_counter() - tt_start, 5)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
        unittest.main()
