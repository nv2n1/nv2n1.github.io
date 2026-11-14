---
title: "stdswapstdshared_lock(3)"
name: "stdswapstdshared_lock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdshared_lock/"
---

std::swap(std::shared_lock) - std::swap(std::shared_lock)

<h2>Synopsis</h2>

<pre><code>template &lt;class Mutex&gt;

void swap(shared_lock&lt;Mutex&gt; &amp;lhs, (since C++ 14)

                                       shared_lock&lt;Mutex&gt; &amp;rhs) noexcept;</code></pre> 
Specializes the std::swap algorithm for std::shared_lock. Exchanges the state of lhs with that of rhs. Effectively calls lhs.swap(rhs). 

<h2>Parameters</h2>

lhs, rhs - lock wrappers whose states to swap

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the data members with another shared_lock 
swap <i>(public member function)</i> 
