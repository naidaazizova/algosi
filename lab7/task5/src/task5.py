import os
import utils

def longest_common_subsequence(a, b, c):
    n, m, l = len(a), len(b), len(c)
    dp = [[[0] * (l + 1) for x in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    return dp[n][m][l]

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab7', 'task5', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = longest_common_subsequence(data[1], data[3], data[5])
    utils.print_task_data(7, 5, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab7', 'task5', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)