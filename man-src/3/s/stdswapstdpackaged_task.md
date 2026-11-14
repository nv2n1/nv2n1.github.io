---
title: "stdswapstdpackaged_task(3)"
name: "stdswapstdpackaged_task"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdpackaged_task/"
---

std::swap(std::packaged_task) - std::swap(std::packaged_task)

<h2>Synopsis</h2>

<pre><code>template &lt;class Function, class... Args&gt;

void swap(packaged_task&lt;Function(Args...)&gt; &amp;lhs, (since C++ 11)

                                                     packaged_task&lt;Function(Args...)&gt; &amp;rhs) noexcept;</code></pre> 
Specializes the std::swap algorithm for std::packaged_task. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - packaged tasks whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps two task objects 
swap <i>(public member function)</i> 
