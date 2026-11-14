---
title: "stdnested_exceptionrethrow_nested(3)"
name: "stdnested_exceptionrethrow_nested"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnested_exceptionrethrow_nested/"
---

std::nested_exception::rethrow_nested - std::nested_exception::rethrow_nested

<h2>Synopsis</h2>

[[noreturn]] void rethrow_nested() const; <i>(since C++11)</i> 
Rethrows the stored exception. If there is no stored exceptions (i.e. nested_ptr() returns null pointer), then std::terminate is called. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 
