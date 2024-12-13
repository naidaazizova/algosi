import time, tracemalloc
import os
import utils
from lab2.task3.src.task3 import merge_sort

def test_merge_sort():
    tracemalloc.start()
    t_start = time.perf_counter()

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab2', 'task3', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)

    inversion_count = merge_sort(data[1], 0, len(data[1]) - 1, 0)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab2', 'task3', 'txtf', 'output.txt')
    utils.write_output(output_file_path, [str(inversion_count)])

    print('пример для теста')
    utils.print_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()

if __name__ == '__main__':
    test_merge_sort()

