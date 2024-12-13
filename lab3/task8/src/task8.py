import utils
import os
from lab3.task1.src.task2 import randomized_quicksort

def closest_points(arr, k):
  points = []
  for x,y in arr:
    dist = int((x**2 + y**2)**0.5)
    points.append([dist, [x,y]])
  points_sort = randomized_quicksort(points, 0, len(points) - 1)
  return [x[1] for x in points_sort[0:k]]

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab3', 'task8', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = closest_points(data[1:], data[0][1])
    utils.print_task_data(3, 8, data, res)