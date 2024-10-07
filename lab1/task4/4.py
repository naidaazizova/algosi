def linear_search(a, v):
    res = []
    for i in range(len(a)):
        if a[i] == v:
            res.append(i)
    if len(res)==1:
        return res
    elif len(res)==0:
        return [-1]
    else:
        return len(res), res

import time, tracemalloc
t_start=time.perf_counter()
tracemalloc.start()

file=open('input.txt')
a=[ch for ch in file.readline().split()]
v=file.readline()
file.close()

with open('output.txt','w') as file:
    file.write(', '.join(map(str, linear_search(a, v))))
file.close()

print(time.perf_counter() - t_start)
print(tracemalloc.get_traced_memory()[1]/2**20,'Mб')   