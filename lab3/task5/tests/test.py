import time, tracemalloc
import utils
import os
import unittest
from lab3.task5.src.task5 import hirsh_index

class TestHirshIndex(unittest.TestCase):
    def test_should_check_success_of_hirsh_index(self):
        # given
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        input_file_path = os.path.join(project_root, 'lab3', 'task5', 'txtf', 'input.txt')
        data = utils.read_input(input_file_path)

        # when
        tracemalloc.start()
        t_start = time.perf_counter()

        res = hirsh_index(data[0])

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        output_file_path = os.path.join(project_root, 'lab3', 'task5', 'txtf', 'output.txt')
        utils.write_output(output_file_path, res)

        print('Пример для теста')
        utils.print_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
        tracemalloc.stop()

        # then
        self.assertEqual(res, 3)
        self.assertLess(time.perf_counter() - t_start, 5)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
    unittest.main()