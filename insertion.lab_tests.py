#!/usr/bin/env python3

import sort_utils#!/usr/bin/env python3

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
    print(f"{tests_failed} tests failed...")#!/usr/bin/env python3

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
