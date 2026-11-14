---
title: "stdatomic_signal_fence(3)"
name: "stdatomic_signal_fence"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_signal_fence/"
---

std::atomic_signal_fence - std::atomic_signal_fence

<h2>Synopsis</h2>

Defined in header &lt;atomic&gt; 
extern &quot;C&quot; void atomic_signal_fence( std::memory_order order ) noexcept; <i>(since C++11)</i> 
Establishes memory synchronization ordering of non-atomic and relaxed atomic accesses, as instructed by order, between a thread and a signal handler executed on the same thread. This is equivalent to std::atomic_thread_fence, except no CPU instructions for memory ordering are issued. Only reordering of the instructions by the compiler is suppressed as order instructs. For example, a fence with release semantics prevents reads or writes from being moved past subsequent writes and a fence with acquire semantics prevents reads or writes from being moved ahead of preceding reads. 

<h2>Parameters</h2>

order - the memory ordering executed by this fence

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

memory_order defines memory ordering constraints for the given atomic operation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++11)</i> 
atomic_thread_fence generic memory order-dependent fence synchronization primitive 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
