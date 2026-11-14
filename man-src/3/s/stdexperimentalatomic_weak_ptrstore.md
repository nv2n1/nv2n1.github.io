---
title: "stdexperimentalatomic_weak_ptrstore(3)"
name: "stdexperimentalatomic_weak_ptrstore"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalatomic_weak_ptrstore/"
---

std::experimental::atomic_weak_ptr&lt;T&gt;::store - std::experimental::atomic_weak_ptr&lt;T&gt;::store

<h2>Synopsis</h2>

<pre><code>void store(weak_ptr&lt;T&gt; desired, std::memory_order order = std::memory_order_seq_cst) noexcept;</code></pre> 
Atomically replaces the current value with desired. Memory is affected according to the value of order. 
order must be one of std::memory_order_relaxed, std::memory_order_release or std::memory_order_seq_cst. Otherwise the behavior is undefined. 

<h2>Parameters</h2>

desired - the weak_ptr to store into the atomic variable 
order - memory order constraints to enforce

<h2>Return value</h2>

<i>(none)</i> 
Remarks 
All changes to the atomic_weak_ptr object itself, and all associated use_count increments, are guaranteed to be performed atomically. Associated use_count decrements take place after the atomic operation, but are not required to be part of it. Any associated destruction or deallocation operations take place after the atomic operation and are not part of it. 

<h2>See also</h2>

<pre><code>stores a value into an atomic_weak_ptr object

operator=                                                     (public member function)</code></pre> 
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
