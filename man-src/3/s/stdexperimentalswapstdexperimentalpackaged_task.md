---
title: "stdexperimentalswapstdexperimentalpackaged_task(3)"
name: "stdexperimentalswapstdexperimentalpackaged_task"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalswapstdexperimentalpackaged_task/"
---

std::experimental::swap(std::experimental::packaged_task) - std::experimental::swap(std::experimental::packaged_task)

<h2>Synopsis</h2>

<pre><code>template &lt;class R, class... Args&gt;

void swap(std::experimental::packaged_task&lt;R(Args...)&gt; &amp;lhs,

          std::experimental::packaged_task&lt;R(Args...)&gt; &amp;rhs) noexcept;</code></pre> 
Overloads the swap algorithm for std::experimental::packaged_task. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - packaged_tasks whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps two task objects 
swap <i>(public member function of std::packaged_task&lt;R(Args...)&gt;)</i> 
