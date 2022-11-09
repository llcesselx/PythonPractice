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

You will need to add 2 retrieval methods:
1. `._get_node(self, index)` which should return the **node** at a given index.
2. `.get_value(self, index)` which should return the **value**(`.value`) held inside the node) at a given index

Notice that the `._get_node` mehtod has a leading underscore, indicating that it is **private** to the class. Consumers of the class should not use this method, but it si fine for the class code to use it. The consumers use our Linked List implementation as a means to store a collection of data (like Python `list`), so they do not need to know anything about the implementation details we use to achieve that goal for them. The concept of a "node" should not need to have meaning to consumers since they are just storing values in a list type structure.

**HINT:** The `.get_value` method can and should call the `._get_node` method. If you can already retrive a node by index, then to retrieve the value by index you simply need to first retrieve the node, then access and `return` the data store in the `.value` attribute (`return node.value`). 

### Element Insertion and Removal

You will need to add the following methods:
1. `.insert(self, index, val)` - Inserts a node holding the value `val` at the `index` of the linked list. Remember to hook up both the `.prev` and `.next` methods for all 3 nodes involved: The node itself, the node before (if it exists) and the node after (if it exists). 
2. `.append(self, val)` - Append a value to the end of the linked list. This can be done easily if `.insert` is already implemented, simply call `.insert()` with index as the length of the list (`._length`).
3. `.prepend(self, val)` - Prepend a value to the beginning of the linked list. This can be done easily if `.insert` is already implemented, simply call `.insert()` with index as `0`.
4. `.pop(self, index)` - Removes a node form the linked list by index, `return`ing the `.value` of that node.
5. `.remove(self, val)` - Removes the first instance of a node from the linked list that is holding a `.value` equal to `val`

**NOTE:** The `_length` property should be maintained for each element's insertion or removal. See starting template below.

### Starting Template

```
def _get_node(self, index):
        pass

    def get_value(self, index):
        # Hint: Call `self._get_node(index)`
        pass

    def insert(self, index, val):
        # Hint: Use `self._get_node(index)` to get the node right before the insertion
        pass

    def append(self, val):
        # Hint: Call `self.insert()` using the `len()` as the index
        pass

    def prepend(self, val):
        # Hint: Call `self.insert()` using `0` as the index
        pass

    def remove(self, val):
        # Hint: Iterate from the start checking if `node.value == val`.
        pass

    def pop(self, index):
        # Hint: Call `self._get_node()` using index, or `len()` as the index
        pass

    def print_forward(self):
        # Iterate forward through the Linked List printing the value of each node.
        #   You may print the items out however you like as long there is a clear
        #   distinction between each element.  Here is one example, one element
        #   per line, with header and footer lines:
        print("---- DoubleLinkedList - Forward ---")
        node = self.start
        while node != None:
            print(node.value)
            node = node.next
        print("-------------------------------------")

    def print_reverse(self):
        # Iterate backward through the Linked List printing the value of each node.
        pass
```

### Lab Testing the Module (`DoubleLinkedList.lab_tests.py`)

