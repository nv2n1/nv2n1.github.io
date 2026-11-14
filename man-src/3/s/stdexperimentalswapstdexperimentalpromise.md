---
title: "stdexperimentalswapstdexperimentalpromise(3)"
name: "stdexperimentalswapstdexperimentalpromise"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalswapstdexperimentalpromise/"
---

std::experimental::swap(std::experimental::promise) - std::experimental::swap(std::experimental::promise)

<h2>Synopsis</h2>

<pre><code>template &lt;class R&gt;

void swap(std::experimental::promise&lt;R&gt; &amp;lhs,

          std::experimental::promise&lt;R&gt; &amp;rhs) noexcept;</code></pre> 
Overloads the swap algorithm for std::experimental::promise. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - promises whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps two promise objects 
swap <i>(public member function of std::promise&lt;R&gt;)</i> 
