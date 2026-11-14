---
title: "stdexperimentalflex_barrier(3)"
name: "stdexperimentalflex_barrier"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalflex_barrier/"
---

std::experimental::flex_barrier - std::experimental::flex_barrier

<h2>Synopsis</h2>

Defined in header &lt;experimental/barrier&gt; 
class flex_barrier; (concurrency TS) 
The class std::experimental::flex_barrier provides a thread-coordination mechanism that allows a set of participating threads to block until an operation is completed. Unlike std::experimental::latch, barriers are reusable; once the participating threads are released from a barrier's synchronization point, they can reuse the same barrier. 
A barrier has a completion phase, which is executed by one of the participating threads once all threads in the set of participating threads arrive at the synchronization point. The arrive_and_wait and arrive_and_drop calls synchronize_with the start of the completion phase; the end of the completion phase synchronizes with the returns from all calls blocked by its completion. 
std::experimental::flex_barrier allows the user to control the completion phase with a function object. If the function object returns -1, the set of participating threads is unchanged (and the same set of participating threads must arrive at the synchronization point in the next cycle); otherwise the set of participating threads becomes a new set with a size equal to the returned value N, and consists of the next N threads to arrive at the barrier's synchronization point. 
Users who do not need this functionality can use std::experimental::barrier. 

<h2>Member functions</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a flex_barrier 
constructor <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys the flex_barrier 
destructor <i>(public member function)</i> 

 
operator= not copy-assignable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i> 
[deleted] 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;arrive at the synchronization point and block 
arrive_and_wait <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;arrive at the synchronization point and remove the current thread from the set of participating threads 
arrive_and_drop <i>(public member function)</i>
