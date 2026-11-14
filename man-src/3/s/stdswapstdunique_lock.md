---
title: "stdswapstdunique_lock(3)"
name: "stdswapstdunique_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdunique_lock/"
---

std::swap(std::unique_lock) - std::swap(std::unique_lock)

<h2>Synopsis</h2>

<pre><code>template &lt;class Mutex&gt;

void swap(unique_lock&lt;Mutex&gt; &amp;lhs, (since C++ 11)

                                       unique_lock&lt;Mutex&gt; &amp;rhs) noexcept;</code></pre> 
Specializes the std::swap algorithm for std::unique_lock. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - lock wrappers whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps state with another std::unique_lock 
swap <i>(public member function)</i> 
