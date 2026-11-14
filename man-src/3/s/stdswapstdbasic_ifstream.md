---
title: "stdswapstdbasic_ifstream(3)"
name: "stdswapstdbasic_ifstream"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdbasic_ifstream/"
---

std::swap(std::basic_ifstream) - std::swap(std::basic_ifstream)

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits&gt;

void swap(basic_ifstream&lt;CharT, Traits&gt; &amp;lhs, basic_ifstream&lt;CharT, Traits&gt; &amp;rhs);</code></pre> 
Specializes the std::swap algorithm for std::basic_ifstream. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - streams whose state to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

swap swaps two file streams 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(C++11)</i> 
