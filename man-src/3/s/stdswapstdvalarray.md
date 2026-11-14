---
title: "stdswapstdvalarray(3)"
name: "stdswapstdvalarray"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdvalarray/"
---

std::swap(std::valarray) - std::swap(std::valarray)

<h2>Synopsis</h2>

<pre><code>template &lt;class T&gt;

void swap(valarray&lt;T&gt; &amp;lhs, valarray&lt;T&gt; &amp;rhs);</code></pre> 
Specializes the std::swap algorithm for std::valarray. Swaps the contents of lhs and rhs. Calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - valarrays whose contents to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Constant.

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps with another valarray 
swap <i>(public member function)</i> 
