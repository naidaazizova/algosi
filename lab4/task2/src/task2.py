import utils
import os

def queue_func(commands):
    queue = []
    front_index = 0
    res = []
    for command in commands:
        if command[0] == "+":
            queue.append(int(command[1]))
        elif command[0] == "-":
            res.append(str(queue[front_index]) + "\n")
            front_index += 1
    return res

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab4', 'task2', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = queue_func(data[1:])
    utils.print_task_data(4, 2, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab4', 'task2', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)