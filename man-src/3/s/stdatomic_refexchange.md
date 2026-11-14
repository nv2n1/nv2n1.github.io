---
title: "stdatomic_refexchange(3)"
name: "stdatomic_refexchange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_refexchange/"
---

std::atomic_ref&lt;T&gt;::exchange - std::atomic_ref&lt;T&gt;::exchange

<h2>Synopsis</h2>

<pre><code>T exchange(T desired, std::memory_order order = std::memory_order_seq_cst) const noexcept;
(since C++ 20)</code></pre> 
Atomically replaces the value of the referenced object with desired. The operation is a read-modify-write operation. Memory is affected according to the value of order. 

<h2>Parameters</h2>

desired - value to assign 
order - memory order constraints to enforce

<h2>Return value</h2>

The value of the referenced object before the call. 