```
#!/usr/bin/env python3

from DoubleLinkedNode import DoubleLinkedNode as Node
from DoubleLinkedList import DoubleLinkedList as List

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
desc = "The attr `.start` should default to `None`."
def test():
    dll = List()
    return dll.start
run(test, desc=desc, expected=None)


desc = "The attr `.end` should default to `None`."
def test():
    dll = List()
    return dll.end
run(test, desc=desc, expected=None)


desc = "The attr `._length` should default to `0`."
def test():
    dll = List()
    return dll._length
run(test, desc=desc, expected=0)


# ---- __len__ ---------------------------------------------------------------
desc = "The dunder `__len__` should reflect `._length` attr."
def test():
    dll = List()
    dll._length = 11
    return len(dll)
run(test, desc=desc, expected=11)


# ---- .get_value ---------------------------------------------------------------
desc = "In a 0-node list, `.get_value()` should raise an `IndexError` Exception."
def test():
    dll = List()
    dll.get_value(0) # Exception raised here
    return "SHOULD RAISE EXCEPTION"
run(test, desc=desc, exception=IndexError)


# Single-node List
desc = "In a single-node list, `.get_value()` should raise an `IndexError` Exception if the index is too high."
def test():
    dll = List()
    n = list(map(Node, [71]))
    dll.start = n[0]
    dll.end = n[0]
    dll._length = 1
    return dll.get_value(0)
run(test, desc=desc, expected=71)


desc = "In a single-node list, `.get_value()` should raise an `IndexError` Exception if the index is too high."
def test():
    dll = List()
    n = list(map(Node, [71]))
    dll.start = n[0]
    dll.end = n[0]
    dll._length = 1
    dll.get_value(1) # Exception raised here
    return "SHOULD RAISE EXCEPTION"
run(test, desc=desc, exception=IndexError)


desc = "In a single-node list, `.get_value()` should raise an `IndexError` Exception if the index is too low."
def test():
    dll = List()
    n = list(map(Node, [71]))
    dll.start = n[0]
    dll.end = n[0]
    dll._length = 1
    dll.get_value(-2) # Exception raised here
    return "SHOULD RAISE EXCEPTION"
run(test, desc=desc, exception=IndexError)


# Multi-node List
desc = "(1/3) In a multi-node list, `.get_value()` should return the corresponding element value."
def test():
    dll = List()
    n = list(map(Node, [71, 72, 73]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    return dll.get_value(0)
run(test, desc=desc, expected=71)


desc = "(2/3) In a multi-node list, `.get_value()` should return the corresponding element value."
def test():
    dll = List()
    n = list(map(Node, [71, 72, 73]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    return dll.get_value(1)
run(test, desc=desc, expected=72)


desc = "(3/3) In a multi-node list, `.get_value()` should return the corresponding element value."
def test():
    dll = List()
    n = list(map(Node, [71, 72, 73]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    return dll.get_value(2)
run(test, desc=desc, expected=73)


# ---- .insert() ---------------------------------------------------------------
desc = "`.insert()` links the `.start` attribute correctly."
def test():
    dll = List()
    dll.insert(0, 30)
    return dll.start.value
run(test, desc=desc, expected=30)


desc = "A call to `.insert()` links the `.end` attribute correctly."
def test():
    dll = List()
    dll.insert(0, 40)
    return dll.end.value
run(test, desc=desc, expected=40)


dll = List()
desc = "(1/4) - Multiple `.insert()` calls assign the appropriate nodes to `.start` and `.end`."
def test():
    global dll
    dll.insert(0, 51)
    if dll.start.value != 51 or dll.end.value != 51:
        return False
    return True
run(test, desc=desc, expected=True)


desc = "(2/4) - Multiple `.insert()` calls assign the appropriate nodes to `.start` and `.end`."
def test():
    global dll
    dll.insert(0, 50)
    if dll.start.value != 50 or dll.end.value != 51:
        return False
    return True
run(test, desc=desc, expected=True)


desc = "(3/4) - Multiple `.insert()` calls assign the appropriate nodes to `.start` and `.end`."
def test():
    global dll
    dll.insert(len(dll), 53)
    if dll.start.value != 50 or dll.end.value != 53:
        return False
    return True
run(test, desc=desc, expected=True)


desc = "(4/4) - Multiple `.insert()` calls assign the appropriate nodes to `.start` and `.end`."
def test():
    global dll
    dll.insert(2, 52)
    if dll.start.value != 50 or dll.end.value != 53:
        return False
    return True
run(test, desc=desc, expected=True)


desc = "Multiple `.insert()` calls to the beginning of the list assign all the nodes' `.next` attributes correctly."
def test():
    dll = List()
    dll.insert(0, 83)
    dll.insert(0, 82)
    dll.insert(0, 81)
    dll.insert(0, 80)
    return dll.start.next.next.next.value
run(test, desc=desc, expected=83)


desc = "Multiple `.insert()` calls to the beginning of the list assign all the nodes' `.prev` attributes correctly."
def test():
    dll = List()
    dll.insert(0, 83)
    dll.insert(0, 82)
    dll.insert(0, 81)
    dll.insert(0, 80)
    return dll.end.prev.prev.prev.value
run(test, desc=desc, expected=80)


desc = "Multiple `.insert()` calls to the end of the list assign all the nodes' `.next` attributes correctly."
def test():
    dll = List()
    dll.insert(len(dll), 83)
    dll.insert(len(dll), 82)
    dll.insert(len(dll), 81)
    dll.insert(len(dll), 80)
    return dll.start.next.next.next.value
run(test, desc=desc, expected=80)


desc = "Multiple `.insert()` calls to the end of the list assign all the nodes' `.prev` attributes correctly."
def test():
    dll = List()
    dll.insert(len(dll), 83)
    dll.insert(len(dll), 82)
    dll.insert(len(dll), 81)
    dll.insert(len(dll), 80)
    return dll.end.prev.prev.prev.value
run(test, desc=desc, expected=83)


desc = "A call to `.insert()` with an index too large raises an `IndexError` or adds to the end of the list."
def test():
    dll = List()
    dll.insert(0, 80)
    dll.insert(1, 81)
    dll.insert(3, 83) # Exception may be raised here
    return dll.get_value(2) == 83
run(test, desc=desc, exception=IndexError)


desc = "A call to `.insert()` with an index too small (beyond a valid negative index) raises an `IndexError` or adds to the beginning of the list."
def test():
    dll = List()
    dll.insert(0, 80)
    dll.insert(1, 81)
    dll.insert(-3, 83) # Exception may be raised here
    return dll.get_value(0) == 83
run(test, desc=desc, exception=IndexError)


# ---- .append() ---------------------------------------------------------------
desc = "A call to `.append()` to an empty list assigns `.start` appropriately."
def test():
    dll = List()
    dll.append(100)
    return dll.start.value
run(test, desc=desc, expected=100)


desc = "A call to `.append()` to an empty list assigns `.end` appropriately."
def test():
    dll = List()
    dll.append(100)
    return dll.end.value
run(test, desc=desc, expected=100)


desc = "A call to `.append()` to a non-empty list assigns `.start` appropriately."
def test():
    dll = List()
    dll.append(100)
    dll.append(101)
    return dll.start.value
run(test, desc=desc, expected=100)


desc = "A call to `.append()` to a non-empty list assigns `.end` appropriately."
def test():
    dll = List()
    dll.append(100)
    dll.append(101)
    return dll.end.value
run(test, desc=desc, expected=101)


desc = "A call to `.append()` to a non-empty list links the nodes appropriately."
def test():
    dll = List()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    v = f"{dll.start.value}{dll.start.next.value}{dll.start.next.next.value}"
    v+= f"{dll.end.value}{dll.end.prev.value}{dll.end.prev.prev.value}"
    return v
run(test, desc=desc, expected="123321")


# ---- .prepend() ---------------------------------------------------------------
desc = "A call to `.prepend()` to an empty list assigns `.start` appropriately."
def test():
    dll = List()
    dll.prepend(100)
    return dll.start.value
run(test, desc=desc, expected=100)


desc = "A call to `.prepend()` to an empty list assigns `.end` appropriately."
def test():
    dll = List()
    dll.prepend(100)
    return dll.end.value
run(test, desc=desc, expected=100)


desc = "A call to `.prepend()` to a non-empty list assigns `.start` appropriately."
def test():
    dll = List()
    dll.prepend(100)
    dll.prepend(101)
    return dll.start.value
run(test, desc=desc, expected=101)


desc = "A call to `.prepend()` to a non-empty list assigns `.end` appropriately."
def test():
    dll = List()
    dll.prepend(100)
    dll.prepend(101)
    return dll.end.value
run(test, desc=desc, expected=100)


desc = "A call to `.prepend()` to a non-empty list links the nodes appropriately."
def test():
    dll = List()
    dll.prepend(1)
    dll.prepend(2)
    dll.prepend(3)
    v = f"{dll.start.value}{dll.start.next.value}{dll.start.next.next.value}"
    v+= f"{dll.end.value}{dll.end.prev.value}{dll.end.prev.prev.value}"
    return v
run(test, desc=desc, expected="321123")

# ---- .remove() ---------------------------------------------------------------
desc = "A call to `.remove()` to an empty list should raise a `ValueError`."
def test():
    dll = List()
    dll.remove(1) # Exception raised here
    return "SHOULD RAISE EXCEPTION"
run(test, desc=desc, exception=ValueError)


desc = "A call to `.remove()` to a non-empty list that does not contain the value should raise a `ValueError`."
def test():
    dll = List()
    n = list(map(Node, [0, 1, 2]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    dll.remove(5) # Exception raised here
    return "SHOULD RAISE EXCEPTION"
run(test, desc=desc, exception=ValueError)


desc = "(1/4) - A call to `.remove()` to a non-empty list that does contain the value should link the nodes properly."
def test():
    dll = List()
    n = list(map(Node, [9, 8, 7]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    dll.remove(9)
    v = f"{dll.start.value}{dll.start.next.value}"
    v+= f"{dll.end.value}{dll.end.prev.value}"
    return v
run(test, desc=desc, expected="8778")


desc = "(2/4) - A call to `.remove()` to a non-empty list that does contain the value should link the nodes properly."
def test():
    dll = List()
    n = list(map(Node, [9, 8, 7]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    dll.remove(8)
    v = f"{dll.start.value}{dll.start.next.value}"
    v+= f"{dll.end.value}{dll.end.prev.value}"
    return v
run(test, desc=desc, expected="9779")


desc = "(3/4) - A call to `.remove()` to a non-empty list that does contain the value should link the nodes properly."
def test():
    dll = List()
    n = list(map(Node, [9, 8, 7]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    dll.remove(7)
    v = f"{dll.start.value}{dll.start.next.value}"
    v+= f"{dll.end.value}{dll.end.prev.value}"
    return v
run(test, desc=desc, expected="9889")


desc = "(4/4) - A call to `.remove()` to a non-empty list that does contain the value should link the nodes properly."
def test():
    dll = List()
    n = list(map(Node, [9]))
    dll.start = n[0]
    dll.end = n[0]
    dll._length = 1
    dll.remove(9)
    v = f"{dll.start}"
    v+= f"{dll.end}"
    v+= f"{dll._length}"
    return v
run(test, desc=desc, expected="NoneNone0")


# ---- .pop() ---------------------------------------------------------------
desc = "A call to `.pop()` to an empty list should raise an `IndexError`."
def test():
    dll = List()
    dll.pop() # Exception raised here
    return "SHOULD RAISE EXCEPTION"
run(test, desc=desc, exception=IndexError)


desc = "A call to `.pop()` to a non-empty list should remove the node, return its value, and link the other nodes."
def test():
    dll = List()
    n = list(map(Node, [0, 1, 2]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    v = f"{dll.pop()}"
    v+= f"{dll.start.value}{dll.start.next.value}{dll.start.next.next}"
    v+= f"{dll.end.value}{dll.end.prev.value}{dll.end.prev.prev}"
    v+= f"{dll._length}"
    return v
run(test, desc=desc, expected="201None10None2")


desc = "A call to `.pop(dll._length-1)` to a non-empty list should remove the node, return its value, and link the other nodes."
def test():
    dll = List()
    n = list(map(Node, [0, 1, 2]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    v = f"{dll.pop(dll._length-1)}"
    v+= f"{dll.start.value}{dll.start.next.value}{dll.start.next.next}"
    v+= f"{dll.end.value}{dll.end.prev.value}{dll.end.prev.prev}"
    v+= f"{dll._length}"
    return v
run(test, desc=desc, expected="201None10None2")


desc = "A call to `.pop(0)` to a non-empty list should remove the node, return its value, and link the other nodes."
def test():
    dll = List()
    n = list(map(Node, [0, 1, 2]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    v = f"{dll.pop(0)}"
    v+= f"{dll.start.value}{dll.start.next.value}{dll.start.next.next}"
    v+= f"{dll.end.value}{dll.end.prev.value}{dll.end.prev.prev}"
    v+= f"{dll._length}"
    return v
run(test, desc=desc, expected="012None21None2")


desc = "A call to `.pop(1)` to a non-empty list should remove the node, return its value, and link the other nodes."
def test():
    dll = List()
    n = list(map(Node, [0, 1, 2]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    v = f"{dll.pop(1)}"
    v+= f"{dll.start.value}{dll.start.next.value}{dll.start.next.next}"
    v+= f"{dll.end.value}{dll.end.prev.value}{dll.end.prev.prev}"
    v+= f"{dll._length}"
    return v
run(test, desc=desc, expected="102None20None2")


desc = "A call to `.pop(0)` to a two-element list should remove the node, return its value, and link the other nodes."
def test():
    dll = List()
    n = list(map(Node, [0, 1]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.end = n[1]
    dll.end.prev = n[0]
    dll._length = 2
    v = f"{dll.pop(0)}"
    v+= f"{dll.start.value}{dll.start.next}"
    v+= f"{dll.end.value}{dll.end.prev}"
    v+= f"{dll._length}"
    return v
run(test, desc=desc, expected="01None1None1")


desc = "A call to `.pop(1)` to a two-element list should remove the node, return its value, and link the other nodes."
def test():
    dll = List()
    n = list(map(Node, [0, 1]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.end = n[1]
    dll.end.prev = n[0]
    dll._length = 2
    v = f"{dll.pop(1)}"
    v+= f"{dll.start.value}{dll.start.next}"
    v+= f"{dll.end.value}{dll.end.prev}"
    v+= f"{dll._length}"
    return v
run(test, desc=desc, expected="10None0None1")


desc = "A call to `.pop(0)` to a single-element list should remove the node, return its value, and link the other nodes."
def test():
    dll = List()
    n = list(map(Node, [0]))
    dll.start = n[0]
    dll.end = n[0]
    dll._length = 1
    v = f"{dll.pop(0)}"
    v+= f"{dll.start}"
    v+= f"{dll.end}"
    v+= f"{dll._length}"
    return v
run(test, desc=desc, expected="0NoneNone0")





#===================================================================
# ---- .get_value ---------------------------------------------------------------
# Multi-node List
desc = "(1/3) In a multi-node list, `.get_value()` with a negative index should return the corresponding element value."
def test():
    dll = List()
    n = list(map(Node, [71, 72, 73]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    return dll.get_value(-3)
run(test, desc=desc, expected=71)


desc = "(2/3) In a multi-node list, `.get_value()` with a negative index should return the corresponding element value."
def test():
    dll = List()
    n = list(map(Node, [71, 72, 73]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    return dll.get_value(-2)
run(test, desc=desc, expected=72)


desc = "(3/3) In a multi-node list, `.get_value()` with a negative index should return the corresponding element value."
def test():
    dll = List()
    n = list(map(Node, [71, 72, 73]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    return dll.get_value(-1)
run(test, desc=desc, expected=73)


# ---- .insert() ---------------------------------------------------------------
desc = "In a 0-node list `.insert()` with a negative index inserts the first item."
def test():
    dll = List()
    dll.insert(0, 33)
    v = f"{dll.start.value}"
    v+= f"{dll.end.value}"
    return v
run(test, desc=desc, expected="3333")


desc = "(1/2) In a multi-node list `.insert()` with a negative index inserts the items at the correct locations."
def test():
    dll = List()
    n = list(map(Node, [71, 72]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.end = n[1]
    dll.end.prev = n[0]
    dll._length = 2
    dll.insert(-1, 33)
    v = f"{dll.start.value}{dll.start.next.value}{dll.start.next.next.value}{dll.start.next.next.next}"
    v+= f"{dll.end.value}{dll.end.prev.value}{dll.end.prev.prev.value}{dll.end.prev.prev.prev}"
    return v
run(test, desc=desc, expected="713372None723371None")


desc = "(2/2) In a multi-node list `.insert()` with a negative index inserts the items at the correct locations."
def test():
    dll = List()
    n = list(map(Node, [71, 72]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.end = n[1]
    dll.end.prev = n[0]
    dll._length = 2
    dll.insert(-2, 33)
    v = f"{dll.start.value}{dll.start.next.value}{dll.start.next.next.value}{dll.start.next.next.next}"
    v+= f"{dll.end.value}{dll.end.prev.value}{dll.end.prev.prev.value}{dll.end.prev.prev.prev}"
    return v
run(test, desc=desc, expected="337172None727133None")


# ---- .pop() ---------------------------------------------------------------
desc = "(1/3) In a multi-node list `.pop()` with a negative removes the appropriate node and returns its value."
def test():
    dll = List()
    n = list(map(Node, [7, 8, 9]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    val = dll.pop(-1)
    v = f"{val}"
    v+= f"{dll.start.value}{dll.start.next.value}{dll.start.next.next}"
    v+= f"{dll.end.value}{dll.end.prev.value}{dll.end.prev.prev}"
    return v
run(test, desc=desc, expected="978None87None")


desc = "(2/3) In a multi-node list `.pop()` with a negative removes the appropriate node and returns its value."
def test():
    dll = List()
    n = list(map(Node, [7, 8, 9]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    val = dll.pop(-2)
    v = f"{val}"
    v+= f"{dll.start.value}{dll.start.next.value}{dll.start.next.next}"
    v+= f"{dll.end.value}{dll.end.prev.value}{dll.end.prev.prev}"
    return v
run(test, desc=desc, expected="879None97None")


desc = "(3/3) In a multi-node list `.pop()` with a negative removes the appropriate node and returns its value."
def test():
    dll = List()
    n = list(map(Node, [7, 8, 9]))
    dll.start = n[0]
    dll.start.next = n[1]
    dll.start.next.next = n[2]
    dll.end = n[2]
    dll.end.prev = n[1]
    dll.end.prev.prev = n[0]
    dll._length = 3
    val = dll.pop(-3)
    v = f"{val}"
    v+= f"{dll.start.value}{dll.start.next.value}{dll.start.next.next}"
    v+= f"{dll.end.value}{dll.end.prev.value}{dll.end.prev.prev}"
    return v
run(test, desc=desc, expected="789None98None")


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
Name the file correctly or you will receive **zero points**. Similarly make sure the files are executable, containt the hashbang, and contain no carriage returns
1. **(8pts)** - File `DoubleLinkedList.py` has class `DoubleLinkedList` with an initializer that works, setting the specified attributes correctly.
2. **(5pts)** - File `DoubleLinkedList.py`, when run directly (but not when imported), program executes own tests without errors. You must reasonably attempt to test several aspects of your program for full credit (40 lines of code or so under `if __name__ == "__main__"`).
3. **(56pts, 1pt for each test passed)** - File `DoubleLinkedList.lab_tests.py`, when run directluy, will pass all of the tests without cheating. 
