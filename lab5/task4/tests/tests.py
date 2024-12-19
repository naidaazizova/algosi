import time
import tracemalloc
import unittest
from lab5.task4.src.task4 import pyramid_build

class TestPyramidBuild(unittest.TestCase):
    def test_should_check_success_of_build_pyramid(self):
        # given
        data = [5, [5, 4, 3, 2, 1]]
        expected_data = ['3\n', '1 4\n', '0 1\n', '1 3\n']

        # when
        t_start = time.perf_counter()
        tracemalloc.start()
        res = pyramid_build(data[0], data[1])
        tracemalloc.stop()

        # then
        self.assertEqual(res, expected_data)
        self.assertLess(time.perf_counter() - t_start, 2)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)
if __name__ == '__main__':
    unittest.main()