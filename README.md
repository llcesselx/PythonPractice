# Sorting Algorithms

CS-201 - Programming Structures
Fall 2022
Instructor: Mr. Luke May
Sorting Algorithms
Lab Setup

All of the lab assignments are turned in by simply placing the files in the appropriate directory on the CS Server. Create a directory on the CS Server to turn in your work for this assignment if you have not already:

mkdir -p ~/labs/lab4

Note - File and directory names in Linux are case-sensitive, so make sure your names exactly match the lab or you will get no credit.
Lab Problems (66pts)

These lab problems are going to be created as python modules. Each module will be a standard Python 3 file in which the lab text defines specific programming constructs (variables, functions, or classes) to be be defined in the global scope of the module. A second file will be created to import these packages and provide a lab defined context in which to test them. You will want you use the package file itself for your own testing. The first problem will just be a simple demonstration of how this will work.
1) Module Setup - (foo_utils.py, foo_utils.lab_tests.py)

The following is the lab setup for a module called foo_utils.py and the associated lab file to test it. This first file is the module itself.
Module Definition (foo_utils.py)

This next file contains the lab defined tests that will be used to help you determine if you accomplished the task properly, and they will also be used to grade your work.
Lab Defined Tests (foo_utils.lab_tests.py)

#!/usr/bin/env python3

import foo_utils

foo_utils.foo_says("The lab defined this test!!")
foo_utils.foo_name = "LAB"
foo_utils.foo_says(f"Testing version {foo_utils.VERSION}...")

print("All lab tests PASSED!")

Grading (6pts)

    (1pts) foo_utils.py - File exists with the above code and the proper hashbang, line endings, and permissions.
    (2pts) foo_utils.py - File contains a reasonable attempt and the code runs without errors.
    (2pts) foo_utils.py - Correct logic / Correct implementation.
    (1pt each - 1 total) foo_utils.lab_tests.py - Each test passes (must use the exact lab tests file from the lab).

2) Module - Sorting Utilities (sort_utils.py, sort_utils.lab_tests.py)

Create a file that will be used as a module called sort_utils.py. In this module export a module level variable called verbose, which defaults to True. Next you will export a function called swap. This function should take 3 required parameters: The first parameter should be a list, the second and third parameters should be integer index values. Use this as a template for your file:

The verbose variable will allow some additional information to be printed out each time the swap function is called. When the value is set to True, information will be printed to the terminal, but when it is set to false, the function calls will not print data (unless you add print statements).

You should add testing to your code using the line if __name__ == "__main__":. I won't grade the content of your tests, only that there are some. So test this function, and make sure it is swapping values in a list.

Next create a lab testing file sort_utils.lab_tests.py with the following content:

#!/usr/bin/env python3

import sort_utils


tests_passed = 0
total_tests = 0

test_name = "Test 1"
print(f"---- {test_name} ----------------------------")
orig = list("abcdef")
li = list(orig)
sort_utils.swap(li, 2, 3)
print(li)
print("----------------------------------------")

total_tests+= 1
expected = list("abdcef")
if expected == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")


test_name = "Test 2"
print(f"---- {test_name} ----------------------------")
orig = list("abcdef")
li = list(orig)
sort_utils.swap(li, 0, 5)
sort_utils.swap(li, 1, 4)
sort_utils.swap(li, 2, 3)
print(li)
print("----------------------------------------")

total_tests+= 1
if list(orig)[::-1] == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")

# Test Results
print("========================================")
if tests_passed == total_tests:
    print("All lab tests PASSED!")
else:
    print("Not all tests passed...")

Grading (6pts)

    (1pts) sort_utils.py - File exists with the above code and the proper hashbang, line endings, and permissions.
    (1pts) sort_utils.py - File contains a reasonable attempt and the code runs without errors.
    (2pts) sort_utils.py - Correct logic / Correct implementation.
    (1pt each - 2 total) sort_utils.lab_tests.py - Each test passes (must use the exact lab tests file from the lab).

3) Selection Sort (selection.py, selection.lab_tests.py)

Create a module called selection.py. This file will be a python module that we will import into another file. In it we will be implementing the selection sort algorithm for sorting numbers from smallest to largest. Make sure you have read the lecture materials on selection sort.

