import time, tracemalloc
import unittest
from lab5.task3.src.task3 import network_packets

class TestNetworkPackets(unittest.TestCase):
    def test_should_check_success_of_network_packets(self):
        # given
        data = [[2, 3], [0, 1], [3, 1], [10, 1]]
        expected_data = ['0', '3', '10']

        # when
        t_start = time.perf_counter()
        tracemalloc.start()
        res = network_packets(data[0][0], data[1:])
        tracemalloc.stop()

        # then
        self.assertEqual(res, expected_data)
        self.assertLess(time.perf_counter() - t_start, 2)
        self.assertLess(tracemalloc.get_traced_memory()[1] / (1024 ** 2), 256)

if __name__ == '__main__':
    unittest.main()