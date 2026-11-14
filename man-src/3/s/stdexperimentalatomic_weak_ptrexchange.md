---
title: "stdexperimentalatomic_weak_ptrexchange(3)"
name: "stdexperimentalatomic_weak_ptrexchange"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalatomic_weak_ptrexchange/"
---

std::experimental::atomic_weak_ptr&lt;T&gt;::exchange - std::experimental::atomic_weak_ptr&lt;T&gt;::exchange

<h2>Synopsis</h2>

<pre><code>weak_ptr&lt;T&gt; exchange( weak_ptr&lt;T&gt; desired, std::memory_order order = std::memory_order_seq_cst ) noexcept;</code></pre> 
Atomically replaces the underlying weak_ptr with desired. The operation is a read-modify-write operation. Memory is affected according to the value of order. 

<h2>Parameters</h2>

desired - value to assign 
order - memory order constraints to enforce

<h2>Return value</h2>

The value of the atomic variable before the call. 
Remarks 
All changes to the atomic_weak_ptr object itself, and all associated use_count increments, are guaranteed to be performed atomically. Associated use_count decrements take place after the atomic operation, but are not required to be part of it. Any associated destruction or deallocation operations take place after the atomic operation and are not part of it. 

<h2>See also</h2>

std::atomic_is_lock_free(std::shared_ptr) 
std::atomic_load(std::shared_ptr) 
std::atomic_load_explicit(std::shared_ptr) 
std::atomic_store(std::shared_ptr) 
std::atomic_store_explicit(std::shared_ptr) 
std::atomic_exchange(std::shared_ptr) specializes atomic operations for std::shared_ptr 
std::atomic_exchange_explicit(std::shared_ptr) <i>(function template)</i> 
std::atomic_compare_exchange_weak(std::shared_ptr) 
std::atomic_compare_exchange_strong(std::shared_ptr) 
std::atomic_compare_exchange_weak_explicit(std::shared_ptr) 
std::atomic_compare_exchange_strong_explicit(std::shared_ptr) 
(deprecated in C++20) 
