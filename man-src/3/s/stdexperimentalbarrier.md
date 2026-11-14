---
title: "stdexperimentalbarrier(3)"
name: "stdexperimentalbarrier"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalbarrier/"
---

std::experimental::barrier - std::experimental::barrier

<h2>Synopsis</h2>

Defined in header &lt;experimental/barrier&gt; 
class barrier; (concurrency TS) 
The class std::experimental::barrier provides a thread-coordination mechanism that allows a set of participating threads to block until an operation is completed. Unlike std::experimental::latch, barriers are reusable; once the participating threads are released from a barrier's synchronization point, they can reuse the same barrier. 
A barrier has a completion phase, which is executed by one of the participating threads once all threads in the set of participating threads arrive at the synchronization point. The arrive_and_wait and arrive_and_drop calls synchronize_with the start of the completion phase; the end of the completion phase synchronizes with the returns from all calls blocked by its completion. 
For std::experimental::barrier, the completion phase is empty. std::experimental::flex_barrier allows the user to control the completion phase with a function object. 
The set of participating threads for a barrier constructed for num_threads threads is the first num_threads threads to arrive at its synchronization point after construction. The same set of threads (except for threads that called arrive_and_drop()) must arrive at the barrier each cycle. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a barrier 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys the barrier 
destructor <i>(public member function)</i> 

 
operator= not copy-assignable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
[deleted] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;arrive at the synchronization point and block 
arrive_and_wait <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;arrive at the synchronization point and remove the current thread from the set of participating threads 
arrive_and_drop <i>(public member function)</i>
