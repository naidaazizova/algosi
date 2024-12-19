import utils
import os

def process_elections(data):
    votes = {}

    for line in data:
        candidate, vote_count = line
        if candidate in votes:
            votes[candidate] += int(vote_count)
        else:
            votes[candidate] = int(vote_count)
    sorted_candidates = sorted(votes.items())
    res = []
    for candidate, votes in sorted_candidates:
        res.append(f'{candidate} {votes}\n')

    return res

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab6', 'task5', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = process_elections(data)
    utils.print_task_data(6, 5, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab6', 'task5', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)
