---
title: "stdexperimentalatomic_shared_ptroperator(3)"
name: "stdexperimentalatomic_shared_ptroperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalatomic_shared_ptroperator/"
---

std::experimental::atomic_shared_ptr&lt;T&gt;::operator= - std::experimental::atomic_shared_ptr&lt;T&gt;::operator=

<h2>Synopsis</h2>

<pre><code>void operator=(shared_ptr&lt;T&gt; desired) noexcept;
(1)

    void
    operator=(const atomic_shared_ptr &amp;) = delete;
(2)</code></pre> 
1) Atomically assigns a value desired to the atomic variable. Equivalent to store(desired). 
2) Atomic variables are not CopyAssignable. 

<h2>Parameters</h2>

desired - value to assign

<h2>Notes</h2>

Unlike most assignment operators, the assignment operators for atomic_shared_ptr returns void. 
Remarks 
All changes to the atomic_shared_ptr object itself, and all associated use_count increments, are guaranteed to be performed atomically. Associated use_count decrements take place after the atomic operation, but are not required to be part of it. Any associated destruction or deallocation operations take place after the atomic operation and are not part of it. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an atomic_shared_ptr object 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically replaces the value of the atomic object with a non-atomic argument 
store <i>(public member function)</i> 
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
