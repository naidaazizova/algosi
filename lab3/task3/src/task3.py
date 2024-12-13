import utils
import os

def pugalo_sort(A, n, k):
    sorted_flag = False
    while not sorted_flag:
        sorted_flag = True
        for i in range(0, n - k):
            if A[i] > A[i + k]:
                A[i], A[i + k] = A[i + k], A[i]
                sorted_flag = False
    return "ДА" if A == sorted(A) else "НЕТ"

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab3', 'task3', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = pugalo_sort(data[1], data[0][0], data[0][1])
    utils.print_task_data(3, 3, data, res)