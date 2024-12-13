import time, tracemalloc
import random
import utils
import os
from lab2.task7.src.task7 import max_subarray

def test_max_subarray():
    #Проверка по времени и памяти для примера
    tracemalloc.start()
    tt_start = time.perf_counter()

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab2', 'task7', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)

    result = max_subarray(data[1])

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab2', 'task7', 'txtf', 'output.txt')
    utils.write_output(output_file_path, [result])

    print('Пример для теста')
    utils.print_test(time.perf_counter() - tt_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
    tracemalloc.stop()

def test_max_subarray2():
    # Проверка по времени и памяти для худшего, среднего и лучшего случаев
    array_worst = sorted([random.randint(-1000, 1000) for _ in range(10000)], reverse=True)
    array_middle = [random.randint(-1000, 1000) for _ in range(10000)]
    array_best = sorted([random.randint(-1000, 1000) for _ in range(10000)])
    arrays = [array_worst, array_middle, array_best]
    arr_names = ['худший случай', "средний случай", 'лучший случай']

    for i, arr in enumerate(arrays):
        tt_start = time.perf_counter()
        tracemalloc.start()

        result = max_subarray(arr)
        print(arr_names[i])
        utils.print_test(time.perf_counter() - tt_start, tracemalloc.get_traced_memory()[1] / (1024 ** 2))
        tracemalloc.stop()

if __name__ == '__main__':
    test_max_subarray()
    test_max_subarray2()


