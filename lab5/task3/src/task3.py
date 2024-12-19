import utils
import os

def network_packets(buffer_size, packets):
    start_times = []
    buffer = []
    for arrival_time, process_time in packets:
        while buffer and buffer[0] <= arrival_time:
            buffer.pop(0)
        if len(buffer) >= buffer_size:
            start_times.append(-1)
        else:
            if not buffer:
                start_time = arrival_time
            else:
                start_time = buffer[-1]

            start_times.append(str(start_time))
            buffer.append(start_time + process_time)

    return start_times

if __name__ == '__main__':
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    input_file_path = os.path.join(project_root, 'lab5', 'task3', 'txtf', 'input.txt')
    data = utils.read_input(input_file_path)
    res = network_packets(data[0][0], data[1:])
    utils.print_task_data(5, 3, data, res)

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
    output_file_path = os.path.join(project_root, 'lab5', 'task3', 'txtf', 'output.txt')
    utils.write_output(output_file_path, res)

