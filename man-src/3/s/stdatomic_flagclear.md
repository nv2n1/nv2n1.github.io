---
title: "stdatomic_flagclear(3)"
name: "stdatomic_flagclear"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_flagclear/"
---

std::atomic_flag::clear - std::atomic_flag::clear

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;atomic&gt;

    void clear(std::memory_order order = std::memory_order_seq_cst) volatile noexcept;
(1)(since C++ 11)

    void clear(std::memory_order order = std::memory_order_seq_cst) noexcept;
(2)(since C++ 11)</code></pre> 
Atomically changes the state of a std::atomic_flag to clear (false). 

<h2>Parameters</h2>

order - the memory synchronization ordering for this operation (cannot be std::memory_order_consume, std::memory_order_acquire, or std::memory_order_acq_rel)

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomically sets the flag to true and obtains its previous value 
test_and_set <i>(public member function)</i> 
atomic_flag_clear 
atomic_flag_clear_explicit atomically sets the value of the flag to false 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
memory_order defines memory ordering constraints for the given atomic operation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++11)</i> 
