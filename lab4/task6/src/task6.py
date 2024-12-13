import utils
import os

def queue_func_min(commands):
    queue = []
    res = []
    for command in commands:
        if command[0] == "+":
            queue.append(int(command[1]))
        elif command[0] == "-":
            queue.pop(0)
        elif command[0] == '?':
            res.append(str(min(queue))  + "\n")
    return res

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab4', 'task6', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = queue_func_min(data[1:])
    utils.print_task_data(4, 6, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab4', 'task6', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)