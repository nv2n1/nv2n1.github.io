---
title: "stdatomic_refoperatort(3)"
name: "stdatomic_refoperatort"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_refoperatort/"
---

std::atomic_ref&lt;T&gt;::operatorT - std::atomic_ref&lt;T&gt;::operatorT

<h2>Synopsis</h2>

operator T() const noexcept; <i>(since C++20)</i> 
Atomically loads and returns the current value of the referenced object. Equivalent to load(). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The current value of the referenced object. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically obtains the value of the referenced object 
load <i>(public member function)</i> 
