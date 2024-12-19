import os
import utils

def longest_common_subsequence(a, b):
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for x in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab7', 'task4', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = longest_common_subsequence(data[1], data[3])
    utils.print_task_data(7, 4, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab7', 'task4', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)