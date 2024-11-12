from functools import reduce

import group
import unittest

class Tests(unittest.TestCase):

    def test_ceiling_div_1(self):
        result = group.ceiling_div(5, 3)
        expected = 2
        self.assertEqual(expected, result)

    def test_ceiling_div_2(self):
        result = group.ceiling_div(0, 3)
        expected = 0
        self.assertEqual(expected, result)

    def test_groups_of_3_1(self):
        nums = [1,2,3,4,5,6,7,8]
        result = group.groups_of_3(nums)
        expected = [[1, 2, 3], [4, 5, 6], [7, 8]]
        self.assertEqual(expected, result)

    def test_groups_of_3_2(self):
        nums = [1,2,3,4,5,6,7]
        result = group.groups_of_3(nums)
        expected = [[1, 2, 3], [4, 5, 6], [7]]
        self.assertEqual(expected, result)

    def test_groups_of_3_3(self):
        nums = [1,2,3,4,5,6,7,8,9]
        result = group.groups_of_3(nums)
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(expected, result)

    def test_groups_of_3_4(self):
        nums = []
        result = group.groups_of_3(nums)
        expected = []
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()