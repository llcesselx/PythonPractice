# Linked Lists Lab

Each branch is a seperate lab that was required for cS201 - Programming Structures

## Description
  In this lab you will be creating a data structure called a **Double Linked List** . This data strcuture represents a **collection** of values. You can think of it like a very simple Python `list`. The idea is that each **node** is a container that holds one of the collection's values. Each node (`n`) also holds a memory reference to the **next node** in the collection (`n.next`) as well as a memory reference to the **previous node** in the collection (`n.prev`).

### Single Linked List with 3 Values
  To help you understand Double Linked Lists, we can start with a visualization of the simpler Single Linked List. Here, the `Node` class was used to create all the node object instances (this is a single linked list node, which is a different class and object than a double linked list node, though they are named the same). Each instance of this single linked list node has `.next` property that points to the memory location of the  next node instance. The `SSL` class is used to create an instance of a singled linked list object. Here there is only one instance of the single linked list because we are only using one list. You could imagine multiple linked list instances in a program htough, just like how we use multiple Python `list` instances in some programs. Finally, notice that the last node's `.next` attribute points to the `None` value because there are no more nodes. We could extend this Single Linked List by simply setting this node's `.next` attribute to the memory location of another node. 
  
![Single Linked List](https://i.ibb.co/xM99Fw3/singlelink1.png)

### Double Linked List with 3 Values
  Now with the double linked list, we must create a new and different `Node` class because we need to use an additional attribute called `.prev`. Just like the `.next` attribute is meant to hold memory location of the next node, the `.prev` attribute is meant to hold the memory location of the previous node. And similarly, the first node in the double liniked list has no previous node, so it holds the `None` value.
  
  ![Double Linked List](https://i.ibb.co/K9wL0VC/doublelink1.png)
  
  ## Lab Problems 
  
 ### 1) Double Linked Node as a Module (`DoubleLinkedNode.py`)
 Create the Python 3 module file `DoubleLinkedNode.py`. In this file you will create a **class** of the same name (`DoubleLinkedNode`). The initializer (`__init__`) will of course define the `self` **parameter**, and it will define one additional **parameter** called `val` which will hold an arbitrary value for us (just as a Python3) `list` holds arbitrary data in each position). In the body of the initializer you will attach and initialize 3 **attributes**. The first will be `.value` which we assign to `val`. The second attribute will be the `.next`, the third attribute will be `.prev`, which is meant to hold reference (memory location) to the previous node in the linked list, and it too will default to the `None` value. 
 
 ```
 class DoubleLinkedNode: 
  
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
```

Create your own testing section in this module using hte `if __name__ == "__main__":` conditional to verify that the node is correctly implemented as we have done in the lectures.

### Lab Testing the Module `DoublelinkedNode.lab_tests.py`

As usual, we will test this module with a predefined test suite. Copy the following code to a file called `DoubleLinkedNode.lab_tests.py`. Run it to see if your module is working appropriately. 

```
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
```

## Grading
Name the file correclty or you will receive **zero points**. Similarly, make sure the files are executable, contain the hashbang, and contain no carriage returns. 
<ol>
  <li>(**5pts**) - File `DoubleLinkedNode.py` has class `DoubleLinkedNode` with an initializer that works, setting the specified attributes correctly, and has some of your own tests.</li>
   <li>(**5pts**) - File `DoubleLinkedNode.py`, when run directly but not when imported, program executes your own tests without errors. You must reasonably attempt to test all of the aspects of your program for full credit.</li>
    <li>(**10pts, 2pts for each test passed**) - File `DoubleLinkedNode.lab_tests.py`, when run directly, will pass all of the tests without cheating</li>
</ol> 
   
## Double Linked List as a Module (`DoubleLinkedList.py`)

Create the Python 3 module file `DoubleLinkedList.py`. In this file you will need to import the `DoubleLinkedNode` **class** from the **module** of the same name. We will rename the import as simply `Node` to reduce the amount of typing we need to do.

```
from DoubleLinkedNode import DoubleLinkedNode as Node
```
Next you will create a **class** called `DoubleLinkedList`. The initializer will not take any arguments. The initializer should attach 3 **attributes** to the object instance: 
1. `.start` which is meant to hold a reference (memory location) of the first node in the Linked List (or `None` in the case of an empty list).
2. `.end` which will point to the last node in the Linked List (or `None` in the case of an empty list). 
3. `._length` which will track the number of nodes in our list, and it will be maintained (updated) every tmie a list element is added or removed. 

```
class DoubleLinkedList:
   def __init__(self):
       self._length = 0
       self.start = None
       self.end = None

      # allows use of global `len()` function,
      # as in `len(my_dll_instance)`
      def __len__(self):
          return self._length
```

***IMPORTANT*** - Notice the underscore character (`_`) leading the attribute name `_length` here. This is a **convention** that tells anyone who uses our class (called a **consumer** of our code) that they are not to touch this class attribute. This attribute is considered to be **private** to the class, meaning if the consumer modifies it directly, then the functionality of the class could fail. This makes sense because we don't want people manuallhy chaning the length attribute of the list without adding or removing elements. We need this attribute's value to be in sync with the number of nodes in our Linked List. So creating attributes or methods on a class with a leading underscore is a common convention (and a good practice) when the data or method should not be touched by anything outside of the class code itself. -- To clarify, a **consumer** of the class imports the class and uses it , and consumers should not touch those attributes and methods with leading underscores. However the code in the class definition itself can freely access and modify those attributes and methods. 

### Print Methods

You will need the following 2 print methods. These will help yo udebug problems with your code. 
1. `.print_forward(self)` - This method will **iterate forward** throught the linked list, starting at the node `self.start`, printing each value, one value per line.
2. `.print_reverse(self)` - This method does the same as `.print_forward`, but it will instead **iterate backward** through the linked list starting from `self.end`, printing one element per line.

**HINT:** See template below on how to implement `.print_forward`. You will have to implement `.print_backward` on your own.

### Node Retrieval vs. Value Retrieval
