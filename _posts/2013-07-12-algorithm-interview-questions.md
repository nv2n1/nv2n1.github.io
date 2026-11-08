---
title: "Algorithm Interview Questions: Data Structures and Search"
date: 2013-07-12 16:47:41 +0000
modified: 2026-04-11 17:51:44 +0000
author: "Eric Ma"
layout: post
categories: [development-best-practices]
permalink: /algorithm-interview-questions/
canonical: /algorithm-interview-questions/
---

This post walks through common algorithm and data-structure questions that come up in software engineering interviews, with worked explanations of the tradeoffs behind each answer.

Understanding tradeoffs between these structures is essential for algorithm design:

- **Memory allocation**: Arrays use contiguous memory (better cache locality); linked lists scatter across memory with pointer references
- **Access time**: Array O(1) random access; linked list O(n) traversal required
- **Insertion/deletion**: Arrays require O(n) shifts; linked lists require O(1) pointer updates when position is known
- **Size**: Arrays have fixed capacity (dynamic arrays resize with amortized O(1)); linked lists grow dynamically without reallocation
- **Cache performance**: Arrays dominate due to spatial locality; linked lists suffer cache misses

## Sorting Linked Lists with Merge Sort

Merge sort is the optimal choice for linked lists—O(n log n) time and O(log n) space for the recursion stack. Unlike quicksort, it requires no random access and performs consistently regardless of input distribution.

``` python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(l1, l2):
    """Merge two sorted linked lists"""
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach remaining nodes
    current.next = l1 if l1 else l2
    return dummy.next

def merge_sort_list(head):
    """Sort linked list using merge sort"""
    if not head or not head.next:
        return head

    # Find middle using slow/fast pointer technique
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Split list at middle
    mid = slow.next
    slow.next = None

    left = merge_sort_list(head)
    right = merge_sort_list(mid)

    return merge_sorted_lists(left, right)
```

The slow/fast pointer approach avoids materializing the middle index—a natural fit for linked list traversal without random access.

## Sorting Arrays with Quicksort

Quicksort remains standard for arrays despite O(n²) worst-case complexity—average O(n log n) performance, superior cache locality, and in-place operation make it practical. Production implementations often use introsort, switching to heapsort if recursion depth exceeds 2⌊log n⌋ to prevent pathological cases.

