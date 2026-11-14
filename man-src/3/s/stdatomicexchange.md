---
title: "stdatomicexchange(3)"
name: "stdatomicexchange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicexchange/"
---

std::atomic&lt;T&gt;::exchange - std::atomic&lt;T&gt;::exchange

<h2>Synopsis</h2>

<pre><code>T exchange( T desired, std::memory_order order = std::memory_order_seq_cst ) noexcept;           (since C++11)

T exchange( T desired, std::memory_order order = std::memory_order_seq_cst ) volatile noexcept;</code></pre> 
Atomically replaces the underlying value with desired. The operation is read-modify-write operation. Memory is affected according to the value of order. 

<h2>Parameters</h2>

desired - value to assign 
order - memory order constraints to enforce

<h2>Return value</h2>

The value of the atomic variable before the call. 

<h2>See also</h2>

atomic_exchange 
atomic_exchange_explicit atomically replaces the value of the atomic object with non-atomic argument and returns the old value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
