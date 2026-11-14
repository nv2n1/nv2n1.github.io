---
title: "stdexperimentalatomic_shared_ptris_lock_free(3)"
name: "stdexperimentalatomic_shared_ptris_lock_free"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalatomic_shared_ptris_lock_free/"
---

std::experimental::atomic_shared_ptr&lt;T&gt;::is_lock_free - std::experimental::atomic_shared_ptr&lt;T&gt;::is_lock_free

<h2>Synopsis</h2>

<pre><code>bool is_lock_free() const noexcept;</code></pre> 
Checks whether the atomic operations on all objects of this type are lock-free. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

true if the atomic operations on the objects of this type are lock-free, false otherwise. 

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
