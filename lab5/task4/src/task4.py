import utils
import os

def pyramid_build(n, data):
    swaps = []

    def move_down(i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] < data[min_index]:
            min_index = left

        if right < n and data[right] < data[min_index]:
            min_index = right

        if i != min_index:
            swaps.append(f'{i} {min_index}\n')
            data[i], data[min_index] = data[min_index], data[i]
            move_down(min_index)

    for i in range(n // 2 - 1, -1, -1):
        move_down(i)

    swaps.insert(0, str(len(swaps)) + '\n')
    return swaps

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab5', 'task4', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = pyramid_build(data[0], data[1])
    utils.print_task_data(5, 4, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab5', 'task4', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)