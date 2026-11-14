---
title: "stdpackaged_taskswap(3)"
name: "stdpackaged_taskswap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpackaged_taskswap/"
---

std::packaged_task&lt;R(Args...)&gt;::swap - std::packaged_task&lt;R(Args...)&gt;::swap

<h2>Synopsis</h2>

<pre><code>void swap(packaged_task &amp;other) noexcept;
(since C++ 11)</code></pre> 
Exchanges the shared states and stored tasks of *this and other. 

<h2>Parameters</h2>

other - packaged task whose state to swap with

<h2>Return value</h2>

<i>(none)</i> 

<h2>See also</h2>

std::swap(std::packaged_task) specializes the std::swap algorithm 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
