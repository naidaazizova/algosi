import utils
import os

def check_brackets(data):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    for i, char in enumerate(data, start=1):
        if char in "([{":
            stack.append((char, i))
        elif char in ")]}":
            if not stack or stack[-1][0] != bracket_pairs[char]:
                return i
            stack.pop()

    if stack:
        return stack[0][1]

    return "Success"

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab4', 'task4', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = check_brackets(data[0])
    utils.print_task_data(4, 4, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab4', 'task4', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)