Import the package sort_utils so you will have access to your swap() function. Then define a function that will use the selection sort algorithm to sort a list. Make sure to use your swap function when you need to swap elements in the list, rather than doing it manually. Here is a template for you to begin with:

Now create a file for the lab tests called selection.lab_tests.py. Enter the following code:

#!/usr/bin/env python3

import sort_utils
from selection import selection_sort


tests_passed = 0
total_tests = 0

test_name = "Test 1 - a"
print(f"---- {test_name} ----------------------------")
orig = li = [12, 7, 32, 5, 16, 4]
li = list(orig)
selection_sort(li)
print(li)
print("\n".join([
    "---- Expected output -------------------------",
    "[12, 7, 32, 5, 16, 4]",
    "swap 0:12 <--> 5:4",
    "[4, 7, 32, 5, 16, 12]",
    "swap 1:7 <--> 3:5",
    "[4, 5, 32, 7, 16, 12]",
    "swap 2:32 <--> 3:7",
    "[4, 5, 7, 32, 16, 12]",
    "swap 3:32 <--> 5:12",
    "[4, 5, 7, 12, 16, 32]",
    "----------------------------------------------",
]))

total_tests+= 1
expected = [4, 5, 7, 12, 16, 32]
if expected == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", li)


test_name = "Test 1 - b"
print(f"---- {test_name} ----------------------------")


total_tests+= 1
expected = [((0, 12), (5, 4)), ((1, 7), (3, 5)), ((2, 32), (3, 7)), ((3, 32), (5, 12))]

if expected == sort_utils.swaps:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", sort_utils.swaps)


test_name = "Test 2 - a"
print(f"---- {test_name} ----------------------------")
orig = li = [88, 98, 43, 11, 78, 19, 27]
li = list(orig)
selection_sort(li)
print(li)
print("\n".join([
    "---- Expected output -------------------------",
    "[88, 98, 43, 11, 78, 19, 27]",
    "swap 0:88 <--> 3:11",
    "[11, 98, 43, 88, 78, 19, 27]",
    "swap 1:98 <--> 5:19",
    "[11, 19, 43, 88, 78, 98, 27]",
    "swap 2:43 <--> 6:27",
    "[11, 19, 27, 88, 78, 98, 43]",
    "swap 3:88 <--> 6:43",
    "[11, 19, 27, 43, 78, 98, 88]",
    "swap 5:98 <--> 6:88",
    "[11, 19, 27, 43, 78, 88, 98]",
    "----------------------------------------------",
]))

total_tests+= 1
expected = [11, 19, 27, 43, 78, 88, 98]
if expected == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", li)


test_name = "Test 2 - b"
print(f"---- {test_name} ----------------------------")


total_tests+= 1
expected = [((0, 88), (3, 11)), ((1, 98), (5, 19)), ((2, 43), (6, 27)), ((3, 88), (6, 43)), ((5, 98), (6, 88))]

if expected == sort_utils.swaps:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", sort_utils.swaps)


test_name = "Test 3"
print(f"---- {test_name} ----------------------------")
orig = li = [123, 456, 267, 96, 142, 387]
li = list(orig)
selection_sort(li)
print(li)
print("\n".join([
    "---- Expected output -------------------------",
    "[123, 456, 267, 96, 142, 387]",
    "swap 0:123 <--> 3:96",
    "[96, 456, 267, 123, 142, 387]",
    "swap 1:456 <--> 3:123",
    "[96, 123, 267, 456, 142, 387]",
    "swap 2:267 <--> 4:142",
    "[96, 123, 142, 456, 267, 387]",
    "swap 3:456 <--> 4:267",
    "[96, 123, 142, 267, 456, 387]",
    "swap 4:456 <--> 5:387",
    "[96, 123, 142, 267, 387, 456]",
    "----------------------------------------------",
]))

total_tests+= 1
expected = [96, 123, 142, 267, 387, 456]
if expected == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", li)


test_name = "Test 3 - b"
print(f"---- {test_name} ----------------------------")


total_tests+= 1
expected = [((0, 123), (3, 96)), ((1, 456), (3, 123)), ((2, 267), (4, 142)), ((3, 456), (4, 267)), ((4, 456), (5, 387))]

if expected == sort_utils.swaps:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", sort_utils.swaps)


