import time, tracemalloc
import utils
import os
import unittest
from lab4.task4.src.task4 import check_brackets

class TestCheckBrackets(unittest.TestCase):
    def test_should_check_success_of_check_brackets(self):
        # given
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        input_file_path = os.path.join(project_root, 'lab4', 'task4', 'txtf', 'input.txt')
        data = utils.read_input(input_file_path)

        # when
        tt_start = time.perf_counter()
        tracemalloc.start()

        res = check_brackets(data[0])

        # then
        self.assertEqual(res, 10)
        self.assertLess(time.perf_counter() - tt_start, 5)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
    unittest.main()




