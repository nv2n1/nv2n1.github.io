---
title: "stdexperimentalswapstdexperimentalobserver_ptr(3)"
name: "stdexperimentalswapstdexperimentalobserver_ptr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalswapstdexperimentalobserver_ptr/"
---

std::experimental::swap(std::experimental::observer_ptr) - std::experimental::swap(std::experimental::observer_ptr)

<h2>Synopsis</h2>

<pre><code>template &lt;class W&gt;
(library fundamentals TS v2)

    void swap(observer_ptr&lt;W&gt; &amp;lhs, observer_ptr&lt;W&gt; &amp;rhs) noexcept;</code></pre> 
Specializes the swap algorithm for std::experimental::observer_ptr. Swaps the pointers of lhs and rhs. Calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - observer_ptrs whose contents to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Constant

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the values of two objects 
swap <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the watched objects 
swap <i>(public member function)</i> 
