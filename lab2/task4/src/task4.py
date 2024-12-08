import time
import tracemalloc
from lab2.utils import write_output

def binary_search(a, s):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if s == a[mid]:
            return mid
        elif s > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def task():
    with open("../txtf/input.txt", "r") as f:
        n = int(f.readline().strip())
        a = list(map(int, f.readline().strip().split()))
        k = int(f.readline().strip())
        b = list(map(int, f.readline().strip().split()))
    results = [binary_search(a, b[i]) for i in range(k)]

    write_output("../txtf/output.txt", results)

if __name__ == '__main__':
    tracemalloc.start()
    t_start = time.perf_counter()

    task()
    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Max memory: %s MB" % (tracemalloc.get_traced_memory()[1] / 2 ** 20))
    tracemalloc.stop()



