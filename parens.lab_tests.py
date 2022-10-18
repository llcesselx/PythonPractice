#!/usr/bin/env python3

from parens import in_parens

all_passed = True

test = "(test1)"
if in_parens(test) != "test1":
    print("Test 1 failed.")
    all_passed = False

test = "next (test2)"
if in_parens(test) != "test2":
    print("Test 2 failed.")
    all_passed = False

test = "(test3) prev"
if in_parens(test) != "test3":
    print("Test 3 failed.")
    all_passed = False

test = "--(test4)--"
if in_parens(test) != "test4":
    print("Test 4 failed.")
    all_passed = False

test = "()"
if in_parens(test) != "":
    print("Test 5 failed.")
    all_passed = False

test = "--()"
if in_parens(test) != "":
    print("Test 6 failed.")
    all_passed = False

test = "Hi"
if in_parens(test) != None:
    print("Test 7 failed.")
    all_passed = False

test = ""
if in_parens(test) != None:
    print("Test 8 failed.")
    all_passed = False

test = "Look ) at ( this"
if in_parens(test) != None:
    print("Test 9 failed.")
    all_passed = False

test = "Look ) at (this) now"
if in_parens(test) != "this":
    print("Test 10 failed.")
    all_passed = False

if all_passed:
    print("All tests PASSED!")
