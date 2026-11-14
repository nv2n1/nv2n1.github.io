---
title: "stdatomic_(3)"
name: "stdatomic_"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_/"
---

std::atomic_...&lt;std::shared_ptr&gt; - std::atomic_...&lt;std::shared_ptr&gt;

<h2>Synopsis</h2>

<pre><code>template &lt;class T&gt;
(1)(since C++ 11)

    bool atomic_is_lock_free(const std::shared_ptr&lt;T&gt; *p);
(deprecated in C++ 20)

    template &lt;class T&gt;
    (2)(since C++ 11)

        std::shared_ptr&lt;T&gt; atomic_load(const std::shared_ptr&lt;T&gt; *p);
(deprecated in C++ 20)

    template &lt;class T&gt;
    (since C++ 11)

        std::shared_ptr&lt;T&gt; atomic_load_explicit(const std::shared_ptr&lt;T&gt; *p, (3)(deprecated in C++ 20)

                                                                                 std::memory_order mo);

template &lt;class T&gt;
(since C++ 11)

    void atomic_store(std::shared_ptr&lt;T&gt; *p, (4)(deprecated in C++ 20)

                                                 std::shared_ptr&lt;T&gt;
                                                     r);

template &lt;class T&gt;

void atomic_store_explicit(std::shared_ptr&lt;T&gt; *p, (5)(since C++ 11)

                                                      std::shared_ptr&lt;T&gt;
                                                          r,
                           (deprecated in C++ 20)

                               std::memory_order mo);

template &lt;class T&gt;
(since C++ 11)

    std::shared_ptr&lt;T&gt; atomic_exchange(std::shared_ptr&lt;T&gt; *p, (6)(deprecated in C++ 20)

                                                                  std::shared_ptr&lt;T&gt;
                                                                      r);

template &lt;class T&gt;

std::shared_ptr&lt;T&gt; atomic_exchange_explicit(std::shared_ptr&lt;T&gt; *p, (7)(since C++ 11)

                                                                       std::shared_ptr&lt;T&gt;
                                                                           r,
                                            (deprecated in C++ 20)

                                                std::memory_order mo);

template &lt;class T&gt;

bool atomic_compare_exchange_weak(std::shared_ptr&lt;T&gt; *p, (8)(since C++ 11)

                                                             std::shared_ptr&lt;T&gt; *expected,
                                  (deprecated in C++ 20)

                                      std::shared_ptr&lt;T&gt;
                                          desired);

template &lt;class T&gt;

bool atomic_compare_exchange_strong(std::shared_ptr&lt;T&gt; *p, (9)(since C++ 11)

                                                               std::shared_ptr&lt;T&gt; *expected,
                                    (deprecated in C++ 20)

                                        std::shared_ptr&lt;T&gt;
                                            desired);

template &lt;class T&gt;

bool atomic_compare_exchange_strong_explicit(std::shared_ptr&lt;T&gt; *p,

                                             std::shared_ptr&lt;T&gt; *expected, (10)(since C++ 11)

                                                                               std::shared_ptr&lt;T&gt;
                                                                                   desired,
                                             (deprecated in C++ 20)

                                                 std::memory_order success,

                                             std::memory_order failure);

template &lt;class T&gt;

bool atomic_compare_exchange_weak_explicit(std::shared_ptr&lt;T&gt; *p,

                                           std::shared_ptr&lt;T&gt; *expected, (11)(since C++ 11)

                                                                             std::shared_ptr&lt;T&gt;
                                                                                 desired,
                                           (deprecated in C++ 20)

                                               std::memory_order success,

                                           std::memory_order failure);</code></pre> 
