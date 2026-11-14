---
title: "stdfilesystemrecursive_directory_iteratorrecursion_pending(3)"
name: "stdfilesystemrecursive_directory_iteratorrecursion_pending"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemrecursive_directory_iteratorrecursion_pending/"
---

std::filesystem::recursive_directory_iterator::recursion_pending - std::filesystem::recursive_directory_iterator::recursion_pending

<h2>Synopsis</h2>

bool recursion_pending() const; <i>(since C++17)</i> 
Returns true if the next increment will cause the directory currently referred to by *this to be iterated into. 
This function returns true immediately after construction or an increment. Recursion can be disabled via disable_recursion_pending(). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if the next increment will iterate into the currently referred directory, false otherwise. 

<h2>Exceptions</h2>

<i>(none)</i>
