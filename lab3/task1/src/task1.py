import random
import utils
import os
def partition(A, l, r):
  x = A[l]
  j = l
  for i in range(l+1, r+1):
    if A[i] <= x:
      j += 1
      A[j], A[i] = A[i], A[j]
  A[l], A[j] = A[j], A[l]
  return j

def randomized_quicksort(A,l,r):
  if l < r:
    k = random.randint(l, r)
    A[l], A[k] = A[k], A[l]
    m = partition(A, l, r)
    randomized_quicksort(A, l, m-1)
    randomized_quicksort(A, m+1, r)
  return A

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab3', 'task1', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = randomized_quicksort(data[1], 0, data[0] - 1)
    utils.print_task_data(3, 1, data, res)