If multiple threads of execution access the same std::shared_ptr object without synchronization and any of those accesses uses a non-const member function of shared_ptr then a data race will occur unless all such access is performed through these functions, which are overloads of the corresponding atomic access functions (std::atomic_load, std::atomic_store, etc.) 
Note that the control block of a shared_ptr is thread-safe: different std::shared_ptr objects can be accessed using mutable operations, such as operator= or reset, simultaneously by multiple threads, even when these instances are copies, and share the same control block internally. 
1) Determines whether atomic access to the shared pointer pointed-to by p is lock-free. 
2) Equivalent to atomic_load_explicit(p, std::memory_order_seq_cst) 
3) Returns the shared pointer pointed-to by p. As with the non-specialized std::atomic_load_explicit, mo cannot be std::memory_order_release or std::memory_order_acq_rel 
4) Equivalent to atomic_store_explicit(p, r, memory_order_seq_cst) 
5) Stores the shared pointer r in the shared pointer pointed-to by p atomically, effectively executing p-&gt;swap(r). As with the non-specialized std::atomic_store_explicit, mo cannot be std::memory_order_acquire or std::memory_order_acq_rel. 
6) Equivalent to atomic_exchange_explicit(p, r, memory_order_seq_cst) 
7) Stores the shared pointer r in the shared pointer pointed to by p and returns the value formerly pointed-to by p, atomically. Effectively executes p-&gt;swap(r) and returns a copy of r after the swap. 
8) Equivalent to atomic_compare_exchange_weak_explicit(p, expected, desired, std::memory_order_seq_cst, std::memory_order_seq_cst) 
9) Equivalent to atomic_compare_exchange_strong_explicit(p, expected, desired, std::memory_order_seq_cst, std::memory_order_seq_cst) 
10) Compares the shared pointers pointed-to by p and expected. If they are equivalent (store the same pointer value, and either share ownership of the same object or are both empty), assigns desired into *p using the memory ordering constraints specified by success and returns true. If they are not equivalent, assigns *p into *expected using the memory ordering constraints specified by failure and returns false. 
11) Same as 10), but may fail spuriously. 
All these functions invoke undefined behavior if p is a null pointer. 

<h2>Parameters</h2>

p, expected - a pointer to a std::shared_ptr 
r, desired - a std::shared_ptr 
mo, success, failure - memory ordering selectors of type std::memory_order

<h2>Exceptions</h2>

These functions do not throw exceptions.

<h2>Return value</h2>

1) true if atomic access is implemented using lock-free instructions 
2,3) A copy of the pointed-to shared pointer. 
4,5) <i>(none)</i> 
6,7) A copy of the formerly pointed-to shared pointer 
8,9,10,11) true if the shared pointers were equivalent and the exchange was performed, false otherwise. 

<h2>Notes</h2>

These functions are typically implemented using mutexes, stored in a global hash table where the pointer value is used as the key. 
To avoid data races, once a shared pointer is passed to any of these functions, it cannot be accessed non-atomically. In particular, you cannot dereference such a shared_ptr without first atomically loading it into another shared_ptr object, and then dereferencing through the second object. 
The Concurrency_TS offers atomic smart pointer classes atomic_shared_ptr and atomic_weak_ptr as a replacement for the use of these functions. 
These functions were deprecated in favor of the specializations of the std::atomic template: std::atomic&lt;std::shared_ptr&gt; and std::atomic&lt;std::weak_ptr&gt;. <i>(since C++20)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2980 C++11 empty shared_ptrs are never equivalent equivalent if they store the same pointer value 

<h2>See also</h2>

atomic_is_lock_free checks if the atomic type's operations are lock-free 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
atomic_store 
atomic_store_explicit atomically replaces the value of the atomic object with a non-atomic argument 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
atomic_load 
atomic_load_explicit atomically obtains the value stored in an atomic object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
atomic_exchange 
atomic_exchange_explicit atomically replaces the value of the atomic object with non-atomic argument and returns the old value of the atomic 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
atomic_compare_exchange_weak 
atomic_compare_exchange_weak_explicit 
atomic_compare_exchange_strong 
atomic_compare_exchange_strong_explicit atomically compares the value of the atomic object with non-atomic argument and performs atomic exchange if equal or atomic load if not 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
