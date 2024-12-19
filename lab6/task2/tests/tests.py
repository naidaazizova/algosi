import time, tracemalloc
import unittest
from lab6.task2.src.task2 import phone_book

class TestPhoneBook(unittest.TestCase):
    def test_should_check_success_of_phone_book(self):
        # given
        data = [12, ['add', '911', 'police'], ['add', '76213', 'Mom'], ['add', '17239', 'Bob'],
                ['find', '76213'], ['find', '910'], ['find', '911'], ['del', '910'], ['del', '911'],
                ['find', '911'], ['find', '76213'], ['add', '76213', 'daddy'], ['find', '76213']]
        expected_data = ['Mom\n', 'not found\n', 'police\n', 'not found\n', 'Mom\n', 'daddy\n']

        # when
        t_start = time.perf_counter()
        tracemalloc.start()
        res = phone_book(data[1:])
        tracemalloc.stop()

        # then
        self.assertEqual(res, expected_data)
        self.assertLess(time.perf_counter() - t_start, 6)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 512)

if __name__ == '__main__':
    unittest.main()