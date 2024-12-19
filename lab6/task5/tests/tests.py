import time, tracemalloc
import unittest
from lab6.task5.src.task5 import process_elections

class ProcessElectionsTest(unittest.TestCase):
    def test_should_check_success_of_process_elections(self):
        # given
        data = [['ivanov', '100'], ['ivanov', '500'], ['ivanov', '300'], ['petr', '70'], ['tourist', '1'],
                ['tourist', '2']]
        expected_data = ['ivanov 900\n', 'petr 70\n', 'tourist 3\n']

        # when
        tracemalloc.start()
        t_start = time.perf_counter()
        res = process_elections(data)
        tracemalloc.stop()

        # then
        self.assertEqual(res, expected_data)
        self.assertLess(time.perf_counter() - t_start, 6)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512)
if __name__ == '__main__':
    unittest.main()