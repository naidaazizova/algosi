def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def insertion_sort_swap(n, spis):
    for i in range(1, n):
        for p in range(i-1, -1, -1):
            if spis[i] > spis[p]:
                spis[i], spis[p] = swap(spis[i], spis[p])
                i, p = p, i
    return spis

import time, tracemalloc
t_start=time.perf_counter()
tracemalloc.start()

file=open('../txtf/input.txt', 'r')
n=int(file.readline())
mas=[int(ch) for ch in file.readline().split()]
file.close()

itog_spis=insertion_sort_swap(n, mas)

with open('../txtf/output.txt', 'w') as file:
    file.write(' '.join(map(str, itog_spis)))
file.close()

print(time.perf_counter() - t_start)
print(tracemalloc.get_traced_memory()[1]/2**20,'Mб')






