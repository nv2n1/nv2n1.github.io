---
title: "stdatomicstore(3)"
name: "stdatomicstore"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomicstore/"
---

std::atomic&lt;T&gt;::store - std::atomic&lt;T&gt;::store

<h2>Synopsis</h2>

<pre><code>void store(T desired, std::memory_order order = std::memory_order_seq_cst) noexcept;
(since C++ 11)

    void store(T desired, std::memory_order order = std::memory_order_seq_cst) volatile noexcept;</code></pre> 
Atomically replaces the current value with desired. Memory is affected according to the value of order. 
order must be one of std::memory_order_relaxed, std::memory_order_release or std::memory_order_seq_cst. Otherwise the behavior is undefined. 

<h2>Parameters</h2>

desired - the value to store into the atomic variable 
order - memory order constraints to enforce

<h2>Return value</h2>

<i>(none)</i> 

<h2>See also</h2>

<pre><code>stores a value into an atomic object

operator=             (public member function)</code></pre> 
atomic_store 
atomic_store_explicit atomically replaces the value of the atomic object with a non-atomic argument 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
