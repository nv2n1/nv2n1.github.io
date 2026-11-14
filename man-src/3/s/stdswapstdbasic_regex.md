---
title: "stdswapstdbasic_regex(3)"
name: "stdswapstdbasic_regex"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdbasic_regex/"
---

std::swap(std::basic_regex) - std::swap(std::basic_regex)

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits&gt;
(since C++ 11)

    void swap(basic_regex&lt;CharT, Traits&gt; &amp;lhs, basic_regex&lt;CharT, Traits&gt; &amp;rhs) noexcept;</code></pre> 
Overloads the std::swap algorithm for std::basic_regex. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - regular expressions to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents 
swap <i>(public member function)</i> 
