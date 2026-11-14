---
title: "stdatomic_reffetch_xor(3)"
name: "stdatomic_reffetch_xor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_reffetch_xor/"
---

std::atomic_ref&lt;T&gt;::fetch_xor - std::atomic_ref&lt;T&gt;::fetch_xor

<h2>Synopsis</h2>

<pre><code>T fetch_xor(T arg, (since C++ 20)

                       std::memory_order order = std::memory_order_seq_cst) const noexcept;
(member only of atomic_ref&lt;Integral&gt; template specialization)</code></pre> 
Atomically replaces the current value of the referenced object with the result of bitwise XOR of the value and arg. This operation is a read-modify-write operation. Memory is affected according to the value of order. 

<h2>Parameters</h2>

arg - the other argument of bitwise XOR 
order - memory order constraints to enforce

<h2>Return value</h2>

The value of the referenced object, immediately preceding the effects of this function. 
