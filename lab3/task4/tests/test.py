import time, tracemalloc
import os
import unittest
import utils
from lab3.task4.src.task4 import interval_count

class TestIntervalCount(unittest.TestCase):

    def test_should_check_success_of_count_interval(self):
        # given
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        input_file_path = os.path.join(project_root, 'lab3', 'task4', 'txtf', 'input.txt')
        data = utils.read_input(input_file_path)

        # when
        t_start = time.perf_counter()
        tracemalloc.start()

        res = interval_count(data)

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        output_file_path = os.path.join(project_root, 'lab3', 'task4', 'txtf', 'output.txt')
        utils.write_output(output_file_path, [res])

        print('Пример для теста')
        utils.print_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
        tracemalloc.stop()

        # then
        self.assertEqual(res, [2, 0])
        self.assertLess(time.perf_counter() - t_start, 5)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
    unittest.main()