# Test Results
tests_failed = total_tests - tests_passed
print("========================================")
if tests_failed == 0:
    print("All lab tests PASSED!")
else:
    print(f"{tests_failed} tests failed...")

Grading (18pts)

    (1pts) selection.py - File exists with the above code and the proper hashbang, line endings, and permissions.
    (5pts) selection.py - File contains a reasonable attempt and the code runs without errors.
    (6pts) selection.py - Correct logic / Correct implementation.
    (1pt each - 6 total) selection.lab_tests.py - Each test passes (must use the exact lab tests file from the lab).

4) Insertion Sort (insertion.py, insertion.lab_tests.py)

For this lab problem we will do the exact same thing as problem 3, except we will implement the insertion sort algorithm. Make sure you have read the lecture materials on insertion sort. Create a python module called insertion.py. You may use the following as a starting template:

Use the following lab tests file (insertion.lab_tests.py):

#!/usr/bin/env python3

import sort_utils
from insertion import insertion_sort


tests_passed = 0
total_tests = 0

test_name = "Test 1 - a"
print(f"---- {test_name} ----------------------------")
orig = li = [12, 7, 32, 5, 16, 4]
li = list(orig)
insertion_sort(li)
print(li)
print("\n".join([
    "---- Expected output -------------------------",
    "[12, 7, 32, 5, 16, 4]",
    "swap 0:12 <--> 1:7",
    "[7, 12, 32, 5, 16, 4]",
    "swap 2:32 <--> 3:5",
    "[7, 12, 5, 32, 16, 4]",
    "swap 1:12 <--> 2:5",
    "[7, 5, 12, 32, 16, 4]",
    "swap 0:7 <--> 1:5",
    "[5, 7, 12, 32, 16, 4]",
    "swap 3:32 <--> 4:16",
    "[5, 7, 12, 16, 32, 4]",
    "swap 4:32 <--> 5:4",
    "[5, 7, 12, 16, 4, 32]",
    "swap 3:16 <--> 4:4",
    "[5, 7, 12, 4, 16, 32]",
    "swap 2:12 <--> 3:4",
    "[5, 7, 4, 12, 16, 32]",
    "swap 1:7 <--> 2:4",
    "[5, 4, 7, 12, 16, 32]",
    "swap 0:5 <--> 1:4",
    "[4, 5, 7, 12, 16, 32]",
    "----------------------------------------------",
]))

total_tests+= 1
expected = [4, 5, 7, 12, 16, 32]
if expected == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", li)


test_name = "Test 1 - b"
print(f"---- {test_name} ----------------------------")


total_tests+= 1
expected = [((0, 12), (1, 7)), ((2, 32), (3, 5)), ((1, 12), (2, 5)), ((0, 7), (1, 5)), ((3, 32), (4, 16)), ((4, 32), (5, 4)), ((3, 16), (4, 4)), ((2, 12), (3, 4)), ((1, 7), (2, 4)), ((0, 5), (1, 4))]

if expected == sort_utils.swaps:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", sort_utils.swaps)


test_name = "Test 2"
print(f"---- {test_name} ----------------------------")
orig = li = [88, 98, 43, 11, 78, 19, 27]
li = list(orig)
insertion_sort(li)
print(li)
print("\n".join([
    "---- Expected output -------------------------",
    "[88, 98, 43, 11, 78, 19, 27]",
    "swap 1:98 <--> 2:43",
    "[88, 43, 98, 11, 78, 19, 27]",
    "swap 0:88 <--> 1:43",
    "[43, 88, 98, 11, 78, 19, 27]",
    "swap 2:98 <--> 3:11",
    "[43, 88, 11, 98, 78, 19, 27]",
    "swap 1:88 <--> 2:11",
    "[43, 11, 88, 98, 78, 19, 27]",
    "swap 0:43 <--> 1:11",
    "[11, 43, 88, 98, 78, 19, 27]",
    "swap 3:98 <--> 4:78",
    "[11, 43, 88, 78, 98, 19, 27]",
    "swap 2:88 <--> 3:78",
    "[11, 43, 78, 88, 98, 19, 27]",
    "swap 4:98 <--> 5:19",
    "[11, 43, 78, 88, 19, 98, 27]",
    "swap 3:88 <--> 4:19",
    "[11, 43, 78, 19, 88, 98, 27]",
    "swap 2:78 <--> 3:19",
    "[11, 43, 19, 78, 88, 98, 27]",
    "swap 1:43 <--> 2:19",
    "[11, 19, 43, 78, 88, 98, 27]",
    "swap 5:98 <--> 6:27",
    "[11, 19, 43, 78, 88, 27, 98]",
    "swap 4:88 <--> 5:27",
    "[11, 19, 43, 78, 27, 88, 98]",
    "swap 3:78 <--> 4:27",
    "[11, 19, 43, 27, 78, 88, 98]",
    "swap 2:43 <--> 3:27",
    "[11, 19, 27, 43, 78, 88, 98]",
    "----------------------------------------------",
]))

