---
title: "stderror_codedefault_error_condition(3)"
name: "stderror_codedefault_error_condition"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_codedefault_error_condition/"
---

std::error_code::default_error_condition - std::error_code::default_error_condition

<h2>Synopsis</h2>

std::error_condition default_error_condition() const noexcept; <i>(since C++11)</i> 
Returns the default error condition for the current error value. 
Equivalent to category().default_error_condition(value()). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The default error condition for the current error value. 
