---
title: "stdatomicoperatort(3)"
name: "stdatomicoperatort"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicoperatort/"
---

std::atomic&lt;T&gt;::operatorT - std::atomic&lt;T&gt;::operatorT

<h2>Synopsis</h2>

<pre><code>operator T() const noexcept;
(since C++ 11)

operator T() const volatile noexcept;</code></pre> 
Atomically loads and returns the current value of the atomic variable. Equivalent to load(). 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

The current value of the atomic variable. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically obtains the value of the atomic object 
load <i>(public member function)</i> 
