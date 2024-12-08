import time, tracemalloc
t_start=time.perf_counter()
tracemalloc.start()

def bubble_sort(n, spis):
    for i in range(n):
        for j in range(i+1, n):
            if spis[i] > spis[j]:
                spis[i], spis[j] = spis[j], spis[i]
    return spis

def check(spis):
    for i in range(len(spis) - 1):
        if not(spis[i] <= spis[i+1]):
            return False
    return True

with open('../txtf/input.txt', 'r') as file:
    n=int(file.readline())
    spis = list(map(int, file.readline().split()))
file.close()

with open('../txtf/output.txt', 'w') as file:
    file.write(' '.join(map(str, bubble_sort(n, spis))))
file.close()

print(time.perf_counter() - t_start)
print(tracemalloc.get_traced_memory()[1]/2**20,'Mб')