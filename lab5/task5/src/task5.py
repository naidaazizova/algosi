import utils
import os

class Heap:
    def __init__(self, n):
        self.heap = [(0, i) for i in range(n)]

    def push(self, time, thread_index):
        self.heap.append((time, thread_index))
        self.move_up(len(self.heap) - 1)

    def pop(self):
        self.swap(0, len(self.heap) - 1)
        min_thread = self.heap.pop()
        self.move_down(0)
        return min_thread

    def move_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] >= self.heap[parent]:
                break
            self.swap(idx, parent)
            idx = parent

    def move_down(self, idx):
        size = len(self.heap)
        while 2 * idx + 1 < size:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = left
            if right < size and self.heap[right] < self.heap[left]:
                smallest = right
            if self.heap[idx] <= self.heap[smallest]:
                break
            self.swap(idx, smallest)
            idx = smallest

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def task_manager(n, m, tasks):
    heap = Heap(n)
    result = []

    for i in range(m):
        current_time, thread_index = heap.pop()
        result.append(f'{thread_index} {current_time}\n')
        heap.push(current_time + tasks[i], thread_index)

    return result

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab5', 'task5', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = task_manager(data[0][0], data[0][1], data[1])
    utils.print_task_data(5, 5, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab5', 'task5', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)