---
title: "stdswapstdunordered_multiset(3)"
name: "stdswapstdunordered_multiset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdunordered_multiset/"
---

std::swap(std::unordered_multiset) - std::swap(std::unordered_multiset)

<h2>Synopsis</h2>

<pre><code>template &lt;class Key, class Hash, class KeyEqual, class Alloc&gt;
(since C++ 11)

    void swap(unordered_multiset&lt;Key, Hash, KeyEqual, Alloc&gt; &amp;lhs, (until C++ 17)

                                                                       unordered_multiset&lt;Key, Hash, KeyEqual, Alloc&gt; &amp;rhs);

template &lt;class Key, class Hash, class KeyEqual, class Alloc&gt;

void swap(unordered_multiset&lt;Key, Hash, KeyEqual, Alloc&gt; &amp;lhs, (since C++ 17)

                                                                   unordered_multiset&lt;Key, Hash, KeyEqual, Alloc&gt; &amp;rhs) noexcept(/* see below */);</code></pre> 
Specializes the std::swap algorithm for std::unordered_multiset. Swaps the contents of lhs and rhs. Calls lhs.swap(rhs). 

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
