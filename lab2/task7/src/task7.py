import utils
import os

def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    temp_st = 0
    st =0
    end = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_st = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            st = temp_st
            end = i
    return arr[st:end + 1]

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab2', 'task7', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    result = max_subarray(data[1])
    utils.print_task_data(2, 7, data, result)

