import random
import utils
import os

def partition3(A, l, r):
    x = A[l]
    m1 = l
    m2 = r
    i = l
    while i <= m2:
        if A[i] < x:
            A[m1], A[i] = A[i], A[m1]
            m1 += 1
            i += 1
        elif A[i] > x:
            A[i], A[m2] = A[m2], A[i]
            m2 -= 1
        else:
            i += 1
    return m1, m2

def randomized_quicksort(A, l, r):
    if l < r:
        k = random.randint(l, r)
        A[l], A[k] = A[k], A[l]
        m1, m2 = partition3(A, l, r)
        randomized_quicksort(A, l, m1 - 1)
        randomized_quicksort(A, m2 + 1, r)
    return A

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab3', 'task1', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = randomized_quicksort(data[1], 0, data[0]-1)
    utils.print_task_data(3, 1, data, res)