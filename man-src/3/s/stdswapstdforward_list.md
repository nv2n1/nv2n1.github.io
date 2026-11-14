---
title: "stdswapstdforward_list(3)"
name: "stdswapstdforward_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdforward_list/"
---

std::swap(std::forward_list) - std::swap(std::forward_list)

<h2>Synopsis</h2>

<pre><code>template &lt;class T, class Alloc&gt;
(since C++ 11)

    void swap(forward_list&lt;T, Alloc&gt; &amp;lhs, (until C++ 17)

                                               forward_list&lt;T, Alloc&gt; &amp;rhs);

template &lt;class T, class Alloc&gt;

void swap(forward_list&lt;T, Alloc&gt; &amp;lhs, (since C++ 17)

                                           forward_list&lt;T, Alloc&gt; &amp;rhs) noexcept(/* see below */);</code></pre> 
Specializes the std::swap algorithm for std::forward_list. Swaps the contents of lhs and rhs. Calls lhs.swap(rhs). 

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
