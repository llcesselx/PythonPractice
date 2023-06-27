# Leetcode 2: Add Two Numbers
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers adn return the sum as a linked list. 

You may assume the two numbers do not contain any leading zero, except the number 0 itself. 

![linkedlist](https://github.com/llcesselx/PythonPractice/assets/108751430/c4e4a297-cdc9-478f-abbc-b3c18e0f6e0a)

```
Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]
Explanation: 342 + 465 = 807
```
**Example 2:**
```
Input: l1 = [0], l2 = [0]
Output: [0]
```
**Example 3:**
```
Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
Output: [8, 9, 9, 9, 0, 0, 0, 1]
```

**Constraints:**
  <li>The number of nodes in each linked list is in the range [1, 100].</li>
  <li>```0 <= Node.val <= 9```</li>
  <li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
