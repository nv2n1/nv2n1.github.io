---
title: "stdshared_lockswap(3)"
name: "stdshared_lockswap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshared_lockswap/"
---

std::shared_lock&lt;Mutex&gt;::swap - std::shared_lock&lt;Mutex&gt;::swap

<h2>Synopsis</h2>

<pre><code>template &lt;class Mutex&gt;
(since C++ 14)

    void swap(shared_lock&lt;Mutex&gt; &amp;other) noexcept;</code></pre> 
Exchanges the internal states of the lock objects. 

<h2>Parameters</h2>

other - the lock to swap the state with

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specialization of std::swap for shared_lock 
std::swap(std::shared_lock) <i>(function template)</i> 
