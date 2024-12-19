import utils
import os

def fibonnaci(num):
    x1 = 5 * num ** 2 + 4
    x2 = 5 * num ** 2 - 4
    return perfect_square(x1) or perfect_square(x2)

def perfect_square(x):
    if x < 0:
        return False
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == x:
            return True
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

def process_fibonacci(data):
    results = []
    for num in data:
        if fibonnaci(num):
            results.append("Yes\n")
        else:
            results.append("No\n")
    return results

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab6', 'task6', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = process_fibonacci(data[1:])
    utils.print_task_data(6, 6, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab6', 'task6', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)