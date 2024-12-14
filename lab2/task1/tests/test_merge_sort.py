import time, tracemalloc
import random
import utils
import unittest
import os
from lab2.task1.src.task1 import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_should_check_success_of_merge_sort(self):
        # given
        expected_data = [1, 3, 9, 10, 15, 20, 27, 38, 43, 82]
        data = [10, [38, 27, 43, 3, 9, 82, 10, 15, 20, 1]]

        # when
        t_start = time.perf_counter()
        tracemalloc.start()
        arr_sort = merge_sort(data[1],0, len(data[1])-1)
        tracemalloc.stop()

        # then
        self.assertEqual(arr_sort, expected_data)
        self.assertLess(time.perf_counter() - t_start, 5)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)


    def test_should_check_random_cases_of_merge_sort2(self):
        # given
        worst_case = sorted([random.randint(1, 1000) for _ in range(10000)], reverse=True)
        middle_case = [random.randint(1, 1000) for _ in range(10000)]
        best_case = sorted([random.randint(1, 1000) for _ in range(10000)])
        cases = [worst_case, middle_case, best_case]
        cases_name = ['худший случай', 'средний случай', 'лучший случай']

        # when
        for i, arr in enumerate(cases):
            with self.subTest(case=cases_name[i]):
                t_start = time.perf_counter()
                tracemalloc.start()

                arr_sort = merge_sort(arr, 0, len(arr) - 1)

                # then
                self.assertEqual(arr_sort, sorted(arr))
                self.assertLess(time.perf_counter() - t_start, 5)
                self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

                tracemalloc.stop()
if __name__ == '__main__':
    unittest.main()




