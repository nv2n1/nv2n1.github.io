---
title: "stderror_codemessage(3)"
name: "stderror_codemessage"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_codemessage/"
---

std::error_code::message - std::error_code::message

<h2>Synopsis</h2>

std::string message() const; <i>(since C++11)</i> 
Returns the message corresponding to the current error value and category. 
Equivalent to category().message(value()). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The error message corresponding to the current error value and category. 

<h2>Exceptions</h2>

<i>(none)</i>
