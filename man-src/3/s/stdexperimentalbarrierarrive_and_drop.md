---
title: "stdexperimentalbarrierarrive_and_drop(3)"
name: "stdexperimentalbarrierarrive_and_drop"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalbarrierarrive_and_drop/"
---

std::experimental::barrier::arrive_and_drop - std::experimental::barrier::arrive_and_drop

<h2>Synopsis</h2>

<pre><code>void arrive_and_drop();
(concurrency TS)</code></pre> 
Arrive at the barrier's synchronization point and remove the current thread from the set of participating threads. It is unspecified whether this function blocks until the completion phase has ended. 
The behavior is undefined if the calling thread is not in the set of participating threads of this barrier. 
Calls to arrive_and_drop synchronizes with the start of the completion phase of the barrier. If the call blocks, then the completion of the completion phase synchronizes with the return from the call. 
Calls to arrive_and_drop and arrive_and_wait never introduce data races with themselves or each other. 

<h2>Exceptions</h2>

Throws nothing.

<h2>Notes</h2>

If every participating thread calls arrive_and_drop(), the barrier can only be destroyed. 
After a thread calls arrive_and_drop() on a barrier, it is no longer a member of its set of participating threads and hence can no longer call either arrive_and_drop() or arrive_and_wait() on the same barrier. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;arrive at the synchronization point and block 
arrive_and_wait <i>(public member function)</i> 
