---
title: "stderror_categorydefault_error_condition(3)"
name: "stderror_categorydefault_error_condition"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_categorydefault_error_condition/"
---

std::error_category::default_error_condition - std::error_category::default_error_condition

<h2>Synopsis</h2>

virtual std::error_condition default_error_condition( int code ) const noexcept; <i>(since C++11)</i> 
Returns the error condition for the given error code. 
Equivalent to std::error_condition(code, *this). 

<h2>Parameters</h2>

code - error code for which to return error condition

<h2>Return value</h2>

The error condition for the given error code. 
