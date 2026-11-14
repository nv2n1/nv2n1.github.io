---
title: "stdswapstdmultimap(3)"
name: "stdswapstdmultimap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdmultimap/"
---

std::swap(std::multimap) - std::swap(std::multimap)

<h2>Synopsis</h2>

<pre><code>template &lt;class Key, class T, class Compare, class Alloc&gt;

void swap(multimap&lt;Key, T, Compare, Alloc&gt; &amp;lhs, (until C++ 17)

                                                     multimap&lt;Key, T, Compare, Alloc&gt; &amp;rhs);

template &lt;class Key, class T, class Compare, class Alloc&gt;

void swap(multimap&lt;Key, T, Compare, Alloc&gt; &amp;lhs, (since C++ 17)

                                                     multimap&lt;Key, T, Compare, Alloc&gt; &amp;rhs) noexcept(/* see below */);</code></pre> 
Specializes the std::swap algorithm for std::multimap. Swaps the contents of lhs and rhs. Calls lhs.swap(rhs). 

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
