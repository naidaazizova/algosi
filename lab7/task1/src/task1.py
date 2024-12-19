import os
import utils

def min_coins(money, coins):
    dp = [float('inf')] * (money + 1)
    dp[0] = 0

    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[money] if dp[money] != float('inf') else -1
if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab7', 'task1', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = min_coins(data[0][0], data[1])
    utils.print_task_data(7, 1, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab7', 'task1', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)