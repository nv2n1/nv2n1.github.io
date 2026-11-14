---
title: "stdswapstdbasic_stringbuf(3)"
name: "stdswapstdbasic_stringbuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdbasic_stringbuf/"
---

std::swap(std::basic_stringbuf) - std::swap(std::basic_stringbuf)

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits, class Alloc&gt;

void swap(std::basic_stringbuf&lt;CharT, Traits, Alloc&gt; &amp;lhs, (since C++ 11)

                                                               std::basic_stringbuf&lt;CharT, Traits, Alloc&gt; &amp;rhs);</code></pre> 
Overloads the std::swap algorithm for std::basic_stringbuf. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - std::basic_stringbuf objects whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

swap swaps two basic_stringbuf objects 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects 
swap <i>(function template)</i> 
