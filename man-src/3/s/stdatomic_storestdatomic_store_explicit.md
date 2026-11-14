---
title: "stdatomic_storestdatomic_store_explicit(3)"
name: "stdatomic_storestdatomic_store_explicit"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_storestdatomic_store_explicit/"
---

std::atomic_store,std::atomic_store_explicit - std::atomic_store,std::atomic_store_explicit

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;atomic&gt;

    template &lt;class T&gt;

    void atomic_store(std::atomic&lt;T&gt; *obj,

                      typename std::atomic&lt;T&gt;::value_type desr) noexcept;

template &lt;class T&gt;

void atomic_store(volatile std::atomic&lt;T&gt; *obj,

                  typename std::atomic&lt;T&gt;::value_type desr) noexcept;

template &lt;class T&gt;
(1)(since C++ 11)

    void atomic_store_explicit(std::atomic&lt;T&gt; *obj,

                               typename std::atomic&lt;T&gt;::value_type desr,

                               std::memory_order order) noexcept;
(2)(since C++ 11)

    template &lt;class T&gt;

    void atomic_store_explicit(volatile std::atomic&lt;T&gt; *obj,

                               typename std::atomic&lt;T&gt;::value_type desr,

                               std::memory_order order) noexcept;</code></pre> 
1) Atomically replaces the value pointed to by obj with the value of desr as if by obj-&gt;store(desr) 
2) Atomically replaces the value pointed to by obj with the value of desr as if by obj-&gt;store(desr, order) 

<h2>Parameters</h2>

obj - pointer to the atomic object to modify 
desr - the value to store in the atomic object 
order - the memory synchronization ordering for this operation: only std::memory_order_relaxed, std::memory_order_release and std::memory_order_seq_cst are permitted.

<h2>Return value</h2>

none. 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
P0558R1 C++11 exact type match required because T is deduced from multiple arguments T is deduced from the atomic argument only 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically replaces the value of the atomic object with a non-atomic argument 
store <i>(public member function of std::atomic&lt;T&gt;)</i> 
atomic_load 
atomic_load_explicit atomically obtains the value stored in an atomic object 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
memory_order defines memory ordering constraints for the given atomic operation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specializes atomic operations for std::shared_ptr 
std::atomic_store(std::shared_ptr)_ <i>(function template)</i> 
std::atomic_store_explicit(std::shared_ptr) 
