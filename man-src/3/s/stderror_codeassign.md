---
title: "stderror_codeassign(3)"
name: "stderror_codeassign"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_codeassign/"
---

std::error_code::assign - std::error_code::assign

<h2>Synopsis</h2>

<pre><code>void assign(int ec, const error_category &amp;ecat) noexcept;
(since C++ 11)</code></pre> 
Replaces the contents with error code ec and corresponding category ecat. 

<h2>Parameters</h2>

ec - platform-dependent error code enum to assign 
ecat - error category corresponding to ec

<h2>Return value</h2>

<i>(none)</i> 

<h2>See also</h2>

<pre><code>assigns another error code

operator= (public member function)




</code></pre>
