---
title: "stdexperimentalflex_barrierarrive_and_drop(3)"
name: "stdexperimentalflex_barrierarrive_and_drop"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalflex_barrierarrive_and_drop/"
---

std::experimental::flex_barrier::arrive_and_drop - std::experimental::flex_barrier::arrive_and_drop

<h2>Synopsis</h2>

<pre><code>void arrive_and_drop();
(concurrency TS)</code></pre> 
Arrive at the flex_barrier's synchronization point and remove the current thread from the set of participating threads. It is unspecified whether this function blocks until the completion phase has ended. If the function blocks, the calling thread may be chosen to execute the completion phase. 
The behavior is undefined if the calling thread is not in the set of participating threads of this flex_barrier. 
Calls to arrive_and_drop synchronizes with the start of the completion phase of the flex_barrier. If the call blocks, then the completion of the completion phase synchronizes with the return from the call. 
Calls to arrive_and_drop and arrive_and_wait never introduce data races with themselves or each other. 

<h2>Exceptions</h2>

Throws nothing.

<h2>Notes</h2>

The completion phase will be executed even if every participating thread calls arrive_and_drop. 
After a thread calls arrive_and_drop on a flex_barrier, it cannot call any member function on that barrier except for the destructor, even if the function object invoked by the completion phase returns a positive value. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;arrive at the synchronization point and block 
arrive_and_wait <i>(public member function)</i> 
