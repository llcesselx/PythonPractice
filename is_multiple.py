import unittest


def main():
    return 0


def is_multiple(num1=None, num2=None):
    print("Input: {} , {}".format(num1, num2))
    print("---------------------------------")
    if num1 == None or num2 == None:
        print("Invalid input")
        print("")
        return False
    elif not isinstance(num1, int) or not isinstance(num2, int):
        print("Invalid input")
        print("")
        return False
    elif num1 == 0 or num2 == 0:
        print("0 is an invalid number...")
        print("")
        return False
    elif num1 % num2 == 0:
        print("{} is a multiple of {}".format(num2, num1))
        print("")
        return True
    elif num2 % num1 == 0:
        print("{} is a multiple of {}".format(num1, num2))
        print("")
        return True
    else:
        print("Neither number is a multiple of either...")
        print("")
        return False


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

    def testismultiple7(self):
        actual = is_multiple(0, 0)
        expected = False
        self.assertEqual(actual, expected)

    def testismultiple8(self):
        actual = is_multiple(10000, 5)
        expected = True
        self.assertEqual(actual, expected)

    def testismultiple9(self):
        actual = is_multiple("a", 0)
        expected = False
        self.assertEqual(actual, expected)

    def testismultiple10(self):
        actual = is_multiple(1, "b")
        expected = False
        self.assertEqual(actual, expected)

    def testismultiple11(self):
        actual = is_multiple("hello")
        expected = False
        self.assertEqual(actual, expected)
