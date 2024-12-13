import utils
import os

def interval_count(data):
    s, p = data[0][0], data[0][1]
    intervals = [x for x in data[1:1 + s]]
    points = data[-1]
    result = {}
    coordinates = []

    for st, end in intervals:
        coordinates.append([st, "L"])
        coordinates.append([end, "R"])

    for point in points:
        coordinates.append([point, "P"])
        result[point] = 0

    coordinates.sort()

    active = 0
    for pos, coord_type in coordinates:
        if coord_type == "L":
            active += 1
        elif coord_type == "R":
            active -= 1
        elif coord_type == "P":
            result[pos] = active

    return [result[point] for point in points]

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab3', 'task4', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = interval_count(data)
    utils.print_task_data(3, 4, data, res)

