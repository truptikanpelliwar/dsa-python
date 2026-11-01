# DSA Learning Notes — Python

My personal notes for understanding Data Structures and Algorithms through implementation and practice.

## 1. Programming Fundamentals

### What is an Algorithm?
An algorithm is a finite sequence of step-by-step instructions used to solve a problem.

### Programming vs Algorithm
- Algorithm: The logical steps to solve a problem.
- Programming: Converting those steps into executable code.

### Important Python Concepts Practised
- Variables
- Data types: `int`, `float`, `str`, `bool`
- Lists
- Conditional statements: `if`, `elif`, `else`
- Loops: `for`, `while`
- Boolean variables

## 2. Searching Algorithms

### Linear Search

**Concept:** Checks elements one by one until the target is found or the list ends.

**Requirements:** Works with both sorted and unsorted lists.

**Complexity:**
- Best case: O(1)
- Average case: O(n)
- Worst case: O(n)
- Space: O(1)

**When to use:**
- Small datasets.
- Unsorted data.
- When simplicity matters.

**Implementation:** `01-foundations/linear_search.py`

### Binary Search (Additional Practice)

**Concept:** Repeatedly divides a sorted search range into halves.

**Requirement:** Data must be sorted.

**Complexity:**
- Best case: O(1)
- Average case: O(log n)
- Worst case: O(log n)
- Space: O(1) for iterative implementation.

**Implementation:** `01-foundations/binary_search.py`

*Note: Binary Search was explored as additional practice, not part of the textbook concepts covered in this session.*

## 3. Important Concepts

### Big-O Notation
Describes how an algorithm's resource requirements grow as input size increases.

### Time Complexity
Measures how the number of operations grows with input size.

### Space Complexity
Measures the additional memory an algorithm requires.

### ADT vs Data Structure
- ADT: Describes what operations are available.
- Data Structure: Describes how data and operations are implemented.

### Abstraction
Hides unnecessary implementation details and exposes essential functionality.

### Information Hiding
Keeps internal implementation details separate from the user-facing interface.

### Trade-offs
Choosing between competing factors, such as execution speed and memory usage.

## 4. Mistakes and Lessons

- A middle index (`mid`) is different from the value at that index (`students[mid]`).
- Comparison counters should increase every time a comparison happens.
- `break` stops a loop when further searching is unnecessary.
- Binary Search requires sorted data.
- A Boolean variable can track whether an element was found.

## 5. Upcoming Concepts

- Stack ADT
- Queue ADT
- Linked Lists
- Recursion
- Big-O experiments with Python lists and dictionaries

## 6. Learning Rule

For every new concept:
1. Understand the definition.
2. Explain it in my own words.
3. Implement it without copying.
4. Test normal and edge cases.
5. Analyse time and space complexity.
6. Record mistakes and lessons learned.