import unittest


def is_multiple(num1, num2):
    if num1 % num2 == 0:
        print("{} is a multiple of {}".format(num2, num1))
        return True
    elif num2 % num1 == 0:
        print("{} is a multiple of {}".format(num1, num2))
        return True
    elif num1 == 0 or num2 == 0:
        print("{} is an invalid number...")
        return False
    else:
        print("Neither number is a multiple of either...")
        return False


def main():
    return 0


if __name__ == "__main__":
    main()


class TestIsMultiple(unittest.TestCase):
    def testismultiple1(self):
        actual = is_multiple(2, 10)
        expected = True
        self.assertEqual(actual, expected)

    def testismultiple2(self):
        actual = is_multiple(5, 5)
        expected = True
        self.assertEqual(actual, expected)

    def testismultiple3(self):
        actual = is_multiple(15, 5)
        expected = True
        self.assertEqual(actual, expected)

    def testismultiple4(self):
        actual = is_multiple(2, 7)
        expected = False
        self.assertEqual(actual, expected)

    def testismultiple5(self):
        actual = is_multiple(19, 6)
        expected = False
        self.assertEqual(actual, expected)

    def testismultiple6(self):
        actual = is_multiple(1, 0)
        expected = False
        self.assertEqual(actual, expected)

