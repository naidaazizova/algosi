import utils
import os
from lab3.task1.src.task2 import randomized_quicksort

def sum_of_tenth(A, B):
    C = []
    for b in B:
        for a in A:
            C.append(a * b)
    randomized_quicksort(C, 0, len(C) - 1)
    sum_of_tenth = sum(C[i] for i in range(0, len(C), 10))

    return sum_of_tenth

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab3', 'task6', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = sum_of_tenth(data[1], data[2])
    utils.print_task_data(3, 6, data, res)
