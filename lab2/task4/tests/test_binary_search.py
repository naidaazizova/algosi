import time, tracemalloc
import os
import utils
from lab2.task4.src.task4 import find_index

def test_binary_search():
    tracemalloc.start()
    t_start = time.perf_counter()

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab2', 'task4', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)

    indexx = find_index(data[1], data[3], data[0])

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab2', 'task4', 'txtf', 'output.txt')
    utils.write_output(output_file_path, [indexx])

    print('пример для теста')
    utils.print_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()

if __name__ == '__main__':
    test_binary_search()


