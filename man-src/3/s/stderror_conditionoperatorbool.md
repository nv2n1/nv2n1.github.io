---
title: "stderror_conditionoperatorbool(3)"
name: "stderror_conditionoperatorbool"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_conditionoperatorbool/"
---

std::error_condition::operatorbool - std::error_condition::operatorbool

<h2>Synopsis</h2>

explicit operator bool() const noexcept; <i>(since C++11)</i> 
Checks whether the stored error code is not zero. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if value != 0, false otherwise. 
