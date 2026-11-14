---
title: "stdswapstdbasic_syncbuf(3)"
name: "stdswapstdbasic_syncbuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdbasic_syncbuf/"
---

std::swap(std::basic_syncbuf) - std::swap(std::basic_syncbuf)

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits, class Allocator&gt;

void swap(std::basic_syncbuf&lt;CharT, Traits, Allocator&gt; &amp;lhs, (since C++ 20)

                                                                 std::basic_syncbuf&lt;CharT, Traits, Allocator&gt; &amp;rhs) noexcept;</code></pre> 
Overloads the std::swap algorithm for std::basic_syncbuf. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - std::basic_syncbuf objects whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps two basic_syncbuf objects 
swap <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects 
swap <i>(function template)</i> 
