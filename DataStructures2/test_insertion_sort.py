import unittest
import random
import copy

from DataStructures2.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_sort_1(self):

        data1 = [random.randint(-10000, 10000) for i in range(0)]
        data2 = copy.deepcopy(data1)

        data1 = insertion_sort(data1)
        data2.sort()

        self.assertEqual(insertion_sort(data1), data2)

    def test_sort_2(self):

        data1 = [random.randint(-10000, 10000) for i in range(1)]
        data2 = copy.deepcopy(data1)

        data1 = insertion_sort(data1)
        data2.sort()

        self.assertEqual(insertion_sort(data1), data2)

    def test_sort_3(self):

        data1 = [random.randint(-10000, 10000) for i in range(10)]
        data2 = copy.deepcopy(data1)

        data1 = insertion_sort(data1)
        data2.sort()

        self.assertEqual(insertion_sort(data1), data2)

    def test_sort_4(self):
        data1 = [random.randint(-10000, 10000) for i in range(100)]
        data2 = copy.deepcopy(data1)

        data1 = insertion_sort(data1)
        data2.sort()

        self.assertEqual(insertion_sort(data1), data2)

    def test_sort_5(self):
        data1 = [random.randint(-10000, 10000) for i in range(1000)]
        data2 = copy.deepcopy(data1)

        data1 = insertion_sort(data1)
        data2.sort()

        self.assertEqual(insertion_sort(data1), data2)

    def test_sort_6(self):
        data1 = [random.randint(-10000, 10000) for i in range(10000)]
        data2 = copy.deepcopy(data1)

        data1 = insertion_sort(data1)
        data2.sort()

        self.assertEqual(insertion_sort(data1), data2)


if __name__ == '__main__':
    unittest.main()
