import utils
import os

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1+1)
    R = [0] * (n2+1)

    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]

    i, j ,k = 0, 0, p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k +=1

    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    return A

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab2', 'task1', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    result = merge_sort(data[1], 0, data[0]-1)
    utils.print_task_data(2, 1, data, result)





