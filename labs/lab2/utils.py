def read_input(file_path):
    with open(file_path, "r") as file:
        n = int(file.readline().strip())
        arr = list(map(int, file.readline().strip().split()))
    return n, arr

def write_output(file_path, result):
    with open(file_path, "w") as file:
        if isinstance(result, list):
            file.write(" ".join(map(str, result)) + "\n")
        else:
            file.write(str(result) + "\n")
