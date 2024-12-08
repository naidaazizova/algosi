import utils, os

def count_majority(A, target, l, r):
    count = 0
    for i in range(l, r + 1):
        if A[i] == target:
            count += 1

    return count

def majority(A, l, r):
    mid = (l + r) // 2

    if l == r:
        return A[l]

    al = majority(A, l, mid)
    ar = majority(A, mid + 1, r)

    if al == ar:
        return al

    al_count = count_majority(A, al, l, r)
    ar_count = count_majority(A, ar, l, r)

    if al_count > (r - l) // 2:
        return al
    elif ar_count > (r - l) // 2:
        return ar

    return None

def has_majority(A, n):
    res = majority(A, 0, n - 1)
    if res is not None:
        count = count_majority(A, res, 0, n - 1)
        if count > n // 2:
            return 1
    return 0

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab2', 'task5', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = has_majority(data[1], data[0])
    utils.print_task_data(2, 5, data, res)