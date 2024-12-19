import utils
import os

def phone_book(data):
    phonebook = {}
    result = []

    for query in data:
        command = query[0]

        if command == 'add':
            number = query[1]
            name = query[2]
            phonebook[number] = name

        elif command == 'del':
            number = query[1]
            if number in phonebook:
                del phonebook[number]

        elif command == 'find':
            number = query[1]
            if number in phonebook:
                result.append(phonebook[number] + '\n')
            else:
                result.append('not found\n')

    return result
if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab6', 'task2', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = phone_book(data[1:])
    utils.print_task_data(6, 2, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab6', 'task2', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)