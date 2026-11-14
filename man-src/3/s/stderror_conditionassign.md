---
title: "stderror_conditionassign(3)"
name: "stderror_conditionassign"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_conditionassign/"
---

std::error_condition::assign - std::error_condition::assign

<h2>Synopsis</h2>

<pre><code>void assign(int val, const error_category &amp;cat) noexcept;
(since C++ 11)</code></pre> 
Assigns contents to an error condition. Sets the error code to val and error category to cat. 

<h2>Parameters</h2>

val - error code 
cat - error category

<h2>Return value</h2>

<i>(none)</i> 
