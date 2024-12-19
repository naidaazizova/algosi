import utils
import os

def operations_process(n, data):
    result = []
    s = set()
    for i in range(n):
        line = data[i]
        operation = line[0]
        x = int(line[1])

        if operation == 'A':
            s.add(x)
        elif operation == 'D':
            s.discard(x)
        elif operation == '?':
            if x in s:
                result.append('Y\n')
            else:
                result.append('N\n')

    return result
if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab6', 'task1', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = operations_process(data[0], data[1:])
    utils.print_task_data(6, 1, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab6', 'task1', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)

