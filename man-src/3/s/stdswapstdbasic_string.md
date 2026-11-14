---
title: "stdswapstdbasic_string(3)"
name: "stdswapstdbasic_string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdbasic_string/"
---

std::swap(std::basic_string) - std::swap(std::basic_string)

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits, class Alloc&gt;

void swap(std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;lhs, (until C++ 17)

                                                            std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;rhs);

template &lt;class CharT, class Traits, class Alloc&gt;

void swap(std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;lhs, (since C++ 17)

                                                            std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;rhs) noexcept(/* see below */);</code></pre> 
Specializes the std::swap algorithm for std::basic_string. Swaps the contents of lhs and rhs. Equivalent to lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - strings whose contents to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Constant.

<h2>Exceptions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++17)</i> 
noexcept specification: 
noexcept(noexcept(lhs.swap(rhs)))

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents 
swap <i>(public member function)</i> 
