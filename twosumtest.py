import unittest

class TestTwoSum(unittest.TestCase):
    def testtwosum1(self):
        actual = twosum(nums=[1, 2, 3, 4, 5], target=3)
        expected = [0, 1]
        self.assertEqual(actual, expected)

    def testtwosum2(self):
        actual = twosum(nums=[3, 0, 3, 6], target=6)
        expected = [0, 2]
        self.assertEqual(actual, expected)

    def testtwosum3(self):
        actual = twosum(nums=[5, 10, 15, 30], target=65)
        expected = 0
        self.assertEqual(actual, expected)

    def testtwosum4(self):
        actual = twosum(nums=[2, 14, 37, 68, 104, 22, 87, 116, 265], target=109)
        expected = [5, 6]
        self.assertEqual(actual, expected)

    def testtwosum5(self):
        actual = (twosum(nums=[1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1], target=11))
        expected = [5, 11]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()