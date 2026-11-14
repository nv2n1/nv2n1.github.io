---
title: "stdexperimentalswapstdexperimentalfunction(3)"
name: "stdexperimentalswapstdexperimentalfunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalswapstdexperimentalfunction/"
---

std::experimental::swap(std::experimental::function) - std::experimental::swap(std::experimental::function)

<h2>Synopsis</h2>

<pre><code>template &lt;class R, class... Args&gt;

void swap(std::experimental::function&lt;R(Args...)&gt; &amp;lhs,

          std::experimental::function&lt;R(Args...)&gt; &amp;rhs);</code></pre> 
Overloads the swap algorithm for std::experimental::function. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - polymorphic function wrappers whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents 
swap <i>(public member function)</i> 
