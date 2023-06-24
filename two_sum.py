from typing import List
import unittest


def twosum(nums: List[int], target: int) -> List[int]:
    print(nums)
    ognums = nums
    result = []
    for i in nums:
        print("==============================")
        print("i in nums: {}".format(i))
        num1 = nums[0]
        print("nums[0]: {}".format(num1))
        num2 = target - num1
        print("num Needed: {}".format(num2))
        for j in nums[1:]:
            print("j in nums: {}".format(j))

            if j == num1:
                jindex = [index for index, number in enumerate(ognums) if number == num2]
                result.append(ognums.index(num1))
                jind = jindex[1]
                result.append(jind)
                print("Result found: {} and {}".format(num1, j))
                print("Indexes found: {} and {}".format((ognums.index(num1)), jind))
                print(result)
                return result

            if j == num2:
                result.append(ognums.index(num1))
                result.append(ognums.index(j))
                print("Result found: {} and {}".format(num1, j))
                print("Indexes found: {} and {}".format((ognums.index(num1)), (ognums.index(j))))
                print(result)
                return result
            else:
                print("------- NO MATCH -------")
        print("!!----- NEXT NUM -----!!")
        nums = nums[1:]

    print("No compatible values...")
    return 0


def main():
    numslist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    twosum(numslist, 19)
    return 0


if __name__ == "__main__":
    main()


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