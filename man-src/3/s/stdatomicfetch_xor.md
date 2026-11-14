---
title: "stdatomicfetch_xor(3)"
name: "stdatomicfetch_xor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicfetch_xor/"
---

std::atomic&lt;T&gt;::fetch_xor - std::atomic&lt;T&gt;::fetch_xor

<h2>Synopsis</h2>

<pre><code>T fetch_xor( T arg,

std::memory_order order = std::memory_order_seq_cst ) noexcept;           (since C++11)

T fetch_xor( T arg,                                                       (member only of atomic&lt;Integral&gt; template specialization)

std::memory_order order = std::memory_order_seq_cst ) volatile noexcept;</code></pre> 
Atomically replaces the current value with the result of bitwise XOR of the value and arg. The operation is read-modify-write operation. Memory is affected according to the value of order. 

<h2>Parameters</h2>

arg - the other argument of bitwise XOR 
order - memory order constraints to enforce

<h2>Return value</h2>

The value immediately preceding the effects of this function in the modification_order of *this. 

<h2>See also</h2>

atomic_fetch_xor 
atomic_fetch_xor_explicit replaces the atomic object with the result of bitwise XOR with a non-atomic argument and obtains the previous value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
