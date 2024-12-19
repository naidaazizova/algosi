import os
import utils

def min_operations(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    path = []
    current = n
    while current > 1:
        path.append(str(current))
        if current % 3 == 0 and dp[current] == dp[current // 3] + 1:
            current //= 3
        elif current % 2 == 0 and dp[current] == dp[current // 2] + 1:
            current //= 2
        else:
            current -= 1
    path.append(str(1))
    return [str(dp[n]) + "\n", (" ").join(path[::-1])]

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab7', 'task2', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = min_operations(data[0])
    utils.print_task_data(7, 2, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab7', 'task2', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)