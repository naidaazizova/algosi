def read_input(file_path: str):
    file = open(file_path, 'r')
    lines = file.readlines()
    data = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if len(line.split()) == 1:
            try:
                data.append(int(line))
            except ValueError:
                data.append(line)
        else:
            try:
                data.append(list(map(int, line.split())))
            except ValueError:
                data.append(line.split())
        i += 1
    file.close()
    return data

def write_output(file_path, data):
    file2 = open(file_path, 'w')
    if not isinstance(data, list) and str(abs(data)).isdigit():
        file2.write(str(data))
    elif '\n' in data[0]:
        file2.write(("").join(list(map(str, data))))
    else:
        file2.write((" ").join(list(map(str, data))))
    file2.close()

def print_test(time, amount_data):
    print('Время работы: %s секунд' % time)
    print("Память:", amount_data, "mb")

def print_task_data(labnumber, tasknumber, inp, output):
    print(f"lab № {labnumber} task №{tasknumber}")
    print("input: " + str(inp))
    print("output: " + str(output) + "\n")

