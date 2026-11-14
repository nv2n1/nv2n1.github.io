---
title: "stderror_codeoperatorbool(3)"
name: "stderror_codeoperatorbool"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_codeoperatorbool/"
---

std::error_code::operatorbool - std::error_code::operatorbool

<h2>Synopsis</h2>

explicit operator bool() const noexcept; <i>(since C++11)</i> 
Checks if the error value is valid, i.e. non-zero. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

false if value() == 0, true otherwise. 
