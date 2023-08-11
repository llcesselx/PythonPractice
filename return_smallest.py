# Write a function:
#    def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Write an efficient algorithm for the following assumptions:
#         N is an integer within the range [1..100,000];
#         each element of array A is an integer within the range [−1,000,000..1,000,000].

import unittest


def main():

    return 0


def solution(array):
    print("\n")
    small = 1000000
    smallest = 1000000
    for i in array:
        # print("i: {}".format(i))
        if i < small:
            small = i
        # print("small: {}".format(small))

    if small < 0:
        return 1

    for i in array:
        print("i: {}".format(i))
        if i+1 in array:
            continue
        elif i+1 not in array:
            if i+1 < smallest:
                smallest = i+1
        print("smallest: {}".format(smallest))
    return smallest


if __name__ == "__main__":
    main()


class TestReturnSmallest(unittest.TestCase):
    def test1(self):
        array = [1, 2, 3]
        actual = solution(array)
        expected = 4
        self.assertEqual(actual, expected)

    def test2(self):
        array = [1, 3, 6, 1, 2, 4]
        actual = solution(array)
        expected = 5
        self.assertEqual(actual, expected)

    def test3(self):
        array = [-1, -3]
        actual = solution(array)
        expected = 1
        self.assertEqual(actual, expected)
