import time, tracemalloc
t_start=time.perf_counter()
tracemalloc.start()

def merge_list(a, b, left, mid, right, output_file):
    c = []
    N = len(a)
    M = len(b)

    i = 0
    j = 0
    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]

    If = left + 1
    Il = right + 1
    Vf = c[0] if c else 0
    Vl = c[-1] if c else 0

    output_file.write(f"{If} {Il} {Vf} {Vl}\n")
    return c

def split_and_merge(listt, left, right, output_file):
    if left == right:
        return [listt[left]]
    
    mid = (left + right) // 2
    mas1 = split_and_merge(listt, left, mid, output_file)
    mas2 = split_and_merge(listt, mid + 1, right, output_file)
    return merge_list(mas1, mas2, left, mid, right, output_file)

file=open('input.txt')
n = int(file.readline().strip())
mas = [int(ch) for ch in file.readline().strip().split()]
file.close()

with open('output.txt', 'w') as output_file:
    split_and_merge(mas, 0, n-1, output_file)
    sorted_list = sorted(mas)
    output_file.write(' '.join(map(str, sorted_list)) + '\n')

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory:", tracemalloc.get_traced_memory()[1]/2**20,'Mб')
