import time, tracemalloc
import os
import utils
import unittest
from lab2.task5.src.task5 import has_majority

class  TestHasMajority(unittest.TestCase):

    def test_should_check_success_of_has_majority(self):
        # given
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        input_file_path = os.path.join(project_root, 'lab2', 'task5', 'txtf', 'input.txt')
        data = utils.read_input(input_file_path)

        # when
        tracemalloc.start()
        t_start = time.perf_counter()
        res = has_majority(data[1], data[0])

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
        output_file_path = os.path.join(project_root, 'lab2', 'task5', 'txtf', 'output.txt')
        utils.write_output(output_file_path, res)

        # then
        expected_res = 1
        self.assertEqual(res, expected_res)
        self.assertLess(time.perf_counter() - t_start, 5)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
    unittest.main()




