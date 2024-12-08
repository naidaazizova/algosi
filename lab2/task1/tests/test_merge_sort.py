import time, tracemalloc
import random
import utils
import os
from lab2.task1.src.task1 import merge_sort

def test_merge_sort():
    t_start = time.perf_counter()
    tracemalloc.start()

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab2', 'task1', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)

    arr_sort = merge_sort(data[1],0, len(data[1])-1)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab2', 'task1', 'txtf', 'output.txt')
    utils.write_output(output_file_path, [arr_sort])

    print('Пример для теста')
    utils.print_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()

def test_merge_sort2():
    worst_case = sorted([random.randint(1, 1000) for _ in range(10000)], reverse=True)
    middle_case = [random.randint(1, 1000) for _ in range(10000)]
    best_case = sorted([random.randint(1, 1000) for _ in range(10000)])
    cases = [worst_case, middle_case, best_case]
    cases_name = ['худший случай', 'средний случай', 'лучший случай']

    for i, arr in enumerate(cases):
        t_start = time.perf_counter()
        tracemalloc.start()
        arr_sort = merge_sort(arr, 0, len(arr) - 1)
        print(cases_name[i])
        utils.print_test(time.perf_counter() - t_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
        tracemalloc.stop()

if __name__ == '__main__':
    test_merge_sort()
    test_merge_sort2()


