import utils
import os

def bin_search(A, target, l, r):
    if l > r:
        return -1

    mid = (l + r) // 2
    if A[mid] == target:
        return mid
    if target > A[mid]:
        return bin_search(A, target, mid + 1, r)
    if target < A[mid]:
        return bin_search(A, target, l, mid - 1)

def find_index(A, B, n):
    res = []
    for num in B:
        res.append(bin_search(A, num, 0, n - 1))

    return res

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab2', 'task4', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = find_index(data[1], data[3], data[0])
    utils.print_task_data(2, 4, data, res)