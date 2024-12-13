import utils
import os

def hirsh_index(arr):
    arr.sort(reverse=True)
    h = 0
    for i, n in enumerate(arr):
        if n >= i + 1:
            h = i + 1
        else:
            break
    return h

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab3', 'task5', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = hirsh_index(data[0])
    utils.print_task_data(3, 5, data, res)