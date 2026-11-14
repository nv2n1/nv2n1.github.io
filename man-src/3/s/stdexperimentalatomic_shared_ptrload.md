---
title: "stdexperimentalatomic_shared_ptrload(3)"
name: "stdexperimentalatomic_shared_ptrload"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalatomic_shared_ptrload/"
---

std::experimental::atomic_shared_ptr&lt;T&gt;::load - std::experimental::atomic_shared_ptr&lt;T&gt;::load

<h2>Synopsis</h2>

<pre><code>shared_ptr&lt;T&gt; load(std::memory_order order = std::memory_order_seq_cst) const noexcept;</code></pre> 
Atomically loads and returns the current value of the atomic_shared_ptr. Memory is affected according to the value of order. 
order must be one of std::memory_order_relaxed, std::memory_order_consume, std::memory_order_acquire or std::memory_order_seq_cst. Otherwise the behavior is undefined. 

<h2>Parameters</h2>

order - memory order constraints to enforce 

 

 
Remarks 

 
All associated use_count increments are guaranteed to be performed as part of the atomic operation.

<h2>Return value</h2>

The current value of the atomic_shared_ptr. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loads a value from an atomic object 
operator_shared_ptr&lt;T&gt; <i>(public member function)</i> 
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
