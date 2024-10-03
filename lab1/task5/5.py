def selection_sort(n, spis):
    for i in range(n):
        mini = spis[i]
        indexx= i
        for p in range(i+1, n):
            if mini >= spis[p]:
                mini= min(mini, spis[p])
                indexx=p
        spis.pop(indexx)
        spis.insert(i, mini)
    return spis

import time, tracemalloc
t_start=time.perf_counter()
tracemalloc.start()

file=open('input.txt')
n=int(file.readline())
mas=[int(ch) for ch in file.readline().split()]
file.close()

itog_spis=selection_sort(n, mas)

with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, itog_spis)))
file.close()

print(time.perf_counter() - t_start)
print(tracemalloc.get_traced_memory()[1]/2**20,'Mб')

