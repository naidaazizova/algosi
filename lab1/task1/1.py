def insertion_sort(n, spis):
    for i in range(1, n):
        for p in range(i-1, -1, -1):
            if spis[i] < spis[p]:
                spis[i], spis[p] = spis[p], spis[i]
                i, p = p, i
        
    return spis

import time, tracemalloc
t_start=time.perf_counter()
tracemalloc.start()

file=open('input.txt')
n=int(file.readline())
mas=[int(ch) for ch in file.readline().split()]
file.close()

spis_stro=list(map(str, insertion_sort(n, mas)))
itog=" ".join(spis_stro)

open('output.txt','w').write(itog)
print(time.perf_counter() - t_start)
print(tracemalloc.get_traced_memory()[1]/2**20,'Mб')











