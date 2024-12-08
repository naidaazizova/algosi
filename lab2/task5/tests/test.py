import time, tracemalloc
import os
import utils
from lab2.task5.src.task5 import has_majority

def test_has_majority():
    tracemalloc.start()
    t_start = time.perf_counter()

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab2', 'task5', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)

    res = has_majority(data[1], data[0])

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab2', 'task5', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)

    print('пример для теста')
    utils.print_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()


if __name__ == '__main__':
    test_has_majority()

