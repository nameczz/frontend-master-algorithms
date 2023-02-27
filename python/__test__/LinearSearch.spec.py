import unittest
import sys
import os

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from LinearSearch import linearSearch


class TestLinearSearch(unittest.TestCase):

    def test(self):
        arr = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
        self.assertEqual(linearSearch(arr, 69), True)
        self.assertEqual(linearSearch(arr, 1336), False)
        self.assertEqual(linearSearch(arr, 69420), True)


if __name__ == '__main__':
    unittest.main()