``` python
def quicksort(arr, low=0, high=None):
    """Sort array using quicksort algorithm"""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

    return arr

def partition(arr, low, high):
    """Partition array around pivot"""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

For production code, use Python’s built-in `sorted()` (Timsort) unless you need in-place sorting or specific memory constraints. The `sorted()` function handles edge cases and performs optimizations automatically.

## String Searching with KMP Algorithm

Implement substring search with O(n + m) time complexity using the Knuth-Morris-Pratt algorithm, avoiding naive O(n·m) scanning:

``` python
def strstr(haystack, needle):
    """Find first occurrence of needle in haystack using KMP"""
    if not needle:
        return 0
    if len(needle) > len(haystack):
        return -1

    # Build failure function (prefix table)
    def build_failure_table(pattern):
        table = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = table[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            table[i] = j
        return table

    failure = build_failure_table(needle)
    j = 0

    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = failure[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            return i - len(needle) + 1

    return -1
```

The failure table encodes how to skip comparisons when mismatches occur, eliminating backtracking. This is superior to Python’s built-in `str.find()` for interview contexts where you need to demonstrate algorithmic knowledge, though in production code `str.find()` is preferable.

## String Reversal

For standard use, Python’s slice notation is idiomatic and optimal:

``` python
def reverse_string(s):
    """Reverse string using slice"""
    return s[::-1]
```

For in-place reversal on mutable sequences (lists):

``` python
def reverse_string_inplace(s):
    """Reverse list in-place"""
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

The slice approach creates O(n) temporary space for immutable strings—unavoidable due to string immutability. The two-pointer approach is O(1) space for lists.

## Cycle Detection in Linked Lists

Floyd’s cycle detection (tortoise and hare) uses O(1) space and O(n) time:

``` python
def has_cycle(head):
    """Detect if linked list contains a cycle"""
    if not head:
        return False

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

def find_cycle_start(head):
    """Return the node where cycle begins, or None if no cycle"""
    if not head:
        return None

    slow = fast = head

    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    # Find cycle start: move slow to head, advance both one step at a time
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
```

When slow and fast pointers meet, a cycle exists. By resetting slow to head and advancing both at speed 1, they meet at the cycle start. This works because the distance from head to cycle start equals the distance from the meeting point to the cycle start—a mathematical property of the two-pointer technique.

## Fisher-Yates Shuffle

Generate uniformly random permutations in O(n) time and O(1) extra space:

``` python
import random

def shuffle(arr):
    """Shuffle array in-place using Fisher-Yates algorithm"""
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
```

Iterate backward through the array, swapping each element with a randomly selected element from the range \[0, i\]. This ensures uniform distribution—crucial for algorithms like randomized quicksort. Avoid naive shuffle approaches (randomly swapping any two elements) as they produce skewed distributions.

## String to Integer Conversion

Parse signed integers with boundary checking:

``` python
def parse_int(s):
    """Convert string to integer, returning None if invalid"""
    if not s or not isinstance(s, str):
        return None

    s = s.strip()
    if not s:
        return None

    start = 0
    sign = 1

    if s[0] in ['+', '-']:
        sign = -1 if s[0] == '-' else 1
        start = 1

    result = 0
    for i in range(start, len(s)):
        if not s[i].isdigit():
            return None
        result = result * 10 + int(s[i])

    return result * sign
```

Handle leading whitespace and optional sign. For production code, prefer Python’s built-in `int(s)` with exception handling for robustness. This implementation demonstrates manual parsing logic expected in interviews.

## Generating All Permutations

Recursively generate permutations by selecting each element as the first item:

``` python
def permute(elements):
    """Generate all permutations of elements"""
    if len(elements) <= 1:
        return [elements]

    result = []
    for i in range(len(elements)):
        current = elements[i]
        remaining = elements[:i] + elements[i+1:]
        for perm in permute(remaining):
            result.append([current] + perm)

    return result
```

This has O(n!) time complexity (unavoidable for n! outputs) and O(n!) space for storing results. For larger inputs or streaming use cases, use a generator to reduce memory overhead:

``` python
def permute_generator(elements):
    """Generate permutations one at a time"""
    if len(elements) <= 1:
        yield elements
    else:
        for i in range(len(elements)):
            current = elements[i]
            remaining = elements[:i] + elements[i+1:]
            for perm in permute_generator(remaining):
                yield [current] + perm
```

## Sorted Array to Balanced Binary Search Tree

Build a height-balanced BST from a sorted array by recursively choosing the middle element:

``` python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sorted_array_to_bst(arr):
    """Convert sorted array to height-balanced BST"""
    def build(low, high):
        if low > high:
            return None

        mid = (low + high) // 2
        node = TreeNode(arr[mid])
        node.left = build(low, mid - 1)
        node.right = build(mid + 1, high)

        return node

    return build(0, len(arr) - 1)
```

Selecting the middle element ensures O(log n) height and balanced structure. Time complexity is O(n), space is O(log n) for recursion stack on a balanced tree.

## Level-Order Tree Traversal

Use a queue to traverse the tree by level, useful for serialization and tree analysis:

``` python
from collections import deque

def level_order_traversal(root):
    """Return list of lists, each containing one level's node values"""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

Track `level_size` before processing to avoid mixing levels—critical for correct grouping. Use `deque` from `collections` for O(1) popleft operations rather than lists.

## Reversing a Linked List

Iterative approach with proper pointer management:

``` python
def reverse_linked_list(head):
    """Reverse linked list iteratively"""
    prev = None
    current = head

    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    return prev
```

Recursive variant (use cautiously—stack depth equals list length, risking stack overflow on large lists):

``` python
def reverse_linked_list_recursive(head, prev=None):
    """Reverse linked list recursively"""
    if not head:
        return prev

    next_temp = head.next
    head.next = prev
    return reverse_linked_list_recursive(next_temp, head)
```

Prefer the iterative approach for production code—constant O(1) stack space versus O(n) recursion depth. Test both with empty lists and single-node lists to verify boundary handling. The iterative version is also more readable and performs better on systems with stack size limits.
