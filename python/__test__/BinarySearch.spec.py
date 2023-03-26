import unittest
import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from BinarySearch import binary_search


class TestSearch(unittest.TestCase):

    def test(self):
        arr = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420];
        self.assertEqual(binary_search(arr, 69), True)
        self.assertEqual(binary_search(arr, 1336), False)
        self.assertEqual(binary_search(arr, 69420), True)
        self.assertEqual(binary_search(arr, 69421), False)
        self.assertEqual(binary_search(arr, 1), True)
        self.assertEqual(binary_search(arr, 0), False)



if __name__ == '__main__':
    unittest.main()