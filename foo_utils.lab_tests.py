#!/usr/bin/env python3

import foo_utils

foo_utils.foo_says("The lab defined this test!!")
foo_utils.foo_name = "I changed this"
foo_utils.foo_says(f"Testing version {foo_utils.version}...")

print("All lab tests PASSED!")
