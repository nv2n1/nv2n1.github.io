---
title: "stdnested_exceptionoperator(3)"
name: "stdnested_exceptionoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnested_exceptionoperator/"
---

std::nested_exception::operator= - std::nested_exception::operator=

<h2>Synopsis</h2>

<pre><code>nested_exception &amp;operator=(const nested_exception &amp;other) noexcept = default;
(since C++ 11)</code></pre> 
Replaces the stored exception with the one held in other. 

<h2>Parameters</h2>

other - nested exception to replace the contents with

<h2>Return value</h2>

*this 
