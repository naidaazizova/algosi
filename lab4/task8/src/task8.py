import utils
import os

def postfix(expression):
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    return stack.pop()

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab4', 'task8', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = postfix(data[1])
    utils.print_task_data(4, 8, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab4', 'task8', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)