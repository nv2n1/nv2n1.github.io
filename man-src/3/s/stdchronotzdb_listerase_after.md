---
title: "stdchronotzdb_listerase_after(3)"
name: "stdchronotzdb_listerase_after"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronotzdb_listerase_after/"
---

std::chrono::tzdb_list::erase_after - std::chrono::tzdb_list::erase_after

<h2>Synopsis</h2>

const_iterator erase_after(const_iterator p); <i>(since C++20)</i> 
Erases the std::chrono::tzdb referred to by the iterator following p. The behavior is undefined if that iterator is not dereferenceable. No pointers, references, or iterators are invalidated except for those referring to the erased element. 

<h2>Return value</h2>

An iterator pointing to the element following the erased element, or end() if no such element exists. 

<h2>Notes</h2>

tzdb_list is intended to be implementable as a singly linked list, and its interface resembles that of std::forward_list. It has no before_begin(), however, and so it is not possible to erase the first element. 
