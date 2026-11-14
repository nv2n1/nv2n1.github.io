---
title: "stdswapstdweak_ptr(3)"
name: "stdswapstdweak_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdweak_ptr/"
---

std::swap(std::weak_ptr) - std::swap(std::weak_ptr)

<h2>Synopsis</h2>

<pre><code>template &lt;class T&gt;
(since C++ 11)

    void swap(weak_ptr&lt;T&gt; &amp;lhs, weak_ptr&lt;T&gt; &amp;rhs) noexcept;</code></pre> 
Specializes the std::swap algorithm for std::weak_ptr. Swaps the pointers of lhs and rhs. Calls lhs.swap(rhs). 

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
