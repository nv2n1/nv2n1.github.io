---
title: "stdexceptionwhat(3)"
name: "stdexceptionwhat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexceptionwhat/"
---

std::exception::what - std::exception::what

<h2>Synopsis</h2>

virtual const char* what() const throw(); <i>(until C++11)</i> 
virtual const char* what() const noexcept; <i>(since C++11)</i> 
Returns the explanatory string. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

Pointer to a null-terminated string with explanatory information. The pointer is guaranteed to be valid at least until the exception object from which it is obtained is destroyed, or until a non-const member function on the exception object is called. 
