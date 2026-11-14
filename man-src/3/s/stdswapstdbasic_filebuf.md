---
title: "stdswapstdbasic_filebuf(3)"
name: "stdswapstdbasic_filebuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdbasic_filebuf/"
---

std::swap(std::basic_filebuf) - std::swap(std::basic_filebuf)

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits&gt;

void swap(std::basic_filebuf&lt;CharT, Traits&gt; &amp;lhs, (since C++ 11)

                                                      std::basic_filebuf&lt;CharT, Traits&gt; &amp;rhs);</code></pre> 
Overloads the std::swap algorithm for std::basic_filebuf. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - std::basic_filebuf objects whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

swap swaps two basic_filebuf objects 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects 
swap <i>(function template)</i> 
