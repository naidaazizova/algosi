import utils
import os

def is_heap(n , array):
    for i in range(n):
        if 2 * i + 1 < n and array[i] > array[2 * i + 1]:
            return "No"
        if 2 * i + 2 < n and array[i] > array[2 * i + 2]:
            return "No"
    return "Yes"

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab5', 'task1', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = is_heap(data[0], data[1])
    utils.print_task_data(5, 1, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab5', 'task1', 'txtf', 'output.txt')
    utils.write_output(output_file_path, [res])
