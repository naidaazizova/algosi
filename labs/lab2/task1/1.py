import time, tracemalloc
t_start=time.perf_counter()
tracemalloc.start()

def merge_list(a, b):
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
    return c

def split_and_merge(listt):
    N1 = len(listt) // 2
    mas1 = listt[:N1]
    mas2 = listt[N1:]

    if len(mas1) > 1:
        mas1 = split_and_merge(mas1)
    if len(mas2) > 1:
        mas2 = split_and_merge(mas2)
    return merge_list(mas1, mas2)

file=open('input.txt')
n = int(file.readline())
mas = [int(ch) for ch in file.readline().split()]
file.close()

with open('output.txt', 'w') as file:
    file.write(' '.join(list(map(str, split_and_merge(mas)))))
file.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
print("Max memory:", tracemalloc.get_traced_memory()[1]/2**20,'Mб')




