---
title: "stderror_categoryequivalent(3)"
name: "stderror_categoryequivalent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_categoryequivalent/"
---

std::error_category::equivalent - std::error_category::equivalent

<h2>Synopsis</h2>

<pre><code>virtual bool equivalent(int code, (1)(since C++ 11)

                                      const std::error_condition &amp;condition) const noexcept;

virtual bool equivalent(const std::error_code &amp;code, (2)(since C++ 11)

                                                         int condition) const noexcept;</code></pre> 
Checks whether error code is equivalent to an error condition for the error category represented by *this. 
1) Equivalent to default_error_condition(code) == condition. 
2) Equivalent to *this == code.category() &amp;&amp; code.value() == condition. 

<h2>Parameters</h2>

code - specifies the error code to compare 
condition - specifies the error condition to compare

<h2>Return value</h2>

true if the error code is equivalent to the given error condition for the error category represented by *this, false otherwise. 
