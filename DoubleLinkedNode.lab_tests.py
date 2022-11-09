#!/usr/bin/env python3

from DoubleLinkedNode import DoubleLinkedNode as Node

# Test suite variables
suite = {
    "count": 0,
    "results": [],
}

def run(*args, desc=None, exception=None, expected=True, verbose=False):
    fn = args[0]
    args = args[1:]
    suite["count"]+=1
    dsc = ""
    if desc != None:
        dsc += f"{desc}"
    result_str = f"{dsc}"
    if verbose:
        print(f"---- Test {suite['count']} ----")
        print(f"{dsc}")
    try:
        result = fn(*args)
        if result == expected:
            suite["results"].append((suite["count"], "Passed", dsc, f"Expected {type(expected)}: `{expected}`, but got {type(result)}: `{result}`."))
        else:
            suite["results"].append((suite["count"], "Failed", dsc, f"Expected {type(expected)}: `{expected}`, but got {type(result)}: `{result}`."))
    except Exception as e:
        if exception and type(e) is exception:
            suite["results"].append((suite["count"], "Passed", dsc, f"Exception correct. {type(e)}: `{e}`."))
        elif exception:
            suite["results"].append((suite["count"], "Failed", dsc, f"Exception incorrect. Expected {type(exception)}: `{exception}`, but got {type(e)}: `{e}`."))
        else:
            suite["results"].append((suite["count"], "Failed", dsc, f"Expected {type(expected)}: `{expected}`, but got Exception {type(e)}: `{e}`."))
    if verbose:
        r = suite["results"][-1]
        if r[1] == "Failed":
            print(f"  FAILED!")
            print(f"    {r[3]}")
        else:
            print("  Passed.")


# ================================================
# Test Cases
# ================================================
# ---- Attribute defaults ---------------------------------------------------------------
desc = "The attr `.value` should default to the __init__ argument passed in."
def test():
    n = Node(7)
    return n.value
run(test, desc=desc, expected=7)


desc = "The attr `.next` should default to `None`."
def test():
    n = Node(7)
    return n.next
run(test, desc=desc, expected=None)


desc = "The attr `.prev` should default to `None`."
def test():
    n = Node(7)
    return n.prev
run(test, desc=desc, expected=None)


desc = "Attaching a new node to the attr `.next` and `.prev` appropriately should make the original value accessible."
def test():
    n = Node(7)
    n2 = Node(8)
    n.next = n2
    n2.prev = n
    return n.next.prev.value
run(test, desc=desc, expected=7)


desc = "Attaching a new node to the attr `.next` and `.prev` appropriately should make the original value accessible."
def test():
    n = Node(7)
    n2 = Node(8)
    n.next = n2
    n2.prev = n
    return n2.prev.next.value
run(test, desc=desc, expected=8)


# ================================================
# Test Results
# ================================================
failed = [ r for r in suite["results"] if r[1] == "Failed" ]
num_failed = len(failed)
num_passed = suite["count"] - num_failed

print(f"==== {'Test Results ':=<54}")
if num_passed == suite["count"]:
    print(f"  PASSED all {num_passed}/{suite['count']} tests!")
else:
    print(f"  FAILED {num_failed}/{suite['count']} tests:")
    for f in failed:
        print(f"    Test {f[0]}: {f[2]}")
        print(f"      {f[3]}")
    print(f"  PASSED {num_passed}/{suite['count']} tests.")
    print(f"  FAILED {num_failed}/{suite['count']} tests.")
