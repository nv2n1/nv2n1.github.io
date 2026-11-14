---
title: "stdatomicfetch_and(3)"
name: "stdatomicfetch_and"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicfetch_and/"
---

std::atomic&lt;T&gt;::fetch_and - std::atomic&lt;T&gt;::fetch_and

<h2>Synopsis</h2>

<pre><code>T fetch_and( T arg,

std::memory_order order = std::memory_order_seq_cst ) noexcept;           (since C++11)

T fetch_and( T arg,                                                       (member only of atomic&lt;Integral&gt; template specialization)

std::memory_order order = std::memory_order_seq_cst ) volatile noexcept;</code></pre> 
Atomically replaces the current value with the result of bitwise AND of the value and arg. The operation is read-modify-write operation. Memory is affected according to the value of order. 

<h2>Parameters</h2>

arg - the other argument of bitwise AND 
order - memory order constraints to enforce

<h2>Return value</h2>

The value immediately preceding the effects of this function in the modification_order of *this. 

<h2>See also</h2>

atomic_fetch_and 
atomic_fetch_and_explicit replaces the atomic object with the result of bitwise AND with a non-atomic argument and obtains the previous value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
