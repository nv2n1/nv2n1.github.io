---
title: "stdswapstdbasic_istringstream(3)"
name: "stdswapstdbasic_istringstream"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdbasic_istringstream/"
---

std::swap(std::basic_istringstream) - std::swap(std::basic_istringstream)

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits, class Alloc&gt;

void swap(std::basic_istringstream&lt;CharT, Traits, Alloc&gt; &amp;lhs,

          std::basic_istringstream&lt;CharT, Traits, Alloc&gt; &amp;rhs);</code></pre> 
Specializes the std::swap algorithm for std::basic_istringstream. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

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

swap swaps two string streams 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
<i>(C++11)</i> 
