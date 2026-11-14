---
title: "stdswapstdvector(3)"
name: "stdswapstdvector"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdvector/"
---

std::swap(std::vector) - std::swap(std::vector)

<h2>Synopsis</h2>

<pre><code>template &lt;class T, class Alloc&gt;

void swap(vector&lt;T, Alloc&gt; &amp;lhs, (until C++ 17)

                                     vector&lt;T, Alloc&gt; &amp;rhs);

template &lt;class T, class Alloc&gt;

void swap(vector&lt;T, Alloc&gt; &amp;lhs, (since C++ 17)

                                     vector&lt;T, Alloc&gt; &amp;rhs) noexcept(/* see below */);</code></pre> 
Specializes the std::swap algorithm for std::vector. Swaps the contents of lhs and rhs. Calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - containers whose contents to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Constant.

<h2>Exceptions</h2>

noexcept specification: <i>(since C++17)</i> 
noexcept(noexcept(lhs.swap(rhs)))

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents 
swap <i>(public member function)</i> 
