import time, tracemalloc
t_start=time.perf_counter()
tracemalloc.start()

def merge_list(a, b, left, mid, right):
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
    return c

def split_and_merge(listt, left, right):
    if left == right:
        return [listt[left]]
    
    mid = (left + right) // 2
    mas1 = split_and_merge(listt, left, mid)
    mas2 = split_and_merge(listt, mid + 1, right)
    return merge_list(mas1, mas2, left, mid, right)

file=open('input.txt')
n = int(file.readline())
mas = [int(ch) for ch in file.readline().split()]
file.close()

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, split_and_merge(mas, 0, n-1))))
file.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory:", tracemalloc.get_traced_memory()[1]/2**20,'Mб')
