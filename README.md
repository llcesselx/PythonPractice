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
