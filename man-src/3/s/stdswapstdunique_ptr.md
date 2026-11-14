---
title: "stdswapstdunique_ptr(3)"
name: "stdswapstdunique_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdunique_ptr/"
---

std::swap(std::unique_ptr) - std::swap(std::unique_ptr)

<h2>Synopsis</h2>

<pre><code>template &lt;class T, class Deleter&gt;
(since C++ 11)

    void swap(unique_ptr&lt;T, Deleter&gt; &amp;lhs, unique_ptr&lt;T, Deleter&gt; &amp;rhs) noexcept;</code></pre> 
Specializes the std::swap algorithm for std::unique_ptr. Swaps the pointers of lhs and rhs. Calls lhs.swap(rhs). 
This function does not participate in overload resolution unless std::is_swappable&lt;D&gt;::value is true. <i>(since C++17)</i> 

<h2>Parameters</h2>

lhs, rhs - smart pointers whose contents to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Constant

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects 
swap <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents 
swap <i>(public member function)</i> 
