---
title: "stdatomic_refload(3)"
name: "stdatomic_refload"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_refload/"
---

std::atomic_ref&lt;T&gt;::load - std::atomic_ref&lt;T&gt;::load

<h2>Synopsis</h2>

<pre><code>T load(std::memory_order order = std::memory_order_seq_cst) const noexcept;
(since C++ 20)</code></pre> 
Atomically loads and returns the current value of the referenced object. Memory is affected according to the value of order. 
order must be one of std::memory_order_relaxed, std::memory_order_consume, std::memory_order_acquire or std::memory_order_seq_cst. Otherwise the behavior is undefined. 

<h2>Parameters</h2>

order - memory order constraints to enforce

<h2>Return value</h2>

The current value of the referenced object. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loads a value from the referenced object 
operator_T <i>(public member function)</i> 
