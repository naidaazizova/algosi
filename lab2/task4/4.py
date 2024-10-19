import time, tracemalloc
t_start=time.perf_counter()
tracemalloc.start()

def binary_search(spis, low, high, el):
    while high >= low:
        mid = (high + low) // 2
        if spis[mid] == el:
            return mid
        elif spis[mid] < el:
            low = mid+1
        else:
            high = mid-1
    return -1

def main():
    with open('input.txt') as file:
        n = int(file.readline())
        spis = list(map(int, file.readline().split()))
        k = int(file.readline())
        spis_e = list(map(int, file.readline().split()))
    answ=[]
    for i in range(k):
        if time.perf_counter() - t_start > 2:
            answ = ["-1"] * k
            break
        answ.append(binary_search(spis, 0, n-1, spis_e[i]))
    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, answ)))

print("Время работы: %s секунд" % (time.perf_counter() - t_start))
print("Max memory ", tracemalloc.get_traced_memory()[1] / 2 ** 20, "Мб")

if __name__ == "__main__":
    main()



