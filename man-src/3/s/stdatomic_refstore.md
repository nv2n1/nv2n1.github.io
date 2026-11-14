---
title: "stdatomic_refstore(3)"
name: "stdatomic_refstore"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_refstore/"
---

std::atomic_ref&lt;T&gt;::store - std::atomic_ref&lt;T&gt;::store

<h2>Synopsis</h2>

<pre><code>void store(T desired, std::memory_order order = std::memory_order_seq_cst) const noexcept;
(since C++ 20)</code></pre> 
Atomically replaces the current value of the referenced object with desired. Memory is affected according to the value of order. 
order must be one of std::memory_order_relaxed, std::memory_order_release or std::memory_order_seq_cst. Otherwise the behavior is undefined. 

<h2>Parameters</h2>

desired - the value to store into the referenced object 
order - memory order constraints to enforce

<h2>Return value</h2>

<i>(none)</i> 

<h2>See also</h2>

<pre><code>stores a value into the object referenced by an atomic_ref object

operator= (public member function)




</code></pre>