total_tests+= 1
expected = [11, 19, 27, 43, 78, 88, 98]
if expected == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", li)


test_name = "Test 2 - b"
print(f"---- {test_name} ----------------------------")


total_tests+= 1
expected = [((1, 98), (2, 43)), ((0, 88), (1, 43)), ((2, 98), (3, 11)), ((1, 88), (2, 11)), ((0, 43), (1, 11)), ((3, 98), (4, 78)), ((2, 88), (3, 78)), ((4, 98), (5, 19)), ((3, 88), (4, 19)), ((2, 78), (3, 19)), ((1, 43), (2, 19)), ((5, 98), (6, 27)), ((4, 88), (5, 27)), ((3, 78), (4, 27)), ((2, 43), (3, 27))]

if expected == sort_utils.swaps:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", sort_utils.swaps)


test_name = "Test 3"
print(f"---- {test_name} ----------------------------")
orig = li = [123, 456, 267, 96, 142, 387]
li = list(orig)
insertion_sort(li)
print(li)
print("\n".join([
    "---- Expected output -------------------------",
    "[123, 456, 267, 96, 142, 387]",
    "swap 1:456 <--> 2:267",
    "[123, 267, 456, 96, 142, 387]",
    "swap 2:456 <--> 3:96",
    "[123, 267, 96, 456, 142, 387]",
    "swap 1:267 <--> 2:96",
    "[123, 96, 267, 456, 142, 387]",
    "swap 0:123 <--> 1:96",
    "[96, 123, 267, 456, 142, 387]",
    "swap 3:456 <--> 4:142",
    "[96, 123, 267, 142, 456, 387]",
    "swap 2:267 <--> 3:142",
    "[96, 123, 142, 267, 456, 387]",
    "swap 4:456 <--> 5:387",
    "[96, 123, 142, 267, 387, 456]",
    "----------------------------------------------",
]))

total_tests+= 1
expected = [96, 123, 142, 267, 387, 456]
if expected == li:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", li)


test_name = "Test 3 - b"
print(f"---- {test_name} ----------------------------")


total_tests+= 1
expected = [((1, 456), (2, 267)), ((2, 456), (3, 96)), ((1, 267), (2, 96)), ((0, 123), (1, 96)), ((3, 456), (4, 142)), ((2, 267), (3, 142)), ((4, 456), (5, 387))]

if expected == sort_utils.swaps:
    tests_passed+= 1
else:
    print(f"{test_name} failed.")
    print("Expected:", expected)
    print("Actual:", sort_utils.swaps)


# Test Results
tests_failed = total_tests - tests_passed
print("========================================")
if tests_failed == 0:
    print("All lab tests PASSED!")
else:
    print(f"{tests_failed} tests failed...")

Grading (18pts)

    (1pts) insertion.py - File exists with the above code and the proper hashbang, line endings, and permissions.
    (5pts) insertion.py - File contains a reasonable attempt and the code runs without errors.
    (6pts) insertion.py - Correct logic / Correct implementation.
    (1pt each - 6 total) insertion.lab_tests.py - Each test passes (must use the exact lab tests file from the lab).

5) Merge Sort (merge.py, merge.lab_tests.py)

Get started on your own. Details coming soon.
Grading (18pts)

    (1pts) merge.py - File exists with the proper hashbang, line endings, and permissions.
    (5pts) merge.py - File contains a reasonable attempt and the code runs without errors.
    (6pts) merge.py - Correct logic / Correct implementation.
    (1pt each - 6 total) merge.lab_tests.py - Each test passes (must use the exact lab tests file from the lab